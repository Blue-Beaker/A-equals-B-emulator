import random
import aequalsb

file="multiply.aeqb"            #A=B Program file
count=1024                      #Test count

def genInput():                 #Function to generate random input and answer pair
    a=random.getrandbits(4)
    b=random.getrandbits(4)
    input=f"{bin(a)[2:]}*{bin(b)[2:]}"
    answer=bin(a*b)[2:]
    return input,answer

aeqb=aequalsb.AeqB(file)

for i in range(count):
    input,answer=genInput()
    aeqb.printProgramLine=False
    aeqb.printProgress=False
    result=aeqb.getResult(input)
    if result==answer:
        print(f"\033[0;37;42m{input},{result}\033[0m {answer}")
    else:
        aeqb.printProgramLine=True  #Print every move on failure
        aeqb.printProgress=True     #Print every move on failure
        result=aeqb.getResult(input)
        print(f"\033[0;37;41m{input},{result}\033[0m {answer}")