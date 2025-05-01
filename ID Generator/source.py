from datetime import datetime
from cs1033_evaluator import evaluate_L6_E2

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################

file_name = input()  # getting file name 
file = open(file_name, "r") # opening file
years = []
index = 1
results = []

def write():  # -> Function to write rows in file
    output_file = open("output.txt","w")
    for result in results:
        output_file.write(result + "\n")
    output_file.close()
    
def fix_number(val): # -> Function to create numbers in 3 digits by adding zeros 
    if val<10:
        val= "00"+str(val)
    elif val<100:
        val= "0"+str(val)
    return val
    
for line in file: # reading lines from opened file
    result = ''
    details = line.split()
    name,birthday,gender = details[0],details[1],details[2]  # assigning variables
    days = days_to_birthday(str(birthday))
    sliced_birthday = birthday.split('-') # assigning day/month/year
    year = sliced_birthday[0]
    years.append(year)
    index = years.count(year)  # calculating order of submission
    if gender == 'F': # checking for females and if it,add 500 to days
        days+=500
    result = str(name) + " " + str(year) + str(fix_number(days)) + str(fix_number(index)) #creating outputting line
    results.append(result)

write() # -> calling function for write


################################################################################
# Please do not edit anything below this line.
evaluate_L6_E2()

##################### End of the programme #####################################
