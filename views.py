import time
from controller import Fight
from asciimatics.effects import Cycle, Stars, Snow, Print, Sprite
from asciimatics.renderers import FigletText,StaticRenderer, BarChart
from asciimatics.scene import Scene
from asciimatics.event import KeyboardEvent
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, ListBox, Widget
from asciimatics.effects import Background
from asciimatics.event import MouseEvent
from PIL import ImageColor
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.paths import Path, DynamicPath
from asciimatics.parsers import AsciimaticsParser
import sys
import GameSprites
import random
from controller import Fight

global FightController
FightController = Fight()
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
                         screen.width-2,
                         can_scroll=False,
                         title="Menu",
                         x=1, y=screen.height-7
                         )
        self.palette = get_palette()
        layout = Layout([1,1,1,1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("ATTACK", self._attack, add_box=False), 0)
        layout.add_widget(Button("MAGIC", self._magic, add_box=False), 1)
        layout.add_widget(Button("REST", self._rest, add_box=False), 2)
        layout.add_widget(Button("BACK", self._back, add_box=False), 0)
        PlayerHpValue = self.get_player_hp_text()
        self.player_hp_label = Label(PlayerHpValue)
        layout.add_widget(self.player_hp_label, 3)
        MonsterHpValue = self.get_monster_hp_text()
        self.monster_hp_label = Label(MonsterHpValue)
        layout.add_widget(self.monster_hp_label, 3)
        self.mana_label = Label(self.get_player_mana_text())
        layout.add_widget(self.mana_label)
        self.fix()

    @staticmethod
    def _back():
        raise NextScene("MENU")
    @staticmethod
    def _magic():
        raise NextScene("SPELLTYPE")

    @staticmethod
    def _attack():
        raise NextScene("ATTACKTYPE")
    def _rest(self):
        FightController.rest()
        raise NextScene("PLAYERATTACK")

    def get_player_hp_text(self):
        """Helper method to format the HP text."""
        print("HP {}/{}".format(FightController.getPlayerHP(), FightController.getMaxPlayerHP()))
        return "HP {}/{}".format(FightController.getPlayerHP(), FightController.getMaxPlayerHP())

    def get_monster_hp_text(self):
        """Helper method to format the HP text."""
        print("HP {}/{}".format(FightController.getMonsterHP(), FightController.getMaxMonsterHP()))
        return "HP {}/{}".format(FightController.getMonsterHP(), FightController.getMaxMonsterHP())
    def get_player_mana_text(self):
        return "Mana {}/{}".format(FightController.get_mana(), FightController.get_maxmana())

    def update_hp_label(self):
            self.player_hp_label.text = self.get_player_hp_text()
            self.monster_hp_label.text = self.get_monster_hp_text()
            self.mana_label.text = self.get_player_mana_text()



    def _update(self, frame_no):
        # Refresh the list view if needed
        self.update_hp_label()
        super(FightFrame, self)._update(frame_no)

class AttackType(Frame):
    def __init__(self, screen):
        self._hp = FightController.getPlayerHP()
        super().__init__(screen,
                         7,
                         screen.width-2,
                         can_scroll=False,
                         title="Menu",
                         x=1, y=screen.height-7
                         )
        self._last_frame = 0
        self.palette = get_palette()
        layout = Layout([1,1,1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("FAST", self._fast, add_box=False), 0)
        layout.add_widget(Button("NORMAL", self._normal, add_box=False), 1)
        layout.add_widget(Button("HARD", self._strong, add_box=False), 2)
        layout.add_widget(Button("BACK", self._back, add_box=False), 0)
        self.fix()
    @staticmethod
    def _fast():
        FightController.setAttacktype("FAST")
        FightController.playerTurn("WEAPON")
        raise NextScene("PLAYERATTACK")
    @staticmethod
    def _normal():
        FightController.setAttacktype("NORMAL")
        FightController.playerTurn("WEAPON")
        raise NextScene("PLAYERATTACK")
    @staticmethod
    def _strong():
        FightController.setAttacktype("STRONG")
        FightController.playerTurn("WEAPON")
        raise NextScene("PLAYERATTACK")
    @staticmethod
    def _back():
        raise NextScene("FIGHT")

class SpellType(Frame):
    def __init__(self, screen):
        self._hp = FightController.getPlayerHP()
        super().__init__(screen,
                            7,
                            screen.width - 2,
                            can_scroll=False,
                            title="Menu",
                             x=1, y=screen.height - 7
                             )
        self._last_frame = 0
        self.palette = get_palette()
        layout = Layout([1, 1, 1], fill_frame=True)
        self.add_layout(layout)
        self.fireball_button =Button("FIREBALL", self._fireball, add_box=False)
        self.holymissle_button =Button("HOLY MISSLE", self._holymissle, add_box=False)
        self.thundrstrike_button = Button("THUNDER STRIKE", self._thunderstrike, add_box=False)
        layout.add_widget(self.fireball_button, 0)
        layout.add_widget(self.holymissle_button, 1)
        layout.add_widget(self.thundrstrike_button, 2)
        layout.add_widget(Button("BACK", self._back, add_box=False), 0)
        self.fix()

    @staticmethod
    def _fireball():
        if (FightController.check_mana(20) == True):
            FightController.setAttacktype("FIRE")
            FightController.playerTurn("FIREBALL")
            raise NextScene("PLAYERATTACK")

    @staticmethod
    def _holymissle():
        if (FightController.check_mana(20) == True):
            FightController.setAttacktype("HOLY")
            FightController.playerTurn("HOLYMISSLE")
            raise NextScene("PLAYERATTACK")

    @staticmethod
    def _thunderstrike():
        if (FightController.check_mana(20) == True):
            FightController.setAttacktype("THUNDER")
            FightController.playerTurn("THUNDERSTRIKE")
            raise NextScene("PLAYERATTACK")

    def EnoughMana(self):
        if(FightController.check_mana(20) == False):
            self.fireball_button.disabled = True
            self.holymissle_button.disabled = True
            self.thundrstrike_button.disabled = True
        else:
            self.fireball_button.disabled = False
            self.holymissle_button.disabled = False
            self.thundrstrike_button.disabled = False

    @staticmethod
    def _back():
        raise NextScene("FIGHT")

    def _update(self, frame_no):
        self.EnoughMana()
        super(SpellType,self)._update(frame_no)

class ShopFrameBlackSmith(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         30,
                         50,
                         can_scroll=False,
                         title="Menu",
                         x=0, y=0
                         )
        self.items = FightController.get_items_blacksmith()
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            self.items,
            name="SHOP",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._buy)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit), 2)
        self.price_label = Label("PRICE: {}".format(self._list_view.value))
        self.your_gold_label = Label("YOUR GOLD: {}".format(self.get_gold()))
        layout2.add_widget(self.price_label,0)
        layout2.add_widget(self.your_gold_label,1)
        self.fix()

    def _on_pick(self):
        self.price_label.text = "PRICE: {}".format(self._list_view.value)
    def _buy(self):
        if(FightController.isEnoughGold(self._list_view.value)):
            self.save()
            FightController.buy_item_blacksmith(self._list_view.value)
            self.your_gold_label.text = "YOUR GOLD: {}".format(self.get_gold())
            self._reload_list()

    def get_gold(self):
        return FightController.get_player_gold()

    def _reload_list(self, new_value=None):
        self._list_view.options = FightController.get_items_blacksmith()
        self._list_view.value = new_value

    @staticmethod
    def _quit():
        raise NextScene("TOWN")

class ShopFrameWeaponMaster(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         30,
                         50,
                         can_scroll=False,
                         title="Menu",
                         x=0, y=0
                         )
        self.items = FightController.get_items_weaponmaster()
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            self.items,
            name="SHOP",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._buy)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit), 2)
        self.price_label = Label("PRICE: {}".format(self._list_view.value))
        self.your_gold_label = Label("YOUR GOLD: {}".format(self.get_gold()))
        layout2.add_widget(self.price_label,0)
        layout2.add_widget(self.your_gold_label,1)
        self.fix()

    def _on_pick(self):
        self.price_label.text = "PRICE: {}".format(self._list_view.value)
    def _buy(self):
        if(FightController.isEnoughGold(self._list_view.value)):
            self.save()
            print("ON CHANGE")
            FightController.buy_item_weaponmaster(self._list_view.value)
            self.your_gold_label.text = "YOUR GOLD: {}".format(self.get_gold())
            self._reload_list()

    def get_gold(self):
        return FightController.get_player_gold()

    def _reload_list(self, new_value=None):
        self._list_view.options = FightController.get_items_weaponmaster()
        self._list_view.value = new_value


    @staticmethod
    def _quit():
        raise NextScene("TOWN")



class NextSceneFrame(Frame):
    def __init__(self, screen, moveto):
        super().__init__(screen,
                         7,
                         screen.width-2,
                         can_scroll=False,
                         title="Menu",
                         x=1, y=screen.height-7
                         )
        self._moveto = moveto
        self.palette = get_palette()
        layout = Layout([1,1,1], fill_frame=True)
        self.add_layout(layout)
        self.info_label = Label(self.get_damage())
        layout.add_widget(Button("          CONTINUE", self._continue, add_box=False), 1)
        layout.add_widget(self.info_label, 1)
    def _continue(self):
        FightController.setisresting(False)
        if(self._moveto == "ENEMYATTACK"):
            FightController.enemyTurn()
            if(FightController._isplayerdead  == False):
                raise NextScene(self._moveto)
            else:
                raise NextScene("DEATH")
        elif(self._moveto == "FIGHT"):
            if (FightController._ismonsterdead == False):
                raise NextScene(self._moveto)
            else:
                raise NextScene("WIN")
    def get_damage(self):
        """Helper method to format the HP text."""
        if(self._moveto == "ENEMYATTACK"):
            damage = FightController.getLastPlayerDamage
            return "{} attacked {} for {}".format(FightController.getPlayerName(), FightController.getMonsterName(), damage)
        else:
            damage = FightController.getLastMonsterDamage
            return "{} attacked {} for {}".format( FightController.getMonsterName(),FightController.getPlayerName(), damage)
    def set_info_text(self):
        if(FightController.isresting == True):
            self.info_label.text = "You rest for this turn"
        else:
            self.info_label.text = self.get_damage()
        self.fix()


    def _update(self, frame_no):
        self.set_info_text()
        super(NextSceneFrame, self)._update(frame_no)

