from dataclasses import dataclass

@dataclass
class All:
    people: str
    planets: str
    films: str
    species: str
    vehicles: str
    starships: str
    
    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)