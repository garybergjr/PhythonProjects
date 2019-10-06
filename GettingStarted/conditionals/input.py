color_list = ["Red", "Green", "Blue", "Black"]

print("Enter your favorite color: ")
favcolor = input()
if favcolor == color_list[0]:
    print("Red is awesome!")
elif favcolor == color_list[1]:
    print("Green is nature")
elif favcolor == color_list[2]:
    print("Blue is sky")
elif favcolor == color_list[3]:
    print("Back in Black")
elif favcolor in color_list:
    print("Wrong color")
