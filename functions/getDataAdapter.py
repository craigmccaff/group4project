from functions import returnJsonAsDict


def getDataTest():
    flag = True
    while flag:
        data = returnJsonAsDict.getInput()
        if data['success'] == True:
            return data
        else:
            print("You have recently searched for this name, please wait before searching again.")
