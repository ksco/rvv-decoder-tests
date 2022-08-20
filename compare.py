import re

testS =   open('test.S', 'r', encoding='utf-8').read().split('\n')[2:]
outputS = open('output.S', 'r', encoding='utf-8').read().split('\n')


if len(testS) != len(outputS):
    print("ERROR: len(testS) != len(outputS)")
    exit()

e = 0
i = 0
for line in testS:
    oline = outputS[i]
    i += 1

    if re.sub(' +', ' ', oline) != line:
        e += 1
        if e >= 5:
            exit()
        print(f"ERROR: line {i}: {line} != {oline}")

if not e:
    print("ALL PASS.")
