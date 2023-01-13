from dataclasses import dataclass
from typing import List

@dataclass
class Planet:
    climate: str
    created: str
    diameter: str
    edited: str
    films: List[str]
    gravity: str
    name: str
    orbital_period: str
    population: str
    residents: List[str]
    rotation_period: str
    surface_water: str
    terrain: str
    url: str

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)