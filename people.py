from dataclasses import dataclass
from typing import List

@dataclass
class People:
    birth_year: str
    created: str
    edited: str
    eye_color: str
    films: List[str]
    gender: str
    hair_color: str
    height: str
    homeworld: str
    mass: str
    name: str
    skin_color: str
    species: List[str]
    starships: List[str]
    url: str
    vehicles: List[str]

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)