"""Contains functions to run and score pipelines"""

from sklearn.model_selection import cross_validate
from sklearn.model_selection._split import _BaseKFold
from sklearn.pipeline import Pipeline


def cv(
    X,
    y,
    pipeline : Pipeline,
    cross_validator: _BaseKFold, 
    scorer,
):
    """
    Runs RandomizedSearchCV on a give pipeline.

    """


    model : Pipeline = pipeline
    
    scores = cross_validate(
        model,
        X,
        y,
        cv=cross_validator,
        scoring=scorer,
        return_train_score=False,
    )
    return scores
    
    """
    
    acc_score = []
    
    counter = 0
    for train_index , test_index in cross_validator.split(X):
        print(train_index, test_index)
        counter += 1
        X_train , X_test = X.iloc[train_index,:],X.iloc[test_index,:]
        y_train , y_test = y[train_index] , y[test_index]
        
        model.fit(X_train,y_train)
        pred_values = model.predict(X_test)
        
        acc = scorer(pred_values , y_test)
        acc_score.append(acc)
        
    avg_acc_score = sum(acc_score)/counter
    return avg_acc_score
    """    
