def inputData(fileName):
    with open(fileName, 'r') as fileOb:
        text = fileOb.read()
        lines = text.split('\n')
        data = []; 
        for line in lines:
            data.append(line.split(','))
        return data

def outputData(fileName, data):
    dataStr = ""
    for row in data:
        rowStr = ""
        for col in row:
            rowStr += str(col) + ','
        else:
            rowStr = rowStr[:-1]
        dataStr += rowStr + '\n'
    else:
        dataStr = dataStr[:-1]
    with open(fileName, 'w') as fileOb:
        fileOb.write(dataStr)

def backtracking(assignment, slots, depth):
    if (depth == len(assignment)):
        return True
    global subs
    global rooms
    global count
    sub = subs[depth][0]
    available = subs[depth][2:]
    category = subs[depth][1]
    if (category == "c"):
        for slot in available:
            if (slots[slot] == -1):
                assignment[depth] = [sub, slot, rooms[0]]
                slots[slot] = rooms[0]
                for sub in assignment:
                    print(sub)
                print("\n")
                sub = subs[depth][0]
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = -1
                    assignment[depth] = [sub, -1, -1]
        count = count + 1 
        return False
    elif (category == "o"):
        for slot in available:
            if (slots[slot] == -1):
                assignment[depth] = [sub, slot, rooms[0]]
                slots[slot] = [rooms[0]]
                for sub in assignment:
                    print(sub)
                print("\n")
                sub = subs[depth][0]
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = -1
                    assignment[depth] = [sub, -1, -1]
            elif (type(slots[slot]) == list):
                asRooms = slots[slot]
                temp = asRooms[:]
                if (len(asRooms) == len(rooms)):
                    continue
                asRooms.append(rooms[len(asRooms)])
                assignment[depth] = [sub, slot, asRooms[-1]]
                slots[slot] = asRooms
                for sub in assignment:
                    print(sub)
                print("\n")
                sub = subs[depth][0]
                if (backtracking(assignment, slots, depth+1)):
                    return True
                else:
                    slots[slot] = temp
                    assignment[depth] = [sub, -1, -1]
        count = count + 1
        return False

inputDetails = inputData('input.csv')

subs = inputDetails[:-2]
rooms = inputDetails[-2]
slots = {}
assignment = []
count = 0

for sub in subs:
    for slot in sub[2:]:
        if (slot not in slots):
            slots[slot] = -1
    assignment.append([sub[0],-1,-1])

result = backtracking(assignment, slots, 0)

print("Backtrack sebanyak : ")
print(count)

if (result):
    outputData('output.csv', assignment)
    print("\n")
    for sub in assignment:
       print(sub)