list = ["laptop", "Truck", "p%addle /!@# boa%rd", "r%ace /!@# ca%r", "H!i"]
reflection = ""
badchar = " !@#$%^&*()/~|"
def palindrome():
    for examples in list:
        print("Input:", examples)

        for char in badchar:
            examples = examples.replace(char, "")
            cleanexamples = examples.replace(char, "")
            examples = examples.lower()
            reflection = examples[::-1]
        print("Input(purified):", cleanexamples)
        print("Output:", examples)

        if (examples == reflection):
            print(examples, "IS a palindrome \n")
        else:
            print(examples, "IS NOT a palindrome \n")
