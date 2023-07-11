# Exercises # 1
name = "Alan Turing"
age = 42
person = [name, age, "mathematician"]

text = "Hello, my name is {}, I am {} years old and I am a {}.".format(name, age, "mathematician")
print(text)

age_type = type(age)

print(age_type)

import unittest

class TestNotebook(unittest.TestCase):
    def test_name(self):
        self.assertEqual(name, "Alan Turing")

    def test_age(self):
        self.assertEqual(age, 42)

    def test_person(self):
        self.assertEqual(person, ["Alan Turing", 42, "mathematician"])

    def test_text(self):
        self.assertEqual(
            text,
            "Hello, my name is Alan Turing, I am 42 years old and I am a mathematician.",
        )

    def test_type(self):
        self.assertEqual(age_type, int)


unittest.main(argv=[""], verbosity=2, exit=False)

# Conditions
'''
age = 32<br>
age += 10<br>
divAge = age // 7<br>
textDiv = "{} divided by 7 equals {}".format(age, divAge)<br>
restDiv = age % 7<br>
expDiv = restDiv ** 3

print(age)
print(textDiv)
print(restDiv)
print(expDiv)

7. Write a program that enters an integer and then displays the value entered and its type.

#integer = int(input("Enter an integer number: "))
# print(integer, type(integer))

# 8. Use variables to represent the price of materials.

#milk = 2 * 0.45
#raw_cider = 3 * 3.85
#flour = 0.9
#packet_butter = 0.77
#nutella = 1.87

#orderPrice = milk + raw_cider + flour + packet_butter + nutella

#print("The total price is ", orderPrice) '''



""" Create a variable allowanceMoney which has a value of 20 and then create an algorithm that calculates the available money
by subtracting the price of the order.
If there is enough money, record the following sentence in the variable message and subtract the expense from allowanceMoney :
message = "You have spent" + orderPrice + "you have left" + allowanceMoney
If there is not enough money, record the following sentence in the message variable:
message= "Sorry you're missing amountMissing euros"
If there is 0 left, record the following sentence in the message variable:
message = "You are broke!" """

""" allowance_money = 20
order_price = int(input("Enter the expense: "))
available_money = allowance_money - order_price
message = "You have spent {} you have left {}".format(order_price,available_money )
money_missing = order_price - allowance_money


if available_money >= 0 and available_money <= 20:
   print (message)
elif order_price >= 20:
    print("Sorry you're missing {}".format(money_missing))
elif available_money == 0:
    print("You are broke!") """

# 9. Write a program that asks you to enter 2 values and displays the smallest of the 2 values

"""value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))

if value1 <= value2:
    print(value1)
else:
    print(value2)"""

# 10. Write a script that asks you to enter 2 strings and displays the largest of the 2 strings (the one with the most characters).

"""string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) > len(string2):
    print(string1)
else:
    print(string2)"""

# 11. Write a script that converts euros into dollars.

"""devise = input("Enter the 'E' or '$' for devise: ")
symbol_euro = "E"
symbol_dollar = "$"
qty = int(input("Enter qty : "))
euro = 1 #
dollar = 0.92 #euros

if devise == symbol_euro:
    print(euro * qty)
elif devise == symbol_dollar:
    print(dollar * qty)
else:
    print("Please enter a valid choice")
"""

# 12. Check if the variable name is in the studentsTuring list. (Without making a loop)

"""studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Julie"

if name is studentsTuring:
    print("You are at the turing's")
else:
    print("You are not part of the turing's")"""
    
     

# Import math Library

"""import math
print(math.pi)

round_pi = float(round(math.pi))
print(round_pi)"""


# 4. Create a variable reversed_text which contains the character string "Hello world!" backwards.
# The result must be a list object.


"""reversed_text = ("Hello world!")

print (list(reversed(reversed_text)))"""

# 6. Create a variable sorted_num that contains the sorted num list.

"""num = [2, 8, 1, 4, 6, 3, 7]

print (sorted(num))"""

# 7. Create a variable sum_of_list which contains the sum of all the elements in the list num.

"""num = [2, 8, 1, 4, 6, 3, 7]
print(sum(num))
"""

# 8. Create a variable min_value that contains a minimum value of list num.

"""num = [2, 8, 1, 4, 6, 3, 7]

min_value = min(num)
max_value = max(num)
print(min_value)
print(max_value)
"""

# 10. Find a function that will interpret the string of the variable calc
# Save the result in a variable named string_interpret.


# Lists, Tuples and dictionaries

"""
diccionario = {
     "MBonjour" : "Hola",
     "fou" : "loco",
     "voiture" : "carro"
}

diccionario ["Marie"] = "Maria" 
print(diccionario)"""

# 3. How would you cut the following string at each space and put it in a list?

"""sentence = "I am the master of the world"
sentence_list = sentence.split(" ")

print(sentence_list)"""

# 4. Transform this string "The_universal_number_is_42" by removing the underscores: "The universal number is 42"

"""universal_number = "The_universal_number_is_42"
print(universal_number.replace("_", " "))"""

# 5. Display only values of this dictionary.
# 6. Display only keys of this dictionary.

"""heroes = {"Superman": "Clark Kent", "Batman": "Bruce Wayne", "Spiderman": "Tony Parker"}

print(heroes.values())
print(heroes.keys())
"""

# 8. Create a dictionary to build the price base of the products corresponding to the following table.

"""price_products = {
    "Laser sword": 229.0,
    "Mitendo DX": 127.30,
    "Linux cushion": 74.50,
    "Goldorak briefs": 29.90,
    "Nextpresso station": 184.60

}
print(price_products)

price_products_sum = price_products.values()
price_products.pop("Laser sword")
print(sum(price_products_sum))
print(price_products)"""

"""while True:
    n = int(input("give a integer > 0 : "))
    print("You have provided", n)
    if n > 0:
        break
print("correct answer")"""

"""for i in range(10):
    print("Start of iteration", i)
    print("Hello")
    if i == 2:
        break
    print("End of iteration", i)
print("After the loop")"""

# Drill loops and iterations


students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]

"""for pupil in sorted(students):
    print(pupil)
"""

# 3. Display integers from 0 to 15 not included, using a for loop and the range() instruction.

"""for i in range(15):
    print(i)"""

# 4. Create a for loop that displays integers from 1 to 10 included, but use the break instruction to interrupt it at 5.
"""for i in range(10):
    print(i)
    if i == 5:
        break
print("END", i)"""

# 5. Create a for loop that displays integers from 1 to 10 included, but use the continue to modify its execution at 5.

"""for i in range(10):
    print(i)
    if i <= 5:
        continue
    print("Hasta la Vista", i)
"""
"""list_of_numbers = [17, 38, 10, 25, 72]

for x in list_of_numbers:
    list_of_numbers.append(12)
    print(list_of_numbers)"""


'''def multiply(*elements):  # Add "*" to indicate that the parameters are infinite
    result = 1
    for element in elements:
        result = result * element
    return result


print(multiply(3, 3))'''



'''def double_stuff(a_list):
    """Overwrite each element in a_list with double its value."""
    for position in range(len(a_list)):
        a_list[position] = 2 * a_list[position]


things = [2, 5, 9]
print(things)
double_stuff(things)
print(things)'''
# 1. Say Hello : Write a function called hello that returns a string of characters. This function will take as argument a variable name.
# This function will return a string "Hello name".



"""def hello():
    name = (str(input("Enter your first name: ")))
    return print(f"Hello {name}")

hello()"""





