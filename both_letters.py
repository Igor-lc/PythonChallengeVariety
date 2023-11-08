

from sys import argv

word = argv[1]


# ver1
def first(i):
    if i == 0:
        print(word[i])


def last(i):
    if i == len(word) - 1:
        print(word[i])


''.join(map(str, filter(first, [i for i, w in enumerate(word)])))
''.join(map(str, filter(last, [i for i, w in enumerate(word)])))

# ver2
first_letter = word[next(filter(lambda i: i == 0, [i for i, w in enumerate(word)]))]
last_letter = word[next(filter(lambda i: i == len(word) - 1, [i for i, w in enumerate(word)]))]

print(first_letter, last_letter)

# ver3
first_letter = next(filter(lambda i: i[0] == 0, enumerate(word)))
last_letter = next(filter(lambda i: i[0] == len(word) - 1, enumerate(word)))

print(first_letter[1], last_letter[1])