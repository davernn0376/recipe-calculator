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


def get_weight():
    while True:
        try:
            weight = float(input("Enter the weight for this ingredient: "))
            return weight
        except ValueError:
            print("Invalid input. Please enter a valid weight.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_input_with_unit(prompt):
    while True:
        try:
            input_str = input(prompt)
            value_str, unit = input_str.split()
            value = float(value_str)
            unit = unit.lower()
            valid_units = ['kg', 'l', 'g', 'ml', 'sheets']
            if unit not in valid_units:
                print("Invalid unit. Please enter one of:", ", ".join(valid_units))
                continue
            return value, unit
        except ValueError:
            print("Invalid input. Please enter a valid numeric value and unit separated by a space.")


ingredients = []

while True:
    ingredient_name = input("Enter an ingredient name (or type 'quit' to finish): ")
    if ingredient_name.lower() == "quit":
        break
    if ingredient_name != "":
        input_str = input(f"Enter the weight and unit of measurement for {ingredient_name} (e.g., '500 g'): ")
        try:
            weight, unit = input_str.split()
            weight = float(weight)
            unit = unit.lower()
            valid_units = ['kg', 'l', 'g', 'ml', 'sheets']
            if unit not in valid_units:
                print("Invalid unit. Please enter one of:", ", ".join(valid_units))
                continue
        except ValueError:
            print("Invalid input. Please enter the weight and unit separated by a space (e.g., '500 g').")
            continue

        amount_used_str = input(f"Enter how much {ingredient_name} you want to use (e.g., '200 {unit}'): ")
        try:
            amount_used, unit_used = amount_used_str.split()
            amount_used = float(amount_used)
            unit_used = unit_used.lower()
            if unit_used not in valid_units:
                print("Invalid unit. Please enter one of:", ", ".join(valid_units))
                continue
        except ValueError:
            print("Invalid input. Please enter a valid numeric value and unit.")
            continue

        amount_bought, unit_bought = get_input_with_unit(f"How much of {ingredient_name} did you buy (e.g., '500 kg'): ")

        amount_paid = get_float_input("Enter the amount paid for the ingredient: ")
        if unit_used == 'ml' and unit_bought == 'l':
            amount_used /= 1000  # Convert mL to L before calculation
        elif unit_used == 'g' and unit_bought == 'kg':
            amount_used /= 1000  # Convert g to kg before calculation

        ingredients.append(
            (ingredient_name, weight, unit, amount_used, unit_used, amount_bought, unit_bought, amount_paid))
    else:
        print("Ingredient name cannot be empty.")

print("List of ingredients:")
total_cost = 0
for ingredient, weight, unit, amount_used, unit_used, amount_bought, unit_bought, amount_paid in ingredients:
    cost = (amount_paid * amount_used) / amount_bought  # Updated calculation
    print(
        f"{ingredient} - {weight} {unit} - Amount Used: {amount_used:.2f} {unit_used} - Amount Bought: {amount_bought:.2f} {unit_bought} - Amount Paid: ${amount_paid:.2f} - Cost: ${cost:.2f}")
    total_cost += cost

print(f"Total cost to make the recipe: ${total_cost:.2f}")

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