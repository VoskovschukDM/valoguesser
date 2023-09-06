import os
from PIL import Image, ImageTk


class AllPhotos:
    map_images = []
    maps = []
    map_num = -1
    cur_map = 0
    map_choice = 0
    screens = []
    target_img = Image.new(mode='RGBA', size=(16, 16), color='WHITE')


    def init(screenParameters):
        AllPhotos.cur_map = Image.new(mode='RGBA', size=(screenParameters[1], screenParameters[1]), color='WHITE')
        AllPhotos.map_choice = Image.new(mode='RGBA', size=(screenParameters[1], screenParameters[1]), color='WHITE')
        map_names = ['ascend', 'bind', 'fracture', 'haven', 'lotus', 'pearl', 'split']
        map_images = []
        img_choice = Image.new(mode='RGBA', size=(screenParameters[1], screenParameters[1]), color='WHITE')

        for i in range(7):
            map_images.append(Image.open("data/" + map_names[i] + "_map.png"))
            map_images[i].thumbnail((screenParameters[1], screenParameters[1]))
            AllPhotos.maps.append(ImageTk.PhotoImage(map_images[i]))
        AllPhotos.map_images = map_images.copy()

        for i in range(7):
            tmp = map_images[i].copy()
            tmp.thumbnail((screenParameters[1] // 3, screenParameters[1] // 3))
            img_choice.paste(tmp, (screenParameters[1] // 3 * (i % 3), screenParameters[1] // 3 * (i // 3)))
            AllPhotos.map_choice = ImageTk.PhotoImage(img_choice)

        tasks = len(next(os.walk('data/screen_set'))[2])
        for i in range(tasks):
            tmp = Image.open("data/screen_set/scr" + str(i + 1) + ".png")
            tmp.thumbnail((screenParameters[1], screenParameters[1]))
            AllPhotos.screens.append(ImageTk.PhotoImage(tmp))
        print("tasks=" + str(tasks))

        AllPhotos.target_img = Image.open("target.png")


    def add_target(self, x, y):
        new_img = AllPhotos.map_images[AllPhotos.map_num].copy()
        new_img.paste(AllPhotos.target_img, (x - 11, y - 11))
        AllPhotos.cur_map = ImageTk.PhotoImage(new_img)
        return AllPhotos.cur_map
