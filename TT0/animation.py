import time
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

