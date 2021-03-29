def ratio(kills, deaths):
    try:
        kdratio = round(int(kills) / int(deaths), 2)
        print("KD Ratio " + str(kdratio))
        return kdratio
    except:
        print("KD Ratio " + kills)
        return kills
