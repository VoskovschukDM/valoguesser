import tkinter.tix
from tkinter import *
from AllPhotos import AllPhotos


class Consts:
    screen_parameters = (1440, 648)


class Window:

    def application(self):
        if self.type == 0:
            self.answers.append((AllPhotos.map_num, self.target_xy[0], self.target_xy[1]))
            self.index = self.index + 1
            if self.index == len(AllPhotos.screens):
                self.apply_btn.configure(state='disable')
                self.set_ans(self.answers)
                self.chosen_text.insert(END, "file saved")
            else:
                self.screen_label.configure(image=AllPhotos.screens[self.index])
                self.chosen_text.insert(END, "next pic\n")

        if self.type == 1:
            if AllPhotos.map_num == self.answers[self.index][0]:
                dist = pow(pow(self.answers[self.index][1] - self.target_xy[0], 2) + pow(self.answers[self.index][2] - self.target_xy[1], 2), 0.5)
                print(dist)
                self.chosen_text.insert(END, str(int(dist)) + '\n')
            else:
                self.chosen_text.insert(END, "Wrong map\n")

            self.index = self.index + 1
            if self.index == len(self.answers):
                self.apply_btn.configure(state='disable')
            else:
                self.screen_label.configure(image=AllPhotos.screens[self.index])

    def back_click(self):
        AllPhotos.map_num = -1
        Window.map_label.configure(image=AllPhotos.map_choice)
        Window.map_label.bind("<Button-1>", self.map_choice)
        Window.back_btn.configure(state='disable')

    def click_handler(self, event):
        self.target_xy = (event.x, event.y)
        self.map_label.configure(image=AllPhotos.add_target(AllPhotos, event.x, event.y))
        print("clicked x,y = " + str(event.x) + ', ' + str(event.y))

    def map_choice(self, event):
        map_num = event.x // (Consts.screen_parameters[1] // 3) + (event.y // (Consts.screen_parameters[1] // 3) * 3)
        if map_num <= 7:
            AllPhotos.map_num = map_num
            self.map_label.configure(image=AllPhotos.maps[map_num])
            self.map_label.bind("<Button-1>", self.click_handler)
        Window.back_btn.configure(state='normal')

    def get_ans(self):
        answers = []
        with open("ans.gay", 'r') as f:
            tmp = f.readline()
            while tmp:
                cor = tmp.split()
                correct_x = int(cor[1]) * 18 * 18 + int(cor[2]) * 18 + int(cor[3])
                correct_y = int(cor[4]) * 18 * 18 + int(cor[5]) * 18 + int(cor[6])
                answers.append((int(cor[0]), correct_x, correct_y))
                tmp = f.readline()
        return answers

    def set_ans(self, answers):
        with open("ans.gay", 'w') as f:
            for i in answers:
                code = []
                code.append(i[0])
                code.append(i[1] // 18 // 18)
                code.append((i[1] - code[1] * 18 * 18) // 18)
                code.append(i[1] % 18)
                code.append(i[2] // 18 // 18)
                code.append((i[2] - code[4] * 18 * 18) // 18)
                code.append(i[2] % 18)
                f.write(str(code[0]) + ' ' + str(code[1]) + ' ' + str(code[2]) + ' ' + str(code[3]) + ' ' + str(
                    code[4]) + ' ' + str(code[5]) + ' ' + str(code[6]) + '\n')
        return answers

    root = Tk()
    type = -1
    target_xy = (Consts.screen_parameters[1], Consts.screen_parameters[1])
    index = 0
    clickable_state = 0  #0 - map_coice, 1 - click_on_map
    answers = []

    AllPhotos.init(Consts.screen_parameters)

    screen_label = Label(root, image=AllPhotos.screens[0], width=Consts.screen_parameters[1], height=Consts.screen_parameters[1])
    screen_label.pack(fill=None, anchor='w', side='left')

    map_label = Label(root, image=AllPhotos.map_choice, width=Consts.screen_parameters[1], height=Consts.screen_parameters[1])
    map_label.pack(fill=None, anchor='w', side='left')

    apply_btn = Button(root, text="Apply", width=14)
    apply_btn.pack(fill=None, anchor='n', side='top')

    back_btn = Button(root, text="Back", width=14, state='disable')
    back_btn.pack(fill=None, anchor='n', side='top')

    chosen_text = Text()
    chosen_text.pack(fill='y', anchor='s', side='top')

    def __init__(self, type):  #0 - coder, 1 - guesser
        self.type = type
        if type == 1:
            self.answers = self.get_ans()
        self.root.title("Valoguesser_coder")
        self.root.iconphoto(False, PhotoImage(file="logo.ico"))
        self.root.geometry("1440x648")

        self.back_btn.configure(command=self.back_click)

        self.apply_btn.configure(command=self.application)

        self.map_label.bind("<Button-1>", self.map_choice)

        self.root.mainloop()



    #root.mainloop()