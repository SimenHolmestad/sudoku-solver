valid_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
def check_if_valid_row (rekke):
    for element in rekke:
        if not element in valid_characters:
            return False
    return True

def check_if_row_is_valid (rekke):
    #sjekk om rekken inneholder flere av samme tall
    testrekke = rekke[:]
    for i in range(len(testrekke)):
        element = testrekke.pop()
        if (not element == "0") and element in testrekke:
            return False

    #sjekk om rekken inneholder tall som krasjer med tall i kolonnen
    for rad in board:
        for i in range(len(rad)):
            if rad[i] == rekke[i] and rekke[i] != "0":
                return False

    #sjekk om rekken inneholder tall som krasjer med tall i 3*3-ruten
    rekke_nummer = len(board)
    antall_rekker_sjekkes = rekke_nummer % 3; #antall rekker oppover som må sjekkes 
    for i in range(1, antall_rekker_sjekkes+1):
        for j in range(len(rekke)):
            if (rekke[j] == board[rekke_nummer - i][(j//3) * 3] or rekke[j] == board[rekke_nummer - i][(j//3)*3 + 1] or rekke[j] == board[rekke_nummer - i][(j//3) * 3 + 2]) and rekke[j] != "0":
                return False

    return True


def print_board(board):
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

def solve_sudoku(board):
    unsolved_elements = []

    for y in range(9):
        for x in range(9):
            board[y][x] = int(board[y][x])
            if (board[y][x] == 0):
                #Lagrer koordinatene til alle blanke felt:
                unsolved_elements.append(coords(y,x))

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
                print_board(board)
                print ("ooops... brettet var visst ikke gyldig, iterasjoner:", iterations)
                break
        iterations += 1
    print_board(board)
    print ("Antall iterasjoner: ", iterations)

def get_input ():
    for x in range (1,10):
        while True:
            rekke = list(input("Skriv inn rekke %s: " % x))
            if len(rekke) != 9:
                print ("Rekken må inneholde 9 elementer")
            elif not check_if_valid_row(rekke):
                print ("Rekken kan kun inneholde tegnene \"1234567890\"")
            elif not check_if_row_is_valid (rekke):
                print ("Rekken inneholdt et ugyldig tall")
            else:
                board.append(rekke)
                break

    for x in range(9):
        for y in range(9):
            board[x][y] = int(board[x][y])

board = []
get_input()
print ("Brettet ditt ser nå slik ut: ")
print_board(board)
print ("Brettet løst blir:")
solve_sudoku(board)
