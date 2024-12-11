parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

# Your code here
def get_parking_lot(matrix):
    # main parameters
    total_slots = 0
    available_slots = 0
    occupied_slots = 0
    # main loop for search in each slot
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                total_slots += 1
                if matrix[i][j] == 1:
                    occupied_slots += 1
                elif matrix[i][j] == 2:
                    available_slots += 1
    # result into dictionary
    state = {
        "total_slots": total_slots,
        "available_slots": available_slots,
        "occupied_slots": occupied_slots
        }
    # return statement
    return state

print(get_parking_lot(parking_state))