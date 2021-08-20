class King:

    def __init__(self, i, j, user):
        self.i = i
        self.j = j
        self.user = user
        self.priority = 10

    def move(self):
        king = []
        for m in range(self.i - 1, self.i + 2):
            for n in range(self.j - 1, self.j + 2):
                if (0 <= m < 8) and (0 <= n < 8) and not (m == self.i and n == self.j):
                    king.append((m, n))
        return block(king, self.i, self.j)


class Rook:

    def __init__(self, i, j, user):
        self.i = i
        self.j = j
        self.user = user
        self.priority = 5

    def move(self):  # where rook can go
        rook = []
        a = self.i
        b = self.j
        while True:  # go left of rook
            b -= 1
            if not (0 <= b < 8):  # check for inside board
                break
            if board[a][b] == '   ':  # if empty place add that place
                rook.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:  # if found the same type of pawn at a,b
                break
            elif board[a][b][0] != board[self.i][self.j][0]:  # if found the other same type of pawn
                rook.append((a, b))
                break
        b = self.j
        while True:
            b += 1
            if not (0 <= b < 8):
                break
            if board[a][b] == '   ':
                rook.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:
                break
            elif board[a][b][0] != board[self.i][self.j][0]:
                rook.append((a, b))
                break
        b = self.j

        while True:
            a -= 1
            if not (0 <= a < 8):
                break
            if board[a][b] == '   ':
                rook.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:
                break
            elif board[a][b][0] != board[self.i][self.j][0]:
                rook.append((a, b))
                break
        a = self.i
        while True:
            a += 1
            if not (0 <= a < 8):
                break
            if board[a][b] == '   ':
                rook.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:
                break
            elif board[a][b][0] != board[self.i][self.j][0]:
                rook.append((a, b))
                break
        # print(rook, self.i, self.j, self.user, ',,,,,,,,,,,,,,,,,')
        return rook


class Bishop:
    def __init__(self, i, j, user):
        self.i = i
        self.j = j
        self.user = user
        self.priority = 3

    def move(self):
        bishop = []
        a = self.i
        b = self.j
        while True:
            a += 1
            b -= 1
            # print(a, b, self.i, self.j, board[a][b], board[self.i][self.j], '......................')
            if not (0 <= a < 8 and 0 <= b < 8):  # check for out of board
                break
            if board[a][b] == '   ':  # if empty place add that place
                bishop.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:  # if found the same type of pawn at a,b
                break
            elif board[a][b][0] != board[self.i][self.j][0]:  # if found the other same type of pawn
                bishop.append((a, b))
                break

        a = self.i
        b = self.j
        while True:
            a += 1
            b += 1
            if not (0 <= a < 8 and 0 <= b < 8):
                break
            if board[a][b] == '   ':
                bishop.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:
                break
            elif board[a][b][0] != board[self.i][self.j][0]:
                bishop.append((a, b))
                break

        a = self.i
        b = self.j
        while True:
            a -= 1
            b += 1
            if not (0 <= a < 8 and 0 <= b < 8):
                break
            if board[a][b] == '   ':
                bishop.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:
                break
            elif board[a][b][0] != board[self.i][self.j][0]:
                bishop.append((a, b))
                break

        a = self.i
        b = self.j
        while True:
            a -= 1
            b -= 1
            if not (0 <= a < 8 and 0 <= b < 8):
                break
            if board[a][b] == '   ':
                bishop.append((a, b))
            elif board[a][b][0] == board[self.i][self.j][0]:
                break
            elif board[a][b][0] != board[self.i][self.j][0]:
                bishop.append((a, b))
                break

        return bishop


class Horse:
    def __init__(self, i, j, user):
        self.i = i
        self.j = j
        self.user = user
        self.priority = 3

    def move(self):
        horse = [(self.i + 1, self.j + 2), (self.i + 2, self.j + 1), (self.i - 1, self.j + 2), (self.i - 2, self.j + 1),
                 (self.i + 1, self.j - 2), (self.i + 2, self.j - 1), (self.i - 1, self.j - 2), (self.i - 2, self.j - 1)]
        for i in range(8):
            for pos in horse:
                if (pos[0] < 0 or pos[0] > 7) or (pos[1] < 0 or pos[1] > 7):  # if out of board
                    horse.remove(pos)
        # print(horse)
        return block(horse, self.i, self.j)


class Queen:
    def __init__(self, i, j, user):
        self.i = i
        self.j = j
        self.user = user
        self.priority = 7

    def move(self):
        queen = []
        bishop = Bishop(self.i, self.j, self.user)
        rook = Rook(self.i, self.j, self.user)
        b = bishop.move()  # change for storing each element........................
        for i in b:
            queen.append(i)
        r = rook.move()
        for i in r:
            queen.append(i)
        # print(queen)
        return queen


