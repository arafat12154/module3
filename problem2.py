cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")
if cabin_class == "LUX":
    print("You have selected a LUX cabin: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("You have selected an A cabin: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("You have selected a B cabin: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("You have selected a C cabin: windowless cabin below the car deck.")
else:
    print("Error: Invalid cabin class. Please enter LUX, A, B, or C.")
