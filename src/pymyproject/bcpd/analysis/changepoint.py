from typing import Any
import pandas as pd
import matplotlib.pyplot as plt
from arviz.data.inference_data import InferenceData
from . import search


def build_data(
    trace: InferenceData, 
    scores: pd.DataFrame, 
    factor: int,
) -> dict[str, Any]:
    # DATE TYPE SETTING ==========
    date = scores.index.to_timestamp()

    # TARGET FACTOR SCORES ==========
    y = scores[f"f{factor}"].values

    # SEARCH CHANGE POINT DATE ==========
    kwargs = dict(
        trace=trace,
        date=date,
    )
    cps = search.main(**kwargs)

    # MU BY INTERVAL ==========
    mus = (
        trace
        .posterior["mus"]
        .mean(dim=["chain", "draw"])
        .values
    )

    return dict(
        x=date, 
        y=y, 
        mus=mus, 
        cps=cps,
    )


def main(
    trace: InferenceData, 
    scores: pd.DataFrame, 
    factor: int,
    figsize: tuple[int]=(16,6),
):
    N_CPS = trace.posterior["tau"].values.shape[-1]

    # BUILD DATA ==========
    kwargs = dict(
        trace=trace,
        scores=scores, 
        factor=factor, 
    )
    data = build_data(**kwargs)

    # DRAWING PAPER ==========
    fig = plt.figure(figsize=figsize)

    # OBSERVED ==========
    plt.plot(
        *(data["x"], data["y"]), 
        label="observed",
    )

    # CHANGE POINTS ==========
    for cp in data["cps"]:
        kwargs = dict(
            x=cp,
            color="black",
            linestyle="--",
            lw=1,
        )
        plt.axvline(**kwargs)

    # SEGMENT MEAN ==========
    boundaries = [data["x"][0]] + list(data["cps"]) + [data["x"][-1]]

    for i in range(len(data["mus"])):
        kwargs = dict(
            y=data["mus"][i],
            xmin=boundaries[i],
            xmax=boundaries[i+1],
            colors="red",
            linewidth=2,
        )
        plt.hlines(**kwargs)

    # LABELS ==========
    plt.xlabel("yearmonth")
    plt.ylabel("factor scores")

    # TITLE ==========
    plt.title(f"factor {factor} change points (n_cps={N_CPS})")

    # ETC. ==========
    plt.tight_layout()
    plt.show()