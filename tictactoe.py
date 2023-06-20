def disp(r1):
    print(r1)

#def mechanic(game):


def changeValue(board ,position):
    userInput = input('Masukkan nilai yang nada inginkan: ')

    board[position] = userInput

    return board

def inputPosition():
    isNotNumber = True
    isNotInCollection = True

    while isNotNumber and isNotInCollection:
        r = input("Masukkan angka 1 - 3: ")

        if r.isdigit():
            if r in ['1', '2', '3']:
                isNotInCollection = False
                isNotNumber = False
            else:
                print('Angka yang kamu masukkan tidak sesuai')
        else:
            print('Inputan yang kamu masukkan bukan angka')

    return int(r)-1

def gameOnChose():
    r = ''

    while r.upper() not in ['Y', 'N']:
        r = input('Apakah anda mau lanjut bermain:')

        if r.upper() not in ['Y', 'N']:
            print('Masukkan anda tidak sesuai')

    if r.upper() == 'Y':
        return True
    else:
        return False



game = True
r1 = [1,2,3]

while game:
    disp(r1)

    p = inputPosition()
    r1 = changeValue(r1, p)
    game = gameOnChose()


disp(r1)