class Soldier:
    def __init__(self, i, j, user):
        self.i = i
        self.j = j
        self.user = user
        self.priority = 1

    def move(self):
        soldier = []
        if self.user:  # check for black or white

            if (0 <= self.i - 1 < 8) and (0 <= self.j < 8):
                if board[self.i - 1][self.j] == '   ':
                    soldier.append((self.i - 1, self.j))
                    if (0 <= self.i - 2 < 8) and (0 <= self.j < 8):
                        if self.i == 6 and board[self.i - 2][self.j] == '   ':  # check for initial step
                            soldier.append((self.i - 2, self.j))

            if (0 <= self.i - 1 < 8) and (
                    0 <= self.j - 1 < 8):  # when capturing a pawn left check for pawn inside the board
                if board[self.i - 1][self.j - 1] != '   ':
                    if not board[self.i - 1][self.j - 1][0] == 'b':
                        soldier.append((self.i - 1, self.j - 1))
            if (0 <= self.i - 1 < 8) and (
                    0 <= self.j + 1 < 8):  # when capturing a pawn right check for pawn inside the board
                if board[self.i - 1][self.j + 1] != '   ':
                    if not board[self.i - 1][self.j + 1][0] == 'b':
                        soldier.append((self.i - 1, self.j + 1))

        else:

            if (0 <= self.i + 1 < 8) and (0 <= self.j < 8):
                if board[self.i + 1][self.j] == '   ':
                    soldier.append((self.i + 1, self.j))
                    if (0 <= self.i + 2 < 8) and (0 <= self.j < 8):
                        if self.i == 1 and board[self.i + 2][self.j] == '   ':
                            soldier.append((self.i + 2, self.j))

            if (0 <= self.i + 1 < 8) and (0 <= self.j - 1 < 8):
                if board[self.i + 1][self.j - 1] != '   ':
                    if board[self.i + 1][self.j - 1][0] == 'b':
                        soldier.append((self.i + 1, self.j - 1))
            if (0 <= self.i + 1 < 8) and (0 <= self.j + 1 < 8):
                if board[self.i + 1][self.j + 1] != '   ':
                    if board[self.i + 1][self.j + 1][0] == 'b':
                        soldier.append((self.i + 1, self.j + 1))
        # print(soldier)
        return block(soldier, self.i, self.j)


def block(tup, a, b):  # if the pawn in tup is of same kind as pawn at a,b remove that tup
    tup2 = []
    for i, j in tup:
        if board[i][j] == '   ':
            tup2.append((i, j))
        elif board[i][j][0] != board[a][b][0] and (board[i][j][1] != 'S' or board[i][j][1] != 's'):
            tup2.append((i, j))
    # print(tup2, '?????????????????')
    return tup2


WR1 = Rook(0, 0, False)
WR2 = Rook(0, 7, False)
WB1 = Bishop(0, 2, False)
WB2 = Bishop(0, 5, False)
WH1 = Horse(0, 1, False)
WH2 = Horse(0, 6, False)
WK1 = King(0, 3, False)
WQ1 = Queen(0, 4, False)
WS1 = Soldier(1, 0, False)
WS2 = Soldier(1, 1, False)
WS3 = Soldier(1, 2, False)
WS4 = Soldier(1, 3, False)
WS5 = Soldier(1, 4, False)
WS6 = Soldier(1, 5, False)
WS7 = Soldier(1, 6, False)
WS8 = Soldier(1, 7, False)

br1 = Rook(7, 0, True)
br2 = Rook(7, 7, True)
bb1 = Bishop(7, 2, True)
bb2 = Bishop(7, 5, True)
bh1 = Horse(7, 1, True)
bh2 = Horse(7, 6, True)
bk1 = King(7, 3, True)
bq1 = Queen(7, 4, True)
bs1 = Soldier(6, 0, True)
bs2 = Soldier(6, 1, True)
bs3 = Soldier(6, 2, True)
bs4 = Soldier(6, 3, True)
bs5 = Soldier(6, 4, True)
bs6 = Soldier(6, 5, True)
bs7 = Soldier(6, 6, True)
bs8 = Soldier(6, 7, True)

board = [
    ['WR1', 'WH1', 'WB1', 'WK1', 'WQ1', 'WB2', 'WH2', 'WR2'],
    ['WS1', 'WS2', 'WS3', 'WS4', 'WS5', 'WS6', 'WS7', 'WS8'],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ['bs1', 'bs2', 'bs3', 'bs4', 'bs5', 'bs6', 'bs7', 'bs8'],
    ['br1', 'bh1', 'bb1', 'bk1', 'bq1', 'bb2', 'bh2', 'br2']
]

