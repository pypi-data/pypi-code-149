import huble
from huble import Dataset
def run_experiment(experiment):
	model = huble.sklearn.random_forest(parameters={'criterion': 'gini', 'n_estimators': 70, 'max_depth': 2, 'max_leaf_nodes': 10, 'random_state': None})
	data = Dataset('https://ipfs.filebase.io/ipfs/QmRspeqXi9J2PVTmXYwMaBif9dYWVkNhM8EFomUAfajnT1').dataframe
	data = huble.sklearn.drop_duplicates(data=data,parameters={'subset': [], 'keep': 'first', 'inplace': False, 'ignore_index': False})
	data = huble.sklearn.remove_mismatch_data(data=data, parameters={'exceptions': []})
	data = huble.sklearn.remove_outliers(data=data,columns=['Fare'])
	data = huble.sklearn.drop_rows_columns(data=data,parameters={'labels': ['PassengerId', 'Pclass', 'Name'], 'axis': 1, 'inplace': False, 'errors': 'raise'})
	data = huble.sklearn.clean_data(data=data)
	training_dataset, test_dataset = huble.sklearn.train_test_split(data=data,parameters={'test_size': 0.8})
	Model = huble.sklearn.train_model(data=training_dataset, model=model, column='Survived')
	metrics = huble.sklearn.evaluate_model(model=Model, test_dataset=test_dataset, target_column= 'Survived', task_type='classification' )
	experiment.upload_metrics(metrics)