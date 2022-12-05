import sys
sys.stdin = open('2675.txt', 'r')

word = str(input())
chk = 0


def countword(word):
    wordlen = int(len(word))
    for i in range(wordlen):
        if ord(word[i]) > 96:
            ud = int(ord(word[i])) - 32
            if ud
