input = """156 202 -110 -69"""

example = """20 30 -10 -5"""

split = input.split(" ")
target_x1 = int(split[0])
target_x2 = int(split[1])
target_y1 = int(split[2])
target_y2 = int(split[3])

def in_target_area(pos_x, pos_y):
    return pos_x >= target_x1 and pos_x <= target_x2 and pos_y >= target_y1 and pos_y <= target_y2

def passed_target_area(pos_x, pos_y, vel_x, vel_y):
    if in_target_area(pos_x, pos_y):
        return False
    
    elif pos_x > target_x2:
        if pos_y > target_y2:
            return vel_x >= 0
        elif pos_y < target_y1:
            return vel_x >= 0 or vel_y <= 0
        else:
            return vel_x >= 0

    elif pos_x < target_x1:
        if pos_y > target_y2:
            return vel_x <= 0
        elif pos_y < target_y1:
            return vel_x <= 0 or vel_y <= 0
        else:
            return vel_x <= 0
    
    else:
        if pos_y < target_y1:
            return vel_y <= 0
        else:
            return False

def reached_target_area(vel_x, vel_y):
    pos_x = pos_y = step = highest_y_pos = 0
    while(True):
        pos_x += vel_x
        pos_y += vel_y
        if vel_y > 0:
            highest_y_pos = pos_y
        step += 1
        if in_target_area(pos_x, pos_y):
            return True, step, pos_x, pos_y, highest_y_pos
        if passed_target_area(pos_x, pos_y, vel_x, vel_y):
            return False, step, pos_x, pos_y, highest_y_pos
        else:
            if vel_x > 0:
                vel_x -= 1
            elif vel_x < 0:
                vel_x += 1
            vel_y -= 1

result_vx = result_vx = -1
result_highest_y = -100000000000
count = 0
for v_x in range(-250, 250):
    for v_y in range(-250, 250):
        tup = reached_target_area(v_x, v_y)
        if (tup[0]): # Target area reached
            count += 1
            if (tup[len(tup) - 1] > result_highest_y):
                result_highest_y = tup[len(tup) - 1]
                result_vx = v_x
                result_vy = v_y

# Task 1
print("velocity x:", result_vx, "velocity y:", result_vy, "highest y value:", result_highest_y)

# Task 2
print("distinct initial velocity values:", count)

