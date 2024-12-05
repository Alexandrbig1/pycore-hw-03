from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:  # If birthday falls on weekend
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Example usage
users = [
    {"name": "Alice", "birthday": "1990.12.10"},
    {"name": "Bob", "birthday": "1985.12.15"},
    {"name": "Charlie", "birthday": "1992.12.20"}
]

print(get_upcoming_birthdays(users))