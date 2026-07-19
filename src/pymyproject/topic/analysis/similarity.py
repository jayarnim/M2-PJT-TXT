import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# TOPIC SIMILARITY HEATMAP ==========

def main(
    topic_term_mat: np.ndarray, 
    figsize: tuple[int]=(10,8),
):
    # CONSTANTS ==========
    NUM_TOPICS = len(topic_term_mat)
    LABELS = [f"T{i+1}" for i in range(NUM_TOPICS)]
    COLOR_MAP = "coolwarm"

    # DRAWING PAPER ==========
    fig = plt.figure(figsize=figsize)

    # HEATMAP ==========
    similarity = np.corrcoef(topic_term_mat)
    im = plt.imshow(X=similarity, cmap=COLOR_MAP)

    # COLOR BAR ==========
    plt.colorbar(mappable=im, label="correlation")

    # TICKS ==========
    plt.xticks(ticks=range(NUM_TOPICS), labels=LABELS, rotation=45)
    plt.yticks(ticks=range(NUM_TOPICS), labels=LABELS)

    # LABELS ==========
    plt.xlabel("topic number")
    plt.ylabel("topic number")

    # TITLE ==========
    plt.title(f"topic similarity heatmap (k={NUM_TOPICS})")

    # ETC. ==========
    plt.tight_layout()
    plt.show()