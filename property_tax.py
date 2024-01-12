# This program evaluates your property value and gives you
# the assessment value and property tax

PROPERTY_TAX_RATE = 0.72
ASSESSMENT_VALUE = 0.6


def main():
  intro()
  
  keep_going = 'y'
  
  while keep_going.lower() == 'y':
    # Get actual value of property from user
    actual_value = float(input("Please enter your land's actual value: "))
    assessment_value = assessment_value_calculation(actual_value)
    print(f'Your assessment value is ${assessment_value:,}')
    
    # Property tax
    property_tax = property_tax_calculation(assessment_value)
    print(f'Your property tax is ${property_tax:,.2f}')
    
    # ask user if they want to enter another property
    keep_going = input('Do you want to enter another property? (Enter y for yes): ')
    
def intro():
  pass

# function to get assessment value
def assessment_value_calculation(actual_value):
  assessment_value = ASSESSMENT_VALUE * actual_value
  return assessment_value

# function to get property tax based off assessment_value. Every $100 is .42 cents in tax
def property_tax_calculation(assessment_value):
  return (assessment_value / 100) * PROPERTY_TAX_RATE
  

main()