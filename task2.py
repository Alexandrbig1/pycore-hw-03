import random

def get_numbers_ticket(min, max, quantity):
  if min < 1 or max > 1000 or quantity < min or quantity > max:
    return 'Invalid input'
  
  lotto = []
  while len(lotto) < quantity:
    num = random.randint(min, max)
    if num not in lotto:
      lotto.append(num)

  return lotto


lottery_numbers = get_numbers_ticket(1, 300, 5)

print("Ваші лотерейні числа:", lottery_numbers)