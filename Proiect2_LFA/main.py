def parcurgere(stareCurenta, caracter):
    vizitat = [0 for index4 in range(n + 1)]
    vizitat[stareCurenta] = 1
    drum = [stareCurenta]

    if '#' in automat[stareCurenta]:
        for stare in automat[stareCurenta][caracter]:
            if vizitat[stare] == 0:
                drum.extend(parcurgere(stare, caracter))
    lambdaInchideri[stareCurenta] = list(set(drum))
    return drum


fisier = open("date.in", "r")
continutFisier = fisier.read().split("\n")

# Determin valorile lui n si m
valori = continutFisier[0].split()
n = int(valori[0])
m = int(valori[1])

# Construiesc un dicționar de forma
# automat = {stare: {caracter: [stari in care se poate trece prin tranzitia respectiva]}}
automat = {}

for index1 in range(1, m + 1):
    valori = continutFisier[index1].split()
    if int(valori[0]) in automat:  # verific dacă starea curentă există în automat
        if valori[2] in automat[int(valori[0])]:  # verific dacă tranziția există pentru starea curentă
            automat[int(valori[0])][valori[2]].append(int(valori[1]))
        else:
            automat[int(valori[0])][valori[2]] = [int(valori[1])]
    else:
        automat[int(valori[0])] = {valori[2]: [int(valori[1])]}

# Indicele stării inițiale
stareInitiala = int(continutFisier[m + 1])

valori = [int(element) for element in continutFisier[m + 2].split()]
# Memorez numărul de stări finale
nrStariFinale = valori[0]
# Construiesc o listă în care voi consemna existența stărilor finale, asemănător unui vector caracteristic
stariFinale = [0 for index2 in range(n + 1)]
for element in valori[1:]:
    stariFinale[element] = 1

# Construiesc un dicționar de forma
# drumParcurs = {stare: [stari in care se poate trece prin lambda-tranzitii]}
lambdaInchideri = dict()
for index3 in range(n + 1):
    lambdaInchideri[index3] = list()

# Construiesc o listă în care voi consemna trecerea printr-o stare în parcurgere
# vizitat = [0 for index4 in range(n + 1)]

for stare in automat:
    parcurgere(stare, '#')

print(lambdaInchideri)

for stare in lambdaInchideri:
    if lambdaInchideri[stare]:
        stari = list(automat[stare].keys())
