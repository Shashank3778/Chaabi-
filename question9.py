from datetime import datetime, timedelta

def dif(from_date, to_date, difference):
    # Convert strings to datetime objects
    from_datetime = datetime.strptime(from_date, "%y-%m-%d")
    to_datetime = datetime.strptime(to_date, "%y-%m-%d")
    
    # Calculate the difference between the dates in days
    date_diff = (to_datetime - from_datetime).days
    
    # Check if the difference is less than the specified days
    return date_diff < difference

from_date = "23-06-04"
to_date = "23-06-15"
difference = 10

res = dif(from_date, to_date, difference)
print(res)
