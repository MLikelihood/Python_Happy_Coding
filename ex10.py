import random
a = random.sample(range(50), 20)
b = random.sample(range(50), 20)
result = [i for i in set(a) if i in b]
print(a)
print(b)
print(result)

result1 = [i for i in result if result.count(i) == 1]
print(result1)