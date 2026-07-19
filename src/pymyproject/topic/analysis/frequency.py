import pandas as pd
import matplotlib.pyplot as plt


# ANNUAL FREQUENCY PER TOPIC ==========

def main(
    doc_topic_mat: pd.DataFrame, 
    top_k: int, 
    nrows: int, 
    ncols: int, 
    figsize: tuple[int],
):
    # DATE ==========
    doc_topic_mat.index = pd.to_datetime(doc_topic_mat.index)
    doc_topic_mat = doc_topic_mat.sort_index(ascending=True)
    date = doc_topic_mat.index

    # CONSTANTS ==========
    NUM_TOPICS = doc_topic_mat.shape[-1]
    YEAR_MIN = date.year.min()
    YEAR_MAX = date.year.max()

    # DRAWING PAPER ==========
    fig, axes = plt.subplots(
        nrows=nrows, 
        ncols=ncols, 
        figsize=figsize,
        squeeze=False,
    )

    # ITERABLE OBJ ==========
    ITERABLE = zip(
        axes.flatten(), 
        range(NUM_TOPICS),
    )

    # DRAW PER AX ==========
    for ax, idx in ITERABLE:
        TOP_IDX = doc_topic_mat.iloc[:, idx].argsort()[::-1][:top_k]
        TOP_DATE = date[TOP_IDX].year
        COUNTS = TOP_DATE.value_counts().sort_index()

        ax.plot(COUNTS.index, COUNTS.values, marker='o')
        ax.set_xlim(YEAR_MIN, YEAR_MAX)
        ax.set_title(f'Topic {idx+1}')
        ax.grid(True)

    # DEACTIVATE AX ==========
    for ax in axes.flatten()[NUM_TOPICS:]:
        ax.axis("off")

    # TITLE ==========
    TITLE = f'yearly counts of top {top_k} topic-dominant documents (k={NUM_TOPICS})'
    plt.suptitle(t=TITLE, fontsize=16)

    # ETC. ==========
    plt.tight_layout(rect=[0, 0, 1, 0.99])
    plt.show()