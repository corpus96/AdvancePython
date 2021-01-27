import csv

doc = open("archivoW.csv", "r") # r means read

doc_csv = csv.reader(doc)

for(name, number) in doc_csv:
    print(name, number)

doc.close()