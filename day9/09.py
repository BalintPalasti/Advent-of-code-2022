import math

def main():
    file_task1 = open('09.txt', 'r')
    file_task2 = open('09.txt', 'r')
    task_1(file_task1)
    task_2(file_task2)
    file_task1.close()
    file_task2.close()

def move_H(H, direction):
    match direction:
        case "U":
            H[1] += 1
        case "D":
            H[1] -= 1
        case "L":
            H[0] -= 1
        case "R":
            H[0] += 1
        case _:
            print("Wrong value read:", direction)
    return H

def move_T(T, H):
    dist_x = abs(H[0] - T[0])
    dist_y = abs(H[1] - T[1])
    diff_x = H[0] - T[0]
    diff_y = H[1] - T[1]
    if dist_x == 1 and dist_y == 2:
        T[0] += int(math.copysign(1, diff_x))
        T[1] += int(math.copysign(1, diff_y))
    if dist_y == 1 and dist_x == 2:
        T[0] += int(math.copysign(1, diff_x))
        T[1] += int(math.copysign(1, diff_y))
    if dist_x == 0 and dist_y == 2:
        T[1] += int(math.copysign(1, diff_y))
    if dist_y == 0 and dist_x == 2:
        T[0] += int(math.copysign(1, diff_x))
    if dist_y == 2 and dist_x == 2:
        T[0] += int(math.copysign(1, diff_x))
        T[1] += int(math.copysign(1, diff_y))
    return T
    
def save_T_postion(T, T_former_positions):
    temp = T.copy()
    if temp not in T_former_positions:
        T_former_positions.append(temp)
    return T_former_positions


# Task 1: Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
def task_1(file):
    H = [0,0]
    T = [0,0]
    T_former_positions = []

    for line in file.read().splitlines():
        line = line.split()
        direction = line[0]
        step_no = int(line[1])
        for i in range(step_no):
            H = move_H(H, direction)
            T = move_T(T, H)
            T_former_positions = save_T_postion(T, T_former_positions)
    print("Task 1 solution::", len(T_former_positions))

# Task 2: Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
def task_2(file):
    H = [0,0]
    T = []
    indexes = range(1,10)
    for i in indexes: 
        T.append([0,0])
    tail_former_positions = []

    for line in file.read().splitlines():
        line = line.split()
        direction = line[0]
        step_no = int(line[1])
        for i in range(step_no):
            H = move_H(H, direction)
            for id, val in enumerate(T):
                if id == 0:
                    T[0] = move_T(T[0], H)
                else:
                    T[id] = move_T(T[id], T[id-1])

            tail_former_positions = save_T_postion(T[8], tail_former_positions)
    print("Task 2 solution:", len(tail_former_positions))

if __name__ == "__main__":
    main()