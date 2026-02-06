import turtle

# Setup layar
screen = turtle.Screen()
screen.title("Bendera Indonesia")
screen.bgcolor("white")

# Buat turtle
t = turtle.Turtle()
t.speed(3)
t.hideturtle()

# Fungsi menggambar persegi panjang
def draw_rectangle(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Posisi awal
t.penup()
t.goto(-200, 0)
t.pendown()

# Gambar warna merah (atas)
draw_rectangle("red", 400, 100)

# Turun ke bawah untuk warna putih
t.penup()
t.goto(-200, 100)
t.pendown()

# Gambar warna putih (bawah)
draw_rectangle("white", 400, 100)

# Selesai
turtle.done()