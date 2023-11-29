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
        'label': (Screen.COLOUR_GREEN, 1, Screen.COLOUR_BLACK),
        'borders': (Screen.COLOUR_WHITE, 1, Screen.COLOUR_BLACK),
        'scroll': (6, 2, 4),
        'title': (Screen.COLOUR_WHITE, 1, Screen.COLOUR_BLACK),
        'edit_text': (7, 2, 4),
        'focus_edit_text': (7, 1, 6),
        'readonly': (0, 1, 4),
        'focus_readonly': (0, 1, 6),
        'button': (Screen.COLOUR_BLACK, 1, Screen.COLOUR_DEFAULT),
        'focus_button': (Screen.COLOUR_GREEN, 1, Screen.COLOUR_DEFAULT),
        'control': (Screen.COLOUR_BLACK, 1, Screen.COLOUR_DEFAULT),
        'selected_control': (3, 1, 4),
        'focus_control': (3, 2, 4),
        'selected_focus_control': (3, 1, 6),
        'field': (Screen.COLOUR_BLUE, 1, Screen.COLOUR_DEFAULT),
        'selected_field': (Screen.COLOUR_BLACK, 1, Screen.COLOUR_DEFAULT),
        'focus_field': (Screen.COLOUR_CYAN, 1, Screen.COLOUR_DEFAULT),
        'selected_focus_field': (Screen.COLOUR_YELLOW, 1, Screen.COLOUR_RED)
    }
    return custom_dict
