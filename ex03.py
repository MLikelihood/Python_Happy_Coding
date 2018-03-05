#lists and conditional
a = [1, 1, 2, 3, 5, 8, 13, 2, 1, 0, -3, 21, 34, 55, 89]
num = int(input("Choose a number: "))
new_list = []
for i in a:
    if i < num:
        new_list.append(i)
print(new_list)