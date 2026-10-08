# Silly Fishing Shenanigans
Pythonilla toteutettu tekstipohjainen CLI peli, joka on tehty projektityönä Metropolian Ohjelmisto 1 kurssille.

## Pelin idea
Pelin perusideana on, että kalastaja (pelaaja) löytää sattumalta hyvin erikoisen järven, joka on täynnä hölmömpiä kaloja. Kalastaja viettää järvellä 7 päivää. Tavoitteena on pyydystää ainutlaatuisia kalalajikkeita ja viedä ne mukanaan myytäväksi kalamarkkinoille.

## Tavoite
Pelaajan päämääränä on selvitä viikon kalastusreissusta ja tehdä mahdollisimman paljon voittoa. Liikakalastus kuitenkin rasittaa paikallista luontoa, ja voi seurata kalastajalle sakkoja. Pelaajan on siis jatkuvasti tasapainoiltava voiton maksimoimisen ja luonnon suojelemisen välillä.

Pelaajalla on pelissä kolme vaihtoehtoista polkua:
1. Kalastaa vastuullisesti ja ylläpitää tasapainoa voiton tavoittelun ja kestävän kalastuksen välillä.
2. Ylikalastaa ahneuksissaan, kerätä jättituotot ja toivoa, että ne kattavat massiiviset ympäristösakot.
3. Olla pasifisti, nukkua koko viikko ja olla tekemättä yhtään mitään.
 
Kun pelaaja saa kalan, sillä on tietty paino. Alle 1 kg painavat kalat on luokiteltu pieniksi. Pelaajalla on 2 vaihtoehtoa, pitääkö kalaa myyntiä varten vai vapauttaako sen järveen kasvamaan. Jos pelaaja pitää alamittaiset kalat, järven kalakanta ei pääse uusiutumaan. Pelin lopussa pelaajan saalis analysoidaan ja jokaisesta pidetystä pikkukalasta annetaan sakko, joka vähennetään kokonaistuotosta. 


## Toimintaperiaatteet ja toiminnallisuudet
Peli on jaettu modulaarisesti `main.py` tiedostoon ja pelilogiikasta vastaavaan `game` moduuliin.

**Keskeiset toiminnallisuudet:**
1. Luokat `Player`, `Lake` ja `Fish` tilan hallintaan varten. Jokainen kala on uniikki olio omine ominaisuuksineen (nimi, paino, arvo, harvinaisuus).
2. Kaloilla on eri harvinaisuusasteita, jotka vaikuttavat niiden rahalliseen arvoon. Pelin lopussa lasketaan bruttotulot, ympäristösakot ja lopullinen nettotulos.
3.  Pelaaja voi tallentaa pelinsä tilan kesken viikon. Peli muuntaa oliot JSONiin käyttäen sanakirjoja. Tiedostot nimetään dynaamisesti pelaajan nimen mukaan esim. "Meow" pelaajalle `Meow_save.json`. Käynnistyksen yhteydessä peli etsii automaattisesti pelaajan nimellä tallennusta samasta kansiosta ja tarjoaa mahdollisuutta jatkaa sitä tallennusta.
4. Peli käyttää `try/except`, joka nappaa virheelliset syötteet. Päävalikko hyödyntää `match/case`.
5. Peli lukee esittelytekstit ja ohjeet ulkoisista `.txt` tieodostoista.

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
