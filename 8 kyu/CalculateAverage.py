# Calculate average

# Answer 1
def find_average(numbers):
   return sum(numbers)/len(numbers)
  
# Answer 2
from functools import reduce
def find_average(numbers):
    return reduce(lambda a,b: a+b, numbers) / len(numbers)
