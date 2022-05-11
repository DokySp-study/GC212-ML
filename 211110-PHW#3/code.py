import VectorSpaceModel as vc
import file_to_dict as ftd
import pandas as pd
import scoring


# Conver document to dictionary type
documents = ftd.document2dict_cran("data/cran.all.1400.txt")

# Conver query to dictionary type
queries = ftd.query2dict_cran("data/cran.qry.txt")

# Conver cranqrel to DataFrame
relDF = ftd.qrel2dict_cran("data/cranqrel.txt", doc_keys=documents.keys(), query_keys=queries.keys())

# Calculate cosine similarity score with vector space model
print("\nCreate cosine similarity score table")
scoreDF = vc.get_score(documents, queries, is_freq_weight_with_log = True)
print()



# Find best parameter what has best precision and recall value.
print("Find best parameter")

# Number of documents
k = [50, 100, 150, 200, 250, 300]
# Similarity threshold
thresh = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

res = pd.DataFrame({
    "k": [],
    "thresh": [],
    "precision": [],
    "recall": [],
    "f1_avg": [],
})


idx = 0

for k_idx in k:
    for t_idx in thresh:

        precision_avg = 0
        recall_avg = 0
        f1_avg = 0
        count = 0

        for q_idx in range(1, len(queries) + 1):
            predict = scoreDF.loc[q_idx]
            target = relDF.loc[q_idx]

            result = scoring.model_score(predict, target, num_of_doc_k = k_idx, similarity_thresh = t_idx)
            
            precision_avg += result.precision
            recall_avg += result.recall
            f1_avg += result.f_sc

            count += 1

        res.loc[idx, "k"] = k_idx
        res.loc[idx, "thresh"] = t_idx
        res.loc[idx, "precision"] = precision_avg/count
        res.loc[idx, "recall"] = recall_avg/count
        res.loc[idx, "f1_avg"] = f1_avg/count   

        idx += 1
        print(idx, end="")
        print(" / 42")





## Print Result ======================================
# Sorted by precision
print("Best precision's option")
res = res.sort_values("precision", ascending=False)
print(res.head(5))
print()

# Sorted by recall 
print("Best recall's option")
res = res.sort_values("recall", ascending=False)
print(res.head(5))
print()

# Sorted by f1 score
print("Best F1 score's option")
res = res.sort_values("f1_avg", ascending=False)
print(res.head(5))
print()



# Print result document by query and precision, recall, and F1 Score
print("Results")
print("\n========================")
print("Parameter ( k: 50, thresh: 0.5 )")
similarity_thresh = 0.5
doc_k = 50

for i in range(1, len(queries) + 1):
    predict = scoreDF.loc[i]
    predict = predict.sort_values(ascending=False)
    predict = predict.drop(predict[predict < similarity_thresh].index)
    predict = predict.head(doc_k)
    predict = predict.index.tolist()
    print("* Query ", end=str(i))

    pred = scoreDF.loc[i]
    target = relDF.loc[i]
    result = scoring.model_score(pred, target, num_of_doc_k = doc_k, similarity_thresh = similarity_thresh)
    print(" < Precision: ", end="")
    print(result.precision, end="")
    print(" · Recall: ", end="")
    print(result.recall, end="")
    print(" · F1 Score: ", end="")
    print(result.f_sc, end=" >\n")

    print(" · result (document id): ", end="")
    print(predict)



# Print result document by query and precision, recall, and F1 Score
print("\n========================")
print("Parameter ( k: 100, thresh: 0.2 )")
similarity_thresh = 0.2
doc_k = 100

for i in range(1, len(queries) + 1):
    predict = scoreDF.loc[i]
    predict = predict.sort_values(ascending=False)
    predict = predict.drop(predict[predict < similarity_thresh].index)
    predict = predict.head(doc_k)
    predict = predict.index.tolist()
    print(" · Query ", end=str(i))

    pred = scoreDF.loc[i]
    target = relDF.loc[i]
    result = scoring.model_score(pred, target, num_of_doc_k = doc_k, similarity_thresh = similarity_thresh)
    print(" < Precision: ", end="")
    print(result.precision, end="")
    print(" · Recall: ", end="")
    print(result.recall, end="")
    print(" · F1 Score: ", end="")
    print(result.f_sc, end=" >\n")

    print(" · result (document id): ", end="")
    print(predict)
