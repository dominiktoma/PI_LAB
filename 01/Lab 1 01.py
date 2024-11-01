import turtle as t

def print_line(size):
    if size >=20:
        size /=1.41 #w zaokrągleniu sqrt(2)
        t.fd(size)
        t.lt(90)
        for _ in range(2): print_line(size)
        t.lt(90)
        t.fd(size)
    
t.setheading(90)
t.speed(1000)
t.teleport(0,-220) 
print_line(300)
t.mainloop()