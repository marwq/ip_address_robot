import csv


with open('top-level-domain-names.csv', 'r', encoding='utf8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    domains = {
        row['Domain']: (row['Type'], row['Sponsoring Organisation'])
        for row in csvreader
    }