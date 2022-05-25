# Lambda-NFA-to-DFA

Fișierul de intrare se numește "date.in". Datele trebuie să fie de forma:

Număr stări, număr tranziții

tranziții (de forma stare inițială, stare finală, simbol tranziție)

stare inițială

număr stări finale, stări finale

Exemplu:</br>
11 12 </br>
0 1 # </br>
1 2 # </br>
2 3 a </br>
3 6 # </br>
6 7 # </br>
7 8 a </br>
8 9 b </br>
9 10 b </br>
1 4 # </br>
4 5 b </br>
5 6 # </br>
0 7 # </br>
0 </br>
1 10 </br>

Simbol pentru lambda este #, în consecință acesta nu poate fi folosit ca simbol de tranziție cu altă semnificație.

La rularea codului se va creea un folder cu imagini ce surprind tranzițiile pas cu pas, iar în folderul în care se găsește main.py se va salva și un videoclip cu denumirea 'videoclip.avi' ce reprezintă un slideshow cu toate imaginile generate.
