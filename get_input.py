print ("Hei og velkommen til sudoku-løseren")
print ("Du må nå skrive inn hver linje i sudokuen du vil løse fra topp til bunn.")
print ("Skriv inn alle 9 tallene på en og en rekke og bruk \"-\" for der det mangler tall")
print ("Eks: 1--5--6-4")
print ("\n-----------------------------------------------------------------------------------")
print ("Input: \n")
board = []

valid_characters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
def check_if_valid_characters (rekke):
    for element in rekke:
        if not element in valid_characters:
            return False
    return True

def check_if_number_is_valid (rekke):
    #sjekk om rekken inneholder flere av samme tall
    testrekke = rekke[:]
    for i in range(len(testrekke)):
        element = testrekke.pop()
        if (not element == "-") and element in testrekke:
            return False

    #sjekk om rekken inneholder tall som krasjer med tall i kolonnen
    for rad in board:
        for i in range(len(rad)):
            if rad[i] == rekke[i] and rekke[i] != "-":
                return False

    #sjekk om rekken inneholder tall som krasjer med tall i 3*3-ruten
    rekke_nummer = len(board)
    antall_rekker_sjekkes = rekke_nummer % 3; #antall rekker oppover som må sjekkes 
    for i in range(1, antall_rekker_sjekkes+1):
        for j in range(len(rekke)):
            if (rekke[j] == board[rekke_nummer - i][(j//3) * 3] or rekke[j] == board[rekke_nummer - i][(j//3)*3 + 1] or rekke[j] == board[rekke_nummer - i][(j//3) * 3 + 2]) and rekke[j] != "-":
                return False

    return True

def print_board():
    for element in board:
        print (element)

for x in range (1,10):
    while True:
        rekke = list(input("Skriv inn rekke %s: " % x))
        if len(rekke) != 9:
            print ("Rekken må inneholde 9 elementer")
        elif not check_if_valid_characters(rekke):
            print ("Rekken kan kun inneholde tegnene \"123456789-\"")
        elif not check_if_number_is_valid (rekke):
            print ("Rekken inneholdt et ugyldig tall")
        else:
            board.append(rekke)
            break
print ("Brettet ditt ser nå slik ut: ")
print_board()
        