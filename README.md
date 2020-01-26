# Grzyby - PSZT - projekt 2

## Analiza zbioru

Bardzo dużo informacji na temat zbioru grzybów i ich właściwości znajdziemy w pliku `assets/agaricus-lepiota.names`.
Można wyczytać, że atrybuty `odor`, `spore-print-color`, `stalk-surface-below-ring`, `habitat`, `cap-color` są bardzo silnie klasyfikujące.
A mianowicie drzewo decyzyjne które wyglądało by tak: `spore-print-color=green`, daje błąd na poziomie 0.59%, co sprawia, że drzewo powinno być raczej niewielkie.

## Wyniki

W zadaniu zaimplementowano dwa algorytmy ID3 i C45, ten pierwszy jest częścią tego drugiego.

### ID3

Tak wygląda drzewo wygenerowane przez ID3:

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

### C45

Tak wygląda drzewo wygenerowane przez C45:

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

## Autorzy

Adam Jędrzejowski
Dawid Mackiewicz
