## Logistic regression used in go Quai for training the controller

In order to test the regression code used in go-quai, with the MSML simulation
environment the golang code can be compiled into a .so file using cbuild feature
of golang and then imported into python and run to get outputs.

### How do build the golang code
```{go}
 go build -buildmode=c-shared -o logistic.so logistic.go
 ```

How to use the regression inside of python is in the `logistic.py`
