from dataclasses import dataclass
from typing import List, Type

import importlib

# the resourceGeneral class represents the response of any of films, people, planet, species, starship or vehicle endpoits.
# the class has a factory method which initializes a new instance of the class
# the results field is a bot challenging because ideally:
# - we want to reuse ResourceGeneral for any of films, people, planet... 
#   so we do not know exactly which object type the results array is gonna contain. We type it dynamically.
#   results is defined by iterating the json_data and using the corresponding class factory method to instantiate the appropriate item

# each of the item endpoint classes (Film, People, Planet, Species, Starship, Vehicle) accomodate all the fields for the item 
# and has a factory method which takes a json dictionary as parameter and unpacks it to instantiate the class

# I decided to make my code compatible with all the item endpoints and not only the four of them mentioned in the assignment description
# in order to showcase how scalable and neat my code is!

@dataclass
class ResourceGeneral:
    count: int
    next: str
    previous: str
    results: List

    @classmethod
    def from_json(cls, json_data: dict, resource_class: Type):
        resource_module = importlib.import_module(resource_class.__module__)
        resource_class = getattr(resource_module, resource_class.__name__)
        results = [resource_class.from_json(result) for result in json_data["results"]]
        return cls(
            count=json_data["count"],
            next=json_data["next"],
            previous=json_data["previous"],
            results=results
        )