input_str = "Y4g2ke3A3BV"
newstr = " "

for i in range(0, len(input_str)):
    if input_str[i].isdigit() != 1:
        newstr += input_str[i]
    else:
        newstr += (input_str[i - 1] * int(input_str[i])) [:-1]
print(newstr)