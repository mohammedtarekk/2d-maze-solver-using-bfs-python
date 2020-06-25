# region BFSSearchAlgorithms
class Node:
    id = None
    up = None
    down = None
    left = None
    right = None
    previousNode = None

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    board = [[]]  # Represents the 2D board
    rows_count = 0  # Number of rows in maze
    cols_count = 0  # Number of columns in maze

    def __init__(self, mazeStr):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        self.mazeStr = mazeStr

    # This function calculates the number of rows and columns in the maze
    def GetCountOfColsAndRows(self):
        x = 0
        while x != len(self.mazeStr):
            if self.mazeStr[x] == ' ':
                self.rows_count += 1
            x += 1
        self.rows_count += 1

        x = 0
        while self.mazeStr[x] != ' ':
            if self.mazeStr[x] == ',':
                self.cols_count += 1

            x += 1
        self.cols_count += 1

    # This function converts the maze string to a 2D board
    def CreateBoard(self):
        self.board = [x.split(',') for x in self.mazeStr.split(' ')]

    # This function converts the board char elements to nodes and give every node an id
    # id is given to each node as it's the index of this node in a virtual 1D array "output constraint"
    def CreateNodes(self):
        self.GetCountOfColsAndRows()
        avail_id = 0
        for row in range(self.rows_count):
            for col in range(self.cols_count):
                self.board[row][col] = Node(self.board[row][col])
                self.board[row][col].id = avail_id
                avail_id += 1

    # This function initializes every node neighbors "up, down, left, right"
    def InitializeNeighbors(self):
        for row in range(self.rows_count):
            for col in range(self.cols_count):
                if self.board[row - 1][col].value != '#' and (row - 1) >= 0:
                    self.board[row][col].up = self.board[row][col].id - self.cols_count

                if (row + 1) < self.rows_count:
                    if self.board[row + 1][col].value != '#':
                        self.board[row][col].down = self.board[row][col].id + self.cols_count

                if self.board[row][col - 1].value != '#' and (col - 1) >= 0:
                    self.board[row][col].left = self.board[row][col].id - 1

                if (col + 1) < self.cols_count:
                    if self.board[row][col + 1].value != '#':
                        self.board[row][col].right = self.board[row][col].id + 1

    # IMPLEMENTATION OF BFS ALGORITHM
    def BFS(self):

        # ---------- [1] Initializing the board and nodes -----------
        self.CreateBoard()
        self.CreateNodes()
        self.InitializeNeighbors()

        # Find the start node
        for i in range(self.rows_count):
            for j in range(self.cols_count):
                if self.board[i][j].value == 'S':
                    start_node = self.board[i][j]  # StartNode 'S'
        # -----------------------------------------------------------

        # --------- [2] Initializing the lists used in BFS ---------
        visited = []
        not_visited = [start_node]
        # -----------------------------------------------------------

        # --------- [3] SEARCHING FOR THE GOAL NODE AS WELL AS TRACKING ITS FULL & SHORTEST PATH ---------
        while not_visited:  # while not_visited list is not empty

            current_node = not_visited.pop(0)  # getting the first node in the list
            visited.append(current_node.id)  # appending its id to the visited list "MAKE IT VISITED"

            if current_node.value == 'E':  # if the goal node is reached, then save its path and break
                self.fullPath = visited
                break

            # these 4 blocks explore the current node VALID Neighbours "UP, DOWN, LEFT, RIGHT":
            # [1] check if the up neighbour is valid and not visited yet
            # [2] if valid, get it from the 2D board
            # [3] then check if it exists in not_visited list or not, to prevent repeating nodes in the path
            # [4] if not existed in not_visited list, add it
            # [5] then save its previous node, to keep track for the shortest path
            if current_node.up is not None and current_node.up not in visited:
                for i in range(self.rows_count):
                    for j in range(self.cols_count):
                        if self.board[i][j].id == current_node.up:
                            if self.board[i][j] not in not_visited:
                                not_visited.append(self.board[i][j])
                                self.board[i][j].previousNode = current_node
                            break

            if current_node.down is not None and current_node.down not in visited:
                for i in range(self.rows_count):
                    for j in range(self.cols_count):
                        if self.board[i][j].id == current_node.down:
                            if self.board[i][j] not in not_visited:
                                not_visited.append(self.board[i][j])
                                self.board[i][j].previousNode = current_node
                            break

            if current_node.left is not None and current_node.left not in visited:
                for i in range(self.rows_count):
                    for j in range(self.cols_count):
                        if self.board[i][j].id == current_node.left:
                            if self.board[i][j] not in not_visited:
                                not_visited.append(self.board[i][j])
                                self.board[i][j].previousNode = current_node
                            break

            if current_node.right is not None and current_node.right not in visited:
                for i in range(self.rows_count):
                    for j in range(self.cols_count):
                        if self.board[i][j].id == current_node.right:
                            if self.board[i][j] not in not_visited:
                                not_visited.append(self.board[i][j])
                                self.board[i][j].previousNode = current_node
                            break
        # ------------------------------------------------------------------------------------------------

        # --------------- [4] GENERATE SHORTEST PATH ------------------
        while current_node.value != 'S':
            self.path.append(current_node.id)
            current_node = current_node.previousNode

        self.path.append(current_node.id)
        self.path.reverse()
        # -------------------------------------------------------------

        return self.fullPath, self.path
# endregion

######################## MAIN ###########################
if __name__ == '__main__':
    searchAlgo = SearchAlgorithms(input("Enter your 2D maze: "))
    fullPath, path = searchAlgo.BFS()
    print('**MAZE SOLUTION**\n Full Path is: ' + str(fullPath) + "\n Path: " + str(path))
