import turtle as t

t.color("black")
t.width(3)

for i in range(30):
    t.forward(i*10)
    t.right(90)

t.mainloop()