import random as rnd

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
symbols = ['*','!','@','#','$','%','^','&','(',')','_','-','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']

# let's create the format of our password generation game

print('Welcome to our Tech_Genius password generation game')
nr_letters = int(input('how many letters would you like in your password? \n'))
nr_symbols = int(input('how many symbols would you like in your password? \n'))
nr_numbers = int(input('how many numbers would you like in your password? \n'))

# let's create a empty list in which we will store the asked characters:
password_list = []

# we will use a for loop to generate the password
for item in range(0, nr_letters):
    password_list.append(rnd.choice(letters))

for item in range(0, nr_symbols):
    password_list.append(rnd.choice(symbols))

for item in range(0, nr_numbers):
    password_list.append(rnd.choice(numbers))


# As for random password generation we need to shuffle the asked characters
rnd.shuffle(password_list)

# now we will convert the list into a string
password = ""
for item in password_list:
    password += item

print('Your password is : ',password)