from dataclasses import dataclass
from typing import List

@dataclass
class Starship:
    MGLT: str
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    created: str
    crew: str
    edited: str
    films: List[str]
    hyperdrive_rating: str
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: str
    pilots: List[str]
    starship_class: str
    url: str

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)