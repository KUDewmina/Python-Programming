string = "-28"
string = string.lstrip("-")
binary = bin(int(string)).lstrip("0b")
binary = binary.zfill(8)
print(binary)
invert = []
for i in binary:
    if i=="1":
        invert.append("0")
    else:
        invert.append("1")
binary_str = ''.join(invert)
new = int(binary_str,2) + int("1",2)
binary = bin(new).lstrip("0b").zfill(8)
print(binary)
