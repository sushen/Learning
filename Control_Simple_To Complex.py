
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