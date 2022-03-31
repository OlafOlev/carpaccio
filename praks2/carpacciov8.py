hind = float(input("Sisestage 1 kauba hind: "))
kogus = int(input("Sisesta kogus: "))
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

koguhind = hind * kogus
lopuhind = round(koguhind + ((koguhind / 100) * maks),2)
print("Teie 1 kauba hind on: " + str(hind))
print("Teie kogus on: " + str(kogus))
print("Teie maksud on: " + str(maks) + "%")
print("Teie koguse hind on: " + str(koguhind))
print("Teie lõpuhind on: " + str(lopuhind))
