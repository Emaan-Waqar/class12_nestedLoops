decimal= float(input("Enter the decimal number: "))
binary= ""

for i in range(1):
    n= decimal
    while n > 0:
        remainder= n % 2
        binary= str(remainder) + binary
        n//= 2

print("Binary equivalent: ", binary)        