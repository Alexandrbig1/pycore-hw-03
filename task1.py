import datetime

def get_days_from_today(date):
    today = datetime.datetime.now()
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return (today - date).days
  
date = get_days_from_today('2024-11-20')

print(date)