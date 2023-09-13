from overlap import overlap 

# Main method for running overlap 

if __name__ == "__main__":

    # Getting the four coordinate integers as input from the command line
    try:
        num1 = int(input("Enter the x1 coordinate of the first line: "))
        num2 = int(input("Enter the x2 coordinate of the first line: "))
        num3 = int(input("Enter the x3 coordinate of the second line: "))
        num4 = int(input("Enter the x4 coordinate of the second line: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    else:
        # Print the integers
        print(f"The two lines you entered are: ({num1}, {num2}) and ({num3}, {num4})")
        if overlap(num1, num2, num3, num4) == "overlap":
            print("These lines overlap")
        else: 
            print("These lines do not overlap")

