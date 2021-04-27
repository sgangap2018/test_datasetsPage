import pandas as pd

#function to dump json file data into a pandas dataframe from which
#the dataset ID (for url) and the column headers for file are extracted
def get_args():
	IDS = []
	COLUMNS = []
	#open json test data into dataframe
	read_file = open("test_data/data_file.json", "r")
	df = pd.read_json(read_file)
	for column_name, item in df.iteritems():
		if item['dataType'] == 'image':
			continue
		else:
			dataset_id = column_name
			column_headers = item['info']['columnNames']
			IDS.append(dataset_id)
			COLUMNS.append(column_headers)
	DATA = zip(IDS, COLUMNS)
	return DATA




