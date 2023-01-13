from dataclasses import dataclass
from searchGeneral import SearchGeneral

import requests, json

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
    
    def getSearch(self, field, endpointClass):
        url = getattr(self, field)
        response = requests.get(url)
        json_response = json.loads(response.text)
        return SearchGeneral.from_json(json_response, endpointClass)