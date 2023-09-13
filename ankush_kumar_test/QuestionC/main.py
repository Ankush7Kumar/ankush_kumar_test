from geoDistributedLRUCache import GeoDistributedLRUCache 

# Main method for running GeoDistributedLRUCache

if __name__ == "__main__":
    
    # Creating a cache
    cache = GeoDistributedLRUCache(capacity=4, default_ttl=3600)  # Max 4 items, default TTL 1 hour

    # Get a letter as input from the user for command the user wants to execute
    user_input = input("Enter a letter (p for Put, g for Get, or r for Remove): ")

    # PUT
    if user_input == "p":
        print("Enter the key, value, and ttl for the Put command: ")

        try:
            key = int(input("Enter the key: "))
            value = int(input("Enter the value: "))
            ttl = int(input("Enter the ttl: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
        else:
            cache.put(key, value, ttl)
            print("PUT command executed")
            
        
    # GET
    elif user_input == "g":
        print("Enter the key for Get command: ")

        try:
            key = int(input("Enter the key: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
        else:
            cache.get(key)
            print("GET command executed")
    
    # REMOVE
    elif user_input == "r":
        print("Enter the key for Remove command: ")

        try:
            key = int(input("Enter the key: "))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
        else:
            cache.remove(key)
            print("REMOVE command executed")


    else:
        print("Invalid input. Please enter 'p', 'g', or 'r'.")