class gotoMenu(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         7,
                         screen.width-2,
                         can_scroll=False,
                         title="Menu",
                         x=1, y=screen.height-7
                         )
        self.palette = get_palette()
        layout = Layout([1, 1, 1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("   GO TO MENU", self._continue, add_box=False), 1)
        self.fix()

    def _continue(self):
        raise NextScene("TOWN")





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
        layout.add_widget(Divider(line_char=""))
        layout.add_widget(Button("QUIT", self._quit, add_box=False), 0)
        self.fix()
    @staticmethod
    def _fight():
        raise NextScene("FIGHT")

    @staticmethod
    def _wizard():
        raise NextScene("FIGHT")

    @staticmethod
    def _blacksmith():
        raise NextScene("BLACKSMITH")

    @staticmethod
    def _weaponmaster():
        raise NextScene("WEAPONMASTER")

    @staticmethod
    def _quit():
        raise StopApplication("QUIT")

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


def game(screen, scene):
    centre = (screen.width // 2, screen.height // 2)
    scenes = []
    #SCENA MENU#
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
    #SCENA INFORMACJI#
    effectsINFO = [
        Snow(screen),
        Info(screen)
    ]
    scenes.append(Scene(effectsINFO,-1,name="INFO"))
    #SCENA WALKI DEMO DO POPRAWY#
    global player
    global path, devilpath
    global devil
    path = PlayerMove(screen, 10, screen.height // 2-3)
    devilpath = PlayerMove(screen, screen.width-20, screen.height // 2-3)
    effectsFIGHT = [
        Player(screen, path),
        Devil(screen, devilpath),
        FightFrame(screen),
    ]
    scenes.append(Scene(effectsFIGHT, -1, name="FIGHT"))
    #SCENA ATAK GRACZA
    attackPath = Path()
    attackPath.jump_to( 10, screen.height // 2)
    #attackPath.move_straight_to(16, 10, (screen.width + 16) // 2)
    #attackPath.wait(100)
    effectsPlayerAttack = [
        Player(screen, attackPath),
        Devil(screen, devilpath),
        NextSceneFrame(screen,"ENEMYATTACK")
    ]
    scenes.append(Scene(effectsPlayerAttack, -1, name="PLAYERATTACK"))
    effectsTOWN = [
        Town(screen),
    ]
    scenes.append(Scene(effectsTOWN,-1,name="TOWN"))
    effectsEnemyAttack = [
        Player(screen,path),
        Devil(screen, devilpath),
        NextSceneFrame(screen,"FIGHT")
    ]
    scenes.append(Scene(effectsEnemyAttack, -1, name="ENEMYATTACK"))
    effectsDeath = [
        Player(screen, path),
        gotoMenu(screen),
        Cycle(
            screen,
            FigletText("YOU DIE", font='standard'),
            screen.height // 2 - 15)
    ]
    scenes.append(Scene(effectsDeath, -1, name="DEATH"))
    effectsWin = [
        Player(screen, path ),
        gotoMenu(screen),
        Cycle(
            screen,
            FigletText("YOU WIN", font='standard'),
            screen.height // 2 - 15),

    ]
    scenes.append(Scene(effectsWin, -1, name="WIN"))
    effectsAttackType = [
        Player(screen, path),
        Devil(screen, devilpath),
        AttackType(screen)
    ]
    scenes.append(Scene(effectsAttackType, -1, name="ATTACKTYPE"))
    effectsSpellType = [
        Player(screen, path),
        Devil(screen, devilpath),
        SpellType(screen)
    ]
    scenes.append(Scene(effectsSpellType, -1, name="SPELLTYPE"))
    # SCENA ATAK PRZECIWNIKA

    effectsBlackSmith = [
        ShopFrameBlackSmith(screen)
    ]
    scenes.append(Scene(effectsBlackSmith, -1, name="BLACKSMITH"))
    effectsWeaponmaster = [
        ShopFrameWeaponMaster(screen)
    ]
    scenes.append(Scene(effectsWeaponmaster, -1, name="WEAPONMASTER"))

    screen.play(scenes, stop_on_resize=True, start_scene=scene)

def screenchanger():
    last_scene = None
    while True:
        try:
            Screen.wrapper(game,catch_interrupt=True,arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            pass
