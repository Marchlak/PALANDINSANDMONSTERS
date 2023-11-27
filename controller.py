import model as mod
from model import Player, Armor,Weapon,OffensiveSpell,Monster
armor = Armor("basic",10,100 )
weapon = Weapon("Sword", 100,100)
monster1 = Monster("Zniwiarz",40,120,"HOLY","THUNDER")
monster2 = Monster("Diabel", 50,200,"THUNDER","FIRE")
monsters = [ monster1, monster2]
armortobuy1 = Armor("armor1",10,20 )
armortobuy2 = Armor("armor2",10,100 )
armortobuy3 = Armor("armor3",10,200 )
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

    def buy_item_weaponmaster(self,value):
        self._weaponmaster.buy_item(value,self._player)

    def get_player_gold(self):
        return self._player.gold