################FRAMES################################
class FightFrame(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         7,
                         screen.width-2,
                         can_scroll=False,
                         title="DUNGEON",
                         x=1, y=screen.height-7
                         )
        self.palette = get_palette()
        layout = Layout([1,1,1,1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("ATTACK", self._attack, add_box=False), 0)
        layout.add_widget(Button("MAGIC", self._magic, add_box=False), 1)
        layout.add_widget(Button("REST", self._rest, add_box=False), 2)
        layout.add_widget(Divider(line_char=""), 1)
        layout.add_widget(Button("BACK", self._back, add_box=False), 1)
        PlayerHpValue = self.get_player_hp_text()
        self.player_hp_label = Label(PlayerHpValue)
        layout.add_widget(Label("PLAYER STATS"),3)
        layout.add_widget(self.player_hp_label, 3)
        MonsterHpValue = self.get_monster_hp_text()
        self.monster_hp_label = Label(MonsterHpValue)
        self.mana_label = Label(self.get_player_mana_text())
        layout.add_widget(self.mana_label,3)
        layout.add_widget( Label("ENEMY STATS"),3)
        layout.add_widget(self.monster_hp_label, 3)
        self.fix()

    @staticmethod
    def _back():
        raise NextScene("MENU")
    @staticmethod
    def _magic():
        raise NextScene(FightController.scene_controller("SPELLTYPE"))

    @staticmethod
    def _attack():
        raise NextScene(FightController.scene_controller("ATTACKTYPE"))
    def _rest(self):
        FightController.rest()
        raise NextScene(FightController.scene_controller("REST"))

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
                         title="DUNGEON",
                         x=1, y=screen.height-7
                         )
        self._last_frame = 0
        self.palette = get_palette()
        layout = Layout([1,1,1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("                FAST", self._fast, add_box=False), 0)
        layout.add_widget(Button("                NORMAL", self._normal, add_box=False), 1)
        layout.add_widget(Button("                HARD", self._strong, add_box=False), 2)
        layout.add_widget(Divider(line_char=""), 1)
        layout.add_widget(Button("                BACK", self._back, add_box=False), 1)
        self.fix()
    @staticmethod
    def _fast():
        FightController.setAttacktype("FAST")
        FightController.playerTurn("WEAPON")
        raise NextScene(FightController.scene_controller("WEAPON"))
    @staticmethod
    def _normal():
        FightController.setAttacktype("NORMAL")
        FightController.playerTurn("WEAPON")
        raise NextScene(FightController.scene_controller("WEAPON"))
    @staticmethod
    def _strong():
        FightController.setAttacktype("STRONG")
        FightController.playerTurn("WEAPON")
        raise NextScene(FightController.scene_controller("WEAPON"))
    @staticmethod
    def _back():
        raise NextScene(FightController.scene_controller("FIGHT"))

class SpellType(Frame):
    def __init__(self, screen):
        self._hp = FightController.getPlayerHP()
        super().__init__(screen,
                            7,
                            screen.width - 2,
                            can_scroll=False,
                            title="DUNGEON",
                             x=1, y=screen.height - 7
                             )
        self._last_frame = 0
        self.palette = get_palette()
        layout = Layout([1, 1, 1], fill_frame=True)
        self.add_layout(layout)
        self.fireball_button =Button("              FIREBALL", self._fireball, add_box=False)
        self.holymissle_button =Button("              HOLY MISSLE", self._holymissle, add_box=False)
        self.thundrstrike_button = Button("              THUNDER STRIKE", self._thunderstrike, add_box=False)
        layout.add_widget(self.fireball_button, 0)
        layout.add_widget(self.holymissle_button, 1)
        layout.add_widget(self.thundrstrike_button, 2)
        layout.add_widget(Divider(line_char=""), 1)
        layout.add_widget(Button("                BACK", self._back, add_box=False), 1)
        self.fix()

    @staticmethod
    def _fireball():
        if (FightController.check_mana(20) == True):
            FightController.setAttacktype("FIRE")
            FightController.playerTurn("FIREBALL")
            raise NextScene(FightController.scene_controller("FIREBALL"))

    @staticmethod
    def _holymissle():
        if (FightController.check_mana(20) == True):
            FightController.setAttacktype("HOLY")
            FightController.playerTurn("HOLYMISSLE")
            raise NextScene(FightController.scene_controller("HOLYMISSLE"))

    @staticmethod
    def _thunderstrike():
        if (FightController.check_mana(20) == True):
            FightController.setAttacktype("THUNDER")
            FightController.playerTurn("THUNDERSTRIKE")
            raise NextScene(FightController.scene_controller("THUNDERSTRIKE"))

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
        raise NextScene(FightController.scene_controller("FIGHT"))

    def _update(self, frame_no):
        self.EnoughMana()
        super(SpellType,self)._update(frame_no)

class NextSceneFrame(Frame):
    def __init__(self, screen, moveto):
        super().__init__(screen,
                         7,
                         screen.width-2,
                         can_scroll=False,
                         title="Dungeon",
                         x=1, y=screen.height-7
                         )
        self._moveto = moveto
        self.palette = get_palette()
        layout = Layout([1,1,1], fill_frame=True)
        self.add_layout(layout)
        self.info_label = Label(self.get_damage())
        layout.add_widget(Button("               CONTINUE", self._continue, add_box=False), 1)
        layout.add_widget(self.info_label, 1)
    def _continue(self):
        FightController.setisresting(False)
        if(self._moveto == "PLAYERTURN"):
            FightController.enemyTurn()
            if(FightController._isplayerdead  == False):
                raise NextScene(FightController.scene_controller("ENEMYATTACK"))
            else:
                raise NextScene("DEATH")
        elif(self._moveto == "ENEMYTURN"):
            if (FightController._ismonsterdead == False):
                raise NextScene(FightController.scene_controller("FIGHT"))
            else:
                FightController.reset_after_win()
                raise NextScene(FightController.scene_controller("WIN"))
    def get_damage(self):
        """Helper method to format the HP text."""
        if(self._moveto == "PLAYERTURN"):
            damage = FightController.getLastPlayerDamage
            return "   {} attacked {} for {}".format(FightController.getPlayerName(), FightController.getMonsterName(), damage)
        else:
            damage = FightController.getLastMonsterDamage
            return "   {} attacked {} for {}".format( FightController.getMonsterName(),FightController.getPlayerName(), damage)
    def set_info_text(self):
        if(FightController.isresting == True):
            self.info_label.text = "        You rest for this turn"
        else:
            self.info_label.text = self.get_damage()
        self.fix()


    def _update(self, frame_no):
        self.set_info_text()
        super(NextSceneFrame, self)._update(frame_no)

class ShopFrameBlackSmith(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         30,
                         60,
                         can_scroll=False,
                         title="BLACKSMITH SHOP",
                         x=0, y=0
                         )
        self.items = FightController.get_items_blacksmith()
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            self.items,
            name="BLACKSMITH SHOP",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._buy)
        layout = Layout([100], fill_frame=True)
        self.palette = get_palette()
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.price_label = Label("PRICE: {}".format(self._list_view.value))
        self.your_gold_label = Label("YOUR GOLD: {}".format(self.get_gold()))
        layout2.add_widget(self.price_label,0)
        layout2.add_widget(self.your_gold_label,2)
        self.weapon_statistic_label = Label(self.get_statistic())
        layout2.add_widget(self.weapon_statistic_label,1)
        layout2.add_widget(self.weapon_statistic_label)
        self.fix()

    def _on_pick(self):
        self.price_label.text = "PRICE: {}".format(self._list_view.value)
        self.weapon_statistic_label.text = self.get_statistic()
        self.your_gold_label.text = "YOUR GOLD: {}".format(self.get_gold())
    def _buy(self):
        if(FightController.isEnoughGold(self._list_view.value)):
            self.save()
            FightController.buy_item_blacksmith(self._list_view.value)
            self.your_gold_label.text = "YOUR GOLD: {}".format(self.get_gold())
            self._reload_list()

    def get_gold(self):
        return FightController.get_player_gold()
    def get_statistic(self):
        return "RES {}".format(FightController.get_statistic_blacksmith(self._list_view.value))

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
                         60,
                         can_scroll=False,
                         title="BLACKSMITH SHOP",
                         x=0, y=0
                         )
        self.palette = get_palette()
        self.items = FightController.get_items_weaponmaster()
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            self.items,
            name="WEAPON MASTERSHOP",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._buy)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.price_label = Label("PRICE: {}".format(self._list_view.value))
        self.your_gold_label = Label("YOUR GOLD: {}".format(self.get_gold()))
        layout2.add_widget(self.price_label,0)
        layout2.add_widget(self.your_gold_label,2)
        self.weapon_statistic_label = Label(self.get_statistic())
        layout2.add_widget(self.weapon_statistic_label,1)
        self.fix()

    def _on_pick(self):
        self.price_label.text = "PRICE: {}".format(self._list_view.value)
        self.weapon_statistic_label.text = self.get_statistic()
        self.your_gold_label.text = "YOUR GOLD: {}".format(self.get_gold())
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
    def get_statistic(self):
        return "DAMAGE: {}".format(FightController.get_statistic_weaponmaster(self._list_view.value))


    @staticmethod
    def _quit():
        raise NextScene("TOWN")


class ShopFrameWizard(Frame):
    def __init__(self, screen):
        super().__init__(screen,
                         30,
                         60,
                         can_scroll=False,
                         title="WIZARD UPGRADE SHOP",
                         x=0, y=0
                         )
        self.items = FightController.get_services_wizard()
        self.palette = get_palette()
        print(self.items)
        self._list_view = ListBox(
            Widget.FILL_FRAME,
            self.items,
            name="UPGRADER",
            add_scroll_bar=True,
            on_change=self._on_pick,
            on_select=self._buy)
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(self._list_view)
        layout.add_widget(Divider())
        layout2 = Layout([1, 1, 1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Quit", self._quit), 3)
        self.price_label = Label(self.get_price())
        self.your_gold_label = Label("YOUR GOLD: {}".format(self.get_gold()))
        self.your_statistic = Label(self.get_statistic())
        layout2.add_widget(self.price_label,0)
        layout2.add_widget(self.your_statistic, 1)
        layout2.add_widget(self.your_gold_label,2)
        self.fix()

    def _on_pick(self):
        self.price_label.text = self.get_price()
        self.your_statistic.text = self.get_statistic()
        self.your_gold_label.text = "YOUR GOLD: {}".format(self.get_gold())
    def _buy(self):
        if(FightController.isEnoughGold(FightController.get_wizard_price(self._list_view.value))):
            self.save()
            FightController.buy_service_wizard(self._list_view.value)
            self.your_statistic.text = self.get_statistic()
            self.your_gold_label.text = "YOUR GOLD: {}".format(self.get_gold())
    def get_gold(self):
        return FightController.get_player_gold()

    def get_price(self):
        return "PRICE: {}".format(FightController.get_wizard_price(self._list_view.value))
    def get_statistic(self):
        if(self._list_view.value == "FIREBALL"):
            print("DAMAGE: {}".format(FightController.get_fireball_dmg()))
            return "DAMAGE: {}".format(FightController.get_fireball_dmg())
        if (self._list_view.value == "HOLYMISSLE"):
            return "DAMAGE: {}".format(FightController.get_holymissle_dmg())
        if (self._list_view.value =="THUNDERSTRIKE"):
            return "DAMAGE: {}".format(FightController.get_thunderstrike_dmg())
        if (self._list_view.value == "HP"):
            return "HP: {}".format(FightController.getMaxPlayerHP())
        if (self._list_view.value == "MANA"):
            return "MANA: {}".format(FightController.get_maxmana())
        if(self._list_view.value == "REST"):
            return "REST: {}".format(FightController.get_rest_stats())





    @staticmethod
    def _quit():
        raise NextScene("TOWN")




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
        layout.add_widget(Button("               CONTINUE", self._continue, add_box=False), 1)
        self.gold_reward = Label(self.get_reward())
        layout.add_widget(self.gold_reward,1)
        self.fix()

    def _continue(self):
        FightController.get_reward()
        raise NextScene("TOWN")

    def get_reward(self):
        return "         Your Reward is: {}".format(FightController.show_reward())

    #poprawic

    def _update(self, frame_no):
        self.gold_reward.text = self.get_reward()
        super(gotoMenu, self)._update(frame_no)

class EndGame(Frame):
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
        raise StopApplication("YOU WIN THE GAME CONGRATULATION")



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
                         11,
                         60,
                         can_scroll=False,
                         title="TOWN",
                         x=screen.width//2-32, y=screen.height//2 -15
                         )
        self.set_theme("green")
        layout = Layout([1,1,1], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Button("     NEXT FIGHT ", self._fight, add_box=False), 1)
        layout.add_widget(Divider(line_char=""),1)
        layout.add_widget(Button("       WIZARD", self._wizard, add_box=False), 1)
        layout.add_widget(Divider(line_char=""),1)
        layout.add_widget(Button("     BLACKSMITH", self._blacksmith, add_box=False), 1)
        layout.add_widget(Divider(line_char=""),1)
        layout.add_widget(Button("    WEAPONMASTER", self._weaponmaster, add_box=False), 1)
        layout.add_widget(Divider(line_char=""),1)
        layout.add_widget(Button("        QUIT", self._quit, add_box=False), 1)
        self.fix()
    @staticmethod
    def _fight():
        raise NextScene(FightController.scene_controller("FIGHT"))

    @staticmethod
    def _wizard():
        raise NextScene("WIZARD")

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
class Reaper(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Reaper,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.reaper())
            },
        colour = Screen.COLOUR_RED,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )

