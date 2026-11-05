from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        # 1. Beregn tiden som er igjen AKKURAT NÅ
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # 2. Skriv ut tiden først
        print(f"{minutes_left}:{seconds_left}")
        
        # 3. Vent og legg til 1 sekund etterpå
        time.sleep(1)
        time_elapsed += 1

    # Trigger alarmen når telleren er ferdig
    print("VÅKN OPP! ⏰")
    playsound("alarm.mp3")

alarm(10)
