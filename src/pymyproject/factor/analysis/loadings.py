import pandas as pd
import matplotlib.pyplot as plt


def main(
    loadings: pd.DataFrame, 
    figsize: tuple[int],
):
    # CONSTANTS ==========
    COLOR_MAP = "coolwarm"
    NUM_FACTORS = loadings.shape[-1]

    # DRAWING PAPER ==========
    fig = plt.figure(figsize=figsize)

    # HEATMAP ==========
    im = plt.imshow(X=loadings.values, aspect="auto", cmap=COLOR_MAP)

    # COLOR BAR ==========
    plt.colorbar(im, label="loadings")

    # TICKS ==========
    plt.xticks(ticks=range(loadings.shape[1]), labels=loadings.columns)
    plt.yticks(ticks=range(loadings.shape[0]), labels=loadings.index)

    # ANNOTATION ==========
    for i in range(loadings.shape[0]):
        for j in range(loadings.shape[1]):
            kwargs = dict(
                x=j,
                y=i,
                s=f"{loadings.iloc[i, j]:.2f}",
                ha="center", 
                va="center", 
                fontsize=10,
            )
            plt.text(**kwargs)

    # LABELS ==========
    plt.xlabel("factor")
    plt.ylabel("topic")

    # TITLE ==========
    plt.title(f"factor loadings heatmap (k={NUM_FACTORS})")

    # ETC. ==========
    plt.tight_layout()
    plt.show()