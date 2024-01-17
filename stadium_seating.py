# This program allows the user to enter how many tickets
# were sold and calculate the total income
# 3 categories of seats: A = $20, B = 15, and C = $10
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

# main function
def main():
  # user input for class A tickets sold
  class_a_tickets_sold = int(input('Enter the amount of class A tickets sold: '))
  class_a_ticket_income = class_a_income(class_a_tickets_sold)
  print(f'There were {class_a_tickets_sold:,} tickets sold for ${class_a_ticket_income:,}')

  # user input for class B tickets sold
  class_b_tickets_sold = int(input('Enter the number of class B tickets sold: '))
  class_b_ticket_income = class_b_income(class_b_tickets_sold)
  print(f'There were {class_b_tickets_sold:,} tickets sold for ${class_b_ticket_income:,}.')
  
  # user input for class C tickets sold
  class_c_tickets_sold = int(input('Enter the amount of class C tickets sold: '))
  class_c_ticket_income = class_c_income(class_c_tickets_sold)
  print(f'There were {class_c_tickets_sold:,} tickets sold for ${class_c_ticket_income:,}.')
  
  
  # get total number of tickets sold and total income
  total_tickets_sold = class_a_tickets_sold + class_b_tickets_sold + class_c_tickets_sold
  total_income = class_a_income + class_b_income + class_c_income
  print(f'All together there were {total_tickets_sold} tickets sold for ${total_income:,}.')
  
# calculate class a income
def class_a_income(class_a_tickets_sold):
  return class_a_tickets_sold * CLASS_A
  

# calculate class b income
def class_b_income(class_b_tickets_sold):
  return class_b_tickets_sold * CLASS_B
 

# calculate class c income
def class_c_income(class_c_tickets_sold):
  return class_c_tickets_sold * CLASS_C
  
main()