white_pawns = {'WR1': WR1, 'WR2': WR2, 'WH1': WH1, 'WH2': WH2, 'WB1': WB1, 'WB2': WB2, 'WK1': WK1, 'WQ1': WQ1,
               'WS1': WS1, 'WS2': WS2, 'WS3': WS3, 'WS4': WS4, 'WS5': WS5, 'WS6': WS6, 'WS7': WS7, 'WS8': WS8}
black_pawns = {'br1': br1, 'br2': br2, 'bb1': bb1, 'bb2': bb2, 'bs1': bs1, 'bs2': bs2, 'bs3': bs3, 'bs4': bs4,
               'bs5': bs5, 'bs6': bs6, 'bs7': bs7, 'bs8': bs8, 'bk1': bk1, 'bq1': bq1, 'bh1': bh1, 'bh2': bh2}
all_pawns = {}
all_pawns.update(white_pawns)
all_pawns.update(black_pawns)
eliminated_black_pawns = []
eliminated_white_pawns = []
u_list = [bs1, bs2, bs3, bs4, bs5, bs6, bs7, bs8, br1, bh1, bb1, bk1, bq1, bb2, bh2, br2]
c_list = [WS1, WS2, WS3, WS4, WS5, WS6, WS7, WS8, WR1, WH1, WB1, WK1, WQ1, WB2, WH2, WR2]
du_list = {'bs1': 0, 'bs2': 1, 'bs3': 2, 'bs4': 3, 'bs5': 4, 'bs6': 5, 'bs7': 6, 'bs8': 7, 'br1': 8, 'bh1': 9,
           'bb1': 10, 'bk1': 11, 'bq1': 12, 'bb2': 13, 'bh2': 14, 'br2': 15}
dc_list = {'WS1': 0, 'WS2': 1, 'WS3': 2, 'WS4': 3, 'WS5': 4, 'WS6': 5, 'WS7': 6, 'WS8': 7, 'WR1': 8, 'WH1': 9,
           'WB1': 10, 'WK1': 11, 'WQ1': 12, 'WB2': 13, 'WH2': 14, 'WR2': 15}


def move_pawn(pawn, x, y):
    all_possible_moves = pawn.move()  # get all paths
    # print(pawn)
    if (x, y) in all_possible_moves:  # check if it can move
        if board[x][y] == '   ':  # if move to empty space
            board[x][y] = board[pawn.i][pawn.j]
            board[pawn.i][pawn.j] = '   '
            pawn.i = x
            pawn.j = y

        elif board[pawn.i][pawn.j][0] != board[x][y][0]:  # compare 'W' and 'b'
            p = all_pawns[board[x][y]]  # Pawn that is getting killed
            if p.user is False:  # Pawn killed is computer's(white)
                eliminated_white_pawns.append((board[x][y], x, y))
                # print(eliminated_black_pawns, eliminated_white_pawns)
                ob = white_pawns[board[x][y]]
                c_list.remove(ob)
            else:  # Pawn killed is user's(black)
                eliminated_black_pawns.append((board[x][y], x, y))
                # print(eliminated_black_pawns, eliminated_white_pawns)
                ob = black_pawns[board[x][y]]
                u_list.remove(ob)
            board[x][y] = board[pawn.i][pawn.j]
            board[pawn.i][pawn.j] = '   '
            pawn.i = x
            pawn.j = y
        else:
            print("can't kill same type of pawn")
    else:
        print('enter correct possition')


def move_back(x, y, i, j, max_player):
    # print(eliminated_white_pawns, 'eliminated_white_pawns')
    # print(eliminated_black_pawns, 'eliminated_black_pawns')
    if len(eliminated_black_pawns) != 0 and (eliminated_black_pawns[-1][-2], eliminated_black_pawns[-1][-1]) == (
    x, y) and not max_player:  # check eleminated pawn is black or white
        board[i][j] = board[x][y]  # Move back the white pawn
        white_pawns[board[i][j]].i = i
        white_pawns[board[i][j]].j = j
        board[x][y] = eliminated_black_pawns[-1][0]  # Bring back the killed black pawn
        ele = eliminated_black_pawns[-1][0]
        u_list.insert(du_list[ele], black_pawns[ele])
        eliminated_black_pawns.pop()
    elif len(eliminated_white_pawns) != 0 and (eliminated_white_pawns[-1][-2], eliminated_white_pawns[-1][-1]) == (
    x, y) and max_player:
        board[i][j] = board[x][y]
        black_pawns[board[i][j]].i = i
        black_pawns[board[i][j]].j = j
        board[x][y] = eliminated_white_pawns[-1][0]
        ele = eliminated_white_pawns[-1][0]
        c_list.insert(dc_list[ele], white_pawns[ele])
        eliminated_white_pawns.pop()
    else:
        board[i][j] = board[x][y]
        board[x][y] = '   '
        if all_pawns[board[i][j]].user:  # or check in ulist
            black_pawns[board[i][j]].i = i
            black_pawns[board[i][j]].j = j
        else:
            white_pawns[board[i][j]].i = i
            white_pawns[board[i][j]].j = j


