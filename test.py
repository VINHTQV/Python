
import math 
import os 
import random 
import re 
import sys

if name == 'main': n = int(raw_input().strip())
    #print(n % 2)
    if n%2 != 0: ## odd
        print("Weird")
    else: ## even
        if (n >= 2) and (n <= 5):
            print("Not Weird")
        elif n <= 20:
            print("Weird")
        else:
            print("Not Weird")