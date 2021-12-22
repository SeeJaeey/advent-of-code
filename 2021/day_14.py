input = """VFHKKOKKCPBONFHNPHPN

VS -> B
HK -> B
FO -> P
NC -> F
VN -> C
BS -> O
HS -> K
NS -> C
CV -> P
NV -> C
PH -> H
PB -> B
PK -> K
HF -> P
FV -> C
NN -> H
VO -> K
VP -> P
BC -> B
KK -> S
OK -> C
PN -> H
SB -> V
KO -> P
KH -> C
KS -> S
FP -> B
PV -> B
BO -> C
OS -> H
NB -> S
SP -> C
HN -> N
FN -> B
PO -> O
FS -> O
NH -> B
SO -> P
OB -> S
KC -> C
OO -> H
BB -> V
SC -> F
NP -> P
SH -> C
BH -> O
BP -> F
CC -> S
BN -> H
SS -> P
BF -> B
VK -> P
OV -> H
FC -> S
VB -> S
PF -> N
HH -> O
HC -> V
CH -> B
HP -> H
FF -> H
VF -> V
CS -> F
KP -> F
OP -> H
KF -> F
PP -> V
OC -> C
PS -> F
ON -> H
BK -> B
HV -> S
CO -> K
FH -> C
FB -> F
OF -> V
SN -> S
PC -> K
NF -> F
NK -> P
NO -> P
CP -> P
CK -> S
HB -> H
BV -> C
SF -> K
HO -> H
OH -> B
KV -> S
KN -> F
SK -> K
VH -> S
CN -> S
VC -> P
CB -> H
SV -> S
VV -> P
CF -> F
FK -> F
KB -> V"""

example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

split = input.splitlines()

polymer_template = split[0]

insertions = {}
for i in range(2, len(split)):
    left_right = split[i].split(" -> ")
    insertions[left_right[0]] = left_right[1]

steps = 40

# task 1
#for i in range(steps):
  #  print(i)
  #  new_polymer_template = polymer_template
   # for i in range(len(polymer_template) - 1):
        #pair = polymer_template[i] + polymer_template[i + 1]
       # to_insert = insertions[pair]
        #new_polymer_template = new_polymer_template[:i + 1 * (i+1)] + to_insert + new_polymer_template[i + 1 * (i+1):]
    #polymer_template = new_polymer_template

# task 2
occs = {}
pair_occs = []
for i in range(len(polymer_template) - 1):
    pair = polymer_template[i] + polymer_template[i + 1]
    occs[pair] = 0
    if pair not in pair_occs:
        pair_occs.append(pair)
for i in range(len(polymer_template) - 1):
    occs[polymer_template[i] + polymer_template[i + 1]] += 1

single_occurences = {}
single_c = []
for char in polymer_template:
    if char not in single_c:
        single_c.append(char)
        single_occurences[char] = 1
    else:
        single_occurences[char] += 1

for i in range(steps):
    #print(i)
    new_pair_occs = pair_occs.copy()
    new_occs = occs.copy()
    for p in pair_occs:
        count = occs[p]
        if count == 0:
            continue
        #print("pair:", p, "count:", count)
        to_insert = insertions[p]
        #print("insert", to_insert)
        if to_insert in single_c:
            single_occurences[to_insert] += count
        else:
            single_c.append(to_insert)
            single_occurences[to_insert] = count
        new_pair1 = p[0] + to_insert
        new_pair2 = to_insert + p[1]
        new_occs[p[0] + p[1]] -= count
        #print("substracted", count, "from:", p[0] + p[1])
        if new_pair1 not in new_pair_occs:
            new_pair_occs.append(new_pair1)
            new_occs[new_pair1] = count
            #print("added new pair:", new_pair1)
        else:
            new_occs[new_pair1] += count
            #print("raised counter of new pair:", new_pair1, "counter now at:", new_occs[new_pair1])
        if new_pair2 not in new_pair_occs:
            new_pair_occs.append(new_pair2)
            new_occs[new_pair2] = count
            #print("added new pair:", new_pair2)
        else:
            new_occs[new_pair2] += count
            #print("raised counter of new pair:", new_pair2, "counter now at:", new_occs[new_pair2])
    pair_occs = new_pair_occs
    occs = new_occs
    #print(occs)
        

# Prepare occurences
#occurences = {}
#single_chars = []
#for pair in pair_occs:
    #if not (pair[0], 0) in occurences:
        #occurences[pair[0]] = 0
        #single_chars.append(pair[0])
    #if not (pair[1], 0) in occurences:
        #occurences[pair[1]] = 0
        #single_chars.append(pair[1])

# Count occurences
#for char in polymer_template:
    #occurences[char] += 1

#print(single_c)
#print(single_occurences)
min = ""
min_v = 9223372036854775807 # int max
max = ""
max_v = -1
for char in single_c:
    if (single_occurences[char] > max_v):
        max_v = single_occurences[char]
        max = char
    if (single_occurences[char] < min_v):
        min_v = single_occurences[char]
        min = char

print("min value:", min_v, "-->", min)
print("max value:", max_v, "-->", max)
print("----------------------------------")
print(max_v - min_v)
