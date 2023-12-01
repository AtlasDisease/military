#Author: Brendan (@atlasdisease)
#Copyright: 2023
#Description:

# --- Imports --- #

from dataclasses import dataclass, field, KW_ONLY
from enum import StrEnum, auto
from .units import Unit

__all__ = ("AircraftTypes", "Squadron")

# --- AircraftTypes Enum --- #

class AircraftTypes(StrEnum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ").title()
	
    FIGHTER = auto()
    BOMBER = auto()


# --- Aircraft Class --- #

@dataclass(repr = False, kw_only = True, slots = True)
class Squadron(Unit):
    """Default Air Force Class"""
	
    _: KW_ONLY
    _prefix: str = ""

    def __str__(self) -> str:
        return f"{self._prefix} {self.name} {self.type_} {self.__class__.__name__}"
    
    @property
    def prefix(self) -> str | None:
        return self._prefix
			
    @property
    def prefix(self, prefix: str) -> None:
        self._prefix = prefix


# --- Testing --- #

if __name__ == "__main__":
    def main():
        fighter = Aircraft("F-15", AircraftTypes.FIGHTER, prefix="US")
        print(fighter)
		
    main()
