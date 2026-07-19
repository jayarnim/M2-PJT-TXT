import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def compare(
    scores: dict[int, np.float64], 
    figsize: tuple[int],
):
    X = range(len(scores))
    Y = list(scores.values())
    LABELS = list(scores.keys())

    # DRAWING PAPER ==========
    fig = plt.figure(figsize=figsize)

    # DRAW PLOT ==========
    plt.plot(*(X, Y), marker='o')

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
    plt.xlabel("number of topics")
    plt.ylabel("coherence score")

    # TITLE ==========
    plt.title("coherence score by number of topics")

    # ETC. ==========
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def per_topic(
    scores: list[np.float64], 
    figsize: tuple[int],
):
    X = range(len(scores))
    Y = scores
    LABELS = [f"T{i+1}" for i in range(len(scores))]

    # DRAWING PAPER ==========
    fig = plt.figure(figsize=figsize)

    # DRAW PLOT ==========
    plt.bar(x=X, height=Y)

    # TICKS ==========
    plt.xticks(ticks=X, labels=LABELS, rotation=45)

    # BASE SCORE ==========
    plt.axhline(y=0.6, color="red")

    # ANNOTATION ==========
    for x, y in zip(X, Y):
        kwargs = dict(
            x=x, 
            y=y+0.01, 
            s=f"{y:.2f}", 
            ha="center", 
            rotation=50,
        )
        plt.text(**kwargs)

    # LABEL ==========
    plt.xlabel("topic number")
    plt.ylabel("coherence score")

    # TITLE ==========
    plt.title(f"coherence score per topic (k={len(scores)})")

    # ETC. ==========
    plt.tight_layout()
    plt.show()