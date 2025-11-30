import math
a = int(input())
if a==1:
    num = int(input("Enter a number: "))
    sum = 0
    for i in range(num):
        prob = float(input("Enter a probability: "))
        sum = sum + prob * math.log2(prob)
    print(-sum)
elif a==2:
    num = int(input("Enter a number of letters: "))
    sum = 0
    for i in range(num):
        num_of_letters = float(input("Enter a number of letters in code: "))
        prob = float(input("Enter a probability: "))
        sum = sum + prob * num_of_letters
    print(sum)
