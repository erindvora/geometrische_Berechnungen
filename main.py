def calculate_circle_area(radius):
    return 3.14 * radius * radius

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_square_area(side):
    return side * side
if __name__ == "__main__":
    choice = input("Choose a function: 1) Circle Area 2) Rectangle Perimeter 3) Square Area\n")
    if choice == '1':
        print(calculate_circle_area(5))
    elif choice == '2':
        print(calculate_rectangle_perimeter(4, 6))
    elif choice == '3':
        print(calculate_square_area(3))
    else:
        print("Invalid choice")
