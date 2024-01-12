# This program takes user input to calculate the total
# monthly and annual expenses of a car payment, insurance, gas, oil, tires, and
# maintenance 

# constant for annual cost
ANNUAL_COST = 12

# main function
def main():
  intro()
  
  # get loan cost
  loan = float(input('Enter your monthly loan cost: '))

  # get insurance cost
  insurance = float(input('Enter your monthly insurance cost: '))
  
  # get gas cost
  gas = float(input('Enter your monthly gas cost: '))
  
  # get oil cost
  oil = float(input('Enter your monthly oil cost: '))
  
  # get tires cost
  tires = float(input('Enter your monthly tire cost: '))
  
  # get maintenance cost
  maintenance = float(input('Enter your monthly maintenance cost: '))
  
  # call to function to calculate total monthly
  total_monthly = calculate_monthly(loan, insurance, gas, oil, tires, maintenance)
  
  total_annual = calculate_annual(loan, insurance, gas, oil, tires, maintenance)
  
  print(f'Your total monthly expenses is ${total_monthly}.')
  print(f'Your total annual cost is ${total_annual:,.2f}.')
  
# intro
def intro():
  print('This program allows you to enter your monthly expenses')
  print('and it will calculate your total monthly cost as well as')
  print('calculate your annual cost')

def calculate_annual(loan, insurance, gas, oil, tires, maintenance):
  total_annual = (loan + insurance + gas + oil + tires + maintenance) * ANNUAL_COST
  return total_annual

def calculate_monthly(loan, insurance, gas, oil, tires, maintenance):
  monthly_total = loan + insurance + gas + oil + tires + maintenance
  return monthly_total

main()