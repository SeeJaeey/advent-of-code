input = """7313511551
3724855867
2374331571
4438213437
6511566287
6727245532
3736868662
2348138263
2417483121
8812617112"""

example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

rows = input.splitlines()

w = len(rows[0])
h = len(rows)

grid = []
for row in rows:
    for char in row:
        grid.append(int(char))

steps = 100000000
counter = 0

first_step = 0
for step in range(1, steps + 1):
    flashes = []

    # First increase energy level of every octopus by 1
    for i in range(len(grid)):
        grid[i] += 1
    
    # Any octopus with energy level > 9 flashes
    while True:
        any_oc_flashed = False

        # flash corners
        if (grid[0] > 9 and 0 not in flashes):
            counter += 1
            any_oc_flashed = True
            grid[1] += 1
            grid[10] += 1
            grid[11] += 1
            flashes.append(0)

        if (grid[9] > 9 and 9 not in flashes):
            counter += 1
            any_oc_flashed = True
            grid[8] += 1
            grid[18] += 1
            grid[19] += 1
            flashes.append(9)

        if (grid[90] > 9 and 90 not in flashes):
            counter += 1
            any_oc_flashed = True
            grid[80] += 1
            grid[81] += 1
            grid[91] += 1
            flashes.append(90)

        if (grid[99] > 9 and 99 not in flashes):
            counter += 1
            any_oc_flashed = True
            grid[89] += 1
            grid[88] += 1
            grid[98] += 1
            flashes.append(99)

        print("done with corners in step", step)

        for i in range(len(grid)):
            # Skip corners
            if (i == 0 or i == 9 or i == 90 or i == 99):
                continue

            if (grid[i] > 9 and i not in flashes):
                counter += 1
                any_oc_flashed = True
                #print("flashed in step:", step)

                # Increase all energy levels of adjacent octupi
                if ((i + 1) % w == 0):
                    grid[i - 1] += 1
                    grid[i - w] += 1
                    grid[i + w] += 1
                    grid[i - w - 1] += 1
                    grid[i + w - 1] += 1
                elif (i % w == 0):
                    grid[i + 1] += 1
                    grid[i - w] += 1
                    grid[i + w] += 1
                    grid[i - w + 1] += 1
                    grid[i + w + 1] += 1
                elif (i < 10):
                    grid[i - 1] += 1
                    grid[i + 1] += 1
                    grid[i + w] += 1
                    grid[i + w + 1] += 1
                    grid[i + w - 1] += 1
                elif (i >= 90):
                    grid[i - 1] += 1
                    grid[i + 1] += 1
                    grid[i - w] += 1
                    grid[i - w + 1] += 1
                    grid[i - w - 1] += 1
                else:
                    grid[i + 1] += 1
                    grid[i - 1] += 1
                    grid[i - w] += 1
                    grid[i + w] += 1
                    grid[i - w - 1] += 1
                    grid[i + w - 1] += 1
                    grid[i - w + 1] += 1
                    grid[i + w + 1] += 1

                flashes.append(i)

        if not any_oc_flashed:
            break
    
    for f in flashes:
        grid[f] = 0

    if(len(flashes) == len(grid)):
        first_step = step
        break
    #print("number of flashes in step", step, "is:", counter)
    #for i in range(len(grid)):
        #num = grid[i]
        #if i % w == 0:
            #print()
        #print(num, end="")
    #print()

#print()
#print(counter)
print(first_step)
