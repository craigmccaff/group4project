def ratio(kills, deaths):
    try:
        kdratio = round(int(kills) / int(deaths), 2)
        display = "KD Ratio " + str(kdratio)
        return display
    except:
        display = "KD Ratio " + str(kills)
        return display
