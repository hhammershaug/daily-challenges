### Harald Hammershaug
- S374171 / S374171@oslomet.no

# Arrow Simulator

En 3D-fysikksimulator i Python som beregner banen til en pil skutt gjennom lufta ved hjelp av numerisk integrasjon (Eulers metode). Modellen tar høyde for tyngdekraft, sidevind og luftmotstand.

## Krav & Kjøring
- Python 3
```powershell
python arrow-simulator/arrow.py
```

## Slik fungerer simulatoren
1. Skriptet simulerer pilens posisjon i et tredimensjonalt koordinatsystem `(x, y, z)`.
2. Hvert tidsskritt (`dt = 0.1` sekund) oppdateres kreftene som virker på pilen:
   - **X-akse:** Fart fremover (bremses gradvis av luftmotstand).
   - **Y-akse:** Posisjon til siden (påvirkes av en konstant sidevind).
   - **Z-akse:** Høyde (akselereres nedover av tyngdekraften g = 9.81 m/s²).
3. Simulatoren kjører i en `while`-løkke og skriver ut posisjonen sekund for sekund helt til pilen treffer bakken (z ≤ 0).