class Centaur(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Centaur,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.centaur())
            },
        colour = Screen.COLOUR_RED,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )

class Dragon(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Dragon,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.dragon())
            },
        colour = Screen.COLOUR_RED,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )

class Wizard(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Wizard,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.Wizard())
            },
        colour = Screen.COLOUR_WHITE,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )

class Weaponmaster(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Weaponmaster,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.WeaponMaster())
            },
        colour = Screen.COLOUR_WHITE,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )

class Blacksmith(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(Blacksmith,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.Blacksmith())
            },
        colour = Screen.COLOUR_WHITE,
        path = path,
        start_frame = start_frame,
        stop_frame = stop_frame
        )

class TownSprite(Sprite):
    def __init__(self, screen,path, start_frame=0, stop_frame=0):
        super(TownSprite,self).__init__(
            screen,
            renderer_dict={
             "default": StaticRenderer(GameSprites.Town())
            },
        colour = Screen.COLOUR_WHITE,
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
    TownSpritePath = PlayerMove(screen, screen.width//2, screen.height-8)
    effectsTOWN = [
        TownSprite(screen, TownSpritePath),
        Town(screen)
    ]
    scenes.append(Scene(effectsTOWN, -1, name="TOWN"))
    #SCENY REAPER FIGHT#
    #SCENY REAPER FIGHT#
    #SCENY REAPER FIGHT#
    global player
    global path
    global devilpath
    global Reaper
    path = PlayerMove(screen, 10, screen.height // 2-3)
    devilpath = PlayerMove(screen, screen.width-20, screen.height // 2-3)

    effectsFIGHTREAPER = [
        Player(screen, path),
        Reaper(screen, devilpath),
        FightFrame(screen),
    ]
    scenes.append(Scene(effectsFIGHTREAPER, -1, name="FIGHTREAPER"))
    attackPath = Path()
    attackPath.jump_to( 10, screen.height // 2)
    #attackPath.move_straight_to(16, 10, (screen.width + 16) // 2)
    #attackPath.wait(100)
    effectsPlayerAttackReaperWeapon = [
        Player(screen, attackPath),
        Reaper(screen, devilpath),
        NextSceneFrame(screen,"PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackReaperWeapon, -1, name="PLAYERATTACKREAPERWEAPON"))
    effectsPlayerAttackReaperFireball = [
        Player(screen, attackPath),
        Reaper(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackReaperFireball, -1, name="PLAYERATTACKREAPERFIREBALL"))
    effectsPlayerAttackReaperHollymissle = [
        Player(screen, attackPath),
        Reaper(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackReaperHollymissle, -1, name="PLAYERATTACKREAPERHOLYMISSLE"))
    effectsPlayerAttackReaperThunderStrike = [
        Player(screen, attackPath),
        Reaper(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackReaperThunderStrike, -1, name="PLAYERATTACKREAPERTHUNDERSTRIKE"))
    effectsPlayerAttackReaperRest= [
        Player(screen, attackPath),
        Reaper(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackReaperRest, -1, name="PLAYERATTACKREAPERREST"))

    effectsEnemyAttackReaper = [
        Player(screen,path),
        Reaper(screen, devilpath),
        NextSceneFrame(screen,"ENEMYTURN")
    ]
    scenes.append(Scene(effectsEnemyAttackReaper, -1, name="ENEMYATTACKREAPER"))
    effectsAttackTypeReaper = [
        Player(screen, path),
        Reaper(screen, devilpath),
        AttackType(screen)
    ]
    scenes.append(Scene(effectsAttackTypeReaper, -1, name="ATTACKTYPEREAPER"))
    effectsSpellTypeReaper = [
        Player(screen, path),
        Reaper(screen, devilpath),
        SpellType(screen)
    ]
    scenes.append(Scene(effectsSpellTypeReaper, -1, name="SPELLTYPEREAPER"))
    # SCENY CENTAUR FIGHT#
    # SCENY CENTAUR FIGHT#
    # SCENY CENTAUR FIGHT#
    global Centaur
    path = PlayerMove(screen, 10, screen.height // 2 - 3)
    devilpath = PlayerMove(screen, screen.width - 20, screen.height // 2 - 3)

    effectsFIGHTCentaur = [
        Player(screen, path),
        Centaur(screen, devilpath),
        FightFrame(screen),
    ]
    scenes.append(Scene(effectsFIGHTCentaur, -1, name="FIGHTCENTAUR"))
    attackPath = Path()
    attackPath.jump_to(10, screen.height // 2)
    # attackPath.move_straight_to(16, 10, (screen.width + 16) // 2)
    # attackPath.wait(100)
    effectsPlayerAttackCentaurWeapon = [
        Player(screen, attackPath),
        Centaur(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackCentaurWeapon, -1, name="PLAYERATTACKCENTAURWEAPON"))
    effectsPlayerAttackCentaurFireball = [
        Player(screen, attackPath),
        Centaur(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackCentaurFireball, -1, name="PLAYERATTACKCENTAURFIREBALL"))
    effectsPlayerAttackCentaurHollymissle = [
        Player(screen, attackPath),
        Centaur(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackCentaurHollymissle, -1, name="PLAYERATTACKCENTAURHOLYMISSLE"))
    effectsPlayerAttackCentaurThunderStrike = [
        Player(screen, attackPath),
        Centaur(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackCentaurThunderStrike, -1, name="PLAYERATTACKCENTAURTHUNDERSTRIKE"))
    effectsPlayerAttackCentaurRest = [
        Player(screen, attackPath),
        Centaur(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackCentaurRest, -1, name="PLAYERATTACKCENTAURREST"))

    effectsEnemyAttackCentaur = [
        Player(screen, path),
        Centaur(screen, devilpath),
        NextSceneFrame(screen, "ENEMYTURN")
    ]
    scenes.append(Scene(effectsEnemyAttackCentaur, -1, name="ENEMYATTACKCENTAUR"))
    effectsAttackTypeCentaur = [
        Player(screen, path),
        Centaur(screen, devilpath),
        AttackType(screen)
    ]
    scenes.append(Scene(effectsAttackTypeCentaur, -1, name="ATTACKTYPECENTAUR"))
    effectsSpellTypeCentaur = [
        Player(screen, path),
        Centaur(screen, devilpath),
        SpellType(screen)
    ]
    scenes.append(Scene(effectsSpellTypeCentaur, -1, name="SPELLTYPECENTAUR"))
    #SCENY DRAGON FIGHT
    # SCENY DRAGON FIGHT
    global Dragon
    path = PlayerMove(screen, 10, screen.height // 2 - 3)
    devilpath = PlayerMove(screen, screen.width - 20, screen.height // 2 - 3)

    effectsFIGHTDragon = [
        Player(screen, path),
        Dragon(screen, devilpath),
        FightFrame(screen),
    ]
    scenes.append(Scene(effectsFIGHTDragon, -1, name="FIGHTDRAGON"))
    attackPath = Path()
    attackPath.jump_to(10, screen.height // 2)
    # attackPath.move_straight_to(16, 10, (screen.width + 16) // 2)
    # attackPath.wait(100)
    effectsPlayerAttackDragonWeapon = [
        Player(screen, attackPath),
        Dragon(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackDragonWeapon, -1, name="PLAYERATTACKDRAGONWEAPON"))
    effectsPlayerAttackDragonFireball = [
        Player(screen, attackPath),
        Dragon(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackDragonFireball, -1, name="PLAYERATTACKDRAGONFIREBALL"))
    effectsPlayerAttackDragonHollymissle = [
        Player(screen, attackPath),
        Dragon(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackDragonHollymissle, -1, name="PLAYERATTACKDRAGONHOLYMISSLE"))
    effectsPlayerAttackDragonThunderStrike = [
        Player(screen, attackPath),
        Dragon(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackDragonThunderStrike, -1, name="PLAYERATTACKDRAGONTHUNDERSTRIKE"))
    effectsPlayerAttackDragonRest = [
        Player(screen, attackPath),
        Dragon(screen, devilpath),
        NextSceneFrame(screen, "PLAYERTURN")
    ]
    scenes.append(Scene(effectsPlayerAttackDragonRest, -1, name="PLAYERATTACKDRAGONREST"))

    effectsEnemyAttack = [
        Player(screen, path),
        Dragon(screen, devilpath),
        NextSceneFrame(screen, "ENEMYTURN")
    ]
    scenes.append(Scene(effectsEnemyAttack, -1, name="ENEMYATTACKDRAGON"))
    effectsAttackTypeDragon = [
        Player(screen, path),
        Dragon(screen, devilpath),
        AttackType(screen)
    ]
    scenes.append(Scene(effectsAttackTypeDragon, -1, name="ATTACKTYPEDRAGON"))
    effectsSpellTypeDragon = [
        Player(screen, path),
        Dragon(screen, devilpath),
        SpellType(screen)
    ]
    scenes.append(Scene(effectsSpellTypeDragon, -1, name="SPELLTYPEDRAGON"))
    ## inne
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

    effectsEndGame = [
        Player(screen, path),
        EndGame(screen),
        Cycle(
            screen,
            FigletText("YOU WIN", font='standard'),
            screen.height // 2 - 15),

    ]
    scenes.append(Scene(effectsEndGame, -1, name="ENDGAME"))
    BlacksmithPath = PlayerMove(screen, screen.width - 28, screen.height // 2 + 5)
    effectsBlackSmith = [
        Blacksmith(screen,BlacksmithPath),
        ShopFrameBlackSmith(screen)
    ]
    scenes.append(Scene(effectsBlackSmith, -1, name="BLACKSMITH"))
    WeaponmasterPath = PlayerMove(screen, screen.width - 34, screen.height // 2 - 5)
    effectsWeaponmaster = [
        Weaponmaster(screen, WeaponmasterPath),
        ShopFrameWeaponMaster(screen)
    ]
    scenes.append(Scene(effectsWeaponmaster, -1, name="WEAPONMASTER"))
    WizardPath = PlayerMove(screen, screen.width-28, screen.height // 2)
    effectsWizard = [
        Wizard(screen,WizardPath),
        ShopFrameWizard(screen)
    ]
    scenes.append(Scene(effectsWizard, -1, name="WIZARD"))
    screen.play(scenes, stop_on_resize=True, start_scene=scene)

def screenchanger():
    last_scene = None
    while True:
        try:
            Screen.wrapper(game,catch_interrupt=True,arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            pass
