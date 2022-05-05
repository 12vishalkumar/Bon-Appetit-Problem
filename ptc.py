import math
import os
import random
import re
import sys

# Complete the 'bonAppetit' function below.
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b

def bonAppetit(bill, k, b):
    # Write your code here
    L = len(bill)
    c = 0
    for i in range(L):
        if(i==k):
            continue
        else:
            c += bill[i]
    b_chr = int(c/2)
    if(b_chr==b):
        print('Bon Appetit')
    elif(b>b_chr):
        print(b-b_chr)
    else:
        print('Not valid')
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)