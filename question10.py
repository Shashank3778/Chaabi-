from datetime import datetime, timedelta

def get_date(date, n):
    # Convert string to datetime object
    date1 = datetime.strptime(date, "%y-%m-%d")
    
    # Calculate the date before by subtracting timedelta
    prev_date = date1 - timedelta(days=n)
    
    # string representation
    date2 = datetime.strftime(prev_date, "%y-%m-%d")
    
    return date2


date = "23-06-05"
n = 45

result = get_date(date, n)
print(result)  
