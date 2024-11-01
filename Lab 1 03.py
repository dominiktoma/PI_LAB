import turtle as t

def triangle(size):
    if size >=32:
        for _ in range(3):
            t.lt(60)
            t.fd(size/4)
            triangle(size/2)
            t.fd((size/4)*3)
            t.rt(180)

t.speed(100)
t.teleport(-128,-64)
t.setheading(0)
triangle(256)
t.mainloop()