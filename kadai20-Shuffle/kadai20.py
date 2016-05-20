#山札(文字列)を入力
deck = input()
#ハイフン(-)が山札に入力されるまで実行
while deck != "-":
    #回数の入力
    times = int(input())
    #文字列をリスト化
    shuffle = list(deck)
    #文字列の長さを格納
    deck_length = len(deck)
    #timesの回数だけシャッフル
    for i in range(times):
        #どこで区切るかを入力し、その値でシャッフル
        val = int(input())
        shuffle = shuffle[val:] + shuffle[:val]
    #結果を出力
    print("".join(shuffle))
    #次の山札を入力
    deck = input()

