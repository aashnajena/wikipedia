import csv

lt = ["animalsOutput.csv", "actorsOutput.csv", "countriesOutput.csv", "languageOutput.csv", "booksOutput.csv"]

with open("train-data.csv", "w") as wf:
    csvwriter = csv.writer(wf)
    csvwriter.writerow(["id", "text"])
    for fl in lt:
        with open(fl, "r") as csvfile:
            csvreader = csv.reader(fl)
            for row in csvreader:
                csvwriter.writerow(row)
