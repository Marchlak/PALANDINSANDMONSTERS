import random
class Armor:
    def __init__(self, name, reduction, price):
        self._name = name
        self._reduction = reduction
        self._price = price

    # Getter dla nazwy
    @property
    def name(self):
        return self._name

    # Setter dla nazwy
    @name.setter
    def name(self, value):
        self._name = value

    # Getter dla redukcji obrażeń
    @property
    def price(self):
        return self._price
    @property
    def reduction(self):
        return self._reduction

    # Setter dla redukcji obrażeń
    @reduction.setter
    def reduction(self, value):
        self._reduction = value
class Weapon:
    def __init__(self, name, damage, price):
        self._name = name
        self._damage = damage
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

class Monster:
    def __init__(self, name, damage, hp, weakness, reduction):
        self._name = name
        self._damage = damage
        self._hp = hp
        self._maxhp = hp
        self._weakness = weakness
        self._reduction = reduction
        self._attacktype = "FAST"


    @property
    def attacktype(self):
        return self._attacktype

    @attacktype.setter
    def attacktype(self, value):
        self._attacktype = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    @property
    def hp(self):
        return self._hp

    @property
    def maxhp(self):
        return self._maxhp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        else:
            self._hp = value

    def is_dead(self):
        if(self._hp<0):
            return True
        else:
            return False

    def take_damage(self, damage):
        chance = random.randint(1, 100)
        if(self._attacktype == "FAST"):
            if chance <= 10:
                damage= 1
            self._hp = self._hp - damage//2
            #print("take_damage function damage {} hp {}".format(damage, self.hp))
            return damage//2
        elif (self._attacktype == "NORMAL"):
            if chance <= 40:
                damage=0
            self._hp = self._hp - damage
            return damage
        elif (self._attacktype == "STRONG"):
            if chance <= 60:
                damage=0
            self._hp = self._hp - damage*2
            return damage*2
        elif(self._attacktype == self._reduction):
            self._hp = self._hp - damage * 4
            return damage * 4
        elif (self.attacktype == self._reduction):
            self._hp = self._hp - damage // 2
            return damage //2
        else:
            self._hp = self._hp - damage
            return damage


class OffensiveSpell:
    def __init__(self, name, damage, price):
        self._name = name
        self._damage = damage
        self._upgrade_price = price

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    def upgrade(self, value):
        self._damage += value


class Player:
    def __init__(self, armor, weapon, hp, mana, gold):
        self._armor = armor
        self._fireball = OffensiveSpell("Fireball",40,40)
        self._holymissle = OffensiveSpell("HolyMissle",40,40)
        self._thunderstrike = OffensiveSpell("ThunderStrike",40,40)
        self._weapon = weapon
        self._hp = hp
        self._maxhp = hp
        self._mana = mana
        self._maxmana = mana
        self.name = "palladin"
        self._gold = gold
        self._rest_value = 20

    # Getter i setter dla armor

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def gold(self):
        return self._gold
    def get_gold(self, value):
        self._gold += value

    def minus_gold(self, value):
        self._gold -= value

    @property
    def mana(self):
        return self._mana


    def set_mana(self, value):
        self._mana = value

    @property
    def maxmana(self):
        return self._maxmana

    @maxmana.setter
    def maxmana(self, value):
        self._maxmana = value

    def enoughMana(self, manacost):
        if(self.mana>=manacost):
            return True
        else:
            return False
    @property
    def armor(self):
        return self._armor

    @armor.setter
    def armor(self, value):
        self._armor = value

    # Getter i setter dla spell
    @property
    def spell(self):
        return self._spell

    @spell.setter
    def spell(self, value):
        self._spell = value

    # Getter i setter dla weapon
    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value):
        self._weapon = value

    # Getter i setter dla hp
    @property
    def hp(self):
        return self._hp

    @property
    def maxhp(self):
        return self._maxhp


    def set_hp(self, value):
        self._hp = value

    def is_dead(self):
        if( self._hp > 0):
            return False
        else:
            return True

    def damage(self,option):
        #print("option {}".format(option))
        if(option == "WEAPON"):
            return self._weapon.damage
        if(option == "FIREBALL"):
            self._mana -= 10
            #print("mana {}".format(self._mana))
            return self._fireball.damage
        if(option == "HOLYMISSLE"):
            self._mana -= 10
            #print("mana {}".format(self._mana))
            return self._holymissle.damage
        if (option == "THUNDERSTRIKE"):
            self._mana -= 10
           # print("mana {}".format(self._mana))
            return self._thunderstrike.damage

    def get_spell_damage(self,option):
        if (option == "WEAPON"):
            return self._weapon.damage
        if (option == "FIREBALL"):
            return self._fireball.damage
        if (option == "HOLYMISSLE"):
            return self._holymissle.damage
        if (option == "THUNDERSTRIKE"):
            return self._thunderstrike.damage

    def get_rest_stats(self):
        return self._rest_value


    def take_damage(self,damage):
        self._hp = self._hp - (damage-self._armor.reduction)
        #("player take damage hp {} damage{}".format((damage-self._armor.reduction),self._hp))
        return damage-self._armor.reduction

    def rest(self):
        self._hp += self._rest_value
        self._mana += (self._rest_value//2)
        if(self._hp>self._maxhp):
            self._hp = self.maxhp
        if(self._mana>self._maxmana):
            self._mana = self._maxmana

    def wear(self, item):
        if(isinstance(item, Weapon)):
            self._weapon= item
        if (isinstance(item, Armor)):
            self._armor = item

    def upgrade_hp(self, value):
        self._maxhp += value
        self._hp = self.maxhp
    def upgrade_mana(self, value):
        self._maxmana += value
        self._mana = self._mana

    def upgrade_spell(self,spelltype):
        if(spelltype=="FIREBALL"):
            self._fireball.upgrade(20)
        if(spelltype=="HOLYMISSLE"):
            self._holymissle.upgrade(20)
        if(spelltype=="THUNDERSTRIKE"):
            self._thunderstrike.upgrade(20)
    def upgrade_rest(self,value):
        self._rest_value += value

    def add_gold(self, value):
        self._gold += value




