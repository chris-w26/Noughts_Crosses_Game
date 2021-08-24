#### Title: Automated Sandwich Shop (Codecademy project)
#### Author: Chris Woodham
#### Date: 20/08/21

# Create the menu
menu = [['white bread', 1.00, 0.50, 'yes - vegetarian', 'yes - vegan'],
        ['seeded bread', 1.00, 0.50, 'yes - vegetarian', 'yes - vegan'],
        ['brown bread', 1.00, 0.50, 'yes - vegetarian', 'yes - vegan'],
        ['falafel', 2.00, 1.50, 'yes - vegetarian', 'yes - vegan'],
        ['vegan Hoisin duck', 3.00, 2.25, 'yes - vegetarian', 'yes - vegan'],
        ['tomato, avocado and coriander', 1.50, 1.25, 'yes - vegetarian', 'yes - vegan'],
        ['egg mayo', 2.00, 1.50, 'yes - vegetarian', 'no - vegan'],
        ['tomato, avocado and mozzarela', 2.00, 1.50, 'yes - vegetarian', 'no - vegan'],
        ['chicken and stuffing', 3.00, 2.25, 'no - vegetarian', 'no - vegan'],
        ['sausage and bacon', 3.50, 2.75, 'no - vegetarian', 'no - vegan'],
        ['house salad', 1.00, 0.75, 'yes - vegetarian', 'yes - vegan'],
        ['grated cheddar', 1.00, 0.75, 'yes - vegetarian', 'no - vegan'],
        ['hummous', 1.00, 0.75, 'yes - vegetarian', 'yes - vegan']]

## Automated sandwich shop

# Step 1 - ask the customer if they will be eating in or taking out
print('Good afternoon and welcome to the automated sandwich shop, will you be eating in or taking out?' + '\n' +
'1) Eat in;  2) Take out' + '\n' +
'Please enter the number of your selected option below:')
eat_in_or_take_out = int(input())


# Step 2 - ask the customer if they have any dietary preferences
print('Thank you, and do you have any dietary preferences:' + '\n' +
'1) Vegan;  2) Vegetarian;  3) Meat eater' + '\n' +
'Please enter the number of your selected option below:')
diet_pref = int(input())

# Step 3 - ask the customer to select their bread and fillings
# modify the menu according to the customers dietary preferences
dietary_pref_menu = []
if diet_pref == 3:
    dietary_pref_menu = menu
elif diet_pref == 2:
    for ingredient in menu:
        if ingredient[3] == 'yes - vegetarian':
            dietary_pref_menu.append(ingredient)
elif diet_pref == 1:
    for ingredient in menu:
        if ingredient[4] == 'yes - vegan': 
            dietary_pref_menu.append(ingredient)

# now modify the menu according to whether the customer is eating in or taking out
if eat_in_or_take_out == 1:
    for i in range(0, len(dietary_pref_menu), 1):
        dietary_pref_menu[i].pop(2)
elif eat_in_or_take_out == 2:
    for i in range(0, len(dietary_pref_menu), 1):
        dietary_pref_menu[i].pop(1)

# print the menu in a customer friendly format
print('Please select the bread and fillings you would like from the menu below:' + '\n')
for i in range(0, len(dietary_pref_menu), 1):
    print(((str(i+1) + ') {ingredient}; price = £{price}')).format(ingredient = dietary_pref_menu[i][0], price = dietary_pref_menu[i][1]) + '\n')
print('Please enter the row numbers of the bread and fillings you would like (e.g. 1 4 7) below:')
bread_fill_list = input().split()
for i in range(0, len(bread_fill_list), 1):
    bread_fill_list[i] = int(bread_fill_list[i])
# Step 4 - use the selection of bread and fillings to calculate the total cost 
total_cost = 0
for value in bread_fill_list:
    total_cost += dietary_pref_menu[value - 1][1]

# Step 5 - check how many sandwiches the customer would like 
print('Thank you for selecting the fillings for your sandwich. How many sandwiches of this type would you like?' + '\n' +
'1) 1 sandwich;  2) 2 sandwiches;  3) 3 sandwiches;  4) 4 sandwiches' + '\n' +
'Please enter the number of your selected option below:')
no_sandwich = int(input())
# adjust the total_cost according to the number of sandwiches purchased
total_cost = total_cost * no_sandwich

# Step 6 - check if the customer would like another different type of sandwich
print('Would you like to order any other sandwiches?' + '\n' +
'1) Yes;  2) No' + '\n' +
'Please enter the number of your selected option below')
additional_sandwich = int(input())

while additional_sandwich == 1:
    print('Please select the bread and fillings you would like from the menu below:' + '\n')
    for i in range(0, len(dietary_pref_menu), 1):
        print(((str(i+1) + ') {ingredient}; price = £{price}')).format(ingredient = dietary_pref_menu[i][0], price = dietary_pref_menu[i][1]) + '\n')
    print('Please enter the row numbers of the bread and fillings you would like (e.g. 1 4 7) below:')
    bread_fill_list = input().split()
    for i in range(0, len(bread_fill_list), 1):
        bread_fill_list[i] = int(bread_fill_list[i])
    for value in bread_fill_list:
        total_cost += dietary_pref_menu[value-1][1]
    print('Thank you for selecting the fillings for your sandwich. How many sandwiches of this type would you like?' + '\n' +
    '1) 1 sandwich;  2) 2 sandwiches;  3) 3 sandwiches;  4) 4 sandwiches' + '\n' +
    'Please enter the number of your selected option below:')
    no_sandwich = int(input())
    total_cost = total_cost * no_sandwich
    print('Would you like to order any other sandwiches?' + '\n' +
    '1) Yes;  2) No' + '\n' +
    'Please enter the number of your selected option below')
    additional_sandwich = int(input())

# Ask the customer to pay
print('Please pay now (chip and pin or contacless are available)')

# Would the customer like a receipt?
print('Thank you for your payment. Would you like a receipt?' + '\n' +
'1) Yes;  2) No' + '\n' +
'Please enter the number of your selected option below:')
receipt_option = int(input())
if receipt_option == 1:
    print('Your sandwiches came to a total of £{total_cost}.'.format(total_cost = total_cost))
print('Thank you for shopping with the Automated Sandwich Shop today! :)')
