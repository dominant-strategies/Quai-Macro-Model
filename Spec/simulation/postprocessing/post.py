import pandas as pd
import numpy as np


def post_processing_function(state, params):
    df = pd.DataFrame(state["Simulation History Log"])
    df["Beta0 Error"] = np.abs(df["Population Beta0"] - df["Estimate Beta0"])
    df["Beta1 Error"] = np.abs(df["Population Beta1"] - df["Estimate Beta1"])
    
    # df["Beta Estimation Norm"] = (
    # (
    #        df[["Population Beta0", "Population Beta1"]].values
    #        - df[["Estimate Beta0", "Estimate Beta1"]].values
    #    )
    #    ** 2
    #).sum(axis=1) ** 0.5
    
    df = df.astype('float')    
    df["Beta Estimation Norm"] = np.linalg.norm(df[['Beta0 Error','Beta1 Error']].values,axis=1)
    
    return df
