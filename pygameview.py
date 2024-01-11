import pygame, sys
from controller import Fight
from collections import deque


def render_text(screen, text, position, font_size, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    rendered_text = font.render(text, True, color)
    text_rect = rendered_text.get_rect(center=position)
    screen.blit(rendered_text, text_rect)
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.disable = False
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.disable_color = (177, 180, 181)
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def disable_button(self,dis):
        self.disable = dis

    def checkForInput(self, position):
        if (position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)) and (self.disable == False):
            return True
        return False

    def changeColor(self, position):
        if(self.disable == True):
            self.text = self.font.render(self.text_input, True, self.disable_color)
        elif position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
class ListboxShop:
    def __init__(self,x,y, name):
        image = pygame.image.load("assets/icons/listbox2.png").convert_alpha()
        self.background_image = pygame.transform.scale(image,(image.get_width()*15,image.get_height()*15))
        self.x = x
        self.y = y
        self.name = name
        self.x_start = -200
        self.y_start = -350
        self.title_font = get_font(12)
        self.status_font = get_font(10)
        self.shop_font = get_font(30)
        self.buy_font = get_font(40)

        self.icons = []
        if(name=="blacksmith"):
            image = pygame.image.load("assets/icons/clotharmor.png")
            image = pygame.transform.scale(image,(image.get_width()*0.75,image.get_height()*0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/bramblevest.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/thornmail.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/thornmail.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/thornmail.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/thornmail.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
        if(name=="weaponmaster"):
            image = pygame.image.load("assets/icons/bettersword.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/biggersword.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/bfsword.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
        if(name=="wizard"):
            image = pygame.image.load("assets/icons/fireball.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/holystirke.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/thunderstrike.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/hp.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/mana.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)
            image = pygame.image.load("assets/icons/rest.png")
            image = pygame.transform.scale(image, (image.get_width() * 0.75, image.get_height() * 0.75))
            self.icons.append(image)

        image = pygame.image.load("assets/icons/button_long.png")
        self.button_image = pygame.transform.scale(image,(image.get_width(),image.get_height()))
        image = pygame.image.load("assets/icons/banner.png")
        self.banner = pygame.transform.scale(image,(image.get_width()*5,image.get_height()*5))

        self.rect = self.background_image.get_rect(center=(self.x, self.y))
        self.buy_color = (255, 255, 255)
    def update(self, screen, position):
        screen.blit(self.background_image, self.rect)
        screen.blit(self.banner, (self.x-35 + self.x_start, self.y + self.y_start-200))
        shop_text  = self.shop_font.render("SHOP", True, (0, 0, 0))
        screen.blit(shop_text, (self.x+150 + self.x_start, self.y + self.y_start-135))
        if (self.name == "blacksmith"):
            self.items = FightController.get_items_blacksmith()
        if (self.name == "weaponmaster"):
            self.items = FightController.get_items_weaponmaster()
        if (self.name == "wizard"):
            self.items = FightController.get_services_wizard()
        for (i,item) in enumerate(self.items):
            screen.blit(self.button_image,(self.x+self.x_start, self.y+self.y_start+i*125 - 40 ))
            text_in_tittle = item[0].replace("UPGRADE ","")
            price = item[1]
            if(self.name == "blacksmith"):
                stats = FightController.get_statistic_blacksmith(price)
            if (self.name == "weaponmaster"):
                stats = FightController.get_statistic_weaponmaster(price)
            if (self.name == "wizard"):
                if(i==0):
                    stats = FightController.get_fireball_dmg()
                if(i==1):
                    stats = FightController.get_holymissle_dmg()
                if(i==2):
                    stats = FightController.get_thunderstrike_dmg()
                if(i==3):
                    stats = FightController.getMaxPlayerHP()
                if(i==4):
                    stats = FightController.get_maxmana()
                if(i==5):
                    stats = FightController.get_rest_stats()
            tittle_text = self.title_font.render(text_in_tittle, True, (255, 255, 255))
            if (self.name == "blacksmith"):
                stat_text = self.status_font.render(f"armor {stats}", True, (255, 255, 255))
                price = f"{item[1]}"
                price_text = self.status_font.render(f"price {price} gold", True, (255, 255, 255))
            if (self.name == "weaponmaster"):
                stat_text = self.status_font.render(f"damage {stats}", True, (255, 255, 255))
                price = f"{item[1]}"
                price_text = self.status_font.render(f"price {price} gold", True, (255, 255, 255))
            if (self.name == "wizard"):
                price = FightController.get_wizard_price(item[1])
                price_text = self.status_font.render(f"price {price} gold", True, (255, 255, 255))
                if(i<3):
                    stat_text = self.status_font.render(f"damage {stats}", True, (255, 255, 255))
                if(i==3):
                    stat_text = self.status_font.render(f"hp {stats}", True, (255, 255, 255))
                if(i==4):
                    stat_text = self.status_font.render(f"mana {stats}", True, (255, 255, 255))
                if(i==5):
                    stat_text = self.status_font.render(f"stats {stats}", True, (255, 255, 255))

            screen.blit(tittle_text, (self.x+self.x_start+120, self.y+self.y_start+i*125+20 - 40))
            screen.blit(stat_text, (self.x+self.x_start+120, self.y+self.y_start+i*125+40 - 40))
            screen.blit(price_text, (self.x + self.x_start + 120, self.y + self.y_start + i * 125 + 60 - 40))
            if(self.name=="blacksmith" or self.name=="weaponmaster"):
                if(item[1]==10):
                    screen.blit(self.icons[0],(self.x+self.x_start+5, self.y+self.y_start+i*125+20 - 40))
                if (item[1] == 100):
                    screen.blit(self.icons[1], (self.x + self.x_start + 5, self.y + self.y_start + i * 125 + 20 - 40))
                if (item[1] == 200):
                    screen.blit(self.icons[2], (self.x + self.x_start + 5, self.y + self.y_start + i * 125 + 20 - 40))
            else:
                screen.blit(self.icons[i], (self.x + self.x_start + 5, self.y + self.y_start + i * 125 + 20 - 40))
            gold = FightController.get_player_gold()
            gold_text =self.shop_font.render(f"GOLD {gold}", True , (212, 175, 55))
            screen.blit(gold_text, ( self.x + self.x_start + (self.background_image.get_width() - gold_text.get_width()) // 2 - 150, self.y + self.y_start+770))
            self.changeColor(position, screen,i)

    def changeColor(self, position, screen,i):
            buy_text = self.buy_font.render("BUY", True, self.buy_color)
            button_rect = pygame.Rect(self.x + self.x_start + 275,
                                      self.y + self.y_start + i * 125 + self.button_image.get_height() // 2 - 15 - 40,
                                      buy_text.get_width(), buy_text.get_height())

            if button_rect.collidepoint(position):
                self.buy_color = (255, 255, 0)
            else:
                self.buy_color = (255, 255, 255)


            buy_text = self.buy_font.render("BUY", True, self.buy_color)
            screen.blit(buy_text, (self.x + self.x_start + 275,
                                   self.y + self.y_start + i * 125 + self.button_image.get_height() // 2 - 15 - 40))

    def get_buy_button_index(self, position):
        for i, item in enumerate(self.items):
            buy_text = self.buy_font.render("BUY", True, self.buy_color)
            button_rect = pygame.Rect(self.x + self.x_start + 275,
                                      self.y + self.y_start + i * 125 + self.button_image.get_height() // 2 - 15 - 40,
                                      buy_text.get_width(), buy_text.get_height())

            if button_rect.collidepoint(position):
                return i

        return -1

    def get_buy_button_index(self, position):
        for i, item in enumerate(self.items):
            buy_text = self.buy_font.render("BUY", True, self.buy_color)
            button_rect = pygame.Rect(self.x + self.x_start + 275,
                                      self.y + self.y_start + i * 125 + self.button_image.get_height() // 2 - 15 - 40,
                                      buy_text.get_width(), buy_text.get_height())

            if button_rect.collidepoint(position):
                return i

        return -1


    def buy(self,i):
        if(self.name == "weaponmaster"):
            FightController.buy_item_weaponmaster(self.items[i][1])
        if(self.name == "blacksmith"):
            FightController.buy_item_blacksmith(self.items[i][1])





class HealthBar:
    def __init__(self, screen, max_hp, x, y, name):
        self.screen = screen
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.name = name
        self.x = x
        self.y = y
        self.tittle_font = get_font(10)
        self.multiplayer_size = 5
        image =pygame.image.load(f'assets/icons/{name}BarFrame.png')
        self.frame_image = pygame.transform.scale(image, (image.get_width()*self.multiplayer_size,image.get_height()*self.multiplayer_size))
        image =pygame.image.load(f'assets/icons/{name}BarFill.png')
        self.fill_image = pygame.transform.scale(image, (image.get_width()*self.multiplayer_size,image.get_height()*self.multiplayer_size))
        self.move_x = 19
        self.move_y = 8
        if(name == "Monster"):
            self.frame_image = pygame.transform.flip(self.frame_image, True,False)
            self.move_x = 2
            self.move_y = 8
        self.frame_rect = self.frame_image.get_rect(topleft=(x, y))

    def update(self, current_hp):
        self.current_hp = current_hp
        self.draw()

    def draw(self):

        self.screen.blit(self.frame_image, (self.x, self.y))


        fill_percent = self.current_hp / self.max_hp


        fill_width = int(self.fill_image.get_width()* fill_percent)

        fill_rect = self.fill_image.get_rect()
        fill_rect.width = fill_width


        if(self.name == "Monster"):
            self.screen.blit(self.fill_image, (self.fill_image.get_width()-fill_width+self.x+self.move_x*self.multiplayer_size, self.y+self.move_y*self.multiplayer_size), fill_rect)
        else:
            self.screen.blit(self.fill_image, (self.x + self.move_x * self.multiplayer_size, self.y + self.move_y * self.multiplayer_size), fill_rect)

    def display_health_info(self, screen, font):
        health_info = f"{self.current_hp} / {self.max_hp}"
        health_text = font.render(health_info, True, (255, 255, 255))  # White color
        text_rect = health_text.get_rect(center=(self.frame_rect.centerx, self.frame_rect.centery - 20))
        screen.blit(health_text, text_rect)

    def checkForInput(self, position):
        if self.frame_rect.collidepoint(position):
            return True
        return False








clock = pygame.time.Clock()
fps = 60

SCREEN= None
def screen_loader():
    pygame.init()
    global SCREEN
    SCREEN = pygame.display.set_mode((1920, 1080))

pygame.display.set_caption("Game")
BG = pygame.image.load("assets/Background.png")
TOWN = pygame.image.load("assets/Town.png")
FIGHTBACKGROUND = pygame.image.load("assets/reaperfightbackground.png")
WIZARDBACKGROUND = pygame.image.load("assets/wizard.png")
BLACKSMITHBACKGROUND = pygame.image.load("assets/blacksmith.png")
WEAPONSMITHBACKGROUND = pygame.image.load("assets/weaponmaster.png")
FightController = Fight()
BUTTON = pygame.image.load("assets/icons/button.png")
BUTTON = pygame.transform.scale(BUTTON, (BUTTON.get_width()//4, BUTTON.get_height()//4))





class Paladin():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.animation = []
        self.spell_animation = []
        self.frame_index = 0
        self.spell_frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.spell_update_time = pygame.time.get_ticks()
        self.action = 0
        self.spell_action = -1
        self.wait_action = deque()

        self.wait = 0
        temp_list = []
        for i in range(3):
            image = pygame.image.load(f"assets/animations/paladin/frame_idle_{i+1}.png")
            image = pygame.transform.scale(image, (image.get_width()*6, image.get_height()*6))
            temp_list.append(image)
        self.animation.append(temp_list)
        temp_list = []
        for i in range(6):
            image = pygame.image.load(f"assets/animations/paladin/attack1_{i+1}.png")
            image = pygame.transform.scale(image, (image.get_width() * 6, image.get_height() * 6))
            temp_list.append(image)
        self.animation.append(temp_list)
        temp_list = []
        for i in range(5):
            image = pygame.image.load(f"assets/animations/paladin/attack4_{i + 1}.png")
            image = pygame.transform.scale(image, (image.get_width() * 6, image.get_height() * 6))
            temp_list.append(image)
        self.animation.append(temp_list)

        temp_list = []
        for i in range(5):
            image = pygame.image.load(f"assets/animations/paladin/fall_back_{i + 1}.png")
            image = pygame.transform.scale(image, (image.get_width() * 6, image.get_height() * 6))
            temp_list.append(image)
        self.animation.append(temp_list)

        temp_list = []
        for i in range(3):
            image = pygame.image.load(f"assets/animations/paladin/hit_{i + 1}.png")
            image = pygame.transform.scale(image, (image.get_width() * 6, image.get_height() * 6))
            temp_list.append(image)
        self.animation.append(temp_list)
        temp_list = []
        for i in range(15):
            image = pygame.image.load(f"assets/animations/spells/fire-bomb{i + 1}.png")
            image = pygame.transform.scale(image, (image.get_width() * 4.5, image.get_height() * 4.5))
            image = pygame.transform.flip(image, True, False)
            temp_list.append(image)
        self.spell_animation.append(temp_list)
        temp_list = []
        for i in range(11):
            image = pygame.image.load(f"assets/animations/spells/Lightning{i + 1}.png")
            image = pygame.transform.scale(image, (image.get_width() * 4.5, image.get_height() * 4.5))
            image = pygame.transform.flip(image, True, False)
            temp_list.append(image)
        self.spell_animation.append(temp_list)
        temp_list = []
        for i in range(11):
            image = pygame.image.load(f"assets/animations/spells/Dark-Bolt{i + 1}.png")
            image = pygame.transform.scale(image, (image.get_width() * 4.5, image.get_height() * 4.5))
            image = pygame.transform.flip(image, True, False)
            temp_list.append(image)
        self.spell_animation.append(temp_list)
        self.spell_image = self.spell_animation[0][0]
        self.image = self.animation[self.frame_index][0]
        self.rect = self.animation[0][0].get_rect()
        self.rect.center = (x,y)
    def update(self):
        if(len(self.wait_action) != 0 and self.wait_action[0] == 4):
            waitng_time = 50
            self.wait += 1
            if(self.wait > waitng_time):
                self.action = self.wait_action[0]
                self.wait_action.popleft()
                self.frame_index = 0
                self.wait = 0
            self.animations()
        elif (len(self.wait_action) != 0 and self.wait_action[0] == 3):
            waitng_time = 50
            self.wait += 1
            if (self.wait > waitng_time):
                self.action = self.wait_action[0]
                self.wait_action.popleft()
                self.frame_index = 0
                self.wait = 0
            self.animations()
        else:
            self.animations()
        if(self.spell_action >= 0):
            self.animations_spell()

    def change_position(self,x,y):
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def draw(self):
        SCREEN.blit(self.image, self.rect)
        if((self.action == 3 and self.frame_index != 4) or self.action == 4 or FightController.isresting):
            self.display_number_or_miss(SCREEN, get_font(20), FightController.getLastMonsterDamage)
        if(self.spell_action == 0):
            SCREEN.blit(self.spell_image, (1250,600))
        if (self.spell_action == 1):
            SCREEN.blit(self.spell_image, (1250, 250))
        if (self.spell_action == 2):
            SCREEN.blit(self.spell_image, (1250, 450))


    def display_number_or_miss(self, screen, font, number):
        display_text = "MISS!" if number == 0 else str(number)
        display_text = f"Zzz.. +{FightController.get_rest_stats()} stats" if FightController._isresting else str(number)
        text_surface = font.render(display_text, True, (255, 0, 0))  # Red color for the text
        text_rect = text_surface.get_rect(center=(self.rect.centerx-75, self.rect.top))
        screen.blit(text_surface, text_rect)


    def set_action(self, action):
        if(action == 4):
            self.wait_action.append(action)
        elif(action == 5):
            self.action= 2
            self.spell_action=0
        elif(action == 6):
            self.action= 2
            self.spell_action = 1
        elif(action == 7):
            self.action= 2
            self.spell_action = 2
        elif (action == 3):
            self.wait_action.append(action)
        else:
            self.action = action
            self.frame_index = 0
    def animations_spell(self):
        animation_cooldown = 100
        self.spell_image = self.spell_animation[self.spell_action][self.spell_frame_index]
        if (pygame.time.get_ticks() - self.spell_update_time > animation_cooldown):
            self.spell_update_time = pygame.time.get_ticks()
            self.spell_frame_index += 1
        if (self.spell_frame_index >= len(self.spell_animation[self.spell_action])):
            self.spell_action = -1
            self.spell_frame_index = 0


    def animations(self):
        if(self.action != 4):
            animation_cooldown = 200
        else:
            animation_cooldown = 500
        self.image = self.animation[self.action][self.frame_index]
        if (pygame.time.get_ticks() - self.update_time > animation_cooldown):
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if (self.frame_index >= len(self.animation[self.action])):
            if(self.action==0):
                self.frame_index = 0
            elif(self.action==3):
                self.frame_index -= 1
            elif(self.action != 0):
                self.action = 0
                self.frame_index = 0



class Monster():
    def __init__(self,x,y,name):
        self.name = name
        self.x = x
        self.y = y
        self.animation_idle = []
        self.animation_spells = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.action = 0
        self.wait_action = deque()
        self.wait = 0
        if(self.name == "Skeleton"):
            self.idle_counter = 4
            self.attack_counter = 8
            self.take_hit_counter = 4
            self.death_counter = 4
        if (self.name == "Bringer"):
            self.idle_counter = 8
            self.attack_counter = 10
            self.take_hit_counter = 3
            self.death_counter = 10
        if (self.name == "Demon"):
            self.idle_counter = 6
            self.attack_counter = 15
            self.take_hit_counter = 5
            self.death_counter = 22
        temp_list = []
        for i in range(self.idle_counter):
            image = pygame.image.load(f"assets/animations/{name}/frame_idle_{i}.png")
            image = pygame.transform.scale(image, (image.get_width() * 4.5, image.get_height() * 4.5))
            if(self.name != "Bringer" and self.name != "Demon"):
                image = pygame.transform.flip(image, True, False)
            temp_list.append(image)
        self.animation_idle.append(temp_list)
        temp_list = []
        for i in range(self.attack_counter):
            image = pygame.image.load(f"assets/animations/{name}/frame_attack_{i}.png")
            image = pygame.transform.scale(image, (image.get_width() * 4.5, image.get_height() * 4.5))
            if (self.name != "Bringer" and self.name != "Demon"):
                image = pygame.transform.flip(image, True, False)
            temp_list.append(image)
        self.animation_idle.append(temp_list)
        temp_list = []
        for i in range(self.take_hit_counter):
            image = pygame.image.load(f"assets/animations/{name}/frame_take_hit_{i}.png")
            image = pygame.transform.scale(image, (image.get_width() * 4.5, image.get_height() * 4.5))
            if (self.name != "Bringer" and self.name != "Demon"):
                image = pygame.transform.flip(image, True, False)
            temp_list.append(image)
        self.animation_idle.append(temp_list)
        temp_list = []
        for i in range(self.death_counter):
            image = pygame.image.load(f"assets/animations/{name}/frame_death_{i}.png")
            image = pygame.transform.scale(image, (image.get_width() * 4.5, image.get_height() * 4.5))
            if (self.name != "Bringer" and self.name != "Demon"):
                image = pygame.transform.flip(image, True, False)
            temp_list.append(image)

        self.animation_idle.append(temp_list)
        image = pygame.image.load(f"assets/animations/{name}/frame_idle_0.png")
        if (self.name != "Bringer" and self.name != "Demon"):
            image = pygame.transform.flip(image, True, False)
        self.image = pygame.transform.scale(image, (image.get_width()*4.5, image.get_height()*4.5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        SCREEN.blit(self.image, self.rect)
        if((self.action ==3 and self.frame_index != self.death_counter -1) or self.action == 2):
            self.display_number_or_miss(SCREEN,get_font(20) ,FightController.getLastPlayerDamage)

    def display_number_or_miss(self, screen, font, number):
        display_text = "MISS!" if number == 0 else str(number)
        text_surface = font.render(display_text, True, (255, 0, 0))  # Red color for the text
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.top))
        screen.blit(text_surface, text_rect)

    def set_action(self, action):
        if(action==2):
            self.wait_action.append(2)
        elif(action==1):
            self.wait_action.append(1)
        elif(action==3):
            self.wait_action.append(3)
        else:
            self.action = action
            self.frame_index = 0

    def update(self):
        if(len(self.wait_action) != 0 and self.wait_action[0]==2):
            waiting_time = 10
            self.wait += 1
            if(self.wait > waiting_time):
                self.action = self.wait_action[0]
                self.wait_action.popleft()
                self.frame_index = 0
                self.wait = 0
            self.animations()
        elif(len(self.wait_action) !=0 and self.wait_action[0]==1):
            waiting_time = 15
            self.wait += 1
            if (self.wait > waiting_time):
                self.action = self.wait_action[0]
                self.wait_action.popleft()
                self.frame_index = 0
                self.wait = 0
                FightController.setisresting(False)
            self.animations()
        elif (len(self.wait_action) != 0 and self.wait_action[0] == 3):
            waiting_time = 15
            self.wait += 1
            if (self.wait > waiting_time):
                self.action = self.wait_action[0]
                self.frame_index = 0
                self.wait_action.popleft()
                self.wait = 0
            self.animations()
        else:
            self.animations()


    def animations(self):
        animation_cooldown = 200
        self.image = self.animation_idle[self.action][self.frame_index]
        if (pygame.time.get_ticks() - self.update_time > animation_cooldown):
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if (self.frame_index >= len(self.animation_idle[self.action])):

            if(self.action== 0):
                self.frame_index = 0
            elif(self.action== 3):
                self.frame_index -= 1
            elif(self.action != 0):
                self.action = 0
                self.frame_index = 0

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

paladin = Paladin(550,660)
skeleton = Monster(1400, 690, "Skeleton")
bringer = Monster(1240, 630, "Bringer")
demon = Monster(1390, 530, "Demon")

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(TOWN,(0,0))



        PLAY_BACK = Button(image=None, pos=(1820, 100),text_input="BACK", font=get_font(25), base_color="Yellow", hovering_color="Magenta")
        DUNGEON_BUTTON = Button(image=None,pos=(1045,700), text_input="DUNGEON", font=get_font(25), base_color="#00FFFFFF", hovering_color="Green")
        WIZARD_BUTTON = Button(image=None,pos=(1075,200),text_input="WIZARD", font=get_font(25), base_color="#00FFFFFF", hovering_color="Green")
        BLACKSMITH_BUTTON = Button(image=None,pos=(540,700),text_input="BLACKSMITH", font=get_font(25), base_color="#00FFFFFF", hovering_color="Green")
        WEAPONMASTER_BUTTON = Button(image=None,pos=(1375,675),text_input="WEAPONMASTER", font=get_font(25), base_color="#00FFFFFF", hovering_color="Green")

        DUNGEON_BUTTON.changeColor(PLAY_MOUSE_POS)
        DUNGEON_BUTTON.update(SCREEN)

        WIZARD_BUTTON.changeColor(PLAY_MOUSE_POS)
        WIZARD_BUTTON.update(SCREEN)

        BLACKSMITH_BUTTON.changeColor(PLAY_MOUSE_POS)
        BLACKSMITH_BUTTON.update(SCREEN)

        WEAPONMASTER_BUTTON.changeColor(PLAY_MOUSE_POS)
        WEAPONMASTER_BUTTON.update(SCREEN)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DUNGEON_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    fight()
                if WIZARD_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    wizard()
                if BLACKSMITH_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    blacksmith()
                if WEAPONMASTER_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    weaponmaster()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        bg_image = pygame.image.load("assets/howtoplay.png")
        frame_image = pygame.image.load("assets/icons/endframe.png")
        frame_image = pygame.transform.scale(frame_image, (frame_image.get_width()*12,frame_image.get_height()*12))
        SCREEN.blit(bg_image, (0, 0))
        SCREEN.blit(frame_image,(960-frame_image.get_width()//2,300))
        x_pos = 960-frame_image.get_width()//2 + 150
        y_pos = -50
        OPTIONS_TEXT_1 = get_font(20).render("W grze zmierzysz sie z 3 przeciwnikami", True, "White")
        OPTIONS_TEXT_2 = get_font(20).render(("Sa oni podatni na różne rodzaje magii"), True, "White")
        OPTIONS_TEXT_3 = get_font(20).render(("Twoje ataki maja różna szanse na trafienie"), True, "White")
        OPTIONS_TEXT_4 = get_font(20).render(("Za wygrana otrzymasz złoto"), True, "White")
        OPTIONS_TEXT_5 = get_font(20).render(("Możesz kupować różne ulepszenia u handlarzy"),True, "White")
        SCREEN.blit(OPTIONS_TEXT_1,(x_pos,500+y_pos))
        SCREEN.blit(OPTIONS_TEXT_2, (x_pos, 550+y_pos))
        SCREEN.blit(OPTIONS_TEXT_3, (x_pos, 600+y_pos))
        SCREEN.blit(OPTIONS_TEXT_4, (x_pos, 650+y_pos))
        SCREEN.blit(OPTIONS_TEXT_5, (x_pos, 700+y_pos))

        OPTIONS_BACK = Button(image=None, pos=(1820, 100),
                              text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def blacksmith():
    blacksmith = ListboxShop(400, 540, "blacksmith")
    while True:
        clock.tick(fps)
        BLACKSMITH_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BLACKSMITHBACKGROUND, (0, 0))
        blacksmith.update(SCREEN, BLACKSMITH_MOUSE_POS)
        PLAY_BACK_BACK = Button(image=None, pos=(1820, 100), text_input="BACK", font=get_font(25),
                                base_color="WHITE",
                                hovering_color="Green")
        PLAY_BACK_BACK.changeColor(BLACKSMITH_MOUSE_POS)
        PLAY_BACK_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK_BACK.checkForInput(BLACKSMITH_MOUSE_POS):
                        play()
                    if blacksmith.get_buy_button_index(BLACKSMITH_MOUSE_POS) == 0:
                        blacksmith.buy(0)
                    if blacksmith.get_buy_button_index(BLACKSMITH_MOUSE_POS) == 1:
                        blacksmith.buy(1)
                    if blacksmith.get_buy_button_index(BLACKSMITH_MOUSE_POS) == 2:
                        blacksmith.buy(2)
        pygame.display.update()


def weaponmaster():
    weaponmaster = ListboxShop(400, 540, "weaponmaster")
    while True:
        clock.tick(fps)
        SCREEN.blit(WEAPONSMITHBACKGROUND, (0, 0))
        WEAPONMASTER_MOUSE_POS = pygame.mouse.get_pos()
        weaponmaster.update(SCREEN, WEAPONMASTER_MOUSE_POS)

        PLAY_BACK_BACK = Button(image=None, pos=(1820, 100), text_input="BACK", font=get_font(25),
                                base_color="WHITE",
                                hovering_color="Green")
        PLAY_BACK_BACK.changeColor(WEAPONMASTER_MOUSE_POS)
        PLAY_BACK_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK_BACK.checkForInput(WEAPONMASTER_MOUSE_POS):
                    play()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK_BACK.checkForInput(WEAPONMASTER_MOUSE_POS):
                        play()
                    if weaponmaster.get_buy_button_index(WEAPONMASTER_MOUSE_POS) == 0:
                        weaponmaster.buy(0)
                    if weaponmaster.get_buy_button_index(WEAPONMASTER_MOUSE_POS) == 1:
                        weaponmaster.buy(1)
                    if weaponmaster.get_buy_button_index(WEAPONMASTER_MOUSE_POS) == 2:
                        weaponmaster.buy(2)
        pygame.display.update()

def wizard():
    while True:
        clock.tick(fps)
        SCREEN.blit(WIZARDBACKGROUND, (0, 0))
        WIZARD_MOUSE_POS = pygame.mouse.get_pos()
        wizard = ListboxShop(400, 540, "wizard")
        wizard.update(SCREEN,WIZARD_MOUSE_POS)
        PLAY_BACK_BACK = Button(image=None, pos=(1820, 100), text_input="BACK", font=get_font(25),
                                base_color="White",
                                hovering_color="Green")
        PLAY_BACK_BACK.changeColor(WIZARD_MOUSE_POS)
        PLAY_BACK_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK_BACK.checkForInput(WIZARD_MOUSE_POS):
                    play()
                if wizard.get_buy_button_index(WIZARD_MOUSE_POS) == 0:
                    FightController.buy_service_wizard("FIREBALL")
                if wizard.get_buy_button_index(WIZARD_MOUSE_POS) == 1:
                    FightController.buy_service_wizard("HOLYMISSLE")
                if wizard.get_buy_button_index(WIZARD_MOUSE_POS) == 2:
                    FightController.buy_service_wizard("THUNDERSTRIKE")
                if wizard.get_buy_button_index(WIZARD_MOUSE_POS) == 3:
                    FightController.buy_service_wizard("HP")
                if wizard.get_buy_button_index(WIZARD_MOUSE_POS) == 4:
                    FightController.buy_service_wizard("MANA")
                if wizard.get_buy_button_index(WIZARD_MOUSE_POS) == 5:
                    FightController.buy_service_wizard("REST")

        pygame.display.update()

def main_menu():
    while True:
        clock.tick(fps)
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT_PALADINS = get_font(50).render("PALADINS", True, "#b68f40")
        MENU_RECT_PALADINS = MENU_TEXT_PALADINS.get_rect(center=(960, 300))
        MENU_TEXT_VS = get_font(50).render("VS", True, "#b68f40")
        MENU_RECT_VS = MENU_TEXT_VS.get_rect(center=(960, 380))
        MENU_TEXT_MONSTERS = get_font(50).render("MONSTERS", True, "#b68f40")
        MENU_RECT_MONSTERS = MENU_TEXT_MONSTERS.get_rect(center=(960, 460))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(960, 540),
                             text_input="PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/How Rect.png"), pos=(960, 620),
                                text_input="HOW TO PLAY", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(960, 700),
                             text_input="QUIT", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT_PALADINS, MENU_RECT_PALADINS)
        SCREEN.blit(MENU_TEXT_VS, MENU_RECT_VS)
        SCREEN.blit(MENU_TEXT_MONSTERS, MENU_RECT_MONSTERS)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



def fight():
    BUTTONSTATE = "MENU"
    death_timer = 0
    action_timer = 1000
    attack_timer = 80
    monster_hp_timer = 1000
    player_hp_timer = 1000
    monster_hp = FightController.getMaxMonsterHP()
    player_hp = FightController.getMaxPlayerHP()
    if(FightController._iterator == 0):
        current_monster = skeleton
        FIGHTBACKGROUND = pygame.image.load("assets/reaperfightbackground.png")
    if (FightController._iterator == 1):
        current_monster = bringer
        FIGHTBACKGROUND = pygame.image.load("assets/Backgroundbringer.png")
        attack_timer = 120
    if (FightController._iterator == 2):
        current_monster = demon
        FIGHTBACKGROUND = pygame.image.load("assets/hell.png")
        paladin.change_position(550,740)
        attack_timer = 120
    while True:
        clock.tick(fps)
        #timers
        death_timer += 1
        action_timer += 1
        player_hp_timer += 1
        monster_hp_timer +=1
        #classdefine
        FIGHT_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("Black")
        SCREEN.blit(FIGHTBACKGROUND,(0,0))
        PLAY_ATTACK = Button(image=BUTTON, pos=(660, 1000), text_input="ATTACK", font=get_font(25), base_color="#00FFFFFF",
                           hovering_color="Green")
        PLAY_MAGIC = Button(image=BUTTON, pos=(960, 1000), text_input="MAGIC", font=get_font(25), base_color="#00FFFFFF",
                           hovering_color="Green")
        PLAY_REST = Button(image=BUTTON, pos=(1260, 1000), text_input="REST", font=get_font(25), base_color="#00FFFFFF",
                           hovering_color="Green")
        PLAY_ATTACK_STRONG = Button(image=BUTTON, pos=(1100, 1000), text_input="STRONG", font=get_font(25), base_color="#00FFFFFF",
                           hovering_color="Green")
        PLAY_ATTACK_NORMAL = Button(image=BUTTON, pos=(800, 1000), text_input="NORMAL", font=get_font(25),
                                    base_color="#00FFFFFF",
                                    hovering_color="Green")
        PLAY_ATTACK_FAST = Button(image=BUTTON, pos=(500, 1000), text_input="FAST", font=get_font(25),
                                    base_color="#00FFFFFF",
                                    hovering_color="Green")
        PLAY_MAGIC_FIRE = Button(image=BUTTON, pos=(500, 1000), text_input="FIRE", font=get_font(25),
                                  base_color="#00FFFFFF",
                                  hovering_color="Green")
        PLAY_MAGIC_HOLY = Button(image=BUTTON, pos=(800, 1000), text_input="HOLY", font=get_font(25),
                                  base_color="#00FFFFFF",
                                  hovering_color="Green")
        PLAY_MAGIC_THUNDER = Button(image=BUTTON, pos=(1100, 1000), text_input="THUNDER", font=get_font(25),
                                  base_color="#00FFFFFF",
                                  hovering_color="Green")
        PLAY_BACK_BACK = Button(image=BUTTON, pos=(1400, 1000), text_input="BACK", font=get_font(25),
                                  base_color="#00FFFFFF",
                                  hovering_color="Green")
        PLAY_BACK_TO_MENU = Button(image=None, pos=(960, 620), text_input="RESTART", font=get_font(25),
                                base_color="#00FFFFFF",
                                hovering_color="Green")
        PLAY_BACK_TO_TOWN = Button(image=None, pos=(960, 620), text_input="GO TO TOWN", font=get_font(25),
                                   base_color="#00FFFFFF",
                                   hovering_color="Green")
        PLAY_EXIT = Button(image=None, pos=(960, 620), text_input="EXIT", font=get_font(25),
                                   base_color="#00FFFFFF",
                                   hovering_color="Green")
        paladinHeathBar = HealthBar(SCREEN,FightController.getMaxPlayerHP(),30,750, "Health")
        paladinManaBar = HealthBar(SCREEN,FightController.get_maxmana(),30 ,850,"Mana")
        monsterHealthBar = HealthBar(SCREEN,FightController.getMaxMonsterHP(),1495,800, "Monster")



        if(BUTTONSTATE == "MENU"):
            PLAY_REST.disable_button(False)
            PLAY_MAGIC.disable_button(False)
            PLAY_ATTACK.disable_button(False)
            PLAY_ATTACK_STRONG.disable_button(True)
            PLAY_ATTACK_NORMAL.disable_button(True)
            PLAY_ATTACK_FAST.disable_button(True)
            PLAY_MAGIC_FIRE.disable_button(True)
            PLAY_MAGIC_THUNDER.disable_button(True)
            PLAY_MAGIC_HOLY.disable_button(True)
            if (FightController.isMonsterDead or FightController.isPlayerDead or action_timer < 50):
                PLAY_REST.disable_button(True)
                PLAY_MAGIC.disable_button(True)
                PLAY_ATTACK.disable_button(True)
            PLAY_ATTACK.changeColor(FIGHT_MOUSE_POS)
            PLAY_ATTACK.update(SCREEN)
            PLAY_MAGIC.changeColor(FIGHT_MOUSE_POS)
            PLAY_MAGIC.update(SCREEN)
            PLAY_REST.changeColor(FIGHT_MOUSE_POS)
            PLAY_REST.update(SCREEN)
        elif(BUTTONSTATE == "ATTACK"):
            PLAY_ATTACK_STRONG.disable_button(False)
            PLAY_ATTACK_NORMAL.disable_button(False)
            PLAY_ATTACK_FAST.disable_button(False)
            PLAY_REST.disable_button(True)
            PLAY_MAGIC.disable_button(True)
            PLAY_ATTACK.disable_button(True)
            PLAY_MAGIC_FIRE.disable_button(True)
            PLAY_MAGIC_THUNDER.disable_button(True)
            PLAY_MAGIC_HOLY.disable_button(True)
            PLAY_ATTACK_FAST.changeColor(FIGHT_MOUSE_POS)
            PLAY_ATTACK_FAST.update(SCREEN)
            PLAY_ATTACK_NORMAL.changeColor(FIGHT_MOUSE_POS)
            PLAY_ATTACK_NORMAL.update(SCREEN)
            PLAY_ATTACK_STRONG.changeColor(FIGHT_MOUSE_POS)
            PLAY_ATTACK_STRONG.update(SCREEN)
            PLAY_BACK_BACK.changeColor(FIGHT_MOUSE_POS)
            PLAY_BACK_BACK.update(SCREEN)
        elif (BUTTONSTATE == "MAGIC"):
            PLAY_BACK_BACK.update(SCREEN)
            PLAY_REST.disable_button(True)
            PLAY_MAGIC.disable_button(True)
            PLAY_ATTACK.disable_button(True)
            PLAY_ATTACK_STRONG.disable_button(True)
            PLAY_ATTACK_NORMAL.disable_button(True)
            PLAY_ATTACK_FAST.disable_button(True)
            PLAY_MAGIC_FIRE.disable_button(False)
            PLAY_MAGIC_THUNDER.disable_button(False)
            PLAY_MAGIC_HOLY.disable_button(False)
            if not FightController.check_mana(20):
                PLAY_MAGIC_FIRE.disable_button(True)
                PLAY_MAGIC_THUNDER.disable_button(True)
                PLAY_MAGIC_HOLY.disable_button(True)
            PLAY_MAGIC_FIRE.changeColor(FIGHT_MOUSE_POS)
            PLAY_MAGIC_FIRE.update(SCREEN)
            PLAY_MAGIC_HOLY.changeColor(FIGHT_MOUSE_POS)
            PLAY_MAGIC_HOLY.update(SCREEN)
            PLAY_MAGIC_THUNDER.changeColor(FIGHT_MOUSE_POS)
            PLAY_MAGIC_THUNDER.update(SCREEN)
            PLAY_BACK_BACK.changeColor(FIGHT_MOUSE_POS)

        PLAY_BACK_TO_MENU.disable_button(True)
        PLAY_BACK_TO_TOWN.disable_button(True)
        PLAY_BACK_TO_TOWN.disable_button(True)

        current_monster.draw()
        current_monster.update()
        paladin.update()
        paladin.draw()


        if (FightController.isPlayerDead and death_timer > attack_timer//2):
            image = pygame.image.load("assets/icons/endframe.png")
            image = pygame.transform.scale(image, (image.get_width()*8, image.get_height()*8))
            image_rect = image.get_rect(center=(980, 540))
            SCREEN.blit(image, image_rect)
            PLAY_BACK_TO_TOWN.disable_button(True)
            PLAY_BACK_TO_MENU.disable_button(False)
            lost_font = get_font(30)
            you_lost_text = lost_font.render("YOU LOSE!", True, (255, 255, 255))
            lost_text_rect = you_lost_text.get_rect(center=(960, 440))
            SCREEN.blit(you_lost_text, lost_text_rect)
            PLAY_BACK_TO_MENU.changeColor(FIGHT_MOUSE_POS)
            PLAY_BACK_TO_MENU.update(SCREEN)
        if (FightController.isMonsterDead and death_timer > attack_timer//2):
            image = pygame.image.load("assets/icons/endframe.png")
            image = pygame.transform.scale(image, (image.get_width() * 8, image.get_height() * 8))
            image_rect = image.get_rect(center=(980,540))
            SCREEN.blit(image, image_rect)
            win_font = get_font(30)
            reward_font = get_font(30)
            you_win_text = win_font.render("YOU WIN!", True, (255, 255, 255))
            if(FightController._iterator == 0):
                reward_text = reward_font.render(f"YOUR REWARD is {100}G", True, (255, 255, 255))
            if (FightController._iterator == 1):
                reward_text = reward_font.render(f"YOUR REWARD is {150}G", True, (255, 255, 255))
            if(FightController._iterator == 2):
                reward_text = reward_font.render(f"YOU END THE GAME", True, (255, 255, 255))
            reward_text_rect = reward_text.get_rect(center=(960,500))
            SCREEN.blit(reward_text, reward_text_rect)
            win_text_rect = you_win_text.get_rect(center=(960,440))
            SCREEN.blit(you_win_text, win_text_rect)

            if(FightController._iterator !=2):
                PLAY_BACK_TO_MENU.disable_button(True)
                PLAY_BACK_TO_TOWN.disable_button(False)
                PLAY_BACK_TO_TOWN.changeColor(FIGHT_MOUSE_POS)
                PLAY_BACK_TO_TOWN.update(SCREEN)
            else:
                PLAY_EXIT.disable_button(False)
                PLAY_EXIT.changeColor(FIGHT_MOUSE_POS)
                PLAY_EXIT.update(SCREEN)


        paladinManaBar.update(FightController.get_mana())

        if(current_monster.action == 0):
            monsterHealthBar.update(monster_hp)
        else:
            monster_hp = FightController.getMonsterHP()
            monsterHealthBar.update(monster_hp)

        if (paladin.action == 1 or paladin.action == 0 or paladin.action == 2):
            paladinHeathBar.update(player_hp)
        else:
            player_hp = FightController.getPlayerHP()
            paladinHeathBar.update(player_hp)

        if paladinHeathBar.checkForInput(FIGHT_MOUSE_POS):
            paladinHeathBar.display_health_info(SCREEN, get_font(20))
        if monsterHealthBar.checkForInput(FIGHT_MOUSE_POS):
            monsterHealthBar.display_health_info(SCREEN, get_font(20))
        if paladinManaBar.checkForInput(FIGHT_MOUSE_POS):
            paladinManaBar.display_health_info(SCREEN, get_font(20))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_ATTACK.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "ATTACK"
                if PLAY_MAGIC.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MAGIC"
                if PLAY_BACK_BACK.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                if PLAY_ATTACK_FAST.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                    action_timer = 0
                    FightController.setAttacktype("FAST")
                    paladin.set_action(1)
                    FightController.playerTurn("WEAPON")
                    monster_hp_timer = 0
                    if not FightController.isMonsterDead:
                        player_hp_timer = 0
                        current_monster.set_action(2)
                        FightController.enemyTurn()
                        current_monster.set_action(1)
                        if not FightController.isPlayerDead:
                            paladin.set_action(4)
                        else:
                            paladin.set_action(3)
                            death_timer = 0
                    else:

                        current_monster.set_action(3)
                        death_timer = 0
                if PLAY_ATTACK_NORMAL.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                    action_timer = 0
                    FightController.setAttacktype("NORMAL")
                    paladin.set_action(1)
                    FightController.playerTurn("WEAPON")
                    monster_hp_timer = 0
                    if not FightController.isMonsterDead:
                        player_hp_timer = 0
                        current_monster.set_action(2)
                        FightController.enemyTurn()
                        current_monster.set_action(1)
                        if not FightController.isPlayerDead:
                            paladin.set_action(4)
                        else:
                            paladin.set_action(3)
                            death_timer = 0
                    else:
                        current_monster.set_action(3)
                        death_timer = 0
                if PLAY_ATTACK_STRONG.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                    action_timer = 0
                    FightController.setAttacktype("STRONG")
                    paladin.set_action(1)
                    FightController.playerTurn("WEAPON")
                    monster_hp_timer = 0
                    if not FightController.isMonsterDead:
                        player_hp_timer = 0
                        current_monster.set_action(2)
                        FightController.enemyTurn()
                        current_monster.set_action(1)
                        if not FightController.isPlayerDead:
                            paladin.set_action(4)
                        else:
                            paladin.set_action(3)
                            death_timer = 0
                    else:
                        current_monster.set_action(3)
                        death_timer = 0
                if PLAY_MAGIC_FIRE.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                    action_timer = 0
                    FightController.setAttacktype("FIRE")
                    paladin.set_action(5)
                    FightController.playerTurn("FIREBALL")
                    monster_hp_timer = 0
                    if not FightController.isMonsterDead:
                        player_hp_timer = 0
                        current_monster.set_action(2)
                        FightController.enemyTurn()
                        current_monster.set_action(1)
                        if not FightController.isPlayerDead:
                            paladin.set_action(4)
                        else:
                            paladin.set_action(3)
                            death_timer = 0
                    else:
                        current_monster.set_action(3)
                        death_timer = 0
                if PLAY_MAGIC_HOLY.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                    action_timer = 0
                    FightController.setAttacktype("HOLY")
                    paladin.set_action(6)
                    FightController.playerTurn("HOLYMISSLE")
                    monster_hp_timer = 0
                    if not FightController.isMonsterDead:
                        player_hp_timer = 0
                        current_monster.set_action(2)
                        FightController.enemyTurn()
                        current_monster.set_action(1)
                        if not FightController.isPlayerDead:
                            paladin.set_action(4)
                        else:
                            paladin.set_action(3)
                            death_timer = 0
                    else:
                        current_monster.set_action(3)
                        death_timer = 0
                if PLAY_MAGIC_THUNDER.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                    action_timer = 0
                    FightController.setAttacktype("THUNDER")
                    paladin.set_action(7)
                    FightController.playerTurn("THUNDERSTRIKE")
                    monster_hp_timer = 0
                    if not FightController.isMonsterDead:
                        player_hp_timer = 0
                        current_monster.set_action(2)
                        FightController.enemyTurn()
                        current_monster.set_action(1)
                        if not FightController.isPlayerDead:
                            paladin.set_action(4)
                        else:
                            paladin.set_action(3)
                            death_timer = 0
                    else:
                        current_monster.set_action(3)
                        death_timer = 0
                if PLAY_REST.checkForInput(FIGHT_MOUSE_POS):
                    BUTTONSTATE = "MENU"
                    action_timer = 0
                    FightController.rest()
                    player_hp = FightController.getPlayerHP()
                    if not FightController.isMonsterDead:
                        player_hp_timer = 0
                        current_monster.set_action(0)
                        FightController.enemyTurn()
                        current_monster.set_action(1)
                        if not FightController.isPlayerDead:
                            paladin.set_action(4)
                        else:
                            paladin.set_action(3)
                            death_timer = 0
                    else:
                        current_monster.set_action(3)
                        death_timer = 0
                if PLAY_BACK_TO_MENU.checkForInput(FIGHT_MOUSE_POS):
                    FightController.reset()
                    paladin.set_action(0)
                    current_monster.set_action(0)
                    main_menu()
                if PLAY_BACK_TO_TOWN.checkForInput(FIGHT_MOUSE_POS):
                    FightController.reset_after_win()
                    FightController.get_reward()
                    paladin.set_action(0)
                    current_monster.set_action(0)
                    play()
                if(PLAY_EXIT.checkForInput(FIGHT_MOUSE_POS)):
                    pygame.quit()
                    sys.exit()



        pygame.display.update()


