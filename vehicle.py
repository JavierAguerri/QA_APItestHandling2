from dataclasses import dataclass
from typing import List

@dataclass
class Vehicle:
    cargo_capacity: str
    consumables: str
    cost_in_credits: str
    created: str
    crew: str
    edited: str
    films: List[str]
    length: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    passengers: str
    pilots: List[str]
    url: str
    vehicle_class: str

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)