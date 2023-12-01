# --- Imports --- #

from dataclasses import dataclass, field, KW_ONLY
from typing import Optional

from .army import Division, ArmyTypes
from .navy import Fleet#, ShipTypes
from .airforce import Squadron, AircraftTypes

__all__ = ("Military",)


# --- Military --- #

@dataclass(slots = True, repr = False)
class Military:
    
    prefixes: Optional[tuple] = field(default_factory = tuple)
    _: KW_ONLY
    _army: list[Division] = field(default_factory = list)
    _navy: list[Fleet] = field(default_factory = list)
    _airforce: list[Squadron] = field(default_factory = list)

    def __str__(self) -> str:
        return f"{self._army[0].prefix} {self.__class__.__name__}".strip()
    
    def addDivision(self, name: str, type_: str):
        type_ = type_.upper()
        if type_ in ArmyTypes.__dict__:
            self._army.append(Division(name, ArmyTypes[type_], _prefix=prefixes[0]))
    
    def addFleet(self, name: str):
        self._navy.append(Fleet(name, _prefix=prefixes[1]))
    
    def addSquadron(self, name: str, type_: str):
        type_ = type_.upper()
        if type_ in AircraftTypes.__dict__:
            self._airforce.append(Squadron(name, AircraftTypes[type_], _prefix=prefixes[2]))
    
