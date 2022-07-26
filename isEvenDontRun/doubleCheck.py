from isEven import isEven
import sys, os

testMe = int(sys.argv[1])

#never hurts to triple check!!
os.system(f"python3 doubleCheck.py {testMe}")

print(isEven(testMe))