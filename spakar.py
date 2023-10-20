##rules 
import csv
from tabulate import tabulate
import os

def Rules(gejala):
    conditions = gejala.split(",")
    map_conditions = {
        "PD01":["GD01", "GD02", "GD03", "GD04", "GD05", "GD06"],
        "PD02":["GD07", "GD08", "GD09", "GD10"],
        "PD03":["GD01", "GD12", "GD16"],
        "PD04":["GD17", "GD18", "GD19", "GD20", "GD21"],
        "PD05":["GD01","GD22", "GD23", "GD24", "GD05", "GD25", "GD26", "GD27", "GD28"],
        "PD06":["GD29", "GD30", "GD31", "GD32"],
        "PD07":["GD01", "GD23", "GD24", "GD05", "GD25", "GD27", "GD28", "GD35", "GD36"],
        "PD08":["GD37", "GD38", "GD39", "GD40"]
        }
    for k,v in map_conditions.items():
        if all(condition in conditions for condition in v):
            result = k
            return result
        else:
            result = "00"
    return result


def menuGejala(filename):
    os.system('clear')
    nGejala = []
    with open(filename) as csvfile:
        data = csv.DictReader(csvfile)
        for i in data:
            nGejala.append(i)
    table_data=[[item["kode"], f"{item['gejala']}"] for item in nGejala]
    headers = ["Kode", "Gejala"]
    print(tabulate(table_data, headers, tablefmt="grid"))
    userInput = input(">> ").upper()
    return userInput

list_kode_gejala = menuGejala("nama_gejala.csv")

nPenyakit = {}
with open("nama_penyakit.csv") as csvfile:
    data = csv.DictReader(csvfile)
    for i in data:
        nPenyakit[i["kode"]]=i["nama"]

hasil_penyakit = Rules(list_kode_gejala)
if hasil_penyakit == "00":
    print("Penyakit Tidak ditemukan")
else:
    print(f"Anda Mengalami {nPenyakit[hasil_penyakit]}")

