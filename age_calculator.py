def calculate_ages(names, years_of_birth):
    #define current year as a constant
    CURRENT_YEAR = 2024
    ages = []
    
    #loop through the two arrays simulataneously
    for name, year_of_birth in zip(names, years_of_birth):
        age = CURRENT_YEAR - year_of_birth
        ages.append(f"{name} is {age} years old.")
        
    return ages
    
#examle array for names and birth years
names = ["James","Jack", "Erick", "Felix"]
years_of_birth = [2003, 2001, 2004, 2000]
    
#calling the function and printing the result 

age_info = calculate_ages(names, years_of_birth)
print(age_info)
    