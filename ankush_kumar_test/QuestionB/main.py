from compare import compare 

# Main method for running compare 

if __name__ == "__main__":

    # Get two version strings as input from the user
    string1 = input("Enter the first version string: ")
    string2 = input("Enter the second version string: ")

    # Print the input version strings
    print("You entered the following version strings:")
    print("Version 1:", string1)
    print("Version 2:", string2)

    # string1 is equal to string2
    if compare(string1, string2) == "equal":
        print("String 1 is equal to String 2")
    
    # string1 is greater than string2
    elif compare(string1, string2) == "greater":
        print("String 1 is greater than String 2")
    else:
        # string1 is lesser than string2
        print("String 1 is lesser than String 2")
