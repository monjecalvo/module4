List1 = {1:10, 2:4, 3:0, 4:9}
List2 = {1:9.99, 2:19.9, 3:14.99, 4:4.99}
cash = {1:129.9}

def getPriceProduct(num):
    if num <=4:
     return List2[num]
    else:
        return "OUT"

def getQuantityProduct(num):
    if num <=4:
     return List1[num]
    else:
        return "OUT"
def DetailProduct(num):
    if num <=4:
        return List1[num],List2[num]
    else:
        return "OUT"    

def getCash(num):
    if num ==1:
        return cash[num]
    else:
        return "OUT"     

def addQuantProduct(num,price):
    if num <=4:
        sum = List1[num]+price
        List1[num] = sum
        return List1[num]
    else:
        return "OUT"

def setPriceProduct():
    if num <=4:
        sum = List2[num]+price
        List2[num] = sum
        return List2[num]
    else:
        return "OUT"

def setProduct(num):     
    if List1[num]>0:
        List1[num]=List1[num]-1
        cash[1]=cash[1]+List2[num]
        return True
    else:
        return False   

#def replaceProduct():


#def getFullStock():                

num = int(input("Input a number "))
price = int(input("Input price "))
print(setProduct(num))
print(List1)
print(cash)