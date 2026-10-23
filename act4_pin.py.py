# name 
print("Hello, I'm Tracy Andrea Balboa Panganiban")

# PIN Lock

correct_pin = "1234"
attempts = 0 

while attempts < 3: 
    pin = input("PIN: ")
    attempts += 1 

    if pin == correct_pin: 
        print("Access granted")
        break 

else: 
    print("Card blocked")