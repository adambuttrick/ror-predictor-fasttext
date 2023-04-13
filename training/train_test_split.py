import sys
import csv
import pandas as pd
from sklearn.model_selection import train_test_split

def create_fasttext_files(f):
	with open(f) as f_in:
		df = pd.read_csv(f, names=['label','affiliation'], skiprows = 1)
		df_trn, df_test = train_test_split(df, test_size=0.2, random_state=42)
		df_trn.to_csv('affiliations.train', sep=' ', header=False, index=False)
		df_test.to_csv('affiliations.valid', sep=' ', header=False, index=False)

if __name__ == '__main__':
	create_fasttext_files(sys.argv[1])
