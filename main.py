import time
import lists
def menu():
    print('1 -- Swap Numbers' )
    print('2 -- Animation' )
    print('3 -- TT1')
    print('4 -- Exit' )
    runOptions()

def sub_menu():
    print('1 -- Bigger number First')
    print('2 -- Smaller number First')
    print('3 -- Return')
    print('4 -- Exit')
    subOptions()

def submenu1():
    print('1 -- Factorial', )
    print('2 -- Lists')
    print('3 -- Fibonacci')
    print('4 -- Exit')
    suboptions1()

def num_swap():
    sub_menu()

def animation():
    ship()

def swap():
  while True:
      try:
          num1 = int(input('choose a number:  '))
          num2 = int(input('choose a second number: '))
          swapValues = [num1, num2]
          if True:
            swapValues.sort(reverse = True)
            print(swapValues)
            menu()
          else:
            swapValues.sort()
            print(swapValues)
            menu()
      except ValueError:
          print('Invalid input. Please enter an integer input.')
    
def suboptions1():
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))

            if option == 1:
              lists.tester1()
              time.sleep(2)
              menu()
            elif option == 2:
              lists.tester()
              time.sleep(2)
              menu()
            elif option == 3:
              lists.fibonacci()
              time.sleep(2)
              menu()
            elif option == 4:  
                print('Goodbye!')
                exit() 
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

def subOptions():
    while True:
        try:
            option = int(input('Enter your choice 1-4: '))
            bigger = False
            if option == 1:
                bigger == True
                swap()
            elif option == 2:
                swap()
            elif option == 3:
                menu()
            elif option == 4:  
                print('Goodbye!')
                exit() 
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

def runOptions():
    while True:
        try:
            option = int(input('Enter your choice 1-3: '))
            if option == 1:
                num_swap()
            elif option == 2:
                animation()
                menu()    
            elif option == 3:
              submenu1()
            elif option == 4:  
                print('Goodbye!')
                exit() 
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def ocean_print():

    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)


def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "  \_O   ")
    print(sp + "    |\   ")
    print(sp + "    |")
    print(sp + "   / |")
    print(sp + " \____/  ")
    print(RESET_COLOR)



def ship():

    ocean_print()

    start = 0  
    distance = 60 
    step = 2 

   
    for position in range(start, distance, step):
        ship_print(position) 
        time.sleep(.1)

if __name__ == "__main__":
  menu()        
