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
Dlatego ID3 było wstanie na tyle dobrze sklasyfikować zbiór, że C4.5 nie miał możliwości zadziałać na tak mały drzewie.

### Dzielenie zbioru

Postanowiliśmy podzielić zbiór na treningowy i testujący.
Wyniki poniżej:

| Zbiór treningowy | Zbiór testujący | Wynik ID3 | Wynik C4.5 |
| --- | --- | --- | --- |
| [ 0 : 100 ] | [ 101 : 8123 ] | `0.456245325355273` | `0.456245325355273` | 
| [ 0 : 200 ] | [ 201 : 8123 ] | `0.46200454430699317` | `0.46200454430699317` | 
| [ 0 : 300 ] | [ 301 : 8123 ] | `0.4679110201994375` | `0.4679110201994375` | 
| [ 0 : 400 ] | [ 401 : 8123 ] | `0.473970473970474` | `0.473970473970474` | 
| [ 0 : 500 ] | [ 501 : 8123 ] | `0.48018892679086855` | `0.48018892679086855` | 
| [ 0 : 600 ] | [ 601 : 8123 ] | `0.48657272002127094` | `0.48657272002127094` | 
| [ 0 : 700 ] | [ 701 : 8123 ] | `0.4931285367825384` | `0.4931285367825384` | 
| [ 0 : 800 ] | [ 801 : 8123 ] | `0.49986342529363564` | `0.49986342529363564` | 
| [ 0 : 900 ] | [ 901 : 8123 ] | `0.5067848241484353` | `0.5067848241484353` | 
| [ 0 : 1000 ] | [ 1001 : 8123 ] | `0.5139005897219882` | `0.5139005897219882` | 
| [ 0 : 2000 ] | [ 2001 : 8123 ] | `0.24501796798431885` | `0.24501796798431885` | 
| [ 0 : 3000 ] | [ 3001 : 8123 ] | `0.25536899648574773` | `0.25536899648574773` | 
| [ 0 : 4000 ] | [ 4001 : 8123 ] | `0.3173216885007278` | `0.3173216885007278` | 
| [ 0 : 5000 ] | [ 5001 : 8123 ] | `0.033952594490711085` | `0.033952594490711085` | 
| [ 0 : 6000 ] | [ 6001 : 8123 ] | `0.12252591894439209` | `0.12252591894439209` | 
| [ 0 : 7000 ] | [ 7001 : 8123 ] | `0.0071301247771836` | `0.0071301247771836` | 
| [ 0 : 8000 ] | [ 8001 : 8123 ] | `0.0` | `0.0` | 

W pierwszej kolumnie jest zakres próbek do treningu, w drugiej zakres to testowania, w trzeciej wynik poprawności drzewa ID3 (w skali od `0`, całkowicie poprawne do `1`, całkowicie błędne) a w czwartej wynik poprawności drzewa C45.

Jak widać, aż do 1000 próbek treningowych błąd jest na poziomie 50%, więc drzewo raczej strzela niż decyduje, dopiero dalej sytuacja się polepsza, ale dalej na 4000 próbek treningowych błąd jest na poziomie 32%.

Dodatkowo widać, że algorytm C4.5 nie polepsza wyników ID3  

### Mieszanie próbek

Postanowiliśmy pomieszać próbki za pomocą `random.shuffle`, która używa sortowania losowego i sprawdzić czy próbki są ułożone w jakiś niefortunny sposób.
 
| Zbiór treningowy | Zbiór testujący | Wynik ID3 | Wynik C4.5 |
| --- | --- | --- | --- |
| [ 0 : 100 ] | [ 101 : 8123 ] | `0.018698578908002993` | `0.018698578908002993` | 
| [ 0 : 200 ] | [ 201 : 8123 ] | `0.005806614491290078` | `0.005806614491290078` | 
| [ 0 : 300 ] | [ 301 : 8123 ] | `0.002812579902838149` | `0.21784709792891843` | 
| [ 0 : 400 ] | [ 401 : 8123 ] | `0.0027195027195027195` | `0.0027195027195027195` | 
| [ 0 : 500 ] | [ 501 : 8123 ] | `0.0026239832065074785` | `0.0026239832065074785` | 
| [ 0 : 600 ] | [ 601 : 8123 ] | `0.0029247540547726668` | `0.21935655410795002` | 
| [ 0 : 700 ] | [ 701 : 8123 ] | `0.005524117488547561` | `0.005524117488547561` | 
| [ 0 : 800 ] | [ 801 : 8123 ] | `0.0031412182463807703` | `0.0031412182463807703` | 
| [ 0 : 900 ] | [ 901 : 8123 ] | `0.002630850180005539` | `0.002630850180005539` | 
| [ 0 : 1000 ] | [ 1001 : 8123 ] | `0.0014040999719180005` | `0.0014040999719180005` | 
| [ 0 : 2000 ] | [ 2001 : 8123 ] | `0.0006533812479581836` | `0.0006533812479581836` | 
| [ 0 : 3000 ] | [ 3001 : 8123 ] | `0.0005857087075361187` | `0.001952362358453729` | 
| [ 0 : 4000 ] | [ 4001 : 8123 ] | `0.0009704027171276079` | `0.0009704027171276079` | 
| [ 0 : 5000 ] | [ 5001 : 8123 ] | `0.0` | `0.0` | 
| [ 0 : 6000 ] | [ 6001 : 8123 ] | `0.0` | `0.0` | 
| [ 0 : 7000 ] | [ 7001 : 8123 ] | `0.0` | `0.0` | 
| [ 0 : 8000 ] | [ 8001 : 8123 ] | `0.0` | `0.0` | 

Jak widzimy dało to bardzo dobre skutki.
Już przy 100 próbkach treningowych, algorytmy dają bardzo dobre wyniki na poziomie 2%.
Dalej, aż do 1000 próbek uczących nie widać poprawy, ale potem błędy spadają do zera.

Dla pewności uruchomiliśmy program kilka razy i zawsze dawał podobne wyniki.

Jak widać algorytm C4.5 w niektórych przypadkach pogarsza wyniki drzewa ID3, chodź z samego algorytmu wynika, że powinno polepszać.
Nie wiemy czym jest to spowodowane.

## Kod programu

Aby uruchomić program należy wpisać następujące komendy:
```bash
cd src
./main.py
```

Wszystkie algorytmy związane z wyznaczanie drzewa są zaimplementowane w pliku `src/Algorhythm.py`.
Struktura drzewa jest w `src/Tree.py`.
Algorytmy ID3 i C45 zwracają drzewo, które można wyświetlić w następujący sposób `print(ID3(...).dump())`.

## Autorzy

Adam Jędrzejowski
Dawid Mackiewicz
