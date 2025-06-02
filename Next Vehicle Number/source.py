import string
file = open("a.txt","r")

english = [x for x in string.ascii_uppercase]

def change_letters(pr_letters):
    nw_letters = []
    pr_letters = [char for char in pr_letters]
    nw_letters.append(pr_letters[0])
    if pr_letters[2]=="Z":
        nw_letters.append("A")
        index = english.index(pr_letters[1])
        nw_letters.insert(1,english[index+1])
    else:
        nw_letters.append(pr_letters[1])
        index = english.index(pr_letters[1])
        nw_letters.insert(2,english[index+1])

    return nw_letters

def change_numbers(pr_number,pr_letters):
    nw_number = 0
    if pr_number == 9999:
        nw_number = "0001"
        nw_letters = change_letters(pr_letters)
    else:
        nw_number = str(pr_number+1).zfill(4)
        nw_letters = pr_letters
    return nw_number,nw_letters

outputs = []

for line in file:
    
    pr_letters,pr_number = line.strip().split("-")
    pr_number = int(pr_number)
    nw_number,nw_letters = change_numbers(pr_number,pr_letters)
    outputs.append(''.join(nw_letters)+"-"+nw_number)

outputfile=open("b.txt","w")
for line in outputs:
    outputfile.write(line+"\n")
outputfile.close()

file.close()
