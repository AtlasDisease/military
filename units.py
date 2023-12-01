#Author: Brendan Beard
#Copyright: 2023
#Description:

# --- Imports --- #

from dataclasses import dataclass

__all__ = ("Unit",)


# --- Unit Class --- #

@dataclass(repr = False, slots = True)
class Unit:
    """Base-Class"""

    name: str
    type_: str
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name})"

    def __str__(self) -> str:
        return f"{self.name} {self.type_}"
