from scipy import stats
import pandas as pd
from arviz.data.inference_data import InferenceData


def main(
    trace: InferenceData, 
    date: pd.DatetimeIndex,
):
    N_CPS = trace.posterior["tau"].values.shape[-1]

    kwargs = dict(
        a=trace.posterior["tau"].values.reshape(-1, N_CPS),
        axis=0,
        keepdims=False,
    )
    idx = stats.mode(**kwargs).mode.tolist()

    return date[idx]