# Custom Exception (Making our own special alarm)
class TooYoungError(Exception):
    pass

def book_tickets():
    print("--- Welcome to the Magic Rollercoaster Counter ---")
    
    try:
        # Step 1: Getting inputs (Risky! User might type letters instead of numbers)
        age = int(input("Enter your age: "))
        friends = int(input("How many friends are splitting the $100 bill? "))

        # Step 2: Using 'raise' to enforce our own rules
        if age < 0:
            raise ValueError("Age cannot be a negative number!")
        
        if age < 10:
            raise TooYoungError("Sorry! You must be at least 10 years old to ride.")

        # Step 3: Risky math (User might enter 0 friends -> ZeroDivisionError)
        cost_per_person = 100 / friends

    # Rescue Team 1: Catches text input like "abc" or negative age
    except ValueError as ve:
        print(f"[Input Error]: Please enter valid numbers. Details: {ve}")

    # Rescue Team 2: Catches our custom age rule
    except TooYoungError as tye:
        print(f"[Age Restriction]: {tye}")

    # Rescue Team 3: Catches division by zero
    except ZeroDivisionError:
        print("[Math Error]: At least 1 friend must pay! Cannot divide by zero.")

    # Rescue Team 4: Catch-all safety net for any other unknown error
    except Exception as e:
        print(f"[Unknown Error]: Something unexpected happened: {e}")

    # Bonus Exam Keyword: 'else' runs ONLY if NO errors happened in 'try'
    else:
        print(f"[Success]: Ticket booked! Each friend pays ${cost_per_person:.2f}")

    # Cleanup Crew: Runs EVERY SINGLE TIME no matter what happens above
    finally:
        print("--- Counter Closed. Resetting screen for next customer. ---\n")

# Run the program
book_tickets()