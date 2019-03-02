ip = input("choose from O,A,B,C,F")

#I was giving condition as ip = "O" or "o" , so, when i was entering r as input, 
#first, it was checking against Capital O, and becoming false, 
#then, it was checking it with small o, direct without equalising it to ip. 
#and o condition was true, by boolean approach.
#hence we were getting a true condition and outstanding in print.


# print (ip) 
# r
#     false or true
if (ip == "O") or (ip =="o"):
    print("Outstanding")
if ip == "A" or ip == "a":
    print("Very Good")
if ip == "B" or ip == "b":
    print("Good")
if ip == "C" or ip == "c":
    print("Average")
if ip == "F" or ip == "f":
    print("Fail")


## In computer, all the values are true except 0(zero), None and nil

# print(bool(0))
# print(bool('O'))
# print(bool(None))
# print(bool(-1))
# print(bool(1.23))
# print(bool('$'))
# print(bool('4'))
# print(bool())