import sys
import re
import csv
from predictor import Predictor

# Create class instance with path to model files
PREDICTOR = Predictor('')

def parse_and_predict(f):
	confidence = 0.85
	outfile = 'test_results.csv'
	with open(outfile, 'w') as f_out:
		writer = csv.writer(f_out)
		writer.writerow(['ror_id', 'affiliation', 'predicted_ror_id', 'ratio' ,'match'])
	with open(f, 'r+', encoding='utf-8-sig') as f_in:
		reader = csv.DictReader(f_in)
		for row in reader:
			ror_id = row['ror_id']
			affiliation = row['affiliation']
			prediction = PREDICTOR.predict_ror_id(affiliation, confidence)
			if prediction is not None:
				match = 'Y' if prediction[0] == ror_id else 'N'
				with open(outfile, 'a') as f_out:
					writer = csv.writer(f_out)
					writer.writerow(list(row.values()) + prediction + [match])
			else:
				with open(outfile, 'a') as f_out:
					writer = csv.writer(f_out)
					writer.writerow(list(row.values()) + ['', '', 'NULL'])

if __name__ == '__main__':
	parse_and_predict(sys.argv[1])