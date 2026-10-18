### Harald Hammershaug
- S374171 / S374171@oslomet.no

# Optimized Traffic Signal Timing Plan


#### NORSK VERSJON (NO)
Beregning og optimalisering av signalfaser for et 4-faset vegkryss ved bruk av Websters metode. Kjøres i terminalen.

## Krav & Kjøring
- Python 3
- Python
```powershell
python optimized-traffic-signal-timing-plan/game.py
```

## Slik fungerer det
1. Skriptet henter kritiske trafikkmengder direkte fra oppgavens kryssoppsett.
2. Beregner metningsvannføring og strømningsforhold for hver fase.
3. Finner optimal omløpstid (Cycle Length) ved bruk av Websters formel.
4. Deler opp omløpstiden og spytter ut en ferdig signalplanmatrix med nøyaktige sekunder for grønt og gult lys.



#### ENGLISH VERSION (ENG)
Calculation and optimization of signal phases for a 4-phase intersection using Webster's method. Runs in the terminal.

## Requirements & Execution
- Python 3
- Python
```powershell
python optimized-traffic-signal-timing-plan/game.py
```

## How It Works
1. The script extracts critical traffic volumes directly from the assignment's intersection layout.
2. Calculates the saturation flow rate and individual phase flow ratios.
3. Finds the optimal cycle length using Webster's formula.
4. Splits the cycle time and outputs a completed signal plan matrix with precise green and amber durations.
