from tkinter import*
from math import sqrt
class var:
    window = Tk()
    canvas = Canvas(window, height=500, width=500, bg='white')
    levels = [[['i', 'f'], ['s', 'i']], [['t', 'a', 'n'], ['p', 'i', 'o'], ['x', 'r', 't']], [['t', 'a', 'n', 'f'], ['p', 'i', 'o', 'h'], ['x', 'r', 't', 'k'], ['o', 'p', 'u', 'i']]]
    points = [[[1, 1,
                0, 0], [0, 0,
                        1, 1]], [[1, 1, 1,
                                  0, 0, 0,
                                  0, 0, 0], [0, 0, 1,
                                             0, 0, 1,
                                             0, 0, 1], [0, 1, 0,
                                                        0, 1, 0,
                                                        0, 1, 0]]]
    soposed = [4, 9]
    ps = 0
    level = -1
    letters = [canvas.create_text(250, 250, text='start', fill='black', font=('Helvetica',60))]
    letters_x = []
    letters_y = []
    score = 0
var.canvas.pack()
def res():
    var.letters = []
    var.level += 1
    var.window.destroy()
    var.window = Tk()
    x = (len(var.levels[var.level][0]) * 50) + 50
    y = (len(var.levels[var.level]) * 50) + 50
    lenght = len(var.levels[var.level][0])
    var.canvas = Canvas(var.window, height=y, width=x + 80, bg='white')
    var.canvas.pack()
    sc = var.canvas.create_text(40, y/2, text=str(var.score), fill='black', font=('Helvetica',60))
    plus = 25
    y = plus
    count = 0
    for i in var.levels[var.level]:
        x = plus
        y += plus * 2
        for j in i:
            x += plus * 2
            var.letters.append(var.canvas.create_text((x - 25)+80, y - 25, text=j,
                                fill='black', font=('Helvetica',60)))
        count += 1
    var.canvas.bind_all('<Button-1>', click)
def distance(x1, y1, x2, y2):
    x1, y1, x2, y2 = (int(x1), int(y1), int(x2), int(y2))
    return sqrt(abs(x1-x2)^2+abs(y1-y2)^2)
def positions(Id):
    return var.canvas.coords(Id)
def find(s, l):
    ret = 0
    for i in l:
        if i == s:
            break
        ret+=1
    return ret
def click(pos):
    if len(var.letters) == 1:
        res()
    else:
        a=[]
        for i in var.letters:
            a.append(distance(positions(i)[0], positions(i)[1], pos.x, pos.y))
        var.ps+=sum(var.points[var.level][find(max(a), a)])
        if var.ps == var.soposed[var.level]:
            res()
    print(var.ps)
var.canvas.bind_all('<Button-1>', click)
