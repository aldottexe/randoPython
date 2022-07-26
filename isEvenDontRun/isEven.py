import os

def isEven(i):

    if i%2 == 0:
        return True
    
    #double check just to be sure :)
    os.system(f"python3 doubleCheck.py {i}")
    return False

isEven(3)


