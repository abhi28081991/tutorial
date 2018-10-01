Ticket_price = 10
no_of_tickets= 100
#output name of the person using the name variable 
def username(Name):
    return Name
#output how many tickets are remaining using the ticket_remaining variable 
def remaining(no_of_ticket_purchased):
    return no_of_tickets- no_of_ticket_purchased
def total_price(no_of_ticket_purchased):
    return no_of_ticket_purchased * Ticket_price
while no_of_tickets>=1:
    Name = input("please enter youre name ")
    user = username(Name)

    how_many_ticket = int(input("Please enter how many ticket you want to purchase "))
    total = total_price(how_many_ticket)
    no_of_tickets = remaining(how_many_ticket)
    print("total ticket remaing {}".format(no_of_tickets))
    print("Hello my dear {} youre purchase is successful final amount to pay is {} and total no of tickets are {}".format(user,total,how_many_ticket))
    #prompt user you want to continue

    response = input("would you like to continue (Y/N) ")
    if response.upper() == 'Y':
        
        #remaining tickets
        print("total ticket remaing {}".format(no_of_tickets))
        
    else:
        print("quit")
#notify tickets are sold out
print("sorry tickets are sold out")