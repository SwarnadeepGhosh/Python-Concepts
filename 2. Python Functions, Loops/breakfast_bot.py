# Our goal will be to create a simple program for ordering breakfast
'''
OK, so if we want to build this program, here are some of the things we will need to be sure it does:
Get input and use it to determine what happens next
Handle bad input without crashing
Be flexible with the input the user can enter
Print messages to the console, with a short pause after each one
Allow the player to order again if they like
Now that we have a better idea of the specifications for the program, we can start putting it together.
'''
import time
i=True

def print_pause(printable_value):
    time.sleep(1.5)
    print(printable_value)


def order_again():
    while True:
        time.sleep(1)
        global again
        response = input("Would you like to give another order? Please reply with 'yes' or 'no'\n").lower()
        if 'yes' in response :
            print_pause("Very good, I'm happy to take another order.")
            #global again
            again = 'yes'
            i = True
            break

        elif 'no' in response :
            print_pause('Thank You, Have a great day ! ..')
            i = False
            again = 'no'
            break

        else :
            print_pause('Please enter correct choice !')

print_pause('Hello! I am Swarnadeep, the Breakfast Bot.')
print_pause('Today we have two breakfasts available.')
print_pause('The first is waffles with strawberries and whipped cream.')
print_pause('The second is sweet potato pancakes with butter and syrup.')

while i == True :
    time.sleep(1)
    order = input('Please place your order. Would you like waffles or pancakes?\n').lower()
    if 'waffles' in order :
        print_pause('Waffles it is!')
        print_pause('Thanks for ordering')
        print_pause('Your order will be ready shortly...')
        order_again()
        if again == 'no':
            break

    elif 'pancakes' in order:
        print_pause('Pancakes it is!')
        print_pause('Thanks for ordering')
        print_pause('Your order will be ready shortly...')
        order_again()
        if again == 'no':
            break

    else:
        print_pause('Sorry, I couldn\'t understand, Please enter correct choice ...')
        time.sleep(0.5)
        continue

    #if again == 'yes':
    #    continue
