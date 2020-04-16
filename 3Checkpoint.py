#Q1
Mylist = [1,2,3]
result = Mylist[0] * Mylist[1] * Mylist[2]
print(result)
#Q2
Mylist2= [(3,2),(4,5),(3,1),(8,3),(5,4)]
list2 = []
for x in Mylist2:
    x = x[1]
    print(x)
    

#Q3
mydict1 = { "a":100 , "b":200, "c":300}
mydict2 = { "a":600 , "b":500, "d":400}
for key in mydict2:
    if key in mydict1:
        mydict2[key] = mydict2[key] + mydict1[key]
print(mydict2)
#Q4
list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
for x in list:
    for y in x:
        maximum = y[3]
        if y[1] > maximum:
            maximum = y[1]

