# Silly Fishing Shenanigans

Tämä on Pythonilla toteutettu tekstipohjainen CLI peli, joka on tehty projektityönä Metropolian Ohjelmisto 1 -kurssille. 

Pelin perusideana on, että kalastaja (pelaaja) löytää sattumalta hyvin erikoisen järven, joka on täynnä toinen toistaan hölmömpiä kaloja. Kalastaja viettää järvellä 7 päivää tavoitteenaan pyydystää mahdollisimman monta erilaista kalalajia ja viedä ne mukanaan ihmisten ilmoille voittoa tavoitellen. 

Liikakalastus kuitenkin rasittaa paikallista luontoa, ja siitä voi seurata kalastajalle tuntuvia sakkoja. Siksi pelin toisena tavoitteena on välttää pienten kalojen ylikalastusta.

Pelaajalla on kolme vaihtoehtoista polkua:
1. Kalastaa vastuullisesti ja ylläpitää tasapainoa voiton tavoittelun ja kestävän kalastuksen välillä.
2. Ylikalastaa ahneuksissaan ja kääriä sekä voittoja, että sakkoja.
3. Olla pasifisti ja olla tekemättä yhtään mitään (tylsää).

## Projektin rakenne

```text
peliprojekti/
├── game/
│   ├── __init__.py
│   ├── player.py
│   ├── lake.py
│   ├── fish.py
│   └── menu.py
├── main.py
├── intro.txt
├── instructions.txt
└── readme.md
