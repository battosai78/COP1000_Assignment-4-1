
# Charge for this sign.
charge = None
# Number of characters.
numChars = None
# Color of characters.
color = None
# Type of wood.
woodType = None

# Write assignment and if statements here as appropriate.
print("Enter number of characters on sign:")
numChars = input()
print("Enter wood type:")
woodType = input()
print("Enter color:")
color = input()

charge = 35
if int(numChars) > 5:
    charge = (int(numChars) - 5) * 4 + charge
if str(woodType) == "oak":
    charge = charge + 20
if str(color) == "gold":
    charge = charge + 15

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
