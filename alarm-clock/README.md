### Harald Hammershaug
- S374171 / S374171@oslomet.no

# Alarm Clock

En enkel ned countdown-timer i Python som tar inn et antall sekunder, overvåker gjenværende tid i en løkke, og utløser en alarmlyd når tiden har rent ut.

## Krav & Kjøring
- Python 3
- `playsound` (for avspilling av lydfil)

```powershell
pip install playsound==1.2.2
python clock.py
```

## Slik fungerer vekkerklokken
1. **Initialisering:** Funksjonen `alarm(seconds)` tar imot måltiden i sekunder og starter en teller fra null.
2. **Bakgrunnsløkke:** En `while`-løkke kjører så lenge telleren er mindre enn måltiden, og pauser i ett sekund for hvert steg (`time.sleep(1)`).
3. **Tidsberegning:** For hvert sekund regnes gjenværende tid om til minutter og sekunder:
   - `minutes_left = time_left // 60` (Heltallsdivisjon som gir hele minutter).
   - `seconds_left = time_left % 60` (Modulo/rest-operasjon som gir gjenværende sekunder).
4. **Alarmsignal:** Når løkken er ferdig, printes en tekstbeskjed i terminalen, og lydfilen `alarm.mp3` spilles av.
