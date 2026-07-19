import pandas as pd
import matplotlib.pyplot as plt


def main(
    scores: pd.DataFrame,
):
    # CONSTANTS ==========
    NUM_FACTORS = scores.shape[-1]
    NROWS = NUM_FACTORS
    NCOLS = 1
    FIGSIZE = (16, 4*NROWS)

    # DRAWING PAPER ==========
    fig, axes = plt.subplots(
        nrows=NROWS, 
        ncols=NCOLS,
        figsize=FIGSIZE,
        squeeze=False,
    )

    # DRAW AX ==========
    for ax, idx in zip(axes.flatten(), range(NUM_FACTORS)):
        y = scores.iloc[:,idx].values

        ax.plot(scores.index.to_timestamp(), y)
        ax.set_title(f"factor {idx+1}")
        ax.grid(alpha=0.3)

    # TITLE ==========
    TITLE = f'factor scores (k={NUM_FACTORS})'
    plt.suptitle(t=TITLE, fontsize=16)

    # ETC. ==========
    plt.tight_layout(rect=[0, 0, 1, 0.99])
    plt.show()