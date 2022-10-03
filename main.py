# Задача 1
x = int(input())
print(x ** 2 + 3 * x - 7)

# Задача 2
for i in range(8):
    print(2 ** i)

# Задача 3
a, b = int(input()), int(input())
print(a ** (1 / b))

# Задача 4
s = 'djsbdhjsbdhabddsaxxahophfejfhejfhwekbekjvbjhbvhdvbjsdhvbjshbvjbdjbsjbjdbhvjdvbjsdbvjsvbjbv'
used = ''
ans = 0
for i in s:
    if i not in used:
        ans += 1
        used += i
print(ans)


# Задача 5
def findSum(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum


# Задача 6
def transpose(tup):
    return tuple(zip(*[i for i in tup]))


# Задача 7
def zeros(n):
    x = n // 5
    return x + zeros(x) if x else 0


# Задача 8
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


# Задача 9
def translit(string):
    rusAlphabet = "абвгдеёжзийклмнопрстуфхцчшъыьэюя"
    translitAlphabet = "a b v g d e yo zh z i y k l m n o" \
                       " p r s t u f kh ts ch sh shch ` y ` e yu ia".split()

    trans = {rusAlphabet[i]: translitAlphabet[i] for i in range(len(rusAlphabet))}

    res = ""
    for elem in string:
        if elem in trans:
            res += trans[elem]
        else:
            res += elem

    return res


# Задача 10
def isSolved(board):
    flag = True
    k = {2: 'O', 1: 'X', 0: ''}
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = k[board[i][j]]
    for i in range(len(board)):
        horizontal = ''.join(board[i])
        vertical = ''.join([board[n][i] for n in range(len(board))])
        diagonal1, diagonal2 = (''.join([board[i][i] for i in range(len(board))]),
                                ''.join([board[i][len(board) - i - 1] for i in range(len(board))]))
        flag = False if ((len(horizontal) != 3 or len(vertical) != 3) or not flag) else True
        if any([j == 'XXX' for j in (horizontal, vertical, diagonal1, diagonal2)]):
            return 1
        if any([j == 'OOO' for j in (horizontal, vertical, diagonal1, diagonal2)]):
            return 2
    if flag:
        return 0
    return -1
