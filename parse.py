import csv
import argparse
## uncomment if posting to a RESTful API at end of script
#import requests

parser = argparse.ArgumentParser(description='Process a CSV to a json dictionary')
parser.add_argument('--csvFile')

args = parser.parse_args()

with open(args.csvFile) as f:
    # omit the delimiter value if you just want to use commas
    # the DictReader assumes the first line is the header/field names
    reader = csv.DictReader(f,delimiter='|')
    updates = list(reader)

payload = {'csvEntries' : []}

for line in updates:
    if (len(line) > 0):
        payload['entries'].append(line)
    else:
        continue

## Additional: uncomment the lines below to send the parsed payload to post json to a RESTful api
#url = 'some_API_URL'
#response = requests.post(url, data=payload)

#print response
