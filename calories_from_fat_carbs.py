# this program calculates calories from fat and carbs

#main function
def main():
  keep_going = 'y'
  
  while keep_going.lower() == 'y':
    # get fat grams from user
    fat_grams = float(input('Enter grams of fat consumed: '))
    cal_from_fat = calculate_fat(fat_grams)
    print(f'You have consumed {cal_from_fat} calories from fat.')
    
    # get carb grams from user
    carb_grams = float(input('Enter grams of carbs consumed: '))
    cal_from_carbs = calculate_carbs(carb_grams)
    print(f'You have consumed {cal_from_carbs} calories from carbs.')
    
    keep_going = input('Would you like to restart? (Enter y for yes): ')
    
#calculate calories from fat function
def calculate_fat(cal_from_fat):
  fat_calories = cal_from_fat * 9
  return fat_calories

#calculate calories from carbs function
def calculate_carbs(cal_from_carbs):
  carb_calories = cal_from_carbs * 4
  return carb_calories

main()