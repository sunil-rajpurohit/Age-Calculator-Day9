import os 

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
def calculate_age(birth_date, current_date):
    # Splitting the format 
    b_split = birth_date.split('-')
    c_split = current_date.split('-')
    b_day = int(b_split[0])
    b_month = int(b_split[1])
    b_year = int(b_split[2])
    c_day = int(c_split[0])
    c_month = int(c_split[1])
    c_year = int(c_split[2])

    #end dates of all months    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    # start with year, month, day difference
    years = c_year - b_year
    months = c_month - b_month
    days = c_day - b_day

    # If days are negative, get days from previous month
    if days < 0:
        months -= 1
        days += month_days[(c_month - 2) % 12]  # previous month

    # If months are negative, get months from previous year
    if months < 0:
        years -= 1
        months += 12

    # If the current date is before the birth date, it's invalid
    if years < 0:
        raise ValueError("Current date must be after birth date.")

    return years, months, days

def main():
    print("Simple Age Calculator (dd-mm-yyyy)")
    dob = input("Enter your date of birth: ")
    curr = input("Enter the current date: ")
    try:
        y, m, d = calculate_age(dob, curr)
        print(f"Your age is: {y} years, {m} months, {d} days.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clear_screen()
    main()