#input_str = "YYYYggkeeeAAABV "
input_str = str(input("Введите строку: "))
count = 1
newstr = ""

for i in range (0, (len(input_str) - 1)):
    if input_str[i] == input_str[i + 1]:
        count += 1
    else:
        newstr += input_str[i]
        if count != 1:
            newstr += str(count)
        count = 1
print(newstr) 

