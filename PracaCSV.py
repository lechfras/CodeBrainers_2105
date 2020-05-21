#1: otwracei pliku
f=open("przykladowy.csv", "r", encoding='utf-8')
#"r" - read - odczyt
# "w" write -zapis do pliku - od poczatku
#"a" - append - zapis na koncu pliku

#2:wypisanie
linie = f.readlines()
print(linie[0])

#3: zamkniecie pliku
f.close()

with open("przykladowy.csv", 'r') as dowolne:
    linie = dowolne.readlines()
    print(linie[3])

from csv import DictReader
data=[]

with open("przykladowy.csv", 'r') as f:
    reader=DictReader(f)

    for row in reader:
        data.append(
            {
                "year": int(row["Year"]),
                "score":int(row["Score"]),
                "title":row["Title"]
            }
        )

worst_score=data[0]["score"]
worst_titles =[]
for entry in data:
    if entry["score"] < worst_score:
        worst_score = entry["score"]
        worst_titles = [entry["title"]]
    elif entry ["score"] ==worst_score:
        worst_titles.append(entry["title"])

print(worst_titles)

best_score = data[0]["score"]
best_title = data[0]["title"]
for entry in data:
    if entry["score"] < best_score:
        best_score=entry["score"]
        best_title = entry["title"]

print(f"Najlepszy film RdN to: {best_title} z oceną {best_score}")