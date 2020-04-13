#Q1
print("First Question: Name and last name")
first_name = input("First name: ")
last_name = input("Last name: ")
print(f'{last_name}  {first_name}')
#Q2
print("Second Question n+nn+nnn")
n = int(input("Write a number: "))
output = n + (n*10+n) + (n*100+n*10+n)
print(output)
#Q3
print("Third Question odd*even")
number = int(input("Write a number"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
#Q4
print("Fourth Question leap year ?")
year = int(input("Write a year: "))
leap = year % 4
if leap == 0:
    print("It is surely a leap year!")
else:
    print("No it isn't a leap year")
#Q5
print("Fifth Question remove odd index")
text = input('> ')
length = len(text)
result = ""
for i in range(length):
    if i % 2 == 0:
        result += text[i]
print(result)
#Q6
print("Sixth Question Discount")
price = int(input("Write down the price: "))
final_price = 0
if price >= 500:
    final_price = (price/100)*50
    print(f'the final price is {final_price}')
elif 200 <= price < 500:
    final_price = (price/100)*70
    print(f'the final price is {final_price}')
else:
    final_price = (price/100)*90
    print(f'the final price is {final_price}')



