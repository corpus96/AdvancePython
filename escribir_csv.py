import csv

doc = open("archivoW.csv", 'w', newline='')
doc_csv_w = csv.writer(doc)
lista = [["Pedro", 99836], ["UNO", 1000], ["DOS", 20000], ["TRES", 4000], ["CUATRO", 7777]]

#doc_csv_w.writerows(lista)

for x in lista:
    doc_csv_w.writerow(x)

doc.close()