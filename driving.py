MIN_DRIVING_AGE = 18

# Using normal if-else statements and f-strings
def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if age < 18:
        print(f"{name} is not allowed to drive")
    else:
        print(f"{name} is allowed to drive")

# Using ternary operator and f-strings
def allowed_driving2(name, age):
    drive = "not" if age < 18 else ""
    print(f"{name} is {drive} allowed to drive") # This is efficient, space optimized code