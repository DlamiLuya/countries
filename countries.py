'''A Quiz game that tests how many African countries a person knows'''


# Define a gameplay function
# This function will give usr instructions on how to play the game.
# It will then compare the users input to a list of all the African countries to find if it matches.
# It will then allocate score to the user if the entered a correct country.
def game_play():
    print('''\nLets test your Knowledge of Africa
****************INSTRUCTIONS****************
-Name as many countries as you can
-When done naming type in 'done'
-Names of countries are case sensitive, e.g south africa should be resprected to South Africa
-I will tally up your score and tell you how many you got right\n''')
    
    done = 'typing'
    count = 0
    correct_country = []
    print("Enter Country: ")
    while done == 'typing':
        country = input()
        if country in correct_country:
            print('Oops youve already mentioned this country')
        elif country in countries:
            count += 1
            countries.remove(country)
            correct_country.append(country)
        elif country == 'done' or country == 'Done':
            done= country
        else:
            print('non country')
    print(f"You got {count} out of 54")

        

# A list of all countries in Africa in Alphabetic order.
countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi'
            'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros',
            'Ivory Coast', 'Djibouti', 'Democratic Republic of the Congo', 'Egypt', 
            'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 
            'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 
            'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique',
            'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Sao Tome & Principe',
            'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan',
            'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']


# Defining a menu for the game, gives options to play the game or to quit the game.
# The play game option calls the method to actually start playing the game.
while True:
    main_menu = input('''1.Play Game
2.Quit
Enter option: ''')
    if main_menu == '1':
        print("\ngame start")
        game_play()
    elif main_menu == '2':
        exit()
    else:
        print("Invalid input, try again")