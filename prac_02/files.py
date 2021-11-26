# 1
out_file = open("name.txt", 'w')
user_name = str(input("Enter your name: ".title()))
print("Your name is:", user_name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(name)

# 3
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)

# 4
total = 0
in_file = open("numbers.txt", "r")
for number in in_file:
    number = int(number)
    total = total + number
in_file.close()
print(total)
