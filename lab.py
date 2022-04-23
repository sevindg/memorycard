# Разработай свою игру в этом фаf
from pygame import*
win_width = 700
win_height = 700
class Pic(sprite.Sprite):
    def __init__(self,picture,x,y,w,h,): 
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y   
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
 
class Player(Pic):
    def __init__(self,picture,x,y,w,h,x_speed, y_speed):
        Pic.__init__(self,picture,x,y,w,h)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if player.rect.x <= win_width-80 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        # если зашли за стенку, то встанем вплотную к стене
            platforms_touched = sprite.spritecollide(self, zabors, False)
            if self.x_speed > 0: # идем направо, правый край персонажа - вплотную к левому краю стены
                for p in platforms_touched:
                    self.rect.right = min(self.rect.right, p.rect.left) # если коснулись сразу нескольких, то правый край - минимальный из возможных
            elif self.x_speed < 0: # идем налево, ставим левый край персонажа вплотную к правому краю стены
                for p in platforms_touched:
                    self.rect.left = max(self.rect.left, p.rect.right) # если коснулись нескольких стен, то левый край - максимальный
        if player.rect.y <= win_height-80 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        # если зашли за стенку, то встанем вплотную к стене
            platforms_touched = sprite.spritecollide(self, zabors, False)
            if self.y_speed > 0: # идем вниз
                for p in platforms_touched:
                    self.y_speed = 0
                    # Проверяем, какая из платформ снизу самая высокая, выравниваемся по ней, запоминаем её как свою опору:
                    if p.rect.top < self.rect.bottom:
                        self.rect.bottom = p.rect.top
            elif self.y_speed < 0: # идем вверх
                for p in platforms_touched:
                    self.y_speed = 0  # при столкновении со стеной вертикальная скорость гасится
                    self.rect.top = max(self.rect.top, p.rect.bottom) # выравниваем верхний край по нижним краям стенок, на которые наехали

    def fire(self):
        axe = Bullet('bullet.png', self.rect.right, self.rect.centery, 15, 20, 15)
        axes.add(axe)
 
                
class Enemy(Pic):
    direction = 'left'
    def __init__(self,picture,x,y,w,h,speed):
        Pic.__init__(self,picture,x,y,w,h)
        self.speed = speed
    def update(self):
 
        if self.rect.x <= 0:
            self.direction = "right"
        if self.rect.x >= 650:
            self.direction = 'left'
        
        if self.direction =="left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Bullet(Pic) :
    def __init__(self,picture,w,h,x,y,speed):
        Pic.__init__(self,picture,w,h,x,y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >650 :
            self.kill()
 
axes = sprite.Group()
vrag = Enemy('enemy.png',300,590,60,60,20)
enemys = sprite.Group()
enemys.add(vrag)
player = Player('viking.png',40,30,60,60,0,0)
zaborh = Pic('zabot2.png',400,250,110,100,)
zaborh1 = Pic('zabot2.png',400,320,110,100)
zaborh2 = Pic('zabot2.png',400,390,110,100)
zaborh3 = Pic('zabot2.png',400,460,110,100)
zaborh5 = Pic('zabot2.png',400,180,110,100)
zaborh6 = Pic('zabot2.png',400,110,110,100)
zaborh7 = Pic('zabot2.png',400,40,110,100)
zaborh8 = Pic('zabot2.png',400,-20,110,100)
zaborw2 = Pic('zabot2.png',290,250,110,100)
zaborw3 = Pic('zabot2.png',180,250,110,100)
finish_sprite = Pic('house.png',550,50,100,100)
zaborw4 = Pic('zabot.png',50,460,100,100)
zaborw5 = Pic('zabot.png',0,460,100,100)
zabors = sprite.Group()
zabors.add(zaborh8)
zabors.add(zaborh7)
zabors.add(zaborh6)
zabors.add(zaborh5)
zabors.add(zaborh)
zabors.add(zaborh1)
zabors.add(zaborh2)
zabors.add(zaborh3)
zabors.add(zaborw2)
zabors.add(zaborw3)
zabors.add(zaborw4)
zabors.add(zaborw5)
window=display.set_mode((700,700))
display.set_caption('лабиринт')
game = True
Finish = False
while game:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                player.x_speed = -5
            elif  e.key == K_RIGHT:
                player.x_speed = 5
            elif e.key == K_UP:
                player.y_speed = -5
            elif e.key == K_DOWN:
               player.y_speed = 5
            elif e.key == K_SPACE:
               player.fire()
 
        elif e.type == KEYUP:
            if e.key == K_LEFT:
               player.x_speed = 0
            elif e.key == K_RIGHT:
               player.x_speed = 0
            elif e.key == K_UP:
               player.y_speed = 0
            elif e.key == K_DOWN:
               player.y_speed = 0
   
    if not Finish:
        window.fill((20,200,50)
        player.update()
        player.reset()
        finish_sprite.reset()
        axes.update()
        axes.draw(window)
        zabors.draw(window)
        if not(sprite.groupcollide(enemys, axes, True, True)):
            enemys.draw(window)
            enemys.update()
        sprite.groupcollide(axes,zabors, True, False)
        if sprite.collide_rect(player,finish_sprite):
            Finish= True
            img = image.load('win.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img,(700,700)),(0,0))
        if sprite.spritecollide(player,enemys,False):
            Finish = True
            umg = image.load('lose.png')
            window.fill((255,255,255))
            window.blit(transform.scale(umg,(700,700)),(0,0))
    display.update() 
