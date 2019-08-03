import turtle
wns = turtle.Screen()
thy = turtle. Turtle()
def vong_cung_phai(conso):
    for i in range(conso):
        thy.right(1)
        thy.forward(1)
def vong_cung_trai(conso):
    for i in range(conso):
        thy.right(1)
        thy.forward(-1)
vong_cung_phai(90)
vong_cung_trai(180)

wns.exitonclick()
