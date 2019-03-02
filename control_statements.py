#Input two numbers and check if they are equal

a = int(input("enter a"))
b = int(input("enter b"))

if a==b:
    print("numbers are equal")
else:
    print("not equal") 


#Enter a character and display a text for each respective character


#Find if a digit, alphabet or whitespace is entered

value = input("enter a digit, alphabet or a whitespace ")

if (value.isdigit()):
    print ("its a digit")

elif (value.isspace()):
    print ("whitespace")

elif (value.isalpha()):
    print ("an alphabet")


