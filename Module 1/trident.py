import turtle

tt = turtle.Turtle()
tt.color('#E6D542' , '#F7E653')
tt.speed(5)

tt.begin_fill()
tt.pensize(5)
tt.forward(12.5)
tt.left(90)
tt.forward(300)
tt.right(45)
tt.forward(50)
tt.left(45)
tt.forward(100)
tt.left(45)
tt.forward(25)
tt.left(135)
tt.forward(110)
tt.right(45)
tt.forward(30)
tt.right(135)
tt.forward(150)
tt.left(45)
tt.forward(12.50)
tt.left(90)
tt.forward(12.50)
tt.left(45)
tt.forward(150)
tt.right(135)
tt.forward(30)
tt.right(45)
tt.forward(110)
tt.left(135)
tt.forward(25)
tt.left(45)
tt.forward(100)
tt.left(45)
tt.forward(50)
tt.right(45)
tt.forward(300)
tt.left(90)
tt.forward(12.5)
tt.end_fill()

#Create trident shadow

tt.up()
tt.forward(20)
tt.left(90)
tt.forward(15)
tt.right(90)
tt.down()

tt.color('black' , 'black')
tt.begin_fill()
tt.pensize(1)
tt.right(80)
tt.forward(12.5)
tt.left(90)
tt.forward(300)
tt.right(45)
tt.forward(50)
tt.left(45)
tt.forward(100)
tt.left(45)
tt.forward(25)
tt.left(135)
tt.forward(110)
tt.right(45)
tt.forward(30)
tt.right(135)
tt.forward(150)
tt.left(45)
tt.forward(12.50)
tt.left(90)
tt.forward(12.50)
tt.left(45)
tt.forward(150)
tt.right(135)
tt.forward(30)
tt.right(45)
tt.forward(110)
tt.left(135)
tt.forward(25)
tt.left(45)
tt.forward(100)
tt.left(45)
tt.forward(50)
tt.right(45)
tt.forward(300)
tt.left(90)
tt.forward(12.5)
tt.end_fill()

tt.ht()
tt.done()
