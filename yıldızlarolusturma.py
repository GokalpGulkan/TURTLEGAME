import turtle,random

pencere=turtle.Screen()
pencere.bgcolor("black")
pencere.title("Yıldızlar")
pencere.setup(700,700)


def star():
    yıldız.begin_fill()
    boyut=random.randint(10,100)
    for i in range(5):
        yıldız.forward(boyut)
        yıldız.right(144)
    yıldız.end_fill()



yıldız=turtle.Turtle()
yıldız.speed(0)
colors=["red","green","blue","yellow","white","orange","purple","pink","cyan","line"]

for i in range(10):
    x=random.randint(-300,300)
    y=random.randint(-250,250)
    yıldız.penup()
    yıldız.setposition(x,y)
    yıldız.color(random_renk)


    star()



turtle.mainloop()