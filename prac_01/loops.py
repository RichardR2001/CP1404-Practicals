for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

# a
for j in range(0, 101, 10):
    print(j, end=" ")
print("\n")

# b
for k in range(20, 0, -1):
    print(k, end=" ")
print("\n")

# c
user_stars = int(input("Enter numbers of stars: "))
for m in range(user_stars):
    print("*", end="")
print("\n")

# d
user_stars = int(input("Enter number of stars: "))
for n in range(1, user_stars + 1):
    print("*" * n)
