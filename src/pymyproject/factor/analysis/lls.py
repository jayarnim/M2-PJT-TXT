import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main(
    lls: dict[int, np.float64], 
    figsize: tuple[int],
):
    X = range(len(lls))
    Y = list(lls.values())
    LABELS = list(lls.keys())

    # DRAWING PAPER ==========
    fig = plt.figure(figsize=figsize)

    # DRAW PLOT ==========
    plt.plot(X, Y, marker='o')

    # TICKS ==========
    plt.xticks(ticks=X, labels=LABELS)

    # ANNOTATION ==========
    for x, y in zip(X, Y):
        kwargs = dict(
            x=x, 
            y=y+0.001, 
            s=f"{y:.4f}", 
            ha="center", 
            rotation=50,
        )
        plt.text(**kwargs)

    # LABEL ==========
    plt.xlabel("number of factors")
    plt.ylabel("log likelihood")

    # TITLE ==========
    plt.title("log likelihood by number of factors")

    # ETC. ==========
    plt.grid(True)
    plt.tight_layout()
    plt.show()