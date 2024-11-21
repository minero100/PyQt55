from pygame import * #importa todos los modulos de Pygame
' ' 'Required classes' ' '#Un comentario que indica que las vclases necesarias vienen a continuacion 

#parent class for sprites 
class GameSprite(sprite.Sprite): # Define una clase que hereda de `sprite.Sprite`, lo que significa que los objetos de esta clase serán sprites.
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):#Constructor que recibe la imagen, posición inicial y velocidad del sprite.
        super().__init__()#Llama al constructor de la clase padre `sprite.Sprite`.
 
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (55, 55))# Carga la imagen del sprite y la redimensiona a 55x55 píxeles.
        self.speed = player_speed# Almacena la velocidad del sprite.

 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()#Crea un rectángulo (`rect`) basado en la imagen y asigna sus posiciones `x` e `y`.
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):#Método que dibuja el sprite en la pantalla en su posición actual.
        window.blit(self.image, (self.rect.x, self.rect.y))

#heir class for the player sprite (controlled by arrows)
class Player(GameSprite):#Define una subclase de `GameSprite` para el jugador controlado por el usuario.
    def update(self):#Metodo que actualiza la posicion del jugador segun las teclas presionadas
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#heir class for the enemy sprite (moves by itself)
class Enemy(GameSprite):# define una clase de game sprite para el enemigo que se mueve de izquierda a derecha 
    side = "left"#Variable que controla hacia que lado se mueve el enemigo
    def update(self):#mueve al enemigo a la derecha o izquierda dependiendo su posicion actual
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#clase para los objetos de obstáculos
class Wall(sprite.Sprite): #Define clase  para los obstaculos 
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):#constructor que recibe el color posicion  y tamano de muro
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        #imagen de pared - un rectángulo del tamaño y color requerido
        self.image = Surface([self.width, self.height])#crea una superficie con el tamano de la pared
        self.image.fill((color_1, color_2, color_3))#rellena la superficie con el color especificado
 
        #cada objeto debe almacenar el rect - la propiedad rectangular
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):# Método que dibuja el muro en la pantalla.
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

#Escena del juego:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))# fondo de oantalla de juego
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Personajes del juego:
packman = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()#detecta  cuando ganas o pierdes
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

#música
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:#Controla los eventos del juego (como cerrar la ventana).
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:#te da un pantallaso de si ganaste  o perdiste 
        window.blit(background,(0, 0))
        packman.update()
        monster.update()
        
        packman.reset()
        monster.reset()
        final.reset() 

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        #Juego perdido
        if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2)or sprite.collide_rect(packman, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        #Juego ganado
        if sprite.collide_rect(packman, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)
    #Este código crea un pequeño laberinto donde el jugador debe evitar al enemigo y a las paredes para alcanzar el tesoro.




