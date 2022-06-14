import random
import datetime
x = 10
y = 2
z = 5
count = 0
def main():
    st = datetime.datetime.now()
    play = game()
    et = datetime.datetime.now()
    if play == 1:
        print(f"クリアタイム:{(et-st).seconds}秒")


def mozi():
    global x,y2
    alphabetlist = [chr(c+65) for c in range(26)]
    mozilist = random.sample(alphabetlist,x)
    k_mozilist = random.sample(mozilist,y)
    ans = list(set(mozilist)-set(k_mozilist))
    return mozilist,k_mozilist,ans


def game():
    global count,z,x,y,flag
    count = z
    flag = 0
    while count:
        alpha1,alpha2,alpha_ans = mozi()
        print(f"対象文字\n{alpha1}")
        print(f"表示文字\n{alpha_ans}")
        ans1 = int(input("欠損文字はいくつあるでしょうか？ "))
        if ans1 == y:
            print("正解です それでは、具体的に欠損文字を1つずつ入力してください")
            ans2 = input("1つ目の文字を入力してください ")
            ans3 = input("2つ目の文字を入力してください ")
            if ans2 and ans3 in alpha2:
               print("正解です")
               flag = 1
               return flag
            if not ans2 in alpha2:
                print("不正解です。またチャレンジしてください")
                count -= 1

if __name__ == "__main__":
    main()


