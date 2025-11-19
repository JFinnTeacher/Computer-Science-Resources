# Open a dictionary file and list to hold its entries
dictionary = open("words.txt","r")
dictlist=[]

# Read in our dictionary file and save it as a list (lower case)
while True:
    
    contents = dictionary.readline()
    
    if contents == "":
        break
    else:
        contents = contents.replace("\n","")
        dictlist.append(contents.lower())
       
        
# User enters a password and how many (in billions) passwords can be checked per second
# Typically password cracking system can handle 1 billion per second
password = input("Enter password to check:")
perSecond = 1000000000*int(input("How many passwords per second can be checked? (Billions) :"))

# Firstly check if the password is in the dictionary file...
if password.lower() in dictlist:
    print ("*** Bad news - It's in the dictionary! ***")
        
else:
    print ("*** Good start - Not in the dictionary! ***")


# Lists of the various character types in a password
UpperLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
LowerLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','\"','£','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']',':',';','@','\'','#','~','\\','<','>',',','.','?','/']

TotalPossible = 0
Description = "Your password uses"

UpperLettersFlag = 0
LowerLettersFlag = 0
NumbersFlag = 0
SymbolsFlag = 0

# Check every character in the password and flag what types of character are used.
for i in password:
    if i in UpperLetters:
        UpperLettersFlag = 1
    elif i in LowerLetters:
        LowerLettersFlag = 1
    elif i in Numbers:
        NumbersFlag = 1
    elif i in Symbols:
        SymbolsFlag = 1
    else:
        print ("Warning - Not registered symbol!")
        
# For each type of character used, add the number of possible characters in the set to a total used to calculate permutations
if  UpperLettersFlag == 1:
    TotalPossible += 26
    Description += "\n - uppercase"
if  LowerLettersFlag == 1:
    TotalPossible += 26
    Description += "\n - lowercase"
if  NumbersFlag == 1:
    TotalPossible += 10
    Description += "\n - numbers"
if SymbolsFlag == 1:
    TotalPossible += 33
    Description += "\n - symbols"

# Print a list of character types that are used in the password
print ("\n"+Description)

# Total permutations is the number of possible characters to the power of the password length
permutations = TotalPossible ** len(password)
print ("Total possible permutations:",permutations)

# At rate of password checking print how many seconds it would take to crack the password
# NOTE : We divide our answer by 2 as we assume we'd find the password halfway through a brute force on average
seconds = (permutations/perSecond)/2
print ("\n"+"At a billion attempts per second your password would be cracked in",f'{seconds:.2f}',"seconds.")
# and days...
days = seconds/(3600*24)
print ("At a billion attempts per second your password would be cracked in",f'{days:.2f}',"days.")

# and years...
years = days/365
print ("At a billion attempts per second your password would be cracked in ",f'{years:.2f}',"years.")

    