riik = input("Sisestage riigi kood: ").upper()
if riik == "AL":
    maks = 4
elif riik == "CA":
    maks = 8.25
elif riik == "TX":
    maks = 6.25
elif riik == "NV":
    maks = 6
elif riik == "UT":
    maks = 6.85
print(riik, "maks on", maks, "%")