hind = float(input("Sisestage 1 kauba hind: "))
kogus = int(input("Sisesta kogus: "))

koguhind = hind * kogus
if koguhind >= 50000:
    soodus = 15
elif koguhind >= 10000:
    soodus = 10
elif koguhind >= 7000:
    soodus = 7
elif koguhind >= 5000:
    soodus = 5
elif koguhind >= 1000:
    soodus = 3
print("Teie 1 kauba hind on: " + str(hind))
print("Teie kogus on: " + str(kogus))
print("Teie soodustus on " + str(soodus) + "%")