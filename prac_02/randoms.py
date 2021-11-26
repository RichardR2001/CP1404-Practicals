import random

print(random.randint(5,20))
# 11
# 14
# 10

print(random.randrange(3, 10, 2))
# 7
# 9
# 7

print(random.uniform(2.5, 5.5))
# 4.914763667891557
# 3.4878091967259186
# 3.8132257027371343


# Integer between 5 and 19 inclusive, smallest number is 5, largest number is 19
# Integer between 3 and 9 inclusive, with the difference/step of 2. 4 is not possible
# Any real number between from 2.5 to 5.5 (exclusive of 5.5), largest being 4.999999999999...


print(random.uniform(1, 100.0))
