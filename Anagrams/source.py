file_name = input()
outputs = []

with open(file_name, "r") as file:
    for line in file:
        first, second = line.strip().split()  # Added .strip() to remove newline characters from each line before splitting
        if sorted(first) == sorted(second):
            outputs.append("Anagram\n")  # Appended \n directly to each result for cleaner writing.
        else:
            outputs.append("Not Anagram\n")

with open("output.txt", "w") as f:
  f.writelines(outputs)

# How "writelines()" works
''' 
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
    
Hello -> Output
World 
'''

