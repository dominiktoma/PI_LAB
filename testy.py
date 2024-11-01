import turtle
t = turtle.Turtle()
t.speed(3) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# n - złożoność
# l - długość linii początkowej
def rek(n, l):
  if n < 1:
    return

  for i in range(3):
    t.forward(l)
    t.right(60)
    t.forward(l)
    t.right(60)
    rek(n-1, l/2)

t.left(90)
rek(4, 100)