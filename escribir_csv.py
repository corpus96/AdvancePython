import csv

doc = open("archivoW.csv", "w")
doc_csv_w = csv.writter(doc)
lista = [["Pedro", 99836], ["UNO", 1000], ["DOS", 20000], ["TRES", 4000], ["CUATRO", 7777]]

doc_csv_w.writerow
