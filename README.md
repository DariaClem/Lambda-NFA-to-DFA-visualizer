# Lambda-NFA-to-DFA

Fișierul de intrare se numește "date.in". Datele trebuie să fie de forma:

Număr stări, număr tranziții

tranziții (de forma stare inițială, stare finală, simbol tranziție)

stare inițială

număr stări finale, stări finale

Exemplu:

11 12

0 1 #

1 2 #

2 3 a

3 6 #

6 7 #

7 8 a

8 9 b

9 10 b

1 4 #

4 5 b

5 6 #

0 7 #

0

1 10

Simbol pentru lambda este #, în consecință acesta nu poate fi folosit ca simbol de tranziție cu altă semnificație.
