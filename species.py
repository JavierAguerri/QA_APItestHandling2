from dataclasses import dataclass
from typing import List

@dataclass
class Species:
    average_height: str
    average_lifespan: str
    classification: str
    created: str
    designation: str
    edited: str
    eye_colors: str
    hair_colors: str
    homeworld: str
    language: str
    name: str
    people: List[str]
    films: List[str]
    skin_colors: str
    url: str
    
    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)