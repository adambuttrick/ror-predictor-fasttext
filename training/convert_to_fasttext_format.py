import sys
import csv

def convert(f):
	outfile  = 'converted.csv'
	entries = []
	with open(f) as f_in:
		reader = csv.DictReader(f_in)
		for row in reader:
			ror_id = row['label']
			affiliation = row['text'].lower()
			label = '__label__' + ror_id
			with open(outfile, 'a') as f_out:
				writer = csv.writer(f_out)
				writer.writerow([label, affiliation])

if __name__ == '__main__':
	convert(sys.argv[1])