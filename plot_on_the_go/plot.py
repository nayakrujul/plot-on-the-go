import pygame

pygame.init()

colours = {
    'black': (0,0,0),
    'white': (255,255,255),
    'red': (255,0,0),
    'lime': (0,255,0),
    'blue': (0,0,255),
    'yellow': (255,255,0),
    'cyan': (0,255,255),
    'magenta': (255,0,255),
    'silver': (192,192,192),
    'gray': (128,128,128),
    'maroon': (128,0,0),
    'olive': (128,128,0),
    'green': (0,128,0),
    'purple': (128,0,128),
    'teal': (0,128,128),
    'navy': (0,0,128),
    'maroon': (128,0,0),
    'dark red': (139,0,0),
    'brown': (165,42,42),
    'firebrick': (178,34,34),
    'crimson': (220,20,60),
    'red': (255,0,0),
    'tomato': (255,99,71),
    'coral': (255,127,80),
    'indian red': (205,92,92),
    'light coral': (240,128,128),
    'dark salmon': (233,150,122),
    'salmon': (250,128,114),
    'light salmon': (255,160,122),
    'orange red': (255,69,0),
    'dark orange': (255,140,0),
    'orange': (255,165,0),
    'gold': (255,215,0),
    'dark golden rod': (184,134,11),
    'golden rod': (218,165,32),
    'pale golden rod': (238,232,170),
    'dark khaki': (189,183,107),
    'khaki': (240,230,140),
    'olive': (128,128,0),
    'yellow': (255,255,0),
    'yellow green': (154,205,50),
    'dark olive green': (85,107,47),
    'olive drab': (107,142,35),
    'lawn green': (124,252,0),
    'chartreuse': (127,255,0),
    'green yellow': (173,255,47),
    'dark green': (0,100,0),
    'green': (0,128,0),
    'forest green': (34,139,34),
    'lime': (0,255,0),
    'lime green': (50,205,50),
    'light green': (144,238,144),
    'pale green': (152,251,152),
    'dark sea green': (143,188,143),
    'medium spring green': (0,250,154),
    'spring green': (0,255,127),
    'sea green': (46,139,87),
    'medium aqua marine': (102,205,170),
    'medium sea green': (60,179,113),
    'light sea green': (32,178,170),
    'dark slate gray': (47,79,79),
    'teal': (0,128,128),
    'dark cyan': (0,139,139),
    'aqua': (0,255,255),
    'cyan': (0,255,255),
    'light cyan': (224,255,255),
    'dark turquoise': (0,206,209),
    'turquoise': (64,224,208),
    'medium turquoise': (72,209,204),
    'pale turquoise': (175,238,238),
    'aqua marine': (127,255,212),
    'powder blue': (176,224,230),
    'cadet blue': (95,158,160),
    'steel blue': (70,130,180),
    'corn flower blue': (100,149,237),
    'deep sky blue': (0,191,255),
    'dodger blue': (30,144,255),
    'light blue': (173,216,230),
    'sky blue': (135,206,235),
    'light sky blue': (135,206,250),
    'midnight blue': (25,25,112),
    'navy': (0,0,128),
    'dark blue': (0,0,139),
    'medium blue': (0,0,205),
    'blue': (0,0,255),
    'royal blue': (65,105,225),
    'blue violet': (138,43,226),
    'indigo': (75,0,130),
    'dark slate blue': (72,61,139),
    'slate blue': (106,90,205),
    'medium slate blue': (123,104,238),
    'medium purple': (147,112,219),
    'dark magenta': (139,0,139),
    'dark violet': (148,0,211),
    'dark orchid': (153,50,204),
    'medium orchid': (186,85,211),
    'purple': (128,0,128),
    'thistle': (216,191,216),
    'plum': (221,160,221),
    'violet': (238,130,238),
    'magenta': (255,0,255),
    'orchid': (218,112,214),
    'medium violet red': (199,21,133),
    'pale violet red': (219,112,147),
    'deep pink': (255,20,147),
    'hot pink': (255,105,180),
    'light pink': (255,182,193),
    'pink': (255,192,203),
    'antique white': (250,235,215),
    'beige': (245,245,220),
    'bisque': (255,228,196),
    'blanched almond': (255,235,205),
    'wheat': (245,222,179),
    'corn silk': (255,248,220),
    'lemon chiffon': (255,250,205),
    'light golden rod yellow': (250,250,210),
    'light yellow': (255,255,224),
    'saddle brown': (139,69,19),
    'sienna': (160,82,45),
    'chocolate': (210,105,30),
    'peru': (205,133,63),
    'sandy brown': (244,164,96),
    'burly wood': (222,184,135),
    'tan': (210,180,140),
    'rosy brown': (188,143,143),
    'moccasin': (255,228,181),
    'navajo white': (255,222,173),
    'peach puff': (255,218,185),
    'misty rose': (255,228,225),
    'lavender blush': (255,240,245),
    'linen': (250,240,230),
    'old lace': (253,245,230),
    'papaya whip': (255,239,213),
    'sea shell': (255,245,238),
    'mint cream': (245,255,250),
    'slate gray': (112,128,144),
    'light slate gray': (119,136,153),
    'light steel blue': (176,196,222),
    'lavender': (230,230,250),
    'floral white': (255,250,240),
    'alice blue': (240,248,255),
    'ghost white': (248,248,255),
    'honeydew': (240,255,240),
    'ivory': (255,255,240),
    'azure': (240,255,255),
    'snow': (255,250,250),
    'dim gray': (105,105,105),
    'gray': (128,128,128),
    'dark gray': (169,169,169),
    'silver': (192,192,192),
    'light gray': (211,211,211),
    'gainsboro': (220,220,220),
    'white smoke': (245,245,245)
}

def showMessage(window, message, x, y, colour=colours['black'], size=15):
    font = pygame.font.SysFont("dejavusansmono", size)
    renderedText = font.render(message, True, colour)
    textArea = renderedText.get_rect()
    textArea.center = x, y
    window.blit(renderedText, textArea)

class Scatter:
    def __init__(self, x_max):
        self.__x_max = x_max
        self.__window = pygame.display.set_mode((850, 600))
        pygame.display.set_caption("PlotOnTheGo Grapher")
        self.__points = []
        self.__legend = {}
        self.__title = ''
        self.__update()
    def __draw_axis(self):
        pygame.draw.line(self.__window, colours['black'], (50, 50), (50, 550), 10)
        pygame.draw.line(self.__window, colours['black'], (50, 550), (800, 550), 10)
    def __x_axis_nums(self):
        x = self.__x_max / 15
        for i in range(16):
            n = x * i
            if n < 100:
                d = str(round(n, 1))
            elif n < 1000:
                d = str(round(n))
            else:
                d = str(round(n / 1000, 1)) + 'k'
            showMessage(self.__window, d, 50*(i+1), 570)
    def __y_axis_nums(self):
        y = (max(self.__points, default=(None, 1, None), key=lambda x: x[1])[1] or 1) / 10
        for i in range(11):
            n = y * i
            if n < 10:
                d = str(round(n, 1))
            elif n < 100:
                d = str(round(n))
            elif n < 100000:
                d = str(round(n / 1000)) + 'k'
            else:
                d = str(round(n / 1000000, 1)) + 'm'
            showMessage(self.__window, d, 25, 550 - (i*50))
    def __axis(self):
        self.__draw_axis()
        self.__x_axis_nums()
        self.__y_axis_nums()
    def __draw_points(self):
        max_y = max(self.__points, default=(None, 1, None), key=lambda x: x[1])[1] or 1
        for x, y, c in self.__points:
            scrx = 50 + (x / self.__x_max) * 750
            scry = 550 - (y / max_y) * 500
            pygame.draw.circle(self.__window, c, (scrx, scry), 5)
    def __draw_legend(self):
        for i, (c, l) in enumerate(self.__legend.items()):
            pygame.draw.line(self.__window, c, (700, 400 + (i*20)), (725, 400 + (i*20)), 5)
            showMessage(self.__window, l, 800, 400 + (i*20), c, 20)
    def __draw_title(self):
        showMessage(self.__window, self.__title, 425, 25, size=30)
    def __update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.__window.fill(colours['white'])
        self.__axis()
        self.__draw_points()
        self.__draw_legend()
        self.__draw_title()
        pygame.display.update()
    def plot_point(self, x, y, colour):
        if x < 0 or x > self.__x_max or y < 0:
            raise ValueError(f'Invalid coordinates ({x}, {y})')
        if isinstance(colour, str) and colour.lower() in colours:
            colour = colours[colour.lower()]
        else:
            if not isinstance(colour, tuple):
                raise ValueError(f'Invalid colour {colour!r}')
            if len(colour) != 3:
                raise ValueError(f'Invalid colour {colour!r}')
            if not all(isinstance(x, (int, float)) for x in colour):
                raise ValueError(f'Invalid colour {colour!r}')
            if not all(0 <= i <= 255 for i in colour):
                raise ValueError(f'Invalid colour {colour!r}')
        self.__points.append((x, y, colour))
        self.__update()
    def legend(self, **items):
        for colour, label in items.items():
            if colour.lower().replace('_', ' ') not in colours:
                raise ValueError(f'Invalid colour {colour!r}')
            self.__legend[colours[colour.lower().replace('_', ' ')]] = str(label)
        self.__update()
    def title(self, _title):
        self.__title = str(_title)
        self.__update()
    def stop(self):
        pygame.quit()
    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
