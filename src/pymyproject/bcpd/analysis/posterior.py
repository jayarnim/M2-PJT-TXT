from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import arviz as az
from matplotlib.axes import Axes
from arviz.data.inference_data import InferenceData


def posterior(
    ax: Axes,
    samples: np.ndarray, 
    date: pd.DatetimeIndex, 
    cp_idx: int,
):
    # DRAW AX ==========
    sns.histplot(
        data=date[samples[:, cp_idx]],
        bins=50,
        stat="probability",
        ax=ax,
    )

    # MARKING MODE IDX ==========
    kwargs = dict(
        a=samples[:, cp_idx],
        axis=0,
        keepdims=False,
    )
    mode_idx = stats.mode(**kwargs).mode.item()

    ax.axvline(
        x=date[mode_idx],
        color="red",
    )

    # LABELS ==========
    ax.set_xlabel("yearmonth")
    ax.set_ylabel("density")

    # TITLE ==========
    mode_date = date[mode_idx].to_period("M")
    ax.set_title(f"cp {cp_idx+1} posterior (mode: {mode_date})")


def autocorr(
    ax: Axes, 
    trace: InferenceData, 
    cp_idx: int,
):
    # DRAW AX ==========
    az.plot_autocorr(
        data=trace,
        var_names=["tau"],
        coords={"tau_dim_0": [cp_idx]},
        ax=ax,
    )

    # TITLE ==========
    ax.set_title(f"cp {cp_idx+1} autocorr")


def main(
    trace: InferenceData, 
    date: pd.DatetimeIndex, 
    factor: int,
):
    tau = trace.posterior["tau"].values
    N_CPS = tau.shape[-1]
    samples = tau.reshape(-1, N_CPS)

    # CONSTANTS ==========
    NROWS = N_CPS
    NCOLS = 2
    FIGSIZE = (9*NCOLS, 4*N_CPS)

    # DRAWING PAPER ==========
    fig, axes = plt.subplots(
        nrows=NROWS,
        ncols=NCOLS,
        figsize=FIGSIZE,
        squeeze=False,
    )

    # DRAW AX ==========
    for cp_idx in range(N_CPS):
        ax_post = axes[cp_idx, 0]
        ax_auto = axes[cp_idx, 1]

        # LEFT: posterior
        kwargs = dict(
            samples=samples,
            date=date,
            cp_idx=cp_idx,
            ax=ax_post,
        )
        posterior(**kwargs)

        # RIGHT: autocorrelation
        kwargs = dict(
            trace=trace,
            cp_idx=cp_idx,
            ax=ax_auto,
        )
        autocorr(**kwargs)

    # TITLE ==========
    TITLE = f"factor {factor} tau diagnostics (n_cp={N_CPS})"
    plt.suptitle(t=TITLE, fontsize=16)

    # ETC. ==========
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.show()