import pandas


# checks for yes/ no response
# functions go here

def not_blank(question):
    valid = False

    while not valid:
        user_response = input(question).lower()
        if user_response != "":
            return user_response
        else:
            print("This can't be blank. Enter a response.")


# Show instructions
def instructions():
    print()
    print("Item name,")

    return ""


# Checks that the user has entered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == \
                    var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine starts here

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions (yes/no): ")

if want_instructions == "yes":
    print("")

print()

recipe_name = not_blank("What are you making? ")

quantity = num_check("servings:",
                     "The amount must be a whole number which is more than zero",
                     int)

ingredients = []
while True:
    ingredient_name = input("Enter ingredient name (type 'xxx' to finish): ")
    if ingredient_name.lower() == 'xxx':
        break

    weight = num_check("Enter weight for {}: ".format(ingredient_name), "Weight must be a positive number.", float)
    price = num_check("Enter price for {}: ".format(ingredient_name), "Price must be a positive number.", float)
    ingredients.append({"name": ingredient_name, "weight": weight, "price": price})

print(ingredients)

def get_unit():
    while True:
        unit = input("Enter the unit of measurement for this ingredient ('kg', 'g', or 'L'): ").lower()
        if unit in ['kg', 'g', 'l']:
            return unit
        else:
            print("Invalid unit. Please enter 'kg', 'g', or 'L.'")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")


ingredients = []
while True:
    ingredient_name = input("Enter an ingredient name (or type 'quit' to finish): ")
    if ingredient_name.lower() == "quit":
        break
    if ingredient_name != "":
        input_str = input("Enter the weight and unit of the ingredient separated by a space (e.g., '500 g'): ")
        try:
            weight, unit = input_str.split()
            weight = float(weight)
            unit = unit.lower()
        except ValueError:
            print("Invalid input. Please enter the weight and unit separated by a space (e.g., '500 g').")
            continue

        quantity = get_float_input(f"Enter the quantity of the ingredient in numbers or liters: ")
        amount_paid = get_float_input("Enter the amount paid for the ingredient: ")
        ingredients.append((ingredient_name, weight, unit, quantity, amount_paid))
    else:
        print("Ingredient name cannot be empty.")

print("List of ingredients:")
total_cost = 0
for ingredient, weight, unit, quantity, amount_paid in ingredients:
    cost = quantity * amount_paid
    total_cost += cost
    print(
        f"{ingredient} - {weight} {unit} - Quantity: {quantity:.2f} - Amount Paid: ${amount_paid} - Cost: ${cost:.2f}")

print(f"Total cost to make the recipe: ${total_cost:.2f}")

# Calculate the number of servings
while True:
    try:
        servings = int(input("Enter the number of servings the recipe makes: "))
        if servings <= 0:
            print("Please enter a positive number of servings.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer number of servings.")

price_per_serving = total_cost / servings
print(f"Price per serving: ${price_per_serving:.2f}")








