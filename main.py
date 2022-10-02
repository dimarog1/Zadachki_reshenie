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
inp = list(set(map(int, input().split())))
print(inp[-2])

# Задача 6
def reverseString(string):
    return string[::-1]


# Задача 7
def triangle(a, b, c):
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        return "Это не треугольник"
    return "Это треугольник"


# Задача 8
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


# Задача 9
def convertToInt(strList):
    return list(map(int, strList))


# Задача 10
def totalOrDif(set1, set2, param="and"):
    if param == "and":
        return set1 & set2
    elif param == "dif":
        return set1 ^ set2
