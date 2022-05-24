import graphviz
import cv2
import numpy as np
from math import ceil
import os

# functia transforma un set intr-un string de forma lista sortata pentru notarea noilor stari compuse
def denumire(lista):
    lista = list(set(lista))
    lista.sort()
    return str(lista)


# functia transforma un string de forma lista sortata intr-o lista
def generare(cuvant):
    cuvant = cuvant[1:-1]
    if cuvant:
        cuvant = [int(x) for x in cuvant.split(", ")]
    return cuvant


# functia determina drumul ce porneste din stareCurenta si are ca proprietate ca are tranzitii identice
# se trateaza diferit lambda de restul tranzitiilor intrucat pentru lambda se ia in considerare si stareCurenta,
# spre deosebire de celelalte unde conteaza doar starea unde poti ajunge
def parcurgere(stareCurenta, simbol, vizitat, drum):
    vizitat[stareCurenta] = 1  # consemnez vizitarea starii pentru a nu parcurge de mai multe ori aceeasi stare
    if simbol == '#':
        drum.add(stareCurenta)
    if stareCurenta in automat and simbol in automat[stareCurenta]:
        for stare in automat[stareCurenta][simbol]:
            if simbol != '#':
                drum.add(stare)
            if vizitat[stare] == 0:
                parcurgere(stare, simbol, vizitat, drum)


# functia construieste DFA-ul
def dfs(stareCurenta):
    # adaug in lista verificare stareCurenta pentru a ma asigura ca nu voi intra intr-o bucla infinita ulterior
    verificare.append(stareCurenta)
    # parcurg lista de tranzitii posibile
    for tranzitie in simbolTranzitii:
        # stareCurenta este transmisa prin parametru ca string. Folosesc functia generare pentru a o transforma in lista
        stareCurenta = generare(stareCurenta)
        stareNoua = set()
        # iau fiecare stare componenta a stariiCurente
        for stare in stareCurenta:
            if stare in automat and tranzitie in automat[stare]:
                # reunesc starile ce apartin drumului generat de o tranzitie specifica pentru toate starile componente
                stareNoua = stareNoua.union(lambdaInchideri[stare][tranzitie])
        test = stareNoua
        for subStare in stareNoua:
            # parcurg starile componente a stariiNoi si reunesc starile ce apartin drumului generat de lambda
            # (lambda inchiderile) a acestora
            if subStare in lambdaInchideri and '#' in lambdaInchideri[subStare]:
                test = test.union(lambdaInchideri[subStare]['#'])
        stareNoua = test
        # transform stareNoua  si stareCurenta din liste in string-uri (pregatesc parametrul pentru apel)
        stareNoua = denumire(list(stareNoua))
        stareCurenta = denumire(stareCurenta)
        # actualizez tranzitiile pentru stareCurenta
        if stareCurenta not in stariDfa:
            stariDfa[stareCurenta] = {tranzitie: stareNoua}
        else:
            stariDfa[stareCurenta][tranzitie] = stareNoua
        # daca starea obtinuta nu a mai fost generata pana acum apelez functia dfs pentru ea
        if stareNoua not in verificare:
            dfs(stareNoua)


fisier = open("date.in", "r")
continutFisier = fisier.read().split("\n")

# Determin valorile lui n si m
valori = continutFisier[0].split()
n = int(valori[0])
m = int(valori[1])

# Construiesc un dicționar de forma
# automat = {stare: {caracter: [stari in care se poate trece prin tranzitia respectiva]}}
automat = {}

# tranzitii
simbolTranzitii = set()

for index1 in range(1, m + 1):
    valori = continutFisier[index1].split()
    simbolTranzitii.add(valori[2])  # determin toate posibilele tranzitii din automat
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

# Construiesc un dicționar in care voi memora pentru fiecare nod drumurile care pornesc din el cu o tranzitie specifica
lambdaInchideri = dict()

simbolTranzitii = list(simbolTranzitii)
# pentru fiecare posibila tranzitie iau toate starile din automat si, in cazul in care tranzitia apare in automat[stare],
# generez pentru starea respectiva un drum cu tranzitia specifica
for tranzitie in simbolTranzitii:
    for stare in automat:
        if tranzitie in automat[stare]:
            vizitat = [0 for x in range(n + 1)]
            drum = set()
            parcurgere(stare, tranzitie, vizitat, drum)
            if stare in lambdaInchideri:
                lambdaInchideri[stare][tranzitie] = list(drum)
            else:
                lambdaInchideri[stare] = {tranzitie: list(drum)}
        # in cazul in care din starea respectiva nu exista nicio tranzitie cu lambda trebuie in continuare sa avem acea stare
        elif tranzitie == '#':
            if stare in lambdaInchideri:
                lambdaInchideri[stare][tranzitie] = [stare]
            else:
                lambdaInchideri[stare] = {tranzitie: [stare]}

# starea initiala a automatului final este format din starile lambda inchiderii starii initiale
stareInitialaDfa = denumire(lambdaInchideri[stareInitiala]['#'])

# automatul final
stariDfa = {stareInitialaDfa: dict()}

# in verificare voi adauga toate starile generate
verificare = list()

# dispare lambda in acest moment al generarii automatului final
simbolTranzitii.remove('#')

dfs(stareInitialaDfa)

# vizualizarea automatului final
f = graphviz.Digraph(format="png")
f.attr(rankdir='LR', size='20')
for stare in stariDfa:
    stari = generare(stare)
    ok = 1
    for valoare in stari:
        # daca starea este compusa dintr-o stare finala va fi incercuita de 2 ori
        if stariFinale[valoare] == 1:
            f.attr('node', shape='doublecircle')
            f.node(stare)
            ok = 0
            break
    # daca starea nu are in componenta sa nicio stare finala o vom incercui o singura data
    if ok == 1:
        f.attr('node', shape='circle')
        f.node(stare)
# realizez tranzitiile
for stare in stariDfa:
    for tranzitie in stariDfa[stare]:
        f.edge(stare, stariDfa[stare][tranzitie], label=f'{tranzitie}')

# marchez starea initiala
f.attr('node', shape='none')
f.node('')
f.edge('', f'{stareInitialaDfa}')

f.view()
