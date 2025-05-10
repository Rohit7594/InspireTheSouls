from datetime import datetime

def calculate_root_number(dob):
    """Calculate root number (birth number) from date of birth."""
    # Convert string to datetime object
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    
    # Get the day
    day = dob_date.day
    
    # If day is already a single digit or a master number, return it
    if day <= 9 or day in [11, 22, 33]:
        return day
    
    # Otherwise, reduce to a single digit
    while day > 9:
        day = sum(int(digit) for digit in str(day))
    
    return day

def get_zodiac_sign(dob):
    """Get zodiac sign based on date of birth."""
    # Convert string to datetime object
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    month = dob_date.month
    day = dob_date.day
    
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def calculate_destiny_number(dob):
    """Calculate destiny number from the date of birth."""
    # Convert string to datetime object
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    
    # Get day, month, and year
    day = dob_date.day
    month = dob_date.month
    year = dob_date.year
    
    # Sum the digits of day, month, and year separately
    day_sum = sum(int(digit) for digit in str(day))
    month_sum = sum(int(digit) for digit in str(month))
    year_sum = sum(int(digit) for digit in str(year))
    
    # Sum all the results
    total = day_sum + month_sum + year_sum
    
    # Reduce to single digit unless it's 11, 22, or 33
    while total > 9 and total not in [11, 22, 33]:
        total = sum(int(digit) for digit in str(total))
    
    return total 