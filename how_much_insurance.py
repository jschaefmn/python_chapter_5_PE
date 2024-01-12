# This program asks user to enter replacement cost of a building
# Then displays the minimum amount of insurance he/she should
# buy for the property

#experts advise insuring property for at least 80%
MINIMUM_INSURANCE = 0.8

def main():
  keep_going = 'y' 
  
  while keep_going.lower() == 'y':
    building_cost = float(input('Enter the cost of your property: '))
    min_cost = calculation(building_cost)
    print(f'You should pay at least ${min_cost} to insure your property')
    
    # ask user if they want to enter another property
    keep_going = input('Do you want to enter another property? (Enter y for yes): ')
    
  
def calculation(building_cost): 
  total_cost = building_cost * MINIMUM_INSURANCE
  return total_cost


main()