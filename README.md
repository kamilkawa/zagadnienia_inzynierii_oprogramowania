# zagadnienia_inzynierii_oprogramowania

## Uruchomienie projektu
- Utwórz i aktywuj środowisko: `python -m venv .venv && source .venv/bin/activate`
- Zainstaluj zależności: `pip install -r requirements.txt`
- Uruchom przykładowe obliczenia: `python calculator.py`

## Testy
- Uruchom wszystkie testy jednostkowe: `pytest -v`

## Pokrycie kodu
- Raport pokrycia: `coverage_report.txt` or detailed execution `coverage-html.tar.gz`
- Zbierz pokrycie: `coverage run -m pytest`
- Wygeneruj raport HTML: `coverage html` 