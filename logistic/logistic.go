package main

import (
	"fmt"
	"math/big"
	"unsafe"

	"github.com/dominant-strategies/go-quai/common"
	"github.com/dominant-strategies/go-quai/common/math"
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
)

/*
#cgo LDFLAGS: -lm
#include <stdint.h>
*/
import "C"

var (
	c_learningRate = big.NewFloat(0.001)
	c_lambda       = big.NewFloat(0.5)
	c_epochLength  = 10
)

// sigmoid computes the sigmoid function.
func sigmoid(z *big.Float) *big.Float {
	// Compute exp(-z)
	negZ := new(big.Float).Neg(z)
	expNegZ := math.EToTheX(negZ)

	// Compute 1 + exp(-z)
	denom := new(big.Float).Add(new(big.Float).SetInt(common.Big1), expNegZ)

	// Compute 1 / (1 + exp(-z))
	result := new(big.Float).Quo(new(big.Float).SetInt(common.Big1), denom)

	return result
}

// Predict computes the probability that the input belongs to class 1.
func Predict(x *big.Float, beta0, beta1 *big.Float) *big.Float {
	// z = beta0 + beta1 * x
	beta1x := new(big.Float).Mul(beta1, x)
	z := new(big.Float).Add(beta0, beta1x)

	// Apply sigmoid function
	return sigmoid(z)
}

//export Train
func Train(cX, cY *C.int, n C.int, b0 *C.double, b1 *C.double) {

	fmt.Println("Training using the Quai logistic regression")

	var x, y []*big.Float
	x = make([]*big.Float, n)
	y = make([]*big.Float, n)

	for i := 0; i < int(n); i++ {
		// Use pointer arithmetic to access the elements
		xi := *(*C.int)(unsafe.Pointer(uintptr(unsafe.Pointer(cX)) + uintptr(i)*unsafe.Sizeof(C.int(0))))
		yi := *(*C.int)(unsafe.Pointer(uintptr(unsafe.Pointer(cY)) + uintptr(i)*unsafe.Sizeof(C.int(0))))

		x[i] = big.NewFloat(float64(xi))
		y[i] = big.NewFloat(float64(yi))
	}
	var beta0, beta1 = big.NewFloat(0), big.NewFloat(0)

	for epoch := 0; epoch < c_epochLength; epoch++ {
		// Initialize gradients
		dw := new(big.Float).SetInt(common.Big0)
		db := new(big.Float).SetInt(common.Big0)

		// Compute gradients
		for i := 0; i < int(n); i++ {
			xi := x[i]
			yi := y[i]
			pred := Predict(xi, beta0, beta1)
			error := new(big.Float).Sub(pred, yi)
			dwTerm := new(big.Float).Mul(error, xi)
			dw.Add(dw, dwTerm)
			db.Add(db, error)
		}

		nSamplesFloat := new(big.Float).SetInt(big.NewInt(int64(n))) //big.NewFloat(float64(nSamples))

		// Compute gradient averages
		dw.Quo(dw, nSamplesFloat)
		db.Quo(db, nSamplesFloat)

		// Apply L2 Regularization (Ridge Regression)
		// L2 gradient for weight is lambda * beta1
		lambdaL2 := new(big.Float).Set(c_lambda) // Regularization strength
		l2Penalty := new(big.Float).Mul(lambdaL2, beta1)
		dw.Add(dw, l2Penalty) // Adjust gradient for weight

		// Apply L1 Regularization (Lasso Regression)
		// L1 gradient is sign(beta1) * lambda
		lambdaL1 := new(big.Float).Set(c_lambda)
		signBeta1 := new(big.Float).Copy(beta1)
		if beta1.Sign() > 0 {
			signBeta1.SetFloat64(1)
		} else if beta1.Sign() < 0 {
			signBeta1.SetFloat64(-1)
		} else {
			signBeta1.SetFloat64(0)
		}
		l1Penalty := new(big.Float).Mul(lambdaL1, signBeta1)
		dw.Add(dw, l1Penalty) // Adjust gradient for weight

		// Update weight: beta1 = beta1 - LearningRate * dw
		lrUpdateW := new(big.Float).Mul(c_learningRate, dw)
		beta1.Sub(beta1, lrUpdateW)

		// Update bias: beta0 = beta0 - LearningRate * db
		lrUpdateB := new(big.Float).Mul(c_learningRate, db)
		beta0.Sub(beta0, lrUpdateB)
	}

	bFloat0, _ := beta0.Float64()
	bFloat1, _ := beta1.Float64()

	*b0 = C.double(bFloat0)
	*b1 = C.double(bFloat1)
}

// Plot the given trained logistic regression values with Beta0 and Beta1
func PlotSigmoid(xValues, yValues []float64, blockNumber uint64, betaF0, betaF1 *big.Float) error {
	// Create a new plot
	p := plot.New()

	beta0, _ := betaF0.Float64()
	beta1, _ := betaF1.Float64()

	p.Title.Text = fmt.Sprintf("Sigmoid Function: Beta0=%.10f, Beta1=%.10f", beta0, beta1)
	p.X.Label.Text = "x"
	p.Y.Label.Text = "sigmoid(x)"

	plotValues := make(plotter.XYs, 0)
	for i := range xValues {
		value := plotter.XY{xValues[i], yValues[i]}
		plotValues = append(plotValues, value)
	}

	// Create a line plotter with x and y values
	line, err := plotter.NewScatter(plotValues)
	if err != nil {
		return err
	}

	// Add the line to the plot
	p.Add(line)

	// Create the function to be plotted
	sigmoidFunc := plotter.NewFunction(func(x float64) float64 {
		result := Predict(big.NewFloat(x), betaF0, betaF1)
		resultF, _ := result.Float64()
		return resultF
	})

	// Set the style for the function line
	sigmoidFunc.Color = plotter.DefaultLineStyle.Color
	sigmoidFunc.Width = vg.Points(2)

	// Set the range for x-axis values
	// Find the min and max in the xValues
	xMin := float64(math.MaxInt64)
	xMax := float64(0)
	for _, x := range xValues {
		if x < xMin {
			xMin = x
		} else if x > xMax {
			xMax = x
		}
	}
	sigmoidFunc.XMin = xMin
	sigmoidFunc.XMax = xMax

	p.Add(sigmoidFunc)

	// Save the plot as a PNG image
	if err := p.Save(6*vg.Inch, 4*vg.Inch, fmt.Sprintf("sigmoid-%d.png", blockNumber)); err != nil {
		return err
	}

	return nil
}

func main() {}
