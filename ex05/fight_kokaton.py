import pygame as pg
import sys
import random
import time
import tkinter as tk
import tkinter.messagebox as tkm


class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)        
        self.rct = self.sfc.get_rect()            
        self.bgi_sfc = pg.image.load(image)       
        self.bgi_rct = self.bgi_sfc.get_rect()    

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
    

class Bird:
    def __init__(self,image,exp,xy):
        self.sfc = pg.image.load(image)    
        self.sfc = pg.transform.rotozoom(self.sfc, 0, exp)  
        self.rct = self.sfc.get_rect()          
        self.rct.center = xy
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr:Screen):
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): 
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)
    
    def attack(self):
        return Shot(self)
    
            
class Bomb:
    def __init__(self,color,size,speed,scr:Screen):
        self.sfc = pg.Surface((2*size,2*size))
        self.sfc.set_colorkey((0,0,0)) 
        pg.draw.circle(self.sfc, color, (size,size), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = speed
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self,scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Shot:
    def __init__(self,chr:Bird):
        self.sfc = pg.image.load("ex05/fig/beam.png") #ビームの画像を読み込む
        self.sfc = pg.transform.rotozoom(self.sfc,0,0.3) #拡大
        self.rct = self.sfc.get_rect() 
        self.rct.center = chr.rct.center #こうかとんの真ん中にビームを表示
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) #スクリーンに貼り付ける
    
    def update(self,scr:Screen):
        self.rct.move_ip(+10, 0)
        self.blit(scr)
        if check_bound(self.rct, scr.rct) != (1,1): #壁にぶつかったらビームを削除
            del self


class TimeCount:
    def __init__(self):
        self.font = pg.font.Font(None,25)
        self.start_time = time.time() #プログラムの開始時間を測定
    
    def s_count(self):
        self.elapsed_time = int(time.time()-self.start_time) #プログラムの終了時間を取得
        self.e_hour = self.elapsed_time // 3600 #取得した時間からhourを計算
        self.e_minute = (self.elapsed_time % 3600) // 60 #取得した時間からminuteを計算
        self.e_second = (self.elapsed_time % 3600 % 60) #取得した時間からsecondを計算
    
    def print(self,scr:Screen):
        self.text = (str(self.e_hour).zfill(2)+":"
                            +str(self.e_minute).zfill(2)+":"
                            +str(self.e_second).zfill(2)) #0:0:0の形で時間を表示
        tkm.showinfo("残念！",f"また挑戦しよう！ 経過時間{self.text}") #ウインドウで表示

        
def main():
    clock = pg.time.Clock()
    time = TimeCount()
    scr = Screen("逃げろ！こうかとん",(1600,900),"ex03/fig/pg_bg.jpg")
    bird = Bird("ex03/fig/6.png",2.0,(900,400))
    bomb = Bomb((255,0,0),10,(+1,+1),scr)
    beams = None

    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                beams = bird.attack()
                
        bird.update(scr)
        bomb.update(scr)
        if beams:
              beams.update(scr)
    
        if bird.rct.colliderect(bomb.rct):
            time.s_count()
            time.print(scr)
            return 

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()