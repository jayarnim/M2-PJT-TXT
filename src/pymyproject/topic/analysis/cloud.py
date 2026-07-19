import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer


def word_per_topic(
    topic_term_mat: np.ndarray, 
    vectorizer: CountVectorizer, 
    top_k: int,
):
    WORDS = vectorizer.get_feature_names_out()

    for i, topic in enumerate(topic_term_mat):
        top_words = [
            WORDS[j] 
            for j in topic.argsort()[-top_k:][::-1]
        ]
        print(i+1, top_words)


def wordcloud_per_topic(
    topic_term_mat: np.ndarray, 
    vectorizer: CountVectorizer, 
    nrows: int, 
    ncols: int, 
    figsize: tuple[int],
):
    # CONSTANTS ==========
    NUM_TOPICS = len(topic_term_mat)
    WORDS = vectorizer.get_feature_names_out()
    FONT_PATH = "C:/Windows/Fonts/malgun.ttf"
    BACKGROUND_COLOR = "white"

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
        freq = {
            WORDS[i]: topic_term_mat[idx][i]
            for i in range(len(WORDS))
        }
        kwargs = dict(
            font_path=FONT_PATH,
            background_color=BACKGROUND_COLOR,
        )
        wc = WordCloud(**kwargs).generate_from_frequencies(freq)

        ax.imshow(wc)
        ax.axis("off")
        ax.set_title(f"Topic {idx+1}")

    # DEACTIVATE AX ==========
    for ax in axes.flatten()[NUM_TOPICS:]:
        ax.axis("off")

    # ETC. ==========
    plt.tight_layout()
    plt.show()