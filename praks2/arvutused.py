def kaibemaks(riik):
    if riik == "AL":
        return 4
    elif riik == "CA":
        return 8.25
    elif riik == "TX":
        return 6.25
    elif riik == "NV":
        return 6
    elif riik == "UT":
        return 6.85
    else:
        return 0
def soodustus(hind):
    if hind >= 50000:
        return 15
    elif hind >= 10000:
        return 10
    elif hind >= 7000:
        return 7
    elif hind >= 5000:
        return 5
    elif hind >= 1000:
        return 3
    else:
        return 0