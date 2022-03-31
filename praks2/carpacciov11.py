from arvutused import *
while True:
    #andmete sisestamine kasutaja poolt
    hind = float(input("Sisestage 1 kauba hind: "))
    kogus = int(input("Sisesta kogus: "))
    vale_kogus = 0
    vale_hind = 0
    #hinna ja koguse kontroll, et programm töötaks, tsüklib kuni sobib
    if kogus <= 0:
        print("kogus peab olema positiivne arv")
        vale_kogus = 1
    if hind <= 0:
        print("Hind peab olema positiivne arv")
        vale_hind = 1
    if vale_kogus == 0 and vale_hind == 0:
        break
#riigi koodi sisestamise koht
riik = input("Sisestage riigi kood: ").upper()
#hinnade, soodustuste ja käibemaksude protsendide arvutused
koguhind = hind * kogus
soodus = soodustus(koguhind)
soodustusegahind = round(koguhind - (koguhind / 100 * soodus), 2)
maks = kaibemaks(riik)
lopuhind = round(soodustusegahind + ((soodustusegahind / 100) * maks), 2)
#lõpuandmete prindimine
print("Teie kogus on: " + str(kogus))
print("Teie 1 kauba hind on: " + str(hind) + " €")
print("Teie käibemaksu määr on: " + str(maks) + "%")
print("Teie soodustus protsent on " + str(soodus) + "%")
print("Teie koguhind on: " + str(koguhind))
print("Teie soodusega hind on: " + str(soodustusegahind))
print("Teie koguhind koos soodustusega ja maksutega on: " + str(lopuhind))
