date = input(" Gib ein Datum im Format Jahr.Monat.Tag ein (z.B. 2024.12.13): ")

# der Kurs von 25.11.2024 bis 25.02.2026
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
