valid = False
while not valid:
    try:
        n = int(input("Enter a number : "))
        while n%2 == 0:
            print("Bye Bye Bye")
        valid = True
    except SyntaxError:
        print("Make my life easier by using commas.")
    except ZeroDivisionError:
        print("Make my life easier by giving zero(0) in the second number.")
    except NameError:
        print("Make my life easier by giving numbers instead of alphabet.")
    else:
        print("Make my life easier by giving everything properly.")
    finally:
        print("Congratulations! You made my life easier.")