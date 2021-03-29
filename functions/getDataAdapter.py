from functions import returnJsonAsDict


def getDataAdapter():
    flag = True
    while flag:
        data = returnJsonAsDict.getRecentSearch()
        if data['success'] == True:
            return data
        else:
            print("You have recently searched for this name, please wait before searching again.")
