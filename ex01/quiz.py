import random
def shutudai(Q1):
    Q = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    print("問題"+"\n"+Q[Q1])
    
def kaito(Q1):
    A = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子"]]
    ans = input("答えるんだ>>>")
    if ans in A[Q1]:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    x1 = random.randint(0,2)
    shutudai(x1)
    kaito(x1)
