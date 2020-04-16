#Q1
def max_number(x,y,z):
    maximum = 0
    if x > y and x > z:
        maximum = x
    elif y > x and y > z:
        maximum = y
    else:
        maximum = z
    print(maximum)
max_number(30,8,25)
#2
def sum(mylist):
    result = 0
    for i in mylist:
        result += i
    return result
def extract(mylist1):
    list1 = []
    for x in range(0, len(mylist1)):
        if x % 2 == 0:
            list1.append(mylist1[x])
    total = sum(list1)
    print(total)
    return total
extract([4,2,6])

def multiply(mylist2):
    result = 1
    for i2 in mylist2:
        result *= i2
    return result
def extract(list2):
    odd = []
    for x2 in range(0, len(list2)):
        if x2 % 2 == 0:
            odd.append(list2[x2])
    total = multiply(odd)
    print(total)
    return total
extract([10,2,7])



#Q3
def sortclors():
    colors = 'red-orange-yellow-green-blue'
    items = [item for item in colors.split('-')]
    items.sort()
    print('-'.join(items))
sortclors()
