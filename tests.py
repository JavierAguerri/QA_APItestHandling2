# #!/usr/bin/env python3

from resourceGeneral import ResourceGeneral
from film import Film
from people import People
from planet import Planet
from species import Species
from starship import Starship
from vehicle import Vehicle
from all import All

import requests, unittest, json

baseUrl = "http://swapi.dev/api/"
endpointSearchParam = {"All": "", "People": "people/?search=", "Film": "films/?search=", "Planet": "planets/?search=", "Starship": "starships/?search=", "Species": "species/?search=", "Vehicle": "vehicles/?search="}
# endpointTypes = ["All", "People", "Film", "Planets", "Starships", "Species", "Vehicles"]
# endpointClasses = [All, People, Film, Planet, Starship, Species, Vehicle]

class TestStringMethods(unittest.TestCase):  
    def statusCodeAssertion(self,response, searchUrl):
        statusCode = response.status_code
        self.assertEqual(statusCode,200,f"Endpoint is not OK, code is {str(statusCode)}. The URL was: {searchUrl}")
        
    def dataFormatAssertion(self,response, searchUrl):
        dataFormat = response.headers["content-type"]
        self.assertEqual(dataFormat,"application/json", f"Response data is not in JSON format but {dataFormat}. The URL was: {searchUrl}")

    def searchAssertion(self, json_response, mainClass, *args):
        mainInstance = None
        try:
            mainInstance = mainClass.from_json(json_response, *args)
        finally:
            self.assertIsInstance(mainInstance, mainClass, f"The received json data does not match the {mainClass.__name__} class. JSON contents: {str(json_response)}")
        return mainInstance
    
    def searchPopulated(self,results, nItems):
        nResults = len(results)
        self.assertEqual(nResults, nItems, f"The response payload has {nResults} items, but {nItems} were expected")
    
    def searchMain(self, endpointClass, searchPayload, nItems):
        endpointName = endpointClass.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]+searchPayload
        searchResponse = requests.get(searchUrl)

        # Assert the search returned OK and is JSON
        self.statusCodeAssertion(searchResponse, searchUrl)
        self.dataFormatAssertion(searchResponse, searchUrl)
        
        # Assert that ResourceGeneral class can hold the json data. It should be resourceGeneral
        # and not the specific endpoint type class because search endpoint returns the "contaner" response. 
        # This step validates that the JSON is well formatted (it contains all the fields)
        json_response = json.loads(searchResponse.text)
        resourceInstance = self.searchAssertion(json_response, ResourceGeneral, endpointClass)
        
        # Assert the search results contains the expected number of items
        self.searchPopulated(resourceInstance.results, nItems)
        
    def testSearch1(self):
        endpointClass = People
        searchPayload = "r2"
        self.searchMain(endpointClass,searchPayload, 1)
        
    def testSearch2(self):
        endpointClass = Film
        searchPayload = "the"
        self.searchMain(endpointClass,searchPayload, 5)
        
    def testAll(self):
        endpointName = All.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]
        searchResponse = requests.get(searchUrl)
        
        # Assert the search returned OK and is JSON
        self.statusCodeAssertion(searchResponse, searchUrl)
        self.dataFormatAssertion(searchResponse, searchUrl)
        
        # Assert that All class can hold the json data.
        # This step validates that the JSON is well formatted (it contains all the fields)
        json_response = json.loads(searchResponse.text)
        self.searchAssertion(json_response, All)
        
if __name__ == '__main__':
    unittest.main()