# white - computer,black - player
def minimax(depth, max_player, pawn, alpha, beta):
    # print_board()
    if depth == 0:  # if at end then find the priority
        return staticeval(pawn)

    if max_player:  # user turn
        max_eval = -100
        for pawn in u_list:  # for every pawn in u_list
            a, b = pawn.i, pawn.j
            m_list = pawn.move()  # get all the places the pawn can move
            for tup in m_list:  # for every place it can move
                move_pawn(pawn, tup[0], tup[1])  # move the pawn
                x_eval = minimax(depth - 1, False, pawn, alpha, beta)  # minimax next step
                move_back(tup[0], tup[1], a, b, max_player)  # bring back the pawn
                # print_board()
                max_eval = max(x_eval, max_eval)  # get best path
                alpha = max(alpha, x_eval)
                if beta <= alpha:
                    break
        return max_eval

    else:
        min_eval = 100
        for pawn in c_list:
            a, b = pawn.i, pawn.j
            m_list = pawn.move()
            for tup1 in m_list:
                move_pawn(pawn, tup1[0], tup1[1])
                x_eval = minimax(depth - 1, True, pawn, alpha, beta)
                move_back(tup1[0], tup1[1], a, b, max_player)
                # print_board()
                min_eval = min(x_eval, min_eval)
                beta = min(beta, x_eval)
                if alpha <= beta:
                    break
        return min_eval


def staticeval(pawn):
    arr = arr2 = []
    score = 0
    a = (pawn.i, pawn.j)

    # my pawn is getting killed
    for p in c_list:  # for every pawn in c_list ie, all the places the opponent(computer) pawn can go
        arr.append((p.move(),
                    p.priority))  # get the places it can move and priorities [([(0,1),(),(),(),........],priorities),.......,......,....]
    for i in range(len(arr)):  # collect all the priorities (if) where the computer can kill
        if a == arr[i][0]:
            arr2.append(arr[i][1])
    for i in range(len(arr2)):  # subtract all the priorities from score
        score -= arr2[i][1]

    a = pawn.move()
    for i in u_list:
        arr.append(((i.i, i.j), i.priority))
    for i in range(len(a)):
        for a[i] in arr[0]:
            arr2.append(arr[1])
    for i in range(len(arr2)):
        score += arr2[i][1]
    return score


t = 0


def print_board():
    global t
    print(t)
    t += 1
    i = 0
    print('________________________________________________________')
    print('----------------------------------------------------------')
    while i < 8:
        j = 0
        print(f'{i}  ', end='')
        while j < 8:
            print('| ' + board[i][j] + ' ', end='')
            j += 1
        print('|')
        print('-----------------------------------------------------')
        i += 1
    print('     A      B     C     D     E     F     G     H')
    print('________________________________________________________')


d = {King: 'K', Soldier: 'S', Queen: 'Q', Bishop: 'B', Rook: 'R', Horse: 'H', str: ' '}  # to print which kind of pawn
d_pos = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}  # convert string to nubers for board


def user_turn():
    c_pos = input('Enter current postion: ').lower()  # get positions
    n_pos = input('Enter next position: ').lower()
    y1, x1 = d_pos[c_pos[0]], int(c_pos[1])  # get in terms of numbers
    y2, x2 = d_pos[n_pos[0]], int(n_pos[1])
    if all_pawns[board[x1][y1]].user:  # move only told to move the black pawn
        print(black_pawns[board[x1][y1]].move())
        move_pawn(black_pawns[board[x1][y1]], x2, y2)


def computer_turn():
    print('Wait!!!!! Im thinking............')
    global p, q, m, n
    bestscore = 1000
    for pawn in c_list:  # for every pawn in c_list
        a, b = pawn.i, pawn.j
        m_list = pawn.move()  # get all the places it can move
        for tup in m_list:  # for all the places it can move
            move_pawn(pawn, tup[0], tup[1])  # move that pawn to those, each plsces
            score = minimax(3, True, pawn, -1000, 1000)  # check for even and odd because of static eval...........
            move_back(tup[0], tup[1], a, b, False)  # bring back the pawn to original place
            if score < bestscore:  # store the results
                m, n = tup
                p, q = a, b
                bestscore = score
    move_pawn(white_pawns[board[p][q]], m, n)  # move according to best move calculated


z = 0
while True:
    print_board()
    if z % 2 == 0:
        user_turn()
        z += 1
    else:
        computer_turn()
        z += 1
    eliminated_black_pawns = []
    eliminated_white_pawns = []
