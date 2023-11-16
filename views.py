import time

from asciimatics.effects import Cycle, Stars, Snow, Print, Sprite
from asciimatics.renderers import FigletText,StaticRenderer
from asciimatics.scene import Scene
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu
from asciimatics.effects import Background
from asciimatics.event import MouseEvent
from PIL import ImageColor
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.paths import Path, DynamicPath
from asciimatics.parsers import AsciimaticsParser
import sys
import GameSprites
import random



def get_palette():
    custom_dict = {
        'background': (Screen.COLOUR_BLACK, 1, Screen.COLOUR_DEFAULT),
        'shadow': (0, None, 0),
        'disabled': (0, 1, 4),
        'invalid': (3, 1, 1),
        'label': (2, 1, 4),
        'borders': (Screen.COLOUR_BLACK, 1, Screen.COLOUR_BLACK),
        'scroll': (6, 2, 4),
        'title': (Screen.COLOUR_BLACK, 1, Screen.COLOUR_BLACK),
        'edit_text': (7, 2, 4),
        'focus_edit_text': (7, 1, 6),
        'readonly': (0, 1, 4),
        'focus_readonly': (0, 1, 6),
        'button': (Screen.COLOUR_BLACK, 1, Screen.COLOUR_DEFAULT),
        'focus_button': (Screen.COLOUR_GREEN, 1, Screen.COLOUR_DEFAULT),
        'control': (3, 2, 4),
        'selected_control': (3, 1, 4),
        'focus_control': (3, 2, 4),
        'selected_focus_control': (3, 1, 6),
        'field': (7, 2, 4),
        'selected_field': (3, 1, 4),
        'focus_field': (7, 2, 4),
        'selected_focus_field': (7, 1, 6)
    }
    return custom_dict
################FRAMES################################
class FightFrame(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         7,
                         screen.width//2,
                         can_scroll=False,
                         title="Menu",
                         x=0, y=screen.height-7
                         )
        self.palette = get_palette()
        layout = Layout([1,1,1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("ATTACK", self._attack, add_box=False), 0)
        layout.add_widget(Button("USE ITEM", self._move_right, add_box=False), 1)
        layout.add_widget(Button("MAGIC", self._move_right, add_box=False), 2)
        layout.add_widget(Button("BACK", self._back, add_box=False), 0)
        self.fix()

    @staticmethod
    def _back():
        raise NextScene("MENU")

    @staticmethod
    def _attack():
        raise NextScene("PLAYERATTACK")
    @staticmethod
    def _move_right():
        print("lol")




class FightInfoFrame(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         7,
                         screen.width//2,
                         can_scroll=False,
                         title="Menu",
                         x=screen.width//2, y=screen.height-7
                         )
        self.palette = get_palette()
        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        self.fix()




class Menu(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         13,
                         20,
                         can_scroll=False,
                         title="Menu",
                         x=screen.width//2 - 10, y=screen.height-13
                         )
        self.palette = get_palette()
        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("     NEW GAME   ", self._new_game,add_box=False), 0)
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("     CONTINUE   ", self._quit,add_box=False), 0)
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("       INFO   ", self._info,add_box=False), 0)
        layout.add_widget(Divider(""))
        layout.add_widget(Button("       QUIT   ",self._quit,add_box=False),0)
        self.fix()

    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")
    @staticmethod
    def _info():
        raise NextScene("INFO")

    @staticmethod
    def _new_game():
        raise NextScene("TOWN")

class Town(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         24,
                         60,
                         can_scroll=False,
                         title="INFO",
                         x=screen.width//2 - 30, y=screen.height-26
                         )
        self.set_theme("green")
        layout = Layout([1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("NEXT FIGHT ", self._fight, add_box=False), 0)
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("WIZARD", self._wizard, add_box=False), 0)
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("BLACKSMITH", self._blacksmith, add_box=False), 0)
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("WEAPONMASTER", self._weaponmaster, add_box=False), 0)
        self.fix()
    @staticmethod
    def _fight():
        raise NextScene("FIGHT")

    @staticmethod
    def _wizard():
        raise NextScene("FIGHT")

    @staticmethod
    def _blacksmith():
        raise NextScene("FIGHT")

    @staticmethod
    def _weaponmaster():
        raise NextScene("FIGHT")

class Info(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         24,
                         60,
                         can_scroll=False,
                         title="INFO",
                         x=screen.width//2 - 30, y=screen.height-26
                         )
        self.set_theme("green")
        layout1 = Layout([1], fill_frame=True)
        self.add_layout(layout1)
        layout1.add_widget(Label(chr(random.randint(65, 90))),0)
        layout1.add_widget(Label("Gra nie jest dostosowana do gry w rozdzielczości innej "), 0)
        layout1.add_widget(Label("niż domyślna rozdzieczość terminala cmd"), 0)
        layout1.add_widget(Label("W przypadku zmiany rozdzielczości aplikacja zostanie zamknięta"), 0)
        layout1.add_widget(Label("zostanie zamknięta"), 0)



        layout2 = Layout([1,1,1,1,1])
        self.add_layout(layout2)
        layout2.add_widget(Divider(line_char=""))
        layout2.add_widget(Button("    BACK   ", self._back, add_box=False), 4)
        self.fix()

    def _back(self):
        raise NextScene("MENU")

value = 0
direction = 1
def cycle():
    global value, direction
    value += direction
    if value <= 0 or value >= 3:
        direction = -direction
    return value
class Player(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Player,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.knight())
            },
        colour = Screen.COLOUR_BLUE,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )
class Devil(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Devil,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.devil())
            },
        colour = Screen.COLOUR_RED,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )


#PATHS
class PlayerMove(DynamicPath):
    def process_event(self, event):
            return event


def menu(screen, scene):
    centre = (screen.width // 2, screen.height // 2)
    scenes = []
    MenuObject = Menu(screen)
    cycle_effect = Cycle(
            screen,
            FigletText("PALLANDIN", font='standard'),
            screen.height // 2 -15)
    effectsMenu = [
        Cycle(
            screen,
            FigletText("PALLANDIN", font='standard'),
            screen.height // 2 -15),
        Cycle(
            screen,
            FigletText("VS", font='standard'),
            screen.height // 2 -10 ),
        Cycle(
            screen,
            FigletText("MONSTERS", font='standard'),
            screen.height // 2 -5),
        Stars(screen,250),
        MenuObject
    ]
    scenes.append(Scene(effectsMenu,-1,name="MENU"))
    effectsINFO = [
        Snow(screen),
        Info(screen)
    ]
    scenes.append(Scene(effectsINFO,-1,name="INFO"))
    global player
    global path, devilpath
    global devil
    path = PlayerMove(screen, 10, screen.height // 2-3)
    devilpath = PlayerMove(screen, screen.width-20, screen.height // 2-3)
    effectsFIGHT = [
        Player(screen, path),
        Devil(screen, devilpath),
        FightFrame(screen),
        FightInfoFrame(screen),
    ]
    scenes.append(Scene(effectsFIGHT, -1, name="FIGHT"))
    attackPath = Path()
    attackPath.jump_to( 10, screen.height // 2)
    attackPath.move_straight_to(16, 10, (screen.width + 16) // 2)
    attackPath.wait(100)
    effectsPlayerAttack = [
        Player(screen, attackPath),
        Devil(screen, devilpath),
        FightFrame(screen),
        FightInfoFrame(screen),
    ]
    scenes.append(Scene(effectsPlayerAttack, 100, name="PLAYERATTACK"))
    effectsTOWN = [
        Town(screen)
    ]
    scenes.append(Scene(effectsTOWN,-1,name="TOWN"))

    screen.play(scenes,stop_on_resize=True,start_scene=scene)



def screenchanger():
    last_scene = None
    while True:
        try:
            Screen.wrapper(menu,catch_interrupt=True,arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            pass
