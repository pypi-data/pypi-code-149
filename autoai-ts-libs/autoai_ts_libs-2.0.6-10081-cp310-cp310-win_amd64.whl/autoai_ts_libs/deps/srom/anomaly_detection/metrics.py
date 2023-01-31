from sklearn.metrics import f1_score, accuracy_score, balanced_accuracy_score, precision_score, recall_score, roc_auc_score

def roc_auc_score_with_time_column(y_true, y_pred, time_column):
    y_true_ = y_true[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    y_pred_ = y_pred[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    return roc_auc_score(y_true_, y_pred_)

def f1_score_with_time_column(y_true, y_pred, time_column):
    y_true_ = y_true[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    y_pred_ = y_pred[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    return f1_score(y_true_, y_pred_)

def accuracy_score_with_time_column(y_true, y_pred, time_column):
    y_true_ = y_true[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    y_pred_ = y_pred[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    return accuracy_score(y_true_, y_pred_)

def balanced_accuracy_score_with_time_column(y_true, y_pred, time_column):
    y_true_ = y_true[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    y_pred_ = y_pred[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    return balanced_accuracy_score(y_true_, y_pred_)

def precision_score_with_time_column(y_true, y_pred, time_column):
    y_true_ = y_true[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    y_pred_ = y_pred[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    return precision_score(y_true_, y_pred_)

def recall_score_with_time_column(y_true, y_pred, time_column):
    y_true_ = y_true[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    y_pred_ = y_pred[:, [i for i in range(y_pred.shape[1]) if i not in time_column]]
    return recall_score(y_true_, y_pred_)
