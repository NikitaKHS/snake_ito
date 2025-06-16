from tkinter import *
import random
import os

SEG_SIZE = 20
WIDTH = 600
HEIGHT = 400
IMG_PATH = os.path.join(os.path.dirname(__file__), 'qsfp_texture.png')

class CableSegment:
    def __init__(self, x, y):
        self.instance = c.create_rectangle(
            x, y, x + SEG_SIZE, y + SEG_SIZE,
            fill='turquoise', outline=''
        )

class HeadSegment:
    def __init__(self, x, y):
        self.oval = c.create_oval(
            x, y, x + SEG_SIZE, y + SEG_SIZE,
            fill='white', outline='black'
        )
        self.instance = self.oval
        cx, cy = x + SEG_SIZE/2, y + SEG_SIZE/2
        self.text = c.create_text(
            cx, cy, text='ito', font=('Arial', int(SEG_SIZE/2), 'bold')
        )

    def coords(self, x1, y1, x2, y2):
        c.coords(self.oval, x1, y1, x2, y2)
        cx, cy = (x1 + x2)/2, (y1 + y2)/2
        c.coords(self.text, cx, cy)

class Food:
    def __init__(self, image):
        self.image = image
        self.id = None
        self.reposition()

    def reposition(self):
        if self.id:
            c.delete(self.id)
        x = random.randint(0, WIDTH // SEG_SIZE - 1) * SEG_SIZE
        y = random.randint(0, HEIGHT // SEG_SIZE - 1) * SEG_SIZE
        self.id = c.create_image(
            x + SEG_SIZE/2, y + SEG_SIZE/2, image=self.image
        )

    def coords(self):
        return c.coords(self.id)

class Snake:
    def __init__(self, segments):
        self.segments = segments
        self.mapping = {
            'Down': (0, 1), 'Up': (0, -1),
            'Left': (-1, 0), 'Right': (1, 0)
        }
        self.vector = self.mapping['Right']

    def move(self):
        for i in range(len(self.segments) - 1):
            seg = self.segments[i].instance
            x1, y1, x2, y2 = c.coords(self.segments[i+1].instance)
            c.coords(seg, x1, y1, x2, y2)

        head = self.segments[-1]
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        dx, dy = self.vector[0] * SEG_SIZE, self.vector[1] * SEG_SIZE
        head.coords(x1 + dx, y1 + dy, x2 + dx, y2 + dy)

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def add_segment(self):
        x1, y1, x2, y2 = c.coords(self.segments[0].instance)
        self.segments.insert(0, CableSegment(x1, y1))

    def head_center(self):
        x1, y1, x2, y2 = c.coords(self.segments[-1].oval)
        return (x1 + x2)/2, (y1 + y2)/2

def main():
    global c, qsfp_img, score, score_text, snake, food, restart_btn

    root = Tk()
    root.title('Змейка ИТО')

    c = Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
    c.pack()

    raw = PhotoImage(file=IMG_PATH)
    fx = max(1, raw.width() // SEG_SIZE)
    fy = max(1, raw.height() // SEG_SIZE)
    qsfp_img = raw.subsample(fx, fy)

    def init_game():
        global score, score_text, snake, food, restart_btn
        c.delete('all')
        score = 0
        score_text = c.create_text(
            WIDTH-10, 10, anchor='ne',
            text=f'SCORE: {score}',
            font=('Courier', 16, 'bold'),
            fill='lime'
        )
        segments = [CableSegment(SEG_SIZE*i, SEG_SIZE) for i in range(2)]
        segments.append(HeadSegment(SEG_SIZE*2, SEG_SIZE))
        snake = Snake(segments)
        food = Food(qsfp_img)
        restart_btn = None

    def restart_game():
        init_game()
        game_loop()

    def game_loop():
        global score, restart_btn
        snake.move()

        hx, hy = snake.head_center()
        # проверка врезания в стену
        if hx < 0 or hy < 0 or hx > WIDTH or hy > HEIGHT:
            c.create_text(
                WIDTH/2, HEIGHT/2-10,
                text='Game Over',
                font=('Courier', 24, 'bold'),
                fill='red'
            )
            c.create_text(
                WIDTH/2, HEIGHT/2+20,
                text='ИТО Нуждался в тебе',
                font=('Courier', 14),
                fill='white'
            )
            if not restart_btn:
                restart_btn = Button(
                    root, text='Попробовать ещё раз',
                    font=('Arial', 12),
                    command=restart_game
                )
                c.create_window(
                    WIDTH/2, HEIGHT/2+60,
                    window=restart_btn
                )
            return  # останавливаем цикл

        fx, fy = food.coords()
        if abs(hx - fx) < 1 and abs(hy - fy) < 1:
            snake.add_segment()
            food.reposition()
            score += 1
            c.itemconfigure(score_text, text=f'SCORE: {score}')

        root.after(150, game_loop)

    # управление
    root.bind_all('<KeyPress-Up>', lambda e: snake.change_direction(e))
    root.bind_all('<KeyPress-Down>', lambda e: snake.change_direction(e))
    root.bind_all('<KeyPress-Left>', lambda e: snake.change_direction(e))
    root.bind_all('<KeyPress-Right>', lambda e: snake.change_direction(e))

    init_game()
    game_loop()
    root.mainloop()

if __name__ == '__main__':
    main()
