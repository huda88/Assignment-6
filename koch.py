import turtle
##
##turtle.speed(0)
##def koch(step):
##    if step < 30:
##        turtle.fd(step)
##        return
##    koch(step/3)
##    turtle.lt(60)
##    koch(step/3)
##    turtle.rt(120)
##    koch(step/3)
##    turtle.lt(60)
##    koch(step/3)

turtle.speed(0)

def kochs(step):
    if step < 30:
        turtle.fd(step)
        return
    kochs(step/3)
    turtle.lt(90) #change the angle
    kochs(step/3)
    turtle.rt(90)
    kochs(step/3)
    turtle.rt(90)
    kochs(step/3)
    turtle.lt(90)
    kochs(step/3)
    

kochs(300)
