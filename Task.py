import re

def simplify_numbers(raw_text):
    #function to simplify large numbers
    def simplify_large_number(match):
        num = match.group()
        num = num.replace('.', '').replace(',', '.')
        if '.' in num:
            value = float(num)
        else:
            value = int(num)
        if value >= 1000:
            return f'etwa {round(value, -3):,.0f}'.replace(',', '.')
        else:
            return f'etwa {round(value):,.0f}'.replace(',', '.')

    #function to simplify percentages
    def simplify_percentage(match):
        percent = float(match.group(1))
        if percent == 25:
            return "jeder Vierte"
        elif percent == 50:
            return "die Hälfte"
        elif percent == 75:
            return "drei von vier"
        elif percent >= 90:
            return "fast alle"
        elif percent >= 60:
            return "mehr als die Hälfte"
        elif percent <= 15:
            return "wenige"
        else:
            return "einige"

    #Simplify large numbers
    raw_text = re.sub(r'\b\d{1,3}(?:\.\d{3})*(?:,\d+)?\b', simplify_large_number, raw_text)
    #Simplify percentages
    raw_text = re.sub(r'\b(\d{1,2}(?:,\d+)?) Prozent\b', simplify_percentage, raw_text)
    #Simplify temperatures
    raw_text = re.sub(r'\b(\d{1,2}(?:,\d+)?) Grad Celsius\b',
                      lambda m: f"Bei etwa {round(float(m.group(1).replace(',', '.'))):.0f} Grad Celsius", raw_text)

    return raw_text

test_cases = [
    "324.620,22 Euro wurden gespendet.",
    "1.897 Menschen nahmen teil.",
    "25 Prozent der Bevölkerung sind betroffen.",
    "90 Prozent stimmten zu.",
    "14 Prozent lehnten ab.",
    "Bei 38,7 Grad Celsius ist es sehr heiß.",
    "denn die Rente steigt um 4,57 Prozent.",
    "Im Jahr 2024 gab es 1.234 Ereignisse.",
    "Am 1. Januar 2024 waren es 5.678 Teilnehmer.",
    "Im Jahr 2025 gab es 2018 Ereignisse."
]

for test in test_cases:
    print(simplify_numbers(test))
