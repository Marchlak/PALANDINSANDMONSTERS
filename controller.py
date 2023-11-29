import model as mod
from model import Player, Armor,Weapon,OffensiveSpell,Monster
armor = Armor("basic",10,100 )
weapon = Weapon("Sword", 100,100)
monster1 = Monster("Reaper",40,120,"HOLY","THUNDER")
monster2 = Monster("Centaur", 50,200,"THUNDER","HOLY")
monster3 = Monster("Dragon", 50,300,"HOLY","FIRE")
monster4 = Monster("Bezimienny", 9999,9999,"HOLY","FIRE")
monsters = [ monster1, monster2,monster3, monster4]
armortobuy1 = Armor("Cloth Armor",10,20 )
armortobuy2 = Armor("Bramble Vest",20,100 )
armortobuy3 = Armor("Thornmail",30,200 )
weapon1 = Weapon("Better Sword", 50,10)
weapon2 = Weapon("Bigger Sword", 100,100)
weapon3 = Weapon("B.F Sword", 200,200)

class Shop:
    def __init__(self):
        self.items = []  # List to store Weapon and Armor objects

    def add_item(self, item):
        """Add a Weapon or Armor object to the shop."""
        self.items.append(item)

    def list_items(self):
        """List all items in the shop."""
        return [(item.name, item.price) for item in self.items]

    def get_item_names(self):
        """Return the names of all items in the shop."""
        return tuple(item.name for item in self.items)

    def buy_item(self, item_price, buyer):
        """Handle the purchase of an item by a buyer."""
        # Find the item in the shop
        item = next((item for item in self.items if item.price == item_price), None)
        if item is None:
            return None

        # Check if the buyer has enough funds
        if buyer.gold < item.price:
            return None

        # Transfer ownership of the item
        buyer.wear(item)
        buyer.minus_gold(item.price)
        self.items.remove(item)

    def get_item_attribute(self, item_value):
        """Return the specific attribute of an item based on its class."""
        item = next((item for item in self.items if item.price == item_value), None)
        if item is None:
            return None

        if isinstance(item, Armor):
            return item.reduction
        elif isinstance(item, Weapon):
            return item.damage
        else:
            return None

class Wizard:
    def __init__(self):
        self.services = [
            ("UPGRADE FIREBALL +20 DMG", "FIREBALL", 50),
            ("UPGRADE HOLYMISSLE + 20 DMG", "HOLYMISSLE", 50),
            ("UPGRADE THUNDERSTRIKE + 20 DMG", "THUNDERSTRIKE", 50),
            ("UPGRADE MAX HP + 30 HP", "HP", 30),
            ("UPGRADE MAX MANA + 20 MANA", "MANA", 30),
            ("UPGRADE REST + 10", "REST", 30)
        ]

    def list_services(self):
        """List all services offered by the wizard."""
        return [(service[0], service[1]) for service in self.services]

    def get_service_price(self, internal_service_name):
        """Get the price of a service based on its internal name."""
        service = next((s for s in self.services if s[1] == internal_service_name), None)
        if service is None:
            return None
        return service[2]

    def perform_service(self, internal_service_name, player):
        """Perform a service for a player."""
        # Find the service in the wizard's list
        service = next((s for s in self.services if s[1] == internal_service_name), None)
        if service is None:
            return None

        # Get the cost of the service
        service_cost = service[2]

        # Check if the player has enough gold
        if player.gold < service_cost:
            return None

        # Perform the service
        if internal_service_name == "FIREBALL":
            player.upgrade_spell("FIREBALL")
        elif internal_service_name == "HOLYMISSLE":
            player.upgrade_spell("HOLYMISSLE")
        elif internal_service_name == "THUNDERSTRIKE":
            player.upgrade_spell("THUNDERSTRIKE")
        elif internal_service_name == "HP":
            player.upgrade_hp(30)
        elif internal_service_name == "MANA":
            player.upgrade_mana(20)
        elif internal_service_name == "REST":
            player.upgrade_rest(10)

        # Deduct the cost from the player's gold
        player.minus_gold(service_cost)

