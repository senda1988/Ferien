# Winterferien 2024
ferien_winter = {
    "2024.12.24",
    "2024.12.25",
    "2024.12.26",
    "2024.12.27",
    "2024.12.28",
    "2024.12.29",
    "2024.12.30",
    "2024.12.31",
    "2025.01.01",
}
# Osterferien 2025
ferien_ostern = {
    "2025.04.18",
    "2025.04.19",
    "2025.04.20",
    "2025.04.21",
}

# Sommerferien 2025
ferien_sommer = {
    "2025.08.11",
    "2025.08.12",
    "2025.08.13",
    "2025.08.14",
    "2025.08.15",
    "2025.08.16",
    "2025.08.17",
    "2025.08.18",
    "2025.08.19",
}
#     # Winterferien 2025
ferien_winter2 = {
    "2025.12.24",
    "2025.12.25",
    "2025.12.26",
    "2025.12.27",
    "2025.12.28",
    "2025.12.29",
    "2025.12.30",
    "2025.12.31",
    "2026.01.01",
}
urlaub = {
    "2025.06.15",
    "2025.06.16",
    "2025.06.17",
    "2025.06.18",
    "2025.06.19",
    "2025.06.20",
}

date2 = input(" Gib ein Datum im Format Jahr.Monat.Tag ein (z.B. 2024.12.13): ")

if date2 >= "2024.11.24" and date2 <= "2026.02.25":
    if date2 in ferien_winter:
        print("Ferien")
    elif date2 in ferien_ostern:
        print(" Osterferien ")
    elif date2 in ferien_sommer:
        print("Sommerferien")
    elif date2 in ferien_winter2:
        print("Winterferien 2025")
    elif date2 in urlaub:
        print("Dieses Datum ist Teil meines geplanten Urlaubs!")
    else:
        print(" Es sind keine Ferien!")

else:
    print("Dieses Datum ist nicht in diesem Kurs enthalten!")

# ferien = {
#     # Winterferien 2024
#     "2024.12.24": "Winterferien",
#     "2024.12.25": "Winterferien",
#     "2024.12.26": "Winterferien",
#     "2024.12.27": "Winterferien",
#     "2024.12.28": "Winterferien",
#     "2024.12.29": "Winterferien",
#     "2024.12.30": "Winterferien",
#     "2024.12.31": "Winterferien",
#     "2025.01.01": "Winterferien",
#     # Osterferien 2025
#     "2025.04.18": "Osterferien",
#     "2025.04.19": "Osterferien",
#     "2025.04.20": "Osterferien",
#     "2025.04.21": "Osterferien",
#     # Sommerferien 2025
#     "2025.08.11": "Sommerferien",
#     "2025.08.12": "Sommerferien",
#     "2025.08.13": "Sommerferien",
#     "2025.08.14": "Sommerferien",
#     "2025.08.15": "Sommerferien",
#     "2025.08.16": "Sommerferien",
#     "2025.08.17": "Sommerferien",
#     "2025.08.18": "Sommerferien",
#     "2025.08.19": "Sommerferien",
#     # Winterferien 2025
#     "2025.12.24": "Winterferien 2025",
#     "2025.12.25": "Winterferien 2025",
#     "2025.12.26": "Winterferien 2025",
#     "2025.12.27": "Winterferien 2025",
#     "2025.12.28": "Winterferien 2025",
#     "2025.12.29": "Winterferien 2025",
#     "2025.12.30": "Winterferien 2025",
#     "2025.12.31": "Winterferien 2025",
#     "2026.01.01": "Winterferien 2025",
# }
# date2 = input(" Gib ein Datum im Format Jahr.Monat.Tag ein (z.B. 2024.12.13): ")

# if date2 >= "2024.11.24" and date2 <= "2026.02.25":
#     if date2 in ferien:
#         print(f"es ist {ferien[date2]} .")
#     else:
#         print(" Es sind keine Ferien!")
# else:
#     print("Dieses Datum ist nicht in diesem Kurs enthalten!")
