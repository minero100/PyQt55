from pygame import *
from random import randint 
#cargando de fuent6e por separado
font.init()
font1 = font.Font(None, 80)
win = font1.render('¡GANASTE!', True,(255, 255, 255))
lose = font1.render('¡PENDEJO!', True(180, 0, 0))

font2 = font.Font(None, 36)

#musica de fondo
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

#necesitamos las siguientes imagenes 
img_back = "galaxy.jpg"#fomdo de juego
img_bullet = 'bullet.png' #bala
img_hero = 'rocket'#heroe
img_enemy = 'ufo.png'#enemigo
score = 0#naves destruidas
goal = 10#La cxantoidad de naves que necesitan ser destruidas para ganar
lost = 0 #naves falladas
max_lost = 3 #se pierde si se falla tantas veces
#clasee padre para objetos
class GameSprite(sprite.sprite):
#constriuctor de la clases
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #llamada para el constructor de la clase(Sprite)
        sprite.Sprite.__init__(self)


        #cada onbjeto debe almaacenar lka prpiedad image
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed

        #cada objeto debe tener la propiedad rect representta el rectrangulo en ell que se encuentra 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #metodo de dibujo del personaje en la ventana 
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


#Clase del jugadoe principal
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x  > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
  #Metodo para "disparar"(use la posicion del jugadoe para crear una bala ahi)
    def fire(self)
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


#clase edel objeto enemigo
class Enemy(GameSprite):
    #movimiento del enemigo
    def update(self):
        self.rect.y += self.speed
        global lost
        #desaparece al llegar al borde de la pantalla
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width -80)
            self.rect.y = 0
            lost = lost + 1        


#clase del objeto bala 
class bullet(GameSprite):    
#movimiento de el enemigo   
    def update(self):
        self.rect.y += self.speed
        #desaparece al tocar el borde de la pantalla
        if self.rect.y < 0:
            self.kill()

#Crar una ventana pequena
win_width = 700    
win_height = 500
display.set_caption('Tirador')  
window = display.set_mode((win_width,win_height))  
background = transform.scale(image.load(img_back),(win_width,win_height))
#crear objetos
ship = Player(img_hero, 5, win_height - 100, 80, 100,10 )
#Creando un grupo de objetosenemigos
monsters = sprite.Group()
for i in range(1, 6):
    monsters = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
bullets = sprite.Group()
#La varible""juego terminado":cuando sea True, los objetos dejan de funcionar en el ciclo principal
finish = False
#ciclo de juego principal:
run = True #La bandera es reiniciada con el boton de cerrar ventana 
while run:
    #evento de pulsacion del boton cerrar 
    for e in event.get():
        if e.type == QUIT:
            run = False

        # evento de pulsacion de barra espaciadora - objeto que dispara 
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
#el juego:accion de los objetos, comprobar las reglas del juego, volviendo a dibujor 
    if not finish:
        #actualiza el fondo
        window.blit(background,(0,0))


    #ejecutar los movimientos del objeto
    ship.update()
    monsters.update()
    bullets.update()

    #los actualiza en una nueva ubicacion con cada iteracion del ciclo

    ship.reset():
    monsters.draw(window)
    bullets.draw(window)
       #com[prueba una colision entre una bala  y loos mouunstris(tanto los mounstros como la baala desaparecden al; tocarse
    collides = sprite.groupcollide(monsters, bullets, True, True)
    for c in collides:
        # este ciclo se repite tantas veces coomo se golpee a los enemigos(kjs)
        score = score +1
        monster = Enemy(img_enemy, randint(80, win_width - 80,), -40, -80 ,-50 randint(1,5))
        monsters.add(monster)   

    if sprite.spritecollide(ship, monsters, False) or lost <= max_lost:
        finish = True
        window.blit(win,(200,200))


#Se escribe texto en la oanytalla 
text = fond2.render("Puntaje:" + str(score), 1, (255,255,255))
window.blit(tect,(10,20))

text_lose = font2.render("Fallados:" + str(lost), 1, (255,255,255))
window.blit(text_lose,(10,50))


display.update()
#extra: reinicio automatico del juego 
else:
    finish = False
    score = 0
    lost = 0
    for b in bullets:
        b.kill()
    for m in monsters:    
        m.kill()


time.delay(3000)
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width  - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)


time.delay(50)







               
