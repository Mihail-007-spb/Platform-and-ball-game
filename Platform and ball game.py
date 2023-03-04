"""Platform and ball game.
The image and sound files are located in the repository by
name 'Image-and-sound-for-the-published-repositories'"""


"""Игра платформа и шарик.
Файлы изображения и звука находятся в repository по имени
 'Image-and-sound-for-the-published-repositories'"""



from tkinter import *
import random
from tkinter import messagebox
import time
from PIL import ImageTk, Image
import winsound
import threading
#import os
#from multiprocessing import Pool
from multiprocessing import Process


def pause_igra(event):
    paddle.started = False
    canvas.itemconfig(pause_mon, state='hidden')
    canvas.itemconfig(pause, state='normal')
    print('Пауза')

def start_igra(event):
    paddle.started = True
    canvas.itemconfig(pause, state='hidden')


def musika_kasan_padle_m():
    p = Process(target=musika_kasan_padle)
    p.daemon = True
    p.start()

def musika_kasan_woll_m():
    w = Process(target=musika_kasan_woll)
    w.daemon = True
    w.start()

def musika_end_m():
    e = Process(target=musika_end)
    e.daemon = True
    e.start()


def musika_kasan_padle_p():
    thr_p = threading.Thread(target=musika_kasan_padle).start()
def musika_kasan_padle():
    winsound.PlaySound(r"C:\\FOTO  Python\\padle.wav",
                       winsound.SND_FILENAME)


def musika_kasan_woll_p():
    thr_w = threading.Thread(target=musika_kasan_woll).start()
def musika_kasan_woll():
    winsound.PlaySound(r"C:\\FOTO  Python\\woll.wav",
                       winsound.SND_FILENAME)


def musika_end_p():
    thr_e = threading.Thread(target=musika_end).start()
def musika_end():
    winsound.PlaySound(r"C:\\FOTO  Python\\end-of-game.wav",
                       winsound.SND_FILENAME)



def menu_exit():
    choice = messagebox.askyesno("Выход из игры",
                                 "Новая ИГРА?")
    if choice == True:
        print('Новая')
        new_1(event=tk)

    elif choice == False:
        print('Выход')
        tk.destroy()


z = 0


def new_1(event):
    global paddle, ball, c_iz

    c_iz = 0

    ball = Ball(canvas, paddle, score, 'red')

    while not ball.hit_bottom:

        if paddle.started == True:

            canvas.itemconfig(start, state='hidden')
            canvas.itemconfig(pause_mon, state='normal')

            ball.draw()
            paddle.draw()
            #  что нужно, закончило рисоваться
        tk.update_idletasks()
        # что должно было быть сделано — было сделано
        tk.update()
        # элементов выглядело плавно
        time.sleep(0.01)
    else:
        menu_exit()


class Ball:

    global paddle, score, ball

    def __init__(self, canvas, paddle, score, color):

        self.canvas = canvas
        self.paddle = paddle
        self.score = score

        self.id = canvas.create_oval(10, 10, 70, 70, fill=color, width=3)
        # помещаем шарик в точку с координатами 245,100
        self.canvas.move(self.id, 245, 100)
        # задаём список возможных направлений для старта
        starts = [-2, -1, 1, 2]
        # перемешиваем его
        random.shuffle(starts)
        # выбираем первый из перемешанного — это будет вектор движения шарика
        self.x = starts[0]
        # в самом начале он всегда падает вниз, поэтому уменьшаем
        # значение по оси y
        self.y = -2
        # шарик узнаёт свою высоту и ширину
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # свойство, которое отвечает за то, достиг шарик дна или нет.
        # Пока не достиг, значение будет False
        self.hit_bottom = False

    # обрабатываем касание платформы, для этого получаем 4 координаты шарика
    # в переменной pos (левая верхняя и правая нижняя точки)

    global t, a, a1, z
    t = time.localtime()
    a = time.time()
    a1 = int(a)

    """ДВИЖЕНИЕ ПЛАТФОРМЫ"""
    def hit_paddle(self, pos):
        global z, c_iz, a1, b1, f
        b = time.time()
        b1 = int(b)
        c_iz = (b1 - a1)
        # получаем кординаты платформы через объект paddle (платформа)
        paddle_pos = self.canvas.coords(self.paddle.id)
        # если координаты касания совпадают с координатами платформы
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                z = z + 1
                #musika_kasan_padle_p()
                musika_kasan_padle_m()
                canvas.delete("score")
                canvas.create_text(80, 30, text="Счет: {}".format(z),
                                   font="Times 20",
                                   fill="white", tag="score")
                # увеличиваем счёт (обработчик этого события будет описан ниже)
                self.score.hit()
                print('Это время=' + str(c_iz))
                print('Это z=' + str(z))

                # возвращаем метку о том, что мы успешно коснулись
                return True

            elif z == 3 and pos[1] == 10:
                canvas.coords('padle', 330, 500, 410, 530)

            elif z == 6 and pos[1] == 10:
                canvas.coords('padle', 330, 500, 390, 530)

            elif z == 9 and pos[1] == 10:
                canvas.coords('padle', 330, 500, 370, 530)

        # возвращаем False — касания не было
        return False

    """ДВИЖЕНИЕ ШАРИКА"""

    def draw(self):

        # передвигаем шарик на заданный вектор x и y
        self.canvas.move(self.id, self.x, self.y)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)
        # если шарик падает сверху

        """КАСАНИЕ ВЕРХА"""
        if pos[1] <= 0:
            #musika_kasan_woll_p()

            #многопроцессорность
            musika_kasan_woll_m()

            self.y = 2

        # """ЗАВЕРШЕНИЕ ЦИКЛА"""
        # если шарик правым нижним углом коснулся дна
        elif pos[1] >= self.canvas_height + 10:

            """КОНЕЦ ЦИКЛА"""
            #musika_end_p()
            musika_end_m()
            canvas.coords('padle', 330, 500, 480, 530)
            canvas.delete("score")
            global z
            z = 0
            self.hit_bottom = True

        #"""УСКОРЕНИЕ ШАРИКА"""
        # если было касание платформы
        elif self.hit_paddle(pos) == True and z < 3:
            self.y = -4
            print("Ускорение шарика =" + str(self.y))

        elif self.hit_paddle(pos) == True and 3 <= z <= 12:
            self.y = -8
            print("Ускорение шарика =" + str(self.y))

        elif self.hit_paddle(pos) == True and z > 12:
            self.y = -12
            print("Ускорение шарика =" + str(self.y))

        # если коснулись левой стенки
        elif pos[0] <= 0:
            # движемся вправо
            self.x = 2
            #musika_kasan_woll_p()
            musika_kasan_woll_m()
        # если коснулись правой стенки
        elif pos[2] >= self.canvas_width:
            # движемся влево
            self.x = -2
            #musika_kasan_woll_p()
            musika_kasan_woll_m()


