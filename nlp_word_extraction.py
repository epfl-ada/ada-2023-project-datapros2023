# -------------------------------------------------------------------
# STANDARD IMPORTS
import os
import pickle
import pandas as pd
from tqdm import tqdm

# -------------------------------------------------------------------
# SPACY LIBRARY FOR NLP
import spacy

# -------------------------------------------------------------------
# GLOBAL VARIABLES
DATA_PATH = "data/MovieSummaries/"


def load_summaries(data_path: str) -> pd.DataFrame:
    """Loads movie summaries from a file into a pandas DataFrame.

    Args:
        data_path (str): Path to the file with summaries.

    Returns:
        pd.DataFrame: DataFrame with an id and a summary column.
    """
    summaries = []
    with open(data_path, "r", encoding="utf-8") as ps:
        ps_text = ps.readlines()
        for line in ps_text:
            parts_of_line = line.split("\t")
            summaries.append([parts_of_line[0], parts_of_line[1]])
    summaries = pd.DataFrame(summaries, columns=["MovieID", "Summary"])
    return summaries


# -------------------------------------------------------------------
if __name__ == "__main__":
    # If we want to turn off NER and parsing, do it here:
    # nlp = spacy.load("en_core_web_trf", disable=["ner", "parser"])

    # Otherwise, use the full pipeline:
    nlp = spacy.load("en_core_web_trf")

    movie_summaries = load_summaries(DATA_PATH)

    # Create four dictionaries, containing different types of words for
    # further analysis. Keys of dictionaries will be movie ids.
    nouns = {}
    verbs = {}
    descs = {}  # adjectives and adverbs
    all_words = {}

    # Create pipeline
    docs = nlp.pipe(movie_summaries, as_tuples=True)

    # Load dictionaries with appropriate word types.
    # NOTE: This process takes ~40 minutes on my machine, so it is
    # better to save the results for later reusing. -DC
    for doc, context in tqdm(docs, total=len(movie_summaries)):
        doc_id = context["id"]

        nouns[doc_id] = []
        verbs[doc_id] = []
        descs[doc_id] = []
        all_words[doc_id] = []

        for token in doc:
            if token.is_stop:
                continue
            all_words[doc_id].append(token.lemma_)
            if token.pos_ == "NOUN":
                nouns[doc_id].append(token.lemma_)
            elif token.pos_ == "VERB":
                verbs[doc_id].append(token.lemma_)
            elif token.pos_ in ["ADJ", "ADV"]:
                descs[doc_id].append(token.lemma_)

    # Save results.
    with open("nouns.pickle", "wb") as handle:
        pickle.dump(nouns, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open("verbs.pickle", "wb") as handle:
        pickle.dump(verbs, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open("descs.pickle", "wb") as handle:
        pickle.dump(descs, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open("all_words.pickle", "wb") as handle:
        pickle.dump(all_words, handle, protocol=pickle.HIGHEST_PROTOCOL)
