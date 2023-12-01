#Author: Brendan Beard
#Published: Brendan Beard
#Copyright: 2022

# --- Imports --- #

from dataclasses import dataclass, KW_ONLY
from enum import StrEnum, auto
from .units import Unit

__all__ = ("ArmyTypes", "Division")


# --- ArmyTypes Class --- #

class ArmyTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()

    INFANTRY = auto() #Infantry (troops, militia)
    CAVALRY = auto() #Cavalry (horses, donkeys, camels)
    MOTORIZED = auto() #Vehicles (trucks, cars, troop transports)
    MOUNTAINEERS = auto() #Infantry (ski, mountaineers)
    ARTILLERY = auto() #Cannons, Artillery Guns
    ANTITANK = auto() #Infantry and Armor
    ANTIAIR = auto() #Infantry and Armor
    ARMOR = auto() #Tanks


# --- Infantry Class --- #

@dataclass(repr = False, kw_only = True, slots = True)
class Division(Unit):
    """Default Army Class"""
	
    _: KW_ONLY
    _prefix: str = ""
	
    def __str__(self) -> str:
        return f"{self._prefix} {self.name} {self.type_} {self.__class__.__name__}"

    @property
    def prefix(self) -> str:
        return self._prefix
			
    @prefix.setter
    def prefix(self, prefix: str) -> None:
        self._prefix = prefix


# --- Testing --- #

if __name__ == "__main__":
    def main():
        unit = Division("1st", ArmyTypes.INFANTRY, prefix="US")
        print(unit, repr(unit), sep="\n")
        
    main()