wizard = Wizard()

BlackSmithShop = Shop()
BlackSmithShop.add_item(armortobuy1)
BlackSmithShop.add_item(armortobuy2)
BlackSmithShop.add_item(armortobuy3)
WeaponMasterShop = Shop()
WeaponMasterShop.add_item(weapon1)
WeaponMasterShop.add_item(weapon2)
WeaponMasterShop.add_item(weapon3)
class Fight:
    def __init__(self):
        self._player = Player(armor,weapon,150,50,40)
        self._enemies = monsters
        self._current = self._enemies[0]
        self._iterator = 0
        self._lastdamageplayer = 0
        self._lastdamagemonster = 0
        self._ismonsterdead = False
        self._isplayerdead = False
        self._isresting = False
        self._blacksmith = BlackSmithShop
        self._weaponmaster = WeaponMasterShop
        self._wizard = wizard
    def enemyTurn(self):

        self._lastdamagemonster = self._player.take_damage(self._current.damage)
        self._isplayerdead = self._player.is_dead()
        print("damage {} hp {} ".format(self._current.damage, self._player.hp))
    def playerTurn(self, option):
        print("damage {} hp {} ".format(self._player.damage(option), self._current.hp))
        self._lastdamageplayer = self._current.take_damage(self._player.damage(option))
        self._ismonsterdead = self._current.is_dead()

    def setAttacktype(self,at):
        self._current.attacktype = at
    def changeCurrentEnemy(self):
        self._iterator += 1
        self._current = self._enemies[self._iterator]
    def getMaxPlayerHP(self):
        return self._player.maxhp
    def getPlayerHP(self):
        return self._player.hp
    def getMaxMonsterHP(self):
        return self._current.maxhp
    def getMonsterHP(self):
        return self._current.hp
    @property
    def getLastMonsterDamage(self):
        return self._lastdamagemonster
    @property
    def getLastPlayerDamage(self):
        return self._lastdamageplayer
    @property
    def isPlayerDead(self):
        return self._isplayerdead
    @property
    def isMonsterDead(self):
        return self._ismonsterdead


    def getMonsterName(self):
        return self._current.name

    def getPlayerName(self):
        return self._player.name
    def check_mana(self,mana):
       return self._player.enoughMana(mana)
    def get_mana(self):
        print("MANA IN CONTROLER {}".format(self._player.mana))
        return self._player.mana

    def get_maxmana(self):
        return self._player.maxmana
    def rest(self):
        self._player.rest()
        self._isresting = True
        print(self._isresting)

    @property
    def isresting(self):
        return self._isresting

    def setisresting(self, value):
        self._isresting = value

    def isEnoughGold(self,gold):
        if(self._player.gold >= gold):
            return True
        else:
            return False

    def get_items_blacksmith(self):
       return self._blacksmith.list_items()

    def buy_item_blacksmith(self,value):
        self._blacksmith.buy_item(value,self._player)
    def get_items_weaponmaster(self):
       return self._weaponmaster.list_items()
    def get_statistic_weaponmaster(self, value):
        return self._weaponmaster.get_item_attribute(value)

    def get_statistic_blacksmith(self,value):
        return self._blacksmith.get_item_attribute(value)

    def buy_item_weaponmaster(self,value):
        self._weaponmaster.buy_item(value,self._player)

    def get_player_gold(self):
        return self._player.gold

    def get_services_wizard(self):
        return self._wizard.list_services()

    def buy_service_wizard(self,service_name):
        self._wizard.perform_service(service_name,self._player)

    def get_wizard_price(self,service_name):
        return self._wizard.get_service_price(service_name)
    def get_fireball_dmg(self):
        return self._player.get_spell_damage("FIREBALL")
    def get_holymissle_dmg(self):
        return self._player.get_spell_damage("HOLYMISSLE")
    def get_thunderstrike_dmg(self):
        return self._player.get_spell_damage("THUNDERSTRIKE")

    def get_rest_stats(self):
        return self._player.get_rest_stats()



    def reset_after_win(self):
        self._player.set_hp(self._player.maxhp)
        self._player.set_mana(self._player.maxmana)
        self._iterator += 1
        self._current = self._enemies[self._iterator]

    def scene_controller(self,scenetype):
        if(self._iterator == 0):
            if(scenetype=="WEAPON"):
                return "PLAYERATTACKREAPERWEAPON"
            if(scenetype=="FIREBALL"):
                return "PLAYERATTACKREAPERFIREBALL"
            if(scenetype=="HOLYMISSLE"):
                return "PLAYERATTACKREAPERHOLYMISSLE"
            if(scenetype=="THUNDERSTRIKE"):
                return "PLAYERATTACKREAPERTHUNDERSTRIKE"
            if(scenetype=="REST"):
                return "PLAYERATTACKREAPERREST"
            if(scenetype=="FIGHT"):
                 return "FIGHTREAPER"
            if (scenetype == "ATTACKTYPE"):
                return "ATTACKTYPEREAPER"
            if (scenetype == "SPELLTYPE"):
                return "SPELLTYPEREAPER"
            if (scenetype == "ENEMYATTACK"):
                return "ENEMYATTACKREAPER"
            if(scenetype == "WIN"):
                return "WIN"
        if (self._iterator == 1):
            if (scenetype == "WEAPON"):
                return "PLAYERATTACKCENTAURWEAPON"
            if (scenetype == "FIREBALL"):
                return "PLAYERATTACKCENTAURFIREBALL"
            if (scenetype == "HOLYMISSLE"):
                return "PLAYERATTACKCENTAURHOLYMISSLE"
            if (scenetype == "THUNDERSTRIKE"):
                return "PLAYERATTACKCENTAURTHUNDERSTRIKE"
            if (scenetype == "REST"):
                return "PLAYERATTACKCENTAURREST"
            if (scenetype == "FIGHT"):
                return "FIGHTCENTAUR"
            if (scenetype == "ATTACKTYPE"):
                return "ATTACKTYPECENTAUR"
            if (scenetype == "SPELLTYPE"):
                return "SPELLTYPECENTAUR"
            if (scenetype == "ENEMYATTACK"):
                return "ENEMYATTACKCENTAUR"
            if (scenetype == "WIN"):
                return "WIN"
        if (self._iterator == 2):
            if (scenetype == "WEAPON"):
                return "PLAYERATTACKDRAGONWEAPON"
            if (scenetype == "FIREBALL"):
                return "PLAYERATTACKDRAGONFIREBALL"
            if (scenetype == "HOLYMISSLE"):
                return "PLAYERATTACKDRAGONHOLYMISSLE"
            if (scenetype == "THUNDERSTRIKE"):
                return "PLAYERATTACKDRAGONTHUNDERSTRIKE"
            if (scenetype == "REST"):
                return "PLAYERATTACKDRAGONREST"
            if (scenetype == "FIGHT"):
                return "FIGHTDRAGON"
            if (scenetype == "ATTACKTYPE"):
                return "ATTACKTYPEDRAGON"
            if (scenetype == "SPELLTYPE"):
                return "SPELLTYPEDRAGON"
            if (scenetype == "ENEMYATTACK"):
                return "ENEMYATTACKDRAGON"
            if (scenetype == "WIN"):
                return "WIN"
        if (self._iterator == 3):
            if (scenetype == "WIN"):
                return "ENDGAME"

    def get_reward(self):
        if (self._iterator == 1):
            self._player.add_gold(100)
        if(self._iterator == 2):
            self._player.add_gold(150)
        if (self._iterator == 3):
            self._player.add_gold(250)
    def show_reward(self):
        if (self._iterator == 1):
            return 100
        if(self._iterator == 2):
            return 150
        if (self._iterator == 3):
            return 250




