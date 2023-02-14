print("Enter the Number: ")
num = input()

num = int(num)
print("\nFactors of", num)

i = 1
while i<=num:
    if num%i==0:
        print(i)
    i = i+1