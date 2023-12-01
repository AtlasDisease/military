#Author: Brendan Beard
#Published: Brendan Beard
#Copyright: 2022

# --- Imports --- #

from dataclasses import dataclass, field, KW_ONLY
from enum import StrEnum, auto
from .units import Unit

__all__ = ("ShipTypes", "Fleet")


# --- Ship Types --- #

class ShipTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
	
    CARRIER = auto()
    BATTLESHIP = auto()
    CRUISER = auto()
    DESTROYER = auto()
    PATROL = auto()


# --- Ship Class --- #

@dataclass(init = False, repr = False, kw_only = True, slots = True)
class Ship(Unit):
    """Default Navy Class"""
	
    def __str__(self) -> str:
        return f"{self.type_} {self.name}"


@dataclass(repr=False, slots=True)
class Fleet:
    """Default Navy Class"""
	
    name : str
    _ : KW_ONLY
    _prefix : str
    _units: list[Ship] = field(default_factory=list)
 
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, _prefix={self._prefix})"
	
    def __str__(self) -> str:
        if self._prefix == "":
            return f"{self.name} Naval Fleet"
        return f"{self._prefix} {self.name} Naval Fleet"
		
    @property
    def capitalShip(self) -> None | Ship:
        """The primary ship or commanding ship of a fleet"""
        if self._units:
            return self._units[0]

    @property
    def prefix(self) -> str:
        return self._prefix
		
    @property
    def prefix(self, prefix: str) -> None:
        self._prefix = prefix
		
    def add(self, ship: Ship, *, isCapitalShip=False) -> None:
        if not isinstance(ship, Ship):
            return

        if isCapitalShip:
            self._units.insert(0, ship)
        else:
            self._units.append(ship)
			
    def createShip(self, name: str, type_: str) -> Ship:
        type_ = type_.upper()
        if type_ in ShipTypes.__dict__:
            return Ship(name, ShipTypes[type_])


# --- Testing --- #

if __name__ == "__main__":
    def main():
        fleet = Fleet("1st", _prefix="USS")
        fleet.add(fleet.createShip("Austin", "Battleship"))

    main()
