
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer 
import numpy as np
import pandas as pd
import re


df = pd.DataFrame({
    "fake": [0.0, 0.0, 0.0, 0.0, 0.0],
    "news": [0.0, 0.0, 0.0, 0.0, 0.0],
    "corona": [0.0, 0.0, 0.0, 0.0, 0.0],
    "vaccine": [0.0, 0.0, 0.0, 0.0, 0.0],
    "score": [0.0, 0.0, 0.0, 0.0, 0.0],
})

# Read all text file. Each text file have Document
for i in range(0,5):

    # Read file to each line and eperate into sentense
    sentences = list()
    filename = "doc" + str(i+1) + ".txt"
    with open(filename) as file:
        for line in file:
            for l in re.split(r"\.\s|\?\s|\!\s|\n",line):
                if l: sentences.append(l)

    # Remove stop words and make count vector
    cvec = CountVectorizer(stop_words='english')
    sf = cvec.fit_transform(sentences)

    # tf*idf calculation
    transformer = TfidfTransformer(smooth_idf=False)
    transformed_weights = transformer.fit_transform(sf)

    # Evaluate result (weight value)
    weights = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
    weights_df = pd.DataFrame({'term': cvec.get_feature_names_out(), 'weight': weights})

    dft = weights_df.sort_values(by='weight',ascending=False)

    # Extract terms what is included in query to find cosine similarity
    fake = 0
    news = 0
    corona = 0
    vaccine = 0

    if len(dft[dft["term"] == "fake"]) > 0:
        fake = float(dft[dft["term"] == "fake"]["weight"])
    if len(dft[dft["term"] == "news"]) > 0:
        news = float(dft[dft["term"] == "news"]["weight"])
    if len(dft[dft["term"] == "corona"]) > 0:
        corona = float(dft[dft["term"] == "corona"]["weight"])
    if len(dft[dft["term"] == "vaccine"]) > 0:
        vaccine = float(dft[dft["term"] == "vaccine"]["weight"])

    # Save score data of each Document
    df.loc[i] = [
        fake,
        news,
        corona,
        vaccine,
        fake+news+corona+vaccine,
    ]

# Sort by score of Document's cosine similarity with query
df.sort_values(by="score", inplace=True, ascending=False)

# Print results
print("\nRanked list:")
for i in df.index.to_list():
    print("Document ", end="")
    print(i+1)


