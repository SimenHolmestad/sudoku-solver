board = [[0,0,2,0,0,0,0,9,0],
         [0,7,1,0,9,3,0,0,6],
         [0,0,0,7,0,0,3,0,4],
         [8,1,0,6,0,0,9,0,0],
         [6,0,0,9,0,1,0,0,5],
         [0,0,5,0,0,8,0,6,7],
         [7,0,3,0,0,2,0,0,0],
         [1,0,0,3,8,0,6,7,0],
         [0,5,0,0,0,0,8,0,0]]

def print_board():
    for element in board:
        print (element)

class coords:
    def __init__(self, y, x):
        self.x = x
        self.y = y

def number_is_valid (coordinates):
    number_encountered = False
    #sjekk om tallet er i samme rad
    for element in board[coordinates.y]:
        if (element == board[coordinates.y][coordinates.x]):
            if (number_encountered == False):
                number_encountered = True
            else:
                return False

    number_encountered = False
    #sjekk om tallet er i samme rad
    for y in range(9):
        if (board[y][coordinates.x] == board[coordinates.y][coordinates.x]):
            if (number_encountered == False):
                number_encountered = True
            else:
                return False
    
    number_encountered = False
    #sjekk om tallet er i samme 3*3-rute
    kord_rute_x = (coordinates.x // 3) * 3
    kord_rute_y = (coordinates.y // 3) * 3
    for y in range(3):
        for x in range(3):
            if (board[kord_rute_y + y][kord_rute_x + x] == board[coordinates.y][coordinates.x]):
                if (number_encountered == False):
                    number_encountered = True
                else:
                    return False
    return True        

unsolved_elements = []

for y in range(9):
    for x in range(9):
        board[y][x] = int(board[y][x])
        if (board[y][x] == 0):
            #Lagrer koordinatene til alle blanke felt:
            unsolved_elements.append(coords(y,x))            

print_board()
print ("")

iterations = 0
current_element = 0
while current_element < len(unsolved_elements):
    if board[unsolved_elements[current_element].y][unsolved_elements[current_element].x] < 9:
        board[unsolved_elements[current_element].y][unsolved_elements[current_element].x] += 1 
        if (number_is_valid(unsolved_elements[current_element])):
            current_element += 1
    else:
        board[unsolved_elements[current_element].y][unsolved_elements[current_element].x] = 0
        current_element -= 1
        if (current_element < 0):
            print_board()
            print ("ooops... brettet var visst ikke gyldig, iterasjoner:", iterations)
            break
    iterations += 1

print_board()
print ("Antall iterasjoner: ", iterations)
