import random

# Startposisjon (x, y, z)
x, y, z = 0.0, 0.0, 0.0

# Startfart (m/s)
vx = 25.0  # Fart fremover
vy = 0.0   # Startfart til siden
vz = 20.0  # Fart oppover

# Naturkrefter og konstanter
g = 9.81         # Tyngdekraft (z-retning)
vind_kraft = 2.5  # Sidevind (y-retning)
drag = 0.05       # Luftmotstand (bremser alle retninger)

dt = 0.1  # Tidsskritt i sekunder
t = 0.0

print("Tid (s) | Posisjon (x, y, z)")
print("-" * 40)

# Kjører til pilen treffer bakken
while z >= 0:
    # Beregn luftmotstand basert på gjeldende fart
    vx -= drag * vx * dt
    vy -= drag * vy * dt
    vz -= drag * vz * dt
    
    # Legg til y-vind og z-tyngdekraft
    vy += vind_kraft * dt
    vz -= g * dt
    
    # Oppdater koordinater
    x += vx * dt
    y += vy * dt
    z += vz * dt
    
    t += dt
    print(f"{t:6.1f} | ({x:5.1f}, {y:5.1f}, {z:5.1f})")

print("-" * 40)
print(f"Pilen landet etter {t:.1f} sekunder!")
