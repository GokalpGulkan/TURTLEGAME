import turtle,random,time



def puan(x,y):
    global p
    p +=1
   
    ok.goto(random.randint(-300,300),random.randint(-300,300))


pencere=turtle.Screen()
pencere.title("Fare Oyunu")
pencere.bgcolor("lightgreen")
pencere.setup(width=600,height=600)

ok=turtle.Turtle()
ok.speed(0)
ok.shape("circle")
ok.color("red")
ok.shapesize(3)
ok.penup()
ok.goto(random.randint(-300,300),random.randint(-300,300))



p=0
yaz=turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.goto(0,260)
yaz.hideturtle()
yaz.write("Başla",align="center",font=("Courier",24,"normal"))


sure=5



while True:
    baslangic_suresi=time.time()
    while(time.time()-baslangic_suresi)<sure:

        ok.onclick(puan)
    else:
        yaz.clear()
        yaz.write("Puan {}".format(p),align="center",font=("Courier",24,"normal"))
        time.sleep(2)
        p=0
        yaz.clear()
        yaz.write("Başla",align="center",font=("Courier",24,"normal"))