from ast import keyword
import pgzrun
WIDTH=500
HEIGHT=400
p=Actor('ironman',(200,200))

def draw():
    screen.fill('black')
    p.draw()

def update():
    if keyboard.left:
        p.x-=2
    elif keyboard.right:
        p.x+=2
    elif keyboard.up:
        p.y-=2
    elif keyboard.down:
        p.y+=2
pgzrun.go()

pgzrun.go()