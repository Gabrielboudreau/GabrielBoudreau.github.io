InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Gabriel",  
               "LastName": "Boudreau",  
               "DOB": "January 25",  
               "Residence": "San Diego",  
               "Email": "gabrielb50533@gmail.com",  
               "Pets":["Molly, Obi, Jax, Zoey, Dragon"]  
              })  

InfoDb.append({  
               "FirstName": "Bob",  
               "LastName": "Ross",  
               "DOB": "October 29",  
               "Residence": "Florida",  
               "Email": "calminghillside@gmail.com",  
               "Pets":["Annete, Bob, Bobette"]  
              })

InfoDb.append({  
               "FirstName": "Ryan",  
               "LastName": "Reynolds",  
               "DOB": "October 23",  
               "Residence": "Los Angeles",  
               "Email": "ryansleftpec@gmail.com",  
               "Pets":["Penny, Baxter"]  
              })

InfoDb.append({  
               "FirstName": "Elon",  
               "LastName": "Musk",  
               "DOB": "June 28",  
               "Residence": "Philidelphia",  
               "Email": "cryptocrash@gmail.com",  
               "Pets":["Floki"]
              })

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Pets: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Pets"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)



def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion

