date = input(" Gib ein Datum im Format Jahr.Monat.Tag ein (z.B. 2024.12.13): ")

# das Kurs von 25.11.2024 bis 25.02.2026
if date >= "2024.11.24" and date <= "2026.02.25":
    if date >= "2024.12.24" and date <= "2025.01.01":
        print("Winterferien 2024")
    elif date >= "2025.04.18" and date <= "2025.04.21":
        print("Osterferien ")
    elif date >= "2025.08.11" and date <= "2025.08.19":
        print("Sommerferien")
    elif date >= "2025.12.24" and date <= "2026.01.01":
        print("Winterferien 2025")
    elif date >= "2025.06.15" and date <= "2025.06.20":
        print("Dieses Datum ist Teil meines geplanten Urlaubs!")
    else:
        print(" Es sind keine Ferien!")
else:
    print("Dieses Datum ist nicht in diesem Kurs enthalten!")


# andere Ergebniss

ferien = {
    # Winterferien 2024
    "2024.12.24": "Winterferien",
    "2024.12.25": "Winterferien",
    "2024.12.26": "Winterferien",
    "2024.12.27": "Winterferien",
    "2024.12.28": "Winterferien",
    "2024.12.29": "Winterferien",
    "2024.12.30": "Winterferien",
    "2024.12.31": "Winterferien",
    "2025.01.01": "Winterferien",
    # Osterferien 2025
    "2025.04.18": "Osterferien",
    "2025.04.19": "Osterferien",
    "2025.04.20": "Osterferien",
    "2025.04.21": "Osterferien",
    # Sommerferien 2025
    "2025.08.11": "Sommerferien",
    "2025.08.12": "Sommerferien",
    "2025.08.13": "Sommerferien",
    "2025.08.14": "Sommerferien",
    "2025.08.15": "Sommerferien",
    "2025.08.16": "Sommerferien",
    "2025.08.17": "Sommerferien",
    "2025.08.18": "Sommerferien",
    "2025.08.19": "Sommerferien",
    # Winterferien 2025
    "2025.12.24": "Winterferien 2025",
    "2025.12.25": "Winterferien 2025",
    "2025.12.26": "Winterferien 2025",
    "2025.12.27": "Winterferien 2025",
    "2025.12.28": "Winterferien 2025",
    "2025.12.29": "Winterferien 2025",
    "2025.12.30": "Winterferien 2025",
    "2025.12.31": "Winterferien 2025",
    "2026.01.01": "Winterferien 2025",
}
date2 = input(" Gib ein Datum im Format Jahr.Monat.Tag ein (z.B. 2024.12.13): ")

if date >= "2024.11.24" and date <= "2026.02.25":
    if date2 in ferien:
        print(f"es ist {ferien[date2]} .")
    else:
        print(" Es sind keine Ferien!")
else:
    print("Dieses Datum ist nicht in diesem Kurs enthalten!")
