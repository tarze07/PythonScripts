# PythonScripts

## copy_filtered_chars.py

Skrypt umożliwia kopiowanie określonej liczby znaków z linii, które zawierają
wskazany tekst.

### Uruchomienie

```bash
python copy_filtered_chars.py <plik_wejściowy> <plik_wyjściowy> <szukany_tekst> <liczba_znaków>
```

Przykład:

```bash
python copy_filtered_chars.py dane.txt wynik.txt "ERROR" 20
```

Polecenie powyżej przepisze pierwsze 20 znaków z każdej linii pliku `dane.txt`,
która zawiera tekst `ERROR`, do pliku `wynik.txt`.
