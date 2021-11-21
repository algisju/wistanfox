# Python code to generate
# random numbers and
# append them to a list
import random
# Function to generate
# and append them 
# start = starting range,
# end = ending range
# num = number of 
# elements needs to be appended
def Rand(start, end, num):
    res = []
  
    for j in range(num):
        res.append(random.randint(start, end))
  
    return res
  
# Driver Code
num = 10
start = 20
end = 40
print(Rand(start, end, num))
