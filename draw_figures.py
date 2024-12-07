
import turtle
import figures  

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

figures.draw_square(100)

pen.penup()
pen.goto(300, 200)
pen.pendown()
figures.draw_triangle(100)

pen.penup()
pen.goto(200, 100)
pen.pendown()
figures.draw_rectangle(150, 80)

pen.penup()
pen.goto(-200, -150)
pen.pendown()
figures.draw_square(100)

pen.penup()
pen.goto(200, -150)
pen.pendown()
figures.draw_triangle(100)

pen.penup()
pen.goto(0, -200)
pen.pendown()
figures.draw_rectangle(150, 80)

pen.hideturtle()
window.mainloop()
