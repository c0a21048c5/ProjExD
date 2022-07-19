import pygame as pg
import sys
import random

from scipy import rand

class Display: #ディスプレイの描画内容を規定
    def __init__(self, title, wh, col): #ディスプレイのサイズなどを規定
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.Surface((1600,900))
        self.bgi_sfc.fill(col)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self): #描画
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Ganban: #こうかとんが埋まっている、岩盤について規定。
    def __init__(self): #岩盤のサイズや描画について記載。
        self.gx_size = 250
        self.gy_size = 200
        self.dig_count = 0
        self.dig_impct = 8
        self.kiban_size = pg.Rect(20,20,1000,800)
        self.color_list = [[255,255,255],[210,105,30],[160,82,45],[139,69,19]] #岩盤の色を指定
        self.rock = [[random.randint(1,3) for i in range(self.gx_size)] for j in range(self.gy_size)]
        self.kiban_sfc = pg.Surface((self.gx_size*4,self.gy_size*4))
        self.kiban_sfc.set_alpha(255)
        self.kiban_sfc.set_colorkey([255,255,255])
        self.kiban_rct = self.kiban_sfc.get_rect()
        self.dig_size = 45
        for y in range(self.gy_size):
            for x in range(self.gx_size):#岩盤を描画
                g_c = self.rock[y][x]
                pg.draw.rect(self.kiban_sfc,(self.color_list[g_c][0],self.color_list[g_c][1],self.color_list[g_c][2]),(((4*x)),(4*y),4,4))

    def dig(self): #掘削の作業
        x,y = pg.mouse.get_pos()
        self.pos_x = x//4
        self.pos_y = y//4
        self.dig_count += self.dig_impct
        self.dig_list = []
        self.big_list_x = [[i for i in range(-1*(2+(self.dig_size//4-abs(j-self.dig_size//2))),5+(self.dig_size//4-abs(j-self.dig_size//2)))] for j in range(self.dig_size)]
        self.big_list_y = [i for i in range(-1*(self.dig_size//2),(self.dig_size//2)+5)]
        for y in range(len(self.big_list_x)):
            for x in range(len(self.big_list_x[y])):
                self.big_list_x[y][x] += self.pos_x

        for y in range(len(self.big_list_x)):
            p_y = self.big_list_y[y]
            for x in range(len(self.big_list_x[y])):
                p_x = self.big_list_x[y][x]
                try:
                    self.rock[self.pos_y + p_y][p_x] -= 1
                    g_c = self.rock[self.pos_y + p_y][p_x]
                    if g_c < 0 :
                        g_c = 0
                    pg.draw.rect(self.kiban_sfc,(self.color_list[g_c][0],self.color_list[g_c][1],self.color_list[g_c][2]),(((4*p_x)),(4*(self.pos_y + p_y)),4,4))
                except IndexError:
                    print("out of Index")

    def size_chang(self,size): #ハンマーとドリルの切り替え
        if size == "big":
            self.dig_size = 45
            self.dig_impct = 8
        elif size == "small":
            self.dig_size = 15
            self.dig_impct = 2

    def bilt(self,dis:Display):
        dis.sfc.blit(self.kiban_sfc,(20,20,1000,800),self.kiban_rct)


class Object: #その他オブジェクトについて規定
    def __init__(self,dis:Display): #ボタンなどの描画
        self.big_btn = pg.Rect(1100,50,200,100)
        self.sml_btn = pg.Rect(1350,50,200,100)
        pg.draw.rect(dis.bgi_sfc,(255,0,0),self.big_btn)
        pg.draw.rect(dis.bgi_sfc,(0,255,0),self.sml_btn)
        self.HPbar_sfc = pg.Surface((1000,50))
        self.HPbar_rct = self.HPbar_sfc.get_rect()
        for i in range(500):
            pg.draw.rect(self.HPbar_sfc,(255,0,0),(i*2,0,2,50))
    
    def HP_chang(self,gbn:Ganban): #HPバーの処理を規定
        for i in range(500,500-gbn.dig_count,-1):
            pg.draw.rect(self.HPbar_sfc,(0,0,255),(i*2,0,2,50))

    def yakitori(self,image,size,pos): #こうかとんの描画
        self.yakitori_img_sfc = pg.image.load(image)
        self.yakitori_img_sfc = pg.transform.rotozoom(self.yakitori_img_sfc,0,size)
        self.yakitori_img_rct = self.yakitori_img_sfc.get_rect()
        self.yakitori_img_rct.center = pos
    
    def haikei(self,image,size): #岩盤の後ろ側の画像を描画
        self.haikei_img_sfc = pg.image.load(image)
        self.haikei_img_sfc = pg.transform.scale(self.haikei_img_sfc,size)
        self.haikei_img_rct = self.haikei_img_sfc.get_rect()
        #self.haikei_img_rct.center = pos

    def bilt(self,dis:Display):
        dis.sfc.blit(dis.bgi_sfc, dis.bgi_rct)
        dis.sfc.blit(self.HPbar_sfc,(20,830,1000,50),self.HPbar_rct)
        dis.sfc.blit(self.haikei_img_sfc,(20,20,1000,800),self.haikei_img_rct)
        dis.sfc.blit(self.yakitori_img_sfc,self.yakitori_img_rct)


class Start: #スタート画面を表示するクラス
    def __init__(self,image,dis:Display):
        self.start_img_sfc = pg.image.load(image)
        self.start_img_sfc = pg.transform.scale(self.start_img_sfc,(1600,900))
        self.start_img_rct = self.start_img_sfc.get_rect()
        while True:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    return
            dis.sfc.blit(self.start_img_sfc,self.start_img_rct)
            pg.display.update()


def main(): #クラスの呼び出し
    clock = pg.time.Clock() 
    dis = Display("甦れコウカトン", (1600, 900), (192,192,192)) #Displayを描画
    obj = Object(dis) #Objectクラスを呼び出す
    obj.haikei("ex03/fig/ganban.png",(1000,800)) #背景を描画
    gbn = Ganban() #岩盤を描画
    obj.yakitori("ex03/fig/6.png", 2.0,(random.randint(70,gbn.kiban_sfc.get_width()-50), random.randint(70,gbn.kiban_sfc.get_height()-50)))
    Start("ex03/fig/34428.jpg",dis) #スタート画面を描画
    while True: #以降ゲーム内の処理を記載
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
            if event.type == pg.MOUSEBUTTONDOWN: #イベントを取得し、対応したイベントを実行
                if obj.big_btn.collidepoint(event.pos): #ドリルに切り替え
                    print("red button was pressed") 
                    gbn.size_chang("big")
                if obj.sml_btn.collidepoint(event.pos): #ハンマーに切り替え
                    print("green button was pressed")
                    gbn.size_chang("small")
                if gbn.kiban_size.collidepoint(event.pos): #HPバーの減少について明記
                    gbn.dig()
                    obj.HP_chang(gbn)

        dis.blit()
        obj.bilt(dis)
        gbn.bilt(dis)
        pg.display.update()

        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()