W = input()
count = 0
T = input()
while T != 'END_OF_TEXT':
    #入力された文字列を分割し、各単語を引数としてfor文をまわす
    for i in T.lower().split():
        if W == i:
            count += 1
    T = input()
print(count)
