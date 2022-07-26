""" This program contains a  class called Rectangle. The class has a constructor (initializing method) which takes its
two sides.Each time a new rectangle is instantiated, the class assigns a unique number to it, it calculates its area and
perimeter and stores all the data in an instance of its class.
The program asks the user to create a new rectangle or display a stored rectangle.
Each time a rectangle is asked to be displayed, all the information would be displayed :the rectangle's unique number,
the sides the area and the perimeter.
The user decides when to quit the program.
The program should safeguard itself against invalid inputs such as negative numbers and strings.
Inputs = The user enters height and width of the triangle
Output = The program displays created rectangles details """


l1 = []
l2 = []


class Rectangle:

    unique = 153

    def __init__(self, height, width):
        Rectangle.unique += 23
        self.height = height
        self.width = width
        self.rec_unique = Rectangle.unique
        l1.append(self.rec_unique)

    def area(self):
        self.area = (self.height* self.width)

    def perimeter(self):
        self.perimeter = ((self.height*2) + (self.width*2))

    def rec_details(self):
        v = "Height: {}  Width: {}  Area: {}  Perimeter: {}  Unique No: {}"
        add_v = (v.format(self.height, self.width, self.area(), self.perimeter(), self.rec_unique))
        l2.append(add_v)
        return add_v


def action():
    try:
        a = int(input("1 - To create a new rectangle\n2 - To display rectangle\nEnter your choice: "))
        if a == 1:
            try:
                heig = int(input("Enter the height of the Rectangle: "))
                wid = int(input("Enter the width of the rectangle: "))
                par = Rectangle(heig, wid)
                print(par.rec_details(),"\n")
                exit_option()

            except:
                print("Either the length or breadth entered is not an integer!\n")
                action()

        elif a == 2:
            if len(l1) != 0:
                try:
                    print("THIS A LIST OF EACH OF THE AVAILABLE RECTANGLE'S UNIQUE NUMBER")
                    for i in l1:
                        print(i)
                    c = int(input("Enter any Unique Number from the above listed: "))
                    if c in l1:
                        f = l1.index(c)
                        print("Rectangle Info ="+" "+ l2[f])
                        exit_option()

                    else:
                        print("The unique number not found")
                except:
                    print("The Unique number not found")
                    action()

            else:
                print("Create a Rectangle first")

        else:
            print("Enter a correct assigned number")
            action()

    except:
        print("That is not an Integer")
        action()


def exit_option():
    try:
        i = int(input("Enter any number to continue | 0 to exit\n"))
        if i != 0:
            action()
        else:
            print("Thank you, Bye!")
    except:
        print("Enter an Integer")
        exit_option()


action()






