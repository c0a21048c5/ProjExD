import random
import datetime
x = 10
y = 2
z = 5
count = 0

def mozi():
    global x
    alphabetlist = [chr(c+65) for c in range(26)]
    mozilist = random.sample(alphabetlist,x)
    return mozilist

def mozi2(a):
    global y
    k_mozilist = random.sample(a,y)
    return k_mozilist


def hiyouzi(a,b):
    ans = list(set(a)-set(b))
    return ans

def game():
    global count,z,x,y
    count = z
    while count:
        alpha1 = mozi()
        alpha2 = mozi2(alpha1)
        alpha_ans = hiyouzi(alpha1,alpha2)
        print(f"対象文字\n{alpha1}")
        print(f"欠損文字\n{alpha2}")
        print(f"表示文字\n{alpha_ans}")
        ans1 = int(input("欠損文字はいくつあるでしょうか？ "))
        if ans1 == y:
            print("正解です それでは、具体的に欠損文字を1つずつ入力してください")
            ans2 = input("1つ目の文字を入力してください ")
            ans3 = input("2つ目の文字を入力してください ")
            if ans2 and ans3 in alpha2:
               print("正解です")
               break
            if not ans2 in alpha2:
                print("不正解です。またチャレンジしてください")
                count -= 1

if __name__ == "__main__":
    game()

        


