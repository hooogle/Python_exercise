import time
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
start = time.clock()
print(sum(numbers))
elapsed = (time.clock() - start)
print("Time used:",elapsed)