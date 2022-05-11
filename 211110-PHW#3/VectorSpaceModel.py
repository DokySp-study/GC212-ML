
import pandas as pd
import math


# cosine similarity
def cos_sim(d, q):
    
    doc_corpus = set()
    query_corpus = set()

    for i in d.keys():
        doc_corpus.add(i)
    
    for i in q.keys():
        query_corpus.add(i)

    # query, documents 둘 다 있는 단어 찾음
    union_corpus = doc_corpus & query_corpus

    # Calculate cosine similarity
    ## sum(d*q) / ( sqrt(sum(d^2)) * sqrt((sum(q^2)) )
    denominator = 0
    numerator_d = 0
    numerator_q = 0

    for u in union_corpus:
        denominator += d[u] * q[u] 

    for u in union_corpus:
        numerator_d += d[u] * d[u]
    numerator_d = math.sqrt(numerator_d)
    
    for u in union_corpus:
        numerator_q += q[u] * q[u]
    numerator_q = math.sqrt(numerator_q)

    if numerator_d != 0:
        return denominator / (numerator_d * numerator_q)
    else:
        return 0



def get_score(documents:dict, queries:dict, is_freq_weight_with_log = True):


    ### Build inverted index
    # Make query word corpus
    qCorpus = set()
    for q in queries:
        for i in queries[q]:
            qCorpus.add(i)

    # Initialize inverted index with query corpus
    # Inverted index is made by dictionary type. This makes it easy to search.
    inverted_index = {}
    for q in qCorpus:
        inverted_index[q] = []

    # Find the doc number what contain the word in query
    for doc in documents:
        docWords = documents[doc]
        for q in qCorpus:
            if docWords.count(q) != 0:
                inverted_index[q].append(doc)

    # Remove empty inverted index keywords
    ## the words only in query, not in documents
    remove_target_words = []
    for i in inverted_index:
        if len(inverted_index[i]) == 0:
            remove_target_words.append(i)
    for r in remove_target_words:
        inverted_index.pop(r)




    # Build tf table
    ## calculate df -> 잘못구함 (단어가 나오는 문서 수가 아니라, 총 빈도수로 잘못 구함 => 수정필요)
    tf = pd.DataFrame(columns=documents.keys(), index=inverted_index.keys())
    tf = tf.fillna(0)
    ttf = {} # total of term freq.

    for query_word in inverted_index:
        ttfc = 0  # total of term freq.
        # inverted index에서 query에 해당하는 doc # 찾음
        for docIdx in inverted_index[query_word]:
            # Caculate frequency of the word of query from documents
            freq = documents[docIdx].count(query_word)
            tf.loc[query_word][docIdx] = freq
            ttfc = ttfc + freq
        
        ttf[query_word] = ttfc
        



    # Build idf table
    ## log10(doc#/df)
    idf = {}
    N = len(documents)
    for key in ttf:
        word_freq = ttf[key]
        idf[key] = math.log10( N / word_freq )

    # tf x idf
    tfidf = pd.DataFrame(columns=documents.keys(), index=inverted_index.keys())

    # Use formula for weighting
    if is_freq_weight_with_log:
        # frequent weighting
        ## (1+log10(tf)) * idf
        for idf_idx in idf:
            tf_row = []
            for i in tf.loc[idf_idx].to_numpy().tolist():
                if i != 0: tf_row.append( (1 + math.log10(i)) * idf[idf_idx] ) 
                else: tf_row.append(0)
            tfidf.loc[idf_idx] = tf_row
    else:
        # frequent weighting without log
        ## tf * idf
        for idf_idx in idf:
            tfidf.loc[idf_idx] = tf.loc[idf_idx] * idf[idf_idx]




    # Calculate cosine similartiy to scoring
    scores = pd.DataFrame(columns=documents.keys(), index = queries.keys())
    scores = scores.fillna(0.0)

    for query in queries:

        # TF-IDF of the query
        corpus = queries[query]

        # Make list of words what removed duplicated.
        query_vocab = set()
        for c in corpus:
            query_vocab.add(c)
        
        
        # Make query frequency table
        query_freq = {}
        for vocab in query_vocab:
            query_freq[vocab] = corpus.count(vocab)

        # Calculate idf of query
        query_idf_vec = {}
        for qf in query_freq:
            if qf in idf:
                query_idf_vec[qf] = query_freq[qf] * idf[qf]
            else: 
                query_idf_vec[qf] = 0

        # Caculate and save cosine similarity score
        for i in tfidf.columns:
            scores.loc[query, i] = cos_sim(tfidf.loc[:,i].to_dict(), query_idf_vec)




    # Result of score table
    return scores
    