"""
This is a program that assigns seats on an airplane.
The airplane has 10 seats.
The program asks if a passenger requires a vegetarian meal or a standard meal.
There are only 5 vegetarian meals available.
The seats are numbered 1-10
There are no double seats.
input = The program  what meal plan they want
output = The program displays the seat number and meal plan of the passenger.
""" 



l = []


def main():
    flight_meal()
    passenger_list()
    finish()


def flight_meal():
    no_v = 0
    i = 0
    while i < 10:
        seat_no = i + 1
        try:
            user_meal = int(input("This is Nonso-Way Airlines. Before booking a ticket we would like to know"
                                  "\nWhat meal plan do you want? \n1 for Vegetarian meal\n2 for Standard meal"
                                  "\nEnter your choice: "))

            if user_meal == 1:
                if no_v < 5:
                    no_v += 1
                    first_name = input("Enter your First name: ").upper()
                    last_name = input("Enter your Last name: ").upper()
                    print("Full-name:",first_name, last_name,"\tYour Seat No:", seat_no, "Meal Choice: V-MEAL\n")
                    l_app = "Full-name: {} {} \tSeat Number: {} \tMeal Choice: V-MEAL"
                    l.append(l_app.format(first_name, last_name, seat_no))
                else:
                    i -=1
                    print("Sorry Next Flight in 4 hours")

            elif user_meal == 2:
                first = input("Enter your First name: ").upper()
                last = input("Enter your Last name: ").upper()
                print("Full-name:", first, last, "\tYour Seat No:", seat_no, "Meal Choice: S-MEAL\n")
                l_app = "Full-name: {} {} \tSeat Number: {} \tMeal Choice: S-MEAL"
                l.append(l_app.format(first, last, seat_no))

            else:
                i -= 1
        except:
            print("That is not an integer\n")
            i -= 1
        i += 1
    print("Sorry, the plane capacity is full. Next flight in 4 hours\n")


def passenger_list():
    print("This is Nonso-Way Airlines' Roster for the currently boarding flight")
    for i in range(10):
        print(str(i+1)+")  "+l[i])


def finish():
    i = int(input("Enter any number to continue | 0 to exit\n"))
    if i != 0:
        main()
    else:
        print("Thank you, Bye!")


# Running Code
main()


