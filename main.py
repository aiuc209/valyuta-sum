valyuta_summalari = [100, 200, 300]
kurslar = [1.2, 1.5, 1.8]

eur_summalari = [summa / kurs for summa, kurs in zip(valyuta_summalari, kurslar)]

print(eur_summalari)
