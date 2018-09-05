
#................................  Number 1  ..................................#

if True:
    print("Good Morning")

                        #..........................#

#................................  Number 2  ..................................#
gole = 'yes'

if gole == 'Yes':
        result = "Congratulations! This is a Gole"
else:
        result = "It almost a gole"

print(result)
                        #..........................#

# ................................  Number 3  ..................................#

points = 174

if points <= 50:
        result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
        result = "Oh dear, no prize this time."
elif points <= 180:
        result = "Congratulations! You won a wafer-thin mint!"
else:
        result = "Congratulations! You won a penguin!"

print(result)

                         # ..........................#

# ................................  Number 4  ..................................#

answer = 35
guess = 30   # this is just a sample answer and guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
   result = "Oops!  Your guess was too high."
elif guess==answer:
    result = "Nice!  Your guess matched the answer!"
print(result)

                            # ..........................#

# ................................  Number 5  ..................................#
state = 'CA'
purchase_amount = 20.00    # a sample state and purchase amount

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

                         # ..........................#


# ................................  Number 6  ..................................#


points = 174

points = 174  # use this input when submitting your answer

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)

                          # ..........................#

# ................................  Number 7  ..................................#

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
   usernames.append(name.lower().replace(' ', '_'))

print(usernames)

                          # ..........................#

# ................................  Number 8  ..................................#

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]


# write your for loop here
for user in range(len(usernames)):
    usernames[user] = usernames[user].lower().replace(" ", "_")

print(usernames)

                            # ..........................#

# ................................  Number 9  ..................................#

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

                            # ..........................#

# ................................  Number 10  ..................................#

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)

html_str += "</ul>"

print(html_str)

                            # ..........................#

# ................................  Number 11  ..................................#



cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

                           # ..........................#

# ................................  Number 12  ..................................#

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit, Counts in basket_items.items():
    if fruit in fruits:
        result += Counts
#if the key is in the list of fruits, add the value (number of fruits) to result


print(result)

                         # ..........................#

# ................................  Number 13  ..................................#

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit, count in basket_items.items():
#if the key is in the list of fruits, add to fruit_count.
    if fruit in fruits:
        fruit_count += count
#if the key is not in the list, then add to the not_fruit_count

    else:
        not_fruit_count += count

print(fruit_count, not_fruit_count)

                        # ..........................#

# ................................  Number 14  ..................................#

# number to find the factorial of
number = 6

# start with our product equal to number
product = number

# write your while loop here
while number > 1:
    number -= 1

    product *= number

    # decrement number with each iteration until it reaches 1

    # multiply the product so far by the current number

# print the factorial of number
print(product)

                        # ..........................#

# ................................  Number 15  ..................................#

# number to find the factorial of
number = 6

# start with our product equal to number
product = number

# write your for loop here
for num in range(1,number):
    product *=num


# print the factorial of number
print(product)

                        # ..........................#

# ................................  Number 16  ..................................#

start_num = 10 #provide some start number
end_num =100 #provide some end number that you stop when you hit
count_by =20 #provide some number to count by

# write a while loop that uses break_num as the ongoing number to
#   check against end_num
break_num = start_num
while break_num < end_num:
    break_num += count_by


print(break_num )

                        # ..........................#

# ................................  Number 17  ..................................#

start_num = 1000#provide some start number
end_num = 100#provide some end number that you stop when you hit
count_by = 2#provide some number to count by

# write a condition to check that end_num is larger than start_num before looping
if  start_num > end_num:
    result ="Oops! Looks like your start value is greater than the end value. Please try again."
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
        result = break_num


# write a while loop that uses break_num as the ongoing number to
#   check against end_num


print(result)

                        # ..........................#

# ................................  Number 18  ..................................#

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)

                        # ..........................#

# ................................  Number 19  ..................................#

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

                           # ..........................#

# ................................  Number 20  ..................................#

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

                               # ..........................#


# ................................  Number 21  ..................................#

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels,x_coord,y_coord,z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

                                # ..........................#

# ................................  Number 22  ..................................#

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names,cast_heights))# replace with your code
print(cast)

                                # ..........................#

# ................................  Number 23  ..................................#

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names,heights = zip(*cast)
print(names)
print(heights)

                               # ..........................#

# ................................  Number 24  ..................................#

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))# replace with your code
print(data_transpose)

                              # ..........................#

# ................................  Number 25  ..................................#

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, chraacter in enumerate(cast):
    cast[i] = chraacter + " " + str(heights[i])

print(cast)

                             # ..........................#

# ................................  Number 26  ..................................#

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]# write your list comprehension here
print(first_names)

                             # ..........................#

# ................................  Number 27  ..................................#

multiples_3 =[x * 44 for x in range(1,21)]# write your list comprehension here
print(multiples_3)


                             # ..........................#

# ................................  Number 28  ..................................#

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name,score in scores.items() if score > 65]# write your list comprehension here
print(passed)

                             # ..........................#


#  ................................  Number 29  ..................................#

def say_hello():
    print("Hello")

say_hello()

                             # ..........................#

#  ................................  Number 30  ..................................#
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(6,12))

                             # ..........................#


#  ................................  Number 31  ..................................#

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

                               # ..........................#