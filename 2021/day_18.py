import math

input = """[[0,[[0,9],[6,5]]],[[[5,3],[0,4]],[8,3]]]
[[[[8,6],4],[2,5]],[[[7,4],[4,3]],[[3,4],[3,3]]]]
[[[6,[0,2]],[5,[7,4]]],[1,2]]
[[[[5,4],0],[[5,3],[1,4]]],[[[8,9],[0,0]],1]]
[[[7,0],2],[0,[4,2]]]
[4,[6,2]]
[[[[9,5],[3,4]],[[9,4],[5,3]]],[5,[[0,3],[4,4]]]]
[[[6,0],[3,4]],[9,[[0,3],3]]]
[[[[4,0],5],2],[[4,7],[9,0]]]
[[[2,4],[[3,6],[5,5]]],[[9,[1,1]],[1,1]]]
[[[[8,8],1],8],0]
[[0,6],[[[1,1],8],[[1,7],[6,3]]]]
[[4,8],[[1,[8,4]],[[5,9],[6,3]]]]
[3,[[0,[0,8]],[[2,5],9]]]
[[[[8,8],[5,8]],[[5,2],3]],[[[6,5],2],[6,8]]]
[[[5,[0,8]],[[8,3],[0,4]]],[[[2,5],8],[[0,4],3]]]
[[[7,5],2],[[[3,6],[1,7]],[1,[6,2]]]]
[[[[7,7],1],4],[[8,[5,1]],4]]
[[[[5,0],[9,0]],[[3,3],[1,0]]],[[0,[8,9]],7]]
[[[[4,0],[8,9]],[1,9]],[[[1,7],[9,5]],[[1,4],[9,5]]]]
[[7,0],5]
[[[[3,7],3],[[1,1],[4,9]]],[2,[6,3]]]
[[2,[6,[4,4]]],[0,[0,[6,3]]]]
[[[3,[5,3]],4],[0,4]]
[7,[[[8,8],[6,3]],[9,5]]]
[[7,[4,4]],[5,7]]
[[6,3],[[2,0],[9,6]]]
[[[0,[7,9]],[[5,6],0]],[[4,[8,9]],[8,[3,6]]]]
[[5,[3,[7,0]]],[[4,1],[[1,1],[3,0]]]]
[[9,[2,4]],[[2,[8,1]],[[4,5],1]]]
[[8,[0,[8,2]]],[[2,4],[[2,6],8]]]
[[[[8,1],5],2],[0,[[5,7],8]]]
[[[[9,2],[6,0]],[3,[9,6]]],[[[2,1],0],[[6,2],[2,0]]]]
[[[[6,6],1],[2,3]],[9,[[4,8],5]]]
[[3,[[1,5],[8,4]]],[[6,6],3]]
[[[4,8],5],3]
[[0,[[5,4],[9,7]]],[[[0,5],[7,6]],[[6,9],[1,9]]]]
[[[9,[1,1]],[7,[2,9]]],[[6,[3,6]],[[4,5],[1,0]]]]
[[[5,[7,7]],9],2]
[1,[[0,[3,2]],[1,[8,7]]]]
[5,[[5,[3,5]],[[4,1],[8,3]]]]
[[0,4],[[[2,6],7],3]]
[5,9]
[[[[9,2],[3,9]],3],[0,[[8,4],0]]]
[[[9,7],[6,[3,3]]],3]
[2,[[4,0],[8,[8,4]]]]
[[2,4],[9,[[2,9],4]]]
[[[[9,7],[9,5]],[[9,2],[3,9]]],0]
[2,[0,[[2,2],6]]]
[[[[8,9],[7,9]],[3,[1,4]]],[[1,[9,5]],[[1,9],7]]]
[[[1,[3,6]],0],[9,[8,[2,2]]]]
[[[7,3],[[7,2],[4,3]]],[[9,[7,7]],7]]
[[[3,[6,4]],4],[[[8,9],[6,6]],[1,[9,1]]]]
[[[[6,3],[1,8]],[6,9]],[[[0,0],2],0]]
[[[8,9],7],1]
[[[[3,2],[7,5]],2],9]
[[[[4,9],5],4],[0,[[2,4],[7,8]]]]
[[[[8,1],[6,5]],[[8,1],[9,7]]],9]
[0,[1,6]]
[[[5,9],[[9,8],6]],[0,[5,[1,2]]]]
[9,[[[4,3],5],[9,3]]]
[[[9,[2,7]],[2,[9,0]]],[[1,[8,7]],[[3,5],[2,6]]]]
[9,[[3,8],[[4,5],[7,1]]]]
[[0,[2,8]],[[6,3],5]]
[[[6,[2,5]],[[2,1],8]],[5,[[4,9],[0,3]]]]
[[[[0,4],3],[[1,3],[3,2]]],9]
[9,[[2,8],[[3,8],7]]]
[[[4,[1,9]],[3,3]],[0,[[4,3],[1,7]]]]
[[6,[[5,2],[2,5]]],[1,[[0,0],[1,4]]]]
[9,[1,[7,[5,6]]]]
[[5,4],6]
[6,[[5,6],7]]
[[[3,[6,0]],[8,[3,5]]],[[5,1],[[7,9],3]]]
[[[6,[8,7]],[[5,2],0]],[[6,[4,0]],[1,[1,2]]]]
[3,[[[7,8],0],[[6,5],0]]]
[[4,9],[9,9]]
[[7,[5,[9,7]]],1]
[[[3,[3,3]],[4,6]],[[[9,5],[4,8]],[5,[2,0]]]]
[[[[8,6],6],8],[3,1]]
[6,[5,0]]
[2,[[2,[7,5]],[6,[0,6]]]]
[[[9,[1,3]],[0,[9,4]]],4]
[[[[2,5],[9,9]],[[8,2],2]],[9,[1,[9,1]]]]
[[[[8,9],0],[[2,5],[2,2]]],[[7,[4,1]],[[3,9],[5,8]]]]
[[[7,6],[6,3]],5]
[2,[[[5,8],[1,2]],0]]
[[[8,7],[6,4]],[[[0,6],2],[[2,1],5]]]
[2,1]
[0,[[[4,3],[6,6]],8]]
[4,2]
[[[6,[3,2]],[5,[2,3]]],[[[3,5],[6,2]],[1,[6,6]]]]
[[0,[[8,1],[0,5]]],[[[3,3],3],[[6,8],5]]]
[[[3,0],[4,[6,5]]],[[[3,3],[4,0]],6]]
[[[[7,3],4],4],[[7,[8,2]],0]]
[[[4,3],[0,9]],[[1,[8,9]],[[3,0],0]]]
[[3,2],[2,[[2,6],[2,1]]]]
[2,8]
[[[[1,4],[7,3]],[8,[2,1]]],4]
[[[1,7],[1,[4,8]]],[[[2,2],[6,1]],[[9,9],8]]]
[[[5,[7,2]],[[8,6],6]],[1,5]]"""

example = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

lines = input.splitlines()

def add(lhs: str, rhs: str):
    #print("after adding:", f"[{lhs},{rhs}]")
    return f"[{lhs},{rhs}]"

def explode(number: str, l_bracket_idx: int, r_bracket_idx: int):
    # Get the numbers
    #print(f"exploding pair: {number[l_bracket_idx:r_bracket_idx+1]}")
    nums = number[(l_bracket_idx+1):r_bracket_idx].split(",")
    l_num = nums[0]
    r_num = nums[1]

    # Add left number to another number if there is one
    for i in range(l_bracket_idx - 1, -1, -1):
        if number[i].isdigit():
            # Get number
            r_idx_num = i
            l_idx_num = -1
            for j in range(i, -1, -1):
                if not number[j].isdigit():
                    l_idx_num = j+1
                    break
            n = int(number[l_idx_num:r_idx_num+1])
            old_len = len(number[l_idx_num:r_idx_num+1])
            n += int(l_num)
            new_len = len(str(n))
            if new_len > old_len:
                diff = new_len - old_len
                l_bracket_idx += diff
                r_bracket_idx += diff
            elif new_len < old_len:
                diff = old_len - new_len
                l_bracket_idx -= diff
                r_bracket_idx -= diff
            number = number[:l_idx_num] + str(n) + number[(r_idx_num+1):]
            break
    
    # Add right number to another number if there is one
    for i in range(r_bracket_idx + 1, len(number)):
        if number[i].isdigit():
            # Get number
            l_idx_num = i
            r_idx_num = -1
            for j in range(i, len(number)):
                if not number[j].isdigit():
                    r_idx_num = j-1
                    break
            n = int(number[l_idx_num:r_idx_num+1])
            n += int(r_num)
            number = number[:l_idx_num] + str(n) + number[(r_idx_num+1):]
            break

    # Insert 0 for explode pair
    number = number[:l_bracket_idx] + "0" + number[(r_bracket_idx + 1):]
    #print(f"after explode:", number)
    return number

def split(number: str, num_idx_l: int, num_idx_r: int):
    num = int(number[num_idx_l:num_idx_r+1])
    left = str(math.floor(num / 2))
    right = str(math.ceil(num / 2))
    number = number[:num_idx_l] + "[" + left + "," + right + "]" + number[num_idx_r+1:]
    #print("after split:", number)
    return number

def check_for_explosion(number: str):
    counter = 0
    for i, char in enumerate(number):
        if char == "[":
            counter += 1
            if counter == 5:
                # Explode pair at index i
                left_bracket_idx = i
                right_bracket_idx = -1
                for j in range(i, len(number)):
                    if number[j] == "]":
                        right_bracket_idx = j
                        break
                explosion_res = explode(number, left_bracket_idx, right_bracket_idx)
                return True, explosion_res
        elif char == "]":
            counter -= 1
    return False, ""

def check_for_split(number: str):
    for i, char in enumerate(number):
        if char.isdigit():
            l_idx = i
            r_idx = -1
            for j in range(i, len(number)):
                if not number[j].isdigit():
                    r_idx = j-1
                    break
            num = int(number[i:r_idx+1])
            if num > 9:
                split_res = split(number, l_idx, r_idx)
                return True, split_res
    return False, ""

def check_for_reduction(number: str):
    # First find explosions
    flag1, expl_res = check_for_explosion(number)
    if flag1:
        return True, expl_res

    # Then find splits
    flag2, split_res = check_for_split(number)
    if flag2:
        return True, split_res

    return False, ""

def magnitude(number: str):
    #print("mag for:", number)
    if number == "":
        return 0
    if number.count('[') == 1:
        split1 = number.split("[")
        split2 = number.split("]")
        #print(split1)
        #print(split2)
        if split1[0] != '' and (number[0] != '[' or number[len(number) - 1] != ']'):
            #print("X", f"[{split1[1]}")
            return 3 * int(split1[0][:len(split1[0])-1]) + 2 * magnitude(f"[{split1[1]}")
        elif split2[1] != '' and (number[0] != '[' or number[len(number) - 1] != ']'):
            #print("Y", f"{split2[0]}]")
            return 3 * magnitude(f"{split2[0]}]") + 2 * int(split2[1][1:])
        else:
            #print("Z")
            split = number[1:len(number)-1].split(",")
            return 3 * int(split[0]) + 2 * int(split[1])
    else:
        # Recursive calls for 2 pairs
        counter = 0
        first_pair = second_pair = ""
        for i in range(1, len(number) - 1):
            if number[i] == "[":
                counter += 1
            elif number[i] == "]":
                counter -= 1
                if counter == 0:
                    first_pair = number[1:i+1]
                    second_pair = number[i+2:len(number)-1]
                    break
        # HIER NICHT IMMER magnitude rekursiv aufrufen sondern kucken ob pairs wirklich pairs sind
        #print("2pairs: ", first_pair, second_pair)
        if first_pair == "":
            return magnitude(second_pair)
        elif second_pair == "":
            return magnitude(first_pair)
        else:
            return 3 * magnitude(first_pair) + 2 * magnitude(second_pair)
                


            

# Task 1
left_num = lines[0]
for i in range(1, len(lines)):
    right_num = lines[i]
    res = add(left_num, right_num)

    flag = True
    while(flag):
        flag, red_res = check_for_reduction(res)
        if flag:
            res = red_res
    
    left_num = res

# Task 2
max_mag = -1
for num1 in lines:
    for num2 in lines:
        if num1 == num2:
            continue
        else:
            #print("---------------------")
            #print(num1)
            #print(num2)
            #print("---------------------")
            res2 = add(num1, num2)

            flag2 = True
            while(flag2):
                flag2, red_res2 = check_for_reduction(res2)
                if flag2:
                    res2 = red_res2

            #print(res2)

            mag = magnitude(res2)
            #print(mag)
            if mag > max_mag:
                max_mag = mag

print(f"Task 1: {magnitude(res)}")
print(f"Task 2: {max_mag}")


    

