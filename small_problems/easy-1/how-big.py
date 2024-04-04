# How big is the room?
# Build a program that asks the user to enter the length and width of a room, in meters,
# then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet
# ask input room length from user
# ask input room width from user
# calculate rooms area in meter
# convert room area too square feet
# print room area in meter and in square feet

SQUARE_METER_TO_SQUARE_FEET = 10.7639

def prompt_input(prompt):
    return float(input(prompt))

room_length = prompt_input('Enter the value of room length in meters\n')
room_width = prompt_input('Enter the value of room width in meters\n')

def calculate_room_area(length, width):
    area = length * width
    return area

def convert_to_square_feet(area_in_square_meter):
    area_in_square_feet = area_in_square_meter * SQUARE_METER_TO_SQUARE_FEET
    return area_in_square_feet

area = calculate_room_area(room_length, room_width)
area_in_square_feet = convert_to_square_feet(area)

print(f'The room area is {area} meters or {area_in_square_feet} square feet.')