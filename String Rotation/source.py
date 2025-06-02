file = open("a.txt","r") 

def Write(output):
    output_file = open("b.txt","w")
    for line in output:
        output_file.write(line+"\n")
    else:
        output_file.write("\n")
    output_file.close()

outputs = []
def format(vals):
    n = len(vals)
    middle = "|"
    max_width = 0
    for char in vals:
        if len(char)>max_width:
            max_width = len(char)
    for char in vals:
        middle += str(char).ljust(max_width)+"|"

    line = "-"*max_width

    symbols = "+"
    for _ in range(len(vals)):
        symbols += line + "+"
    
    
    outputs.append(symbols)
    outputs.append(middle)
    outputs.append(symbols)

    Write(outputs)

def rotate(method,count,values):
    
    new = []
    if method=="L":
        new = new + values[-count:]+values[:-count]
    else:
        new = new + values[count:]+values[:count]
    return new

for index,line in enumerate(file):
    if index==0:
        continue
    else:
        method,count,*values = line.strip().split()
        rotated = rotate(method,int(count),values)
        format(rotated)
file.close()


