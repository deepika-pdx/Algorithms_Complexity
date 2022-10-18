class Cell:
    neighbour_counter = 0
    obstruct = "X"
    value = 0
    visited = False
    parent_cell = 0


def createMaze():
    maze = [[Cell() for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            if i == 0 and j == 1:
                maze[i][j].obstruct = "Y"
            elif i == 1 and j == 3:
                maze[i][j].obstruct = "Y"
            elif i == 2 and j in (0, 1, 2, 3):
                maze[i][j].obstruct = "Y"
            elif i == 3 and j in (0, 1, 2, 3):
                maze[i][j].obstruct = "Y"
            elif i == 4 and j in (0, 1, 2, 3):
                maze[i][j].obstruct = "Y"
            elif i == j == 4:
                maze[i][j].obstruct = "T"
            else:
                maze[i][j].obstruct = "N"
    for i in range(5):
        for j in range(5):
            maze[i][j].value = str(i) + str(j)
    return maze


def createAdjList():
    adjList = {
        "00": ["01", "10"],
        "01": ["00", "02", "11"],
        "02": ["01", "03", "12"],
        "03": ["02", "04", "13"],
        "04": ["03", "14"],
        "10": ["00", "11", "20"],
        "11": ["01", "10", "12", "21"],
        "12": ["02", "13", "11", "22"],
        "13": ["03", "12", "14", "23"],
        "14": ["04", "13", "24"],
        "20": ["10", "21", "30"],
        "21": ["11", "20", "22", "31"],
        "22": ["12", "21", "32", "23"],
        "23": ["13", "22", "24", "33"],
        "24": ["14", "23", "34"],
        "30": ["20", "31", "40"],
        "31": ["21", "30", "32", "41"],
        "32": ["22", "31", "33", "42"],
        "33": ["23", "32", "34", "43"],
        "34": ["24", "33", "44"],
        "40": ["30", "41"],
        "41": ["31", "40", "42"],
        "42": ["32", "41", "43"],
        "43": ["33", "42", "44"],
        "44": ["34", "43"]
    }
    return adjList


def BFS():
    maze = createMaze()
    start_node = maze[0][0]
    start_node.neighbour_counter = 0
    start_node.visited = True
    start_node.parent_cell = "00"
    queue = []
    queue.append(start_node)
    path_length = 0
    adjlist = createAdjList()
    path = "cell44"
    while len(queue) != 0:
        node_v = queue.pop(0)
        key = str(node_v.value)
        main_cell = maze[int(key[0])][int(key[1])]
        for k in adjlist.get(key):
            i = int(k[0])
            j = int(k[1])
            neighbour_cell = maze[i][j]
            if neighbour_cell.obstruct != "Y" and neighbour_cell.visited == False:
                if neighbour_cell.obstruct == "T":
                    neighbour_cell.parent_cell = key
                    counter = main_cell.neighbour_counter + 1
                    neighbour_cell.neighbour_counter = counter
                    parent_cell = 0
                    l = 4
                    m = 4
                    while parent_cell != "00":
                        parent_cell = maze[l][m].parent_cell
                        path = path + "-->" + "cell" + parent_cell
                        l = int(parent_cell[0])
                        m = int(parent_cell[1])
                    path_length = neighbour_cell.neighbour_counter
                    return path, path_length
                else:
                    neighbour_cell.parent_cell = key
                    neighbour_cell.visited = True
                    counter = main_cell.neighbour_counter + 1
                    neighbour_cell.neighbour_counter = counter
                    queue.append(neighbour_cell)
    return -1


path, path_length = BFS()
print("Path is: " + str(path) + " and path length is: " + str(path_length))
