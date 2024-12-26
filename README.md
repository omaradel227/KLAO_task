# Omar Adel Gamal

# Simplify Numbers Function
This project provides a Python function called simplify_numbers, which can simplify any numeric values present in texts using rules of readability with regards to such numeric values. It intends to handle big numbers, percentages, and contextual temperatures, in the provided format for its functionality. Following these provided rules, this project shall aim at providing relatable and understandable numbers.

# Features

- **Simplify Large Numbers:**

   Rounds large numbers to the nearest thousand or an appropriate approximation.
   
   Example: 324.620,22 Euro → etwa 325.000 Euro




- **Simplify Percentages:**

   Replaces percentages with descriptive or comparative phrases.
   
   Example: 25 Prozent → jeder Vierte, 90 Prozent → fast alle




- **Simplify Temperatures:**

   Approximates temperature values with "etwa" for clarity.

   Example: 38,7 Grad Celsius → Bei etwa 39 Grad Celsius



**Input**
```
324.620,22 Euro wurden gespendet.
1.897 Menschen nahmen teil.
25 Prozent der Bevölkerung sind betroffen.
90 Prozent stimmten zu.
14 Prozent lehnten ab.
Bei 38,7 Grad Celsius ist es sehr heiß.
denn die Rente steigt um 4,57 Prozent.
Im Jahr 2024 gab es 1.234 Ereignisse.
Am 1. Januar 2024 waren es 5.678 Teilnehmer.
Im Jahr 2025 gab es 2018 Ereignisse.
```

**Expected Output:**
```
etwa 325.000 Euro wurden gespendet.
etwa 2.000 Menschen nahmen teil.
jeder Vierte der Bevölkerung sind betroffen.
fast alle stimmten zu.
wenige lehnten ab.
Bei etwa 39 Grad Celsius ist es sehr heiß.
denn die Rente steigt um wenige.
Im Jahr 2024 gab es etwa 1.000 Ereignisse.
Am 1. Januar 2024 waren es etwa 6.000 Teilnehmer.
Im Jahr 2025 gab es etwa 2.000 Ereignisse.
```
