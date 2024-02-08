#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    # listing the months so i can use em later
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #found zfill online, gks4gks good explanation. keepin it 2-digits
    #i couldn't get it to work without zfill
    return str(months.index(month) + 1).zfill(2)


#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    parts = user_string.split()
    month = parse_month(parts[0])
    day = parts[1][:-1].zfill(2)
    year = parts[2]
    return f"{month}/{day}/{year}"

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    while True:
        user_input = input()
        if user_input =='-1':
            break
        print(parse_date(user_input))