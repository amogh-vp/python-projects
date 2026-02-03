# A simple weight converter program between pounds and kilograms

weight=float(input("enter the weight : "))
unit=input("Kilograms or Pounds? (K/L) : ")

if unit == "K":
    weight=weight*2.205
    unit="Lbs"
    print(f"Your weight is {round(weight,3)}{unit}")
elif unit=="L":
    weight=weight/2.205
    unit="Kgs"
    print(f"Your weight is {round(weight,3)}{unit}")
else:
    print("enter a valid unit")    
    
