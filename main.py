#Завдання 1

from datetime import datetime

def get_days_from_today(date):
    input_date = datetime.strptime(date, '%Y-%m-%d')
    
    current_date = datetime.now()
    
    delta = current_date - input_date
    
    return delta.days

print(get_days_from_today('2025-11-15'))

#Завдання 2

import random

def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)

    numbers.sort()

    return numbers

min_num = 1
max_num = 49
quantity = 6
print(get_numbers_ticket(min_num, max_num, quantity))

#Завдання 3

def normalize_phone(phone_number):
    digits = ''.join(filter(str.isdigit, phone_number))
    
    if digits.startswith('380') and len(digits) == 12:
        return '+' + digits
    elif len(digits) == 10:
        return '+38' + digits
    else:
        return digits

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for phone_number in phone_numbers:
    print(normalize_phone(phone_number))

#Завдання 4
    
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        # Визначаємо день привітання, збільшуючи поточну дату на 7 днів
        congratulation_date = birthday.replace(year=today.year)
        if congratulation_date < today:
            congratulation_date = congratulation_date.replace(year=today.year + 1)

        
        if congratulation_date.weekday() >= 5:
            days_until_monday = 7 - (congratulation_date.weekday() - 4)
            congratulation_date += timedelta(days=days_until_monday)

        
        if (congratulation_date - today).days <= 7:
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


users = [
    {'name': 'John Doe', 'birthday': '1990.03.15'},
    {'name': 'Jane Smith', 'birthday': '1985.03.20'},
    {'name': 'Peter Parker', 'birthday': '1995.03.14'},
]

upcoming = get_upcoming_birthdays(users)
print("Cписок привітань на цьому тижні", upcoming)
