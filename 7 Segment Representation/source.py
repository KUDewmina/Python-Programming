SEGMENTS = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"],
    ':': ["   ", " . ", " . "]
}

time = input()
# Initialize the three output lines
output_lines = ["", "", ""]

# Build each of the three lines
for digit in time:
    segment = SEGMENTS[digit]
    for i in range(3):
        output_lines[i] += segment[i]  
# Print the result
for char in output_lines:
    print(char)
