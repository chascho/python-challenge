import os
import csv
poll_path = os.path.join("Resources", "election_data.csv")

votes_cast = []
candidates = []
total_votes = 0

with open(poll_path, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter",")

    csv_header = next(csvfile)
    print("CSV Header: {csv header}")

    for row in csvreader:
        total_votes += 

