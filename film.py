from dataclasses import dataclass
from typing import List

@dataclass
class Film:
    characters: List[str]
    created: str
    director: str
    edited: str
    episode_id: int
    opening_crawl: str
    planets: List[str]
    producer: str
    release_date: str
    species: List[str]
    starships: List[str]
    title: str
    url: str
    vehicles: List[str]

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)