# Grzyby - PSZT - projekt 2

## Analiza zbioru

Bardzo dużo informacji na temat zbioru grzybów i ich właściwości znajdziemy w pliku `assets/agaricus-lepiota.names`.
Można wyczytać, że atrybuty `odor`, `spore-print-color`, `stalk-surface-below-ring`, `habitat`, `cap-color` są bardzo silnie klasyfikujące.
A mianowicie drzewo decyzyjne które wyglądało by tak: `spore-print-color=green`, daje błąd na poziomie 0.59%, co sprawia, że drzewo powinno być raczej niewielkie.

## Wyniki

W zadaniu zaimplementowano dwa algorytmy ID3 i C45, ten pierwszy jest częścią tego drugiego.

### Pierwsze wyniki

Na początku uruchomiliśmy algorytmy w celu ich porównania, i aby zobaczyć jak wyglądają drzewa:

#### ID3

```bash
odor
 ┣━ almond -> edible
 ┣━ anise -> edible
 ┣━ creosote -> poisonous
 ┣━ fishy -> poisonous
 ┣━ foul -> poisonous
 ┣━ musty -> poisonous
 ┣━ none -> spore-print-color
 ┃  ┣━ black -> edible
 ┃  ┣━ brown -> edible
 ┃  ┣━ buff -> edible
 ┃  ┣━ chocolate -> edible
 ┃  ┣━ green -> poisonous
 ┃  ┣━ orange -> edible
 ┃  ┣━ purple -> edible
 ┃  ┣━ white -> gill-size
 ┃  ┃  ┣━ broad -> edible
 ┃  ┃  ┗━ narrow -> stalk-surface-above-ring
 ┃  ┃     ┣━ fibrous -> edible
 ┃  ┃     ┣━ scaly -> poisonous
 ┃  ┃     ┣━ silky -> poisonous
 ┃  ┃     ┗━ smooth -> cap-color
 ┃  ┃        ┣━ brown -> edible
 ┃  ┃        ┣━ buff -> edible
 ┃  ┃        ┣━ cinnamon -> edible
 ┃  ┃        ┣━ gray -> edible
 ┃  ┃        ┣━ green -> edible
 ┃  ┃        ┣━ pink -> edible
 ┃  ┃        ┣━ purple -> edible
 ┃  ┃        ┣━ red -> edible
 ┃  ┃        ┣━ white -> poisonous
 ┃  ┃        ┗━ yellow -> edible
 ┃  ┗━ yellow -> edible
 ┣━ pungent -> poisonous
 ┗━ spicy -> poisonous

Process finished with exit code 0

```

#### C45

```bash
odor
 ┣━ almond -> edible
 ┣━ anise -> edible
 ┣━ creosote -> poisonous
 ┣━ fishy -> poisonous
 ┣━ foul -> poisonous
 ┣━ musty -> poisonous
 ┣━ none -> spore-print-color
 ┃  ┣━ black -> edible
 ┃  ┣━ brown -> edible
 ┃  ┣━ buff -> edible
 ┃  ┣━ chocolate -> edible
 ┃  ┣━ green -> poisonous
 ┃  ┣━ orange -> edible
 ┃  ┣━ purple -> edible
 ┃  ┣━ white -> gill-size
 ┃  ┃  ┣━ broad -> edible
 ┃  ┃  ┗━ narrow -> stalk-surface-above-ring
 ┃  ┃     ┣━ fibrous -> edible
 ┃  ┃     ┣━ scaly -> poisonous
 ┃  ┃     ┣━ silky -> poisonous
 ┃  ┃     ┗━ smooth -> cap-color
 ┃  ┃        ┣━ brown -> edible
 ┃  ┃        ┣━ buff -> edible
 ┃  ┃        ┣━ cinnamon -> edible
 ┃  ┃        ┣━ gray -> edible
 ┃  ┃        ┣━ green -> edible
 ┃  ┃        ┣━ pink -> edible
 ┃  ┃        ┣━ purple -> edible
 ┃  ┃        ┣━ red -> edible
 ┃  ┃        ┣━ white -> poisonous
 ┃  ┃        ┗━ yellow -> edible
 ┃  ┗━ yellow -> edible
 ┣━ pungent -> poisonous
 ┗━ spicy -> poisonous
```

#### Pierwsze wnioski

Jak widać różnic brak.
Jest to spowodowane wcześniej opisanymi silnie klasyfikującymi atrybutami.
Dlatego ID3 było wstanie na tyle się sklasyfikować, że C4.5 nie miał możliwości zadziałać na tak mały drzewie.

### Dzielenie zbioru

Postanowiliśmy podzielić zbiór na treningowy i testujący.
Wyniki poniżej:

| Zbiór treningowy | Zbiór testujący | Wynik ID3 | Wynik C4.5 |
| --- | --- | --- | --- |  
| [ 0 : 100 ] | [ 101 : 8123 ] | 0.456245325355273 | 0.456245325355273 | 
| [ 0 : 200 ] | [ 201 : 8123 ] | 0.46200454430699317 | 0.46200454430699317 | 
| [ 0 : 300 ] | [ 301 : 8123 ] | 0.4679110201994375 | 0.4679110201994375 | 
| [ 0 : 400 ] | [ 401 : 8123 ] | 0.473970473970474 | 0.473970473970474 | 
| [ 0 : 500 ] | [ 501 : 8123 ] | 0.48018892679086855 | 0.48018892679086855 | 
| [ 0 : 600 ] | [ 601 : 8123 ] | 0.48657272002127094 | 0.48657272002127094 | 
| [ 0 : 700 ] | [ 701 : 8123 ] | 0.4931285367825384 | 0.4931285367825384 | 
| [ 0 : 800 ] | [ 801 : 8123 ] | 0.49986342529363564 | 0.49986342529363564 | 
| [ 0 : 900 ] | [ 901 : 8123 ] | 0.5067848241484353 | 0.5067848241484353 | 
| [ 0 : 1000 ] | [ 1001 : 8123 ] | 0.5139005897219882 | 0.5139005897219882 | 
| [ 0 : 2000 ] | [ 2001 : 8123 ] | 0.24501796798431885 | 0.24501796798431885 | 
| [ 0 : 3000 ] | [ 3001 : 8123 ] | 0.25536899648574773 | 0.25536899648574773 | 
| [ 0 : 4000 ] | [ 4001 : 8123 ] | 0.3173216885007278 | 0.3173216885007278 | 
| [ 0 : 5000 ] | [ 5001 : 8123 ] | 0.033952594490711085 | 0.033952594490711085 | 
| [ 0 : 6000 ] | [ 6001 : 8123 ] | 0.12252591894439209 | 0.12252591894439209 | 
| [ 0 : 7000 ] | [ 7001 : 8123 ] | 0.0071301247771836 | 0.0071301247771836 | 
| [ 0 : 8000 ] | [ 8001 : 8123 ] | 0.0 | 0.0 | 

W pierwszej kolumnie jest zakres próbek do treningu, w drugiej zakres to testowania, w trzeciej wynik poprawności drzewa ID3 (w skali od `0` do `1`) a w czwartej wynik poprawności drzewa C45.

Jak widać, aż do 1000 próbek treningowych błąd jest na poziomie 50%, więc drzewo raczej strzela niż decyduje, dopiero dalej sytuacja się polepsza, ale dalej na 4000 próbek treningowych błąd jest na poziomie 32%.

Dodatkowo widać, że algorytm C4.5 nie polepsza wyników ID3  

### Mieszanie próbek

Postanowiliśmy pomieszać próbki za pomocą `random.shuffle`, która używa sortowania losowego i sprawdzić czy próbki są ułożone w jakiś niefortunny sposób.
 
| Zbiór treningowy | Zbiór testujący | Wynik ID3 | Wynik C4.5 |
| --- | --- | --- | --- |  
| [ 0 : 100 ] | [ 101 : 8123 ] | 0.015332834704562454 | 0.015332834704562454 | 
| [ 0 : 200 ] | [ 201 : 8123 ] | 0.005806614491290078 | 0.005806614491290078 | 
| [ 0 : 300 ] | [ 301 : 8123 ] | 0.007542827921247762 | 0.007542827921247762 | 
| [ 0 : 400 ] | [ 401 : 8123 ] | 0.008547008547008548 | 0.008547008547008548 | 
| [ 0 : 500 ] | [ 501 : 8123 ] | 0.0019679874048806087 | 0.0019679874048806087 | 
| [ 0 : 600 ] | [ 601 : 8123 ] | 0.004653017814411061 | 0.0050518479127891515 | 
| [ 0 : 700 ] | [ 701 : 8123 ] | 0.0030988951765022906 | 0.0030988951765022906 | 
| [ 0 : 800 ] | [ 801 : 8123 ] | 0.0038240917782026767 | 0.0038240917782026767 | 
| [ 0 : 900 ] | [ 901 : 8123 ] | 0.0027693159789531985 | 0.0027693159789531985 | 
| [ 0 : 1000 ] | [ 1001 : 8123 ] | 0.0012636899747262005 | 0.0012636899747262005 | 
| [ 0 : 2000 ] | [ 2001 : 8123 ] | 0.0024501796798431885 | 0.0024501796798431885 | 
| [ 0 : 3000 ] | [ 3001 : 8123 ] | 0.0 | 0.0 | 
| [ 0 : 4000 ] | [ 4001 : 8123 ] | 0.0 | 0.0 | 
| [ 0 : 5000 ] | [ 5001 : 8123 ] | 0.0 | 0.0019218449711723255 | 
| [ 0 : 6000 ] | [ 6001 : 8123 ] | 0.0 | 0.0 | 
| [ 0 : 7000 ] | [ 7001 : 8123 ] | 0.0 | 0.0 | 
| [ 0 : 8000 ] | [ 8001 : 8123 ] | 0.0 | 0.0 | 

Jak widzimy dało to bardzo dobre skutki.
Już przy 100 próbkach treningowych, algorytmy dają bardzo dobre wyniki na poziomie 1%.


## Autorzy

Adam Jędrzejowski
Dawid Mackiewicz