class Paddle:
    # конструктор
    def __init__(self, canvas, color, state):

        self.state = state
        self.canvas = canvas

        self.id = canvas.create_rectangle(0, 0, 150, 30, fill=color, width=2,
                                          tag="padle")
        # задаём список возможных стартовых положений платформы
        start_1 = [330, 300, 350]
        # перемешиваем их
        random.shuffle(start_1)
        # выбираем первое из перемешанных
        self.starting_point_x = start_1[0]
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.id, self.starting_point_x, 500)
        # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.x = 0
        # платформа узнаёт свою ширину
        self.canvas_width = self.canvas.winfo_width()
        # задаём обработчик нажатий
        # если нажата стрелка вправо — выполняется метод turn_right()
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        # если стрелка влево — turn_left()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # пока платформа не двигается, поэтому ждём
        self.started = False
        # как только игрок нажмёт Enter — всё стартует
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    # движемся вправо
    def turn_right(self, event):
        # будем смещаться правее на 2 пикселя по оси х
        self.x = 2

    # движемся влево
    def turn_left(self, event):
        # будем смещаться левее на 2 пикселя по оси х
        self.x = -2

    # игра начинается
    def start_game(self, event):
        # меняем значение переменной, которая отвечает
        # за старт движения платформы
        self.started = True

    # метод, который отвечает за движение платформы
    def draw(self):
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.id, self.x, 0)
        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если мы упёрлись в левую границу
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
        # если упёрлись в правую границу
        elif pos[2] >= self.canvas_width:
            # останавливаемся
            self.x = 0


#  Описываем класс Score, который отвечает за отображение счетов
class Score:
    global score  # конструктор

    def __init__(self, canvas, color):
        # в самом начале счёт равен нулю

        self.score = 0
        # будем использовать наш холст
        self.canvas = canvas
        # создаём надпись, которая показывает текущий счёт,
        # делаем его нужно цвета и запоминаем внутреннее имя этой надписи
        self.id = canvas.create_text(750, 25, text=self.score,
                                     font=('Times', 30), fill=color,
                                     stat='hidden')

    # обрабатываем касание платформы
    def hit(self):
        # увеличиваем счёт на единицу
        self.score += 1
        # пишем новое значение счёта
        self.canvas.itemconfig(self.id, text=self.score)

if __name__ == '__main__':
    tk = Tk()
    tk.geometry('+400+50')
    s = ' '
    # делаем заголовок окна — Games с помощью свойства объекта title
    tk.title(s * 80 + '''ИГРА "ШАРИК И ПЛАТФОРМА"''')
    tk.iconbitmap(default="C:\\FOTO  Python\\mbug48.ico")
# запрещаем менять размеры окна, для этого используем свойство resizable
    tk.resizable(0, 0)
# чтобы другие окна не могли его заслонить
    tk.wm_attributes('-topmost', 1)

    canvas = Canvas(tk, width=800, height=600, highlightthickness=0, bg="#252c58")
    canvas.grid()

    foto1 = ImageTk.PhotoImage(file=r"C:\\FOTO  Python\\3858_original.jpg")
    canvas.create_image(0, 0, image=foto1, anchor=NW)

    canvas.grid()

    canvas.focus_set()

    tk.update()

    start = canvas.create_text(400, 300,
                      text = " Для начала игры\n нажмите ENTER",
                               font='Times 20', fill='white', state='normal')

    pause_mon = canvas.create_text(400, 20,
                      text = "Для ПАУЗЫ нажмите ПРОБЕЛ",
                               font='Times 12', fill='white', state='hidden')

    st = ' '
    pause = canvas.create_text(400, 300,
                      text = st*8+"ПАУЗА!!!\n для продолжения\n"
                                  " нажмите клавишу <w>\n"
                                  "(английская раскладка)",
                               font='Times 30', fill='white', state='hidden')

    canvas.bind('<space>', pause_igra)
    canvas.bind('<w>', start_igra)

    score = Score(canvas, '#c9c9c9')

    paddle = Paddle(canvas, 'yellow', state='normal')

    ball = Ball(canvas, paddle, score, 'red')

    while not ball.hit_bottom:

        if paddle.started == True:

            canvas.itemconfig(start, state='hidden')
            canvas.itemconfig(pause_mon, state='normal')

            ball.draw()
            paddle.draw()

        tk.update_idletasks()

        tk.update()

        time.sleep(0.01)
    else:
        menu_exit()