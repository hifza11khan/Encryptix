import random
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?', '|', '\\']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print ("welcome to password genrator tool")
user_letter =int(input("enter no of letter"))
user_symbols =int(input("enter no of symbols"))
user_numbers =int(input("enter no of numbers"))
password=[]
for i in range (1,user_letter+1):
    char = random.choice(letter)
    password  += char
    
for i in range (1,user_numbers+1):
    char = random.choice(numbers)
    password  += char
   
for i in range (1,user_symbols+1):
    char = random.choice(symbols)
    password  += char
    
print(password)
random.shuffle(password)
password1=""
for char in password:
    password1 += char
print(password1)
