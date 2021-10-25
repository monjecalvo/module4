theList = []

def showMenu():
    print("1.- Add a number to the list ")
    print("2.- Add a number in a position in the list ")
    print("3.- Show the length of the list ")
    print("4.- Delete the last number in the list ")
    print("5.- Delete a number in the list ")
    print("6.- Count numbers ")
    print("7.- Positions of a numbers ")
    print("8.- Show the list ")
    print("9.- Exit ")
    option = int(input("Chosse an option:"))
    return option

def addNumber():
    num = int(input("Input a number"))
    theList.append(num)

def insertNumber(num, pos):
        if pos <= len(theList):
            theList.insert(pos,num)
        else:
            return False

def getLastElement():
    if len(theList) > 0:
        return theList.pop()
    return False    

def deletatpos(pos):
    if pos <= len(theList):
        return theList.pop(pos)
    return False 

def getIndexesFromANumber():
    pos = 0
    for elem in range(0,theList.count(num)):
        index = theList.index(num,pos)
        print(index, end=" ")
        pos = index + 1
    

while True:   
    option = showMenu()
    if option == 1:
        addNumber()   
    elif option == 2:
        num = int(input("Input a number"))
        pos = int(input("Input the position"))  
        insertNumber(num, pos)      
    elif option == 3:
        print(len(theList))
    elif option == 4:
        num = getLastElement()
        if num == False:
           print("The list is empty")
        else:
            print("The last element is ",num)   
    elif option == 5:
        pos = int(input("Input the position"))
        num = deletatpos(pos)
        if num == False:
            print("the position no exsists")
        else:
            print("delete ",num)    
    elif option == 6:
        num = int(input("Input the number"))
        print(num, theList.count(num))
    elif option == 7:
        num = int(input("Input the number")) 
        for i in getIndexesFromANumber(num):
            print(i,end=" ")
        print()
        pos=0    
        """index = 1
        for elem in theList:
            if elem == num:
                print(index, end=" ")
            index += 1
        print()"""    
    elif option == 8:
        for elem in theList:
            print(elem,end=" ")
        print()    
    elif option == 9:
        break    