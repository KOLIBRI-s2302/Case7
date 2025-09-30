# Case №2
# Developers: Shatalov Alexander, Kachkin Denis, Svilin Andrey
#

import local as loc

def main():
  """
  Main function.
  :return: None
  """
  base_utility = 1000
  print(loc.CHOOSE_YOUR_SEX)
  print(loc.MALE, loc.FEMALE, '|' ,loc.PRINT_NUMBER)
  sex=int(input())
  if sex == 1:
    base_utility *= 1
  else:
    base_utility *= 0.7

  print(loc.CHOOSE_YOUR_AGE_PERIOD)
  print('1) 18-30', '2) 31-45', '3) 46-60','4) 60+', '|' ,loc.PRINT_NUMBER)
  age_period=int(input())
  if age_period == 1:
    base_utility *= 1
  elif age_period == 2:
    base_utility *= 0.8
  elif age_period == 3:
    base_utility *= 0.6
  else:
    base_utility *= 0.4

  print(loc.CHOOSE_YOUR_HEALTH_STATUS)
  print(loc.HEALTHY, loc.CHRONIC_DISEASES, loc.INVALID, '|' ,loc.PRINT_NUMBER)
  health_status=int(input())
  if health_status == 1:
    base_utility *= 1
  elif health_status == 2:
    base_utility *= 0.7
  else:
    base_utility *= 0.3

  print(loc.CHOOSE_YOUR_FAMILY_STATUS, '|' ,loc.PRINT_NUMBER)
  print(loc.LONELY, loc.FAMILY)
  family_status=int(input())
  if family_status == 1:
    base_utility *= 1
  else:
    base_utility *= 1.5

  print(loc.CHOOSE_YOUR_SKILLS)
  print(loc.NONE, loc.FARMER, loc.CRAFTSMAN, loc.ARTIST, '|', loc.PRINT_NUMBER)
  skill=int(input())
  if skill == 1:
    base_utility *= 0.8
  if skill == 2:
    base_utility *= 1
  if skill == 3:
    base_utility *= 1.2
  if skill == 4:
    base_utility *= 2.5

  print(loc.CHOOSE_YOUR_REGION)
  print(loc.POOR, loc.USUAL, loc.FERTILE, '|', loc.PRINT_NUMBER)
  region=int(input())
  if region == 1:
    base_utility *= 0.8
  elif region == 2:
    base_utility *= 1
  else:
    base_utility *= 1.2

  bread_quantity = base_utility // 0.23
  print(loc.YOUR_PRICE_IS, int(base_utility), loc.RUBLES)
  print(loc.YOUR_PRICE_IS_EQUAL_TO, int(bread_quantity), loc.LOAFS_OF_BREAD)


if __name__ == '__main__':
  main()