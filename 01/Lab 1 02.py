import turtle as t

def triangle(size):
    if size >=32:
        for _ in range(3):
            t.lt(60)
            triangle(size/2)
            t.fd(size)
            t.rt(180)

t.speed(1000)
t.teleport(-128,-64)
t.setheading(0)
triangle(256)
t.mainloop()