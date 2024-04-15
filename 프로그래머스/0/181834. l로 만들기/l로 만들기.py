def solution(myString):
    for i in range(len(myString)):
        comp_list = [myString[i], "l"]
        if sorted(comp_list)[1] == "l":
            myString = myString[:i] + "l" + myString[i+1:]
    return myString