import pandas as pd
import numpy as np


def post_processing_function(state, params):
    df = pd.DataFrame(state["Simulation History Log"])
    df["Beta0 Error"] = np.abs(df["Population Beta0"] - df["Estimate Beta0"])
    df["Beta1 Error"] = np.abs(df["Population Beta1"] - df["Estimate Beta1"])
    return df
