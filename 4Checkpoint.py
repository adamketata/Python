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




#Q3
def sortclors():
    colors = 'red-orange-yellow-green-blue'
    items = [item for item in colors.split('-')]
    items.sort()
    print('-'.join(items))
sortclors()
