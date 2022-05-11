from nltk.corpus import stopwords
import nltk
import re
import pandas as pd


# Make document -> dictionary for cran
def document2dict_cran(document_filename:str):
    nltk.download('stopwords')

    # Read document file to each line and eperate into sentense
    documents = {}

    text = ""
    filename = document_filename
    with open(filename) as file:
        for line in file:
            text = text + line

    # Parse document's context and seperate to words.
    text = text.split(".I ")

    # Remove stop words, useless signs, make corpus of document
    for n in range(1, len(text)):
        sample = text[n]
        sample = sample.split(".W\n")[1]

        sentence = ""
        for l in re.split(r"\)|\(|\,|\.|\/|\?|\!|\n",sample):
            if l: sentence = sentence + l

        # Remove multiple spaces
        for i in range(0,5): sentence = sentence.replace("  ", " ")

        # Seperate by letters
        sentence = sentence.rstrip()
        sentence = sentence.split(" ")

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in sentence if not w.lower() in stop_words]

        # Add document into dictionary var.
        documents[n] = filtered_sentence
    
    return documents




# Make query -> dictionary for cran
def query2dict_cran(query_filename:str):

    # Read query file to each line and eperate into sentense
    queries = {}

    text = ""
    filename = query_filename
    with open(filename) as file:
        for line in file:
            text = text + line

    # Parse query's context and seperate to words.
    text = text.split(".I ")

    # Remove stop words, useless signs, make corpus of document
    for n in range(1, len(text)):

        sample = text[n]

        # order = int(sample[0])*100 + int(sample[1])*10 + int(sample[2])

        sample = sample.split(".W\n")[1]

        sentence = ""
        for l in re.split(r"\)|\(|\,|\.|\/|\?|\!|\n",sample):
            if l: sentence = sentence + l

        # Remove multiple spaces
        for i in range(0,5): sentence = sentence.replace("  ", " ")

        # Seperate by letters
        sentence = sentence.rstrip()
        sentence = sentence.split(" ")

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        filtered_sentence = [w for w in sentence if not w.lower() in stop_words]

        # Add document into dictionary var.
        queries[n] = filtered_sentence
    
    return queries




# Make cranqrel -> DataFrame for cran
def qrel2dict_cran(filename:str, doc_keys:list, query_keys:list):
    # Make Dataframe for qrel
    relDf = pd.DataFrame(
        index = query_keys,
        columns = doc_keys
    )

    relDf = relDf.fillna(0.0)

    # Build qrel table with text parsing
    fn = filename
    with open(fn) as file:
        for line in file:
            line = line.replace("  ", " ")
            qr = int(line.split(" ")[0])
            doc = int(line.split(" ")[1])
            rel = int(line.split(" ")[2])

            # https://github.com/zijiahu/nlp/blob/a4817064832bf03c78dafe13f5906a244c40139c/Cranfield_collection/README.md
            # In cranqrel, it has the value -1
            # In this description, this is not mentioned, so we assumed that these are same as 1
            
            # set -1 to 1
            if rel == -1 : rel = 1

            # save 1, 2, 3, 4, 5 -> 1.0, 0.8, 0.6, 0.4, 0.2
            relDf.loc[qr][doc] = ((6 - rel) * 2) / 10
    
    return relDf