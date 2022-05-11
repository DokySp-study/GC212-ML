import pandas as pd

def model_score(predict, target, num_of_doc_k = 100, similarity_thresh = 0.4, f_beta = 1):

    ans_pred = pd.DataFrame({
        "index":[],
        "answer": [],
        "predict":[],
        "score":[]
    })
    ans_pred.fillna(0)

    # Specify result
    sorted_doc = predict.sort_values(ascending=False)
    sorted_doc_score = sorted_doc.head(num_of_doc_k)
    sorted_doc = sorted_doc >= similarity_thresh
    sorted_doc = sorted_doc.head(num_of_doc_k)

    target = target >= similarity_thresh

    for i in range(0, len(sorted_doc)):
        ans_pred.loc[i, 'index'] = sorted_doc.index[i]
        ans_pred.loc[i, 'predict'] = sorted_doc.iloc[i]
        ans_pred.loc[i, 'answer'] = target.loc[ int(sorted_doc.index[i]) ]
        ans_pred.loc[i, 'score'] = sorted_doc_score.iloc[i]



    # Calculate Error
    ## True Positive
    tp = ans_pred[ans_pred["answer"] == True]
    tp = tp[tp["predict"] == True]
    tp = len(tp)

    ## Type 1 error (False Positive)
    fp = ans_pred[ans_pred["answer"] == False]
    fp = fp[fp["predict"] == True]
    fp = len(fp)

    ## Type 2 error (False Negative)
    fn = ans_pred[ans_pred["answer"] == True]
    fn = fn[fn["predict"] == False]
    fn = len(fn)



    ## Precision
    ### TP / (TP+FP)
    ### TP / All # of pred. True
    precision = 0
    if tp + fp != 0: 
        precision = tp / ( tp + fp )

    # Recall
    # TP / (TP+FN)
    # TP / All # of True
    recall = 0
    if tp + fn != 0: 
        recall = tp / ( tp + fn )


    def f_score(precision, recall, beta = f_beta):
        return ((beta*beta + 1) * precision * recall) / (beta*beta*precision + recall)

    f_sc = 0
    if precision + recall != 0:
        f_sc = f_score(precision, recall, beta = 1)
    
    class result:
        fn

    res = result()
    res.precision = precision
    res.recall = recall
    res.f_sc = f_sc
    res.tp = tp
    res.fp = fp
    res.fn = fn
    

    return res
