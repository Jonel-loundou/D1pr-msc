import turtle 

### Task2.1
ecran = turtle.Screen()
toto = turtle.Turtle()

toto.forward(100)    # Avance de 100 pixels
toto.right(90)       # Tourne à droite de 90 degrés
toto.forward(100)    
toto.right(90)       
toto.forward(100)    
toto.right(90)       
toto.forward(100)

ecran.exitonclick()  # Ferme la fenêtre lorsque l'on clique dessus

### Task2.2
toto = turtle.Screen()
toto.bgcolor("black")  # Change le fond de la fenetre en noir
titi = turtle.Turtle()
titi.color("red")      # Change la couleur du crayon en rouge
for i in range(3):
    titi.right(90)     # Tourne à droite de 90 degrés
    titi.circle(42)    # Trace un cercle de rayon 42 pixels
toto.exitonclick()

### Task2.3
def draw_polygon(sides): 
    screen = turtle.Screen() 
    toto = turtle.Turtle()

    for _ in range(sides):
        toto.forward(100)
        toto.right(360 / sides)
    screen.exitonclick()
draw_polygon(3) 
### Task2.4
def draw_spiral():
    screen = turtle.Screen()
    toto = turtle.Turtle() 
     
    for i in range(100):
        toto.forward(i * 5) # avance de 5 pixels à chaque itération
        toto.right(20)      
    
draw_spiral()