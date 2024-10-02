import random

# Parameters of the simulations.
N = 10000 # Quantity of simulations.
X = 100   # Quantity of boxes and prisioners. This number Must be pair. 100, 50, 1000... etc.

boxes = {} # Map that represent X quantity of boxes.

win_rate = 0

for i in range(1, N + 1): # Iterate simulations.

    random_list = random.sample(range(1, X + 1), X) # Generate random distribution for the number into the boxes.

    for x in range(1, X + 1):
        boxes[x] = random_list[x - 1] # Fill all boxes with a ramdon number.
    
    # print(boxes) # Uncomment if you want to see the distribution of the numbers in the boxes.

    win_point = 0

    for prisioner in range(1, X + 1): # Iterate prisioners.
        number_to_search = prisioner

        for intent in range(1, int(X / 2) + 1): # Start find his own number.
            number_in_box = boxes[number_to_search]

            if number_in_box == prisioner: # If find it, it breaks the iteration a conitue with the next prisioner.
                win_point += 1
                break

            else: # If can't find his number, choose the next box.
                number_to_search = boxes[number_to_search]

    if win_point == X: # Count every time that prisioner find his number.
        win_rate += 1

win_rate = (win_rate/N) * 100

print(f"Winrate in {N} simulations with {X} prisioners: {win_rate}%")



