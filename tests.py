# #!/usr/bin/env python3

from ast import List
from searchGeneral import SearchGeneral
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

class APItesting(unittest.TestCase):  
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
    
    def searchPopulated(self,count, nItems):
        self.assertEqual(count, nItems, f"The response payload has {count} items, but {nItems} were expected")
    
    def searchMain(self, endpointClass, searchPayload, nItems):
        endpointName = endpointClass.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]+searchPayload
        searchResponse = requests.get(searchUrl)

        # Assert the search returned OK and is JSON
        self.statusCodeAssertion(searchResponse, searchUrl)
        self.dataFormatAssertion(searchResponse, searchUrl)
        
        # Assert that SearchGeneral class can hold the json data. It should be SearchGeneral
        # and not the specific endpoint type class because search endpoint returns the "contaner" response. 
        # This step validates that the JSON is well formatted (it contains all the fields)
        json_response = json.loads(searchResponse.text)
        searchInstance = self.searchAssertion(json_response, SearchGeneral, endpointClass)
        
        # Assert the search results contains the expected number of items
        self.searchPopulated(searchInstance.count, nItems)
        
    ## AUXILIARY METHODS ABOVE
    ## ACTUAL TESTS BELOW
        
    def testSearch1(self):
        endpointClass = People
        searchPayload = "r2"
        self.searchMain(endpointClass,searchPayload, 1)
        
    def testSearch2(self):
        endpointClass = Film
        searchPayload = "the"
        self.searchMain(endpointClass,searchPayload, 5)
    
    # negative/sanity test
    # def testSearch3(self):
    #     endpointClass = Film
    #     searchPayload = "the"
    #     self.searchMain(endpointClass,searchPayload, 3)
        
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
    
    def testAll2(self):
        endpointName = All.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]
        searchResponse = requests.get(searchUrl)
        json_response = json.loads(searchResponse.text)
        allInstance = All.from_json(json_response)
        
        # Assert that I can call the People endpoint and I get a SearchGeneral object
        searchInstance = None
        try:
            searchInstance = allInstance.getSearch('people',People)
        finally:
            self.assertIsInstance(searchInstance, SearchGeneral, f"After calling the All endpoint and accessing its People URL, it seems the returned data does not match the SearchGeneral specification")
    
        # Assert that the obtained SearchGeneral object contains People items
        onePeopleInstance = searchInstance.results[0]
        self.assertIsInstance(onePeopleInstance, People, f"After calling the All endpoint and accessing its People URL, it seems the data contained in the 'results' field does not match the People specification")
           
    def testNavigation1(self):
        endpointClass = Planet
        endpointName = endpointClass.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]
        searchResponse = requests.get(searchUrl)
        json_response = json.loads(searchResponse.text)
        searchInstanceArray = []
        searchInstanceArray.append(SearchGeneral.from_json(json_response, endpointClass))
        
        # Navigate to next page of the results
        searchInstanceArray.append(searchInstanceArray[0].getNext(endpointClass))
        self.assertIsNotNone(searchInstanceArray[1], f"It seems there is only one page of results for {endpointClass.__name__} results. This it not correct.")
        
    def testNavigation2(self):
        endpointClass = Film
        endpointName = endpointClass.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]
        searchResponse = requests.get(searchUrl)
        json_response = json.loads(searchResponse.text)
        searchInstanceArray = []
        searchInstanceArray.append(SearchGeneral.from_json(json_response, endpointClass))
        
        # Navigate to next page of the results
        searchInstanceArray.append(searchInstanceArray[0].getNext(endpointClass))
        self.assertIsNone(searchInstanceArray[1], f"It seems there is more than one page of results for {endpointClass.__name__} results. This it not correct.")
    
    # It would be nice to set up a proper object to manage the different search pages instead of using an array, but I am running out of time!
    
    def testNavigation3(self):
        endpointClass = People
        endpointName = endpointClass.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]
        searchResponse = requests.get(searchUrl)
        json_response = json.loads(searchResponse.text)
        searchInstanceArray = []
        searchInstanceArray.append(SearchGeneral.from_json(json_response, endpointClass))
        
        # Navigate to next page of the results
        searchInstanceArray.append(searchInstanceArray[0].getNext(endpointClass))
        
        # Navigate to previous page of the results - it should be the same as searchInstanceArray[0]
        previousSearchInstance = searchInstanceArray[1].getPrevious(endpointClass)
        self.assertDictEqual(searchInstanceArray[0].__dict__,previousSearchInstance.__dict__, f"It seems that navigating back and forth one step delivered inconsistent results.")
      
    def testExploratory(self):
        # All->People(SearchGeneral)->Next->result[2]->Starships[0]
        endpointName = All.__name__
        searchUrl = baseUrl+endpointSearchParam[endpointName]
        searchResponse = requests.get(searchUrl)
        
        # Assert request
        self.statusCodeAssertion(searchResponse, searchUrl)
        self.dataFormatAssertion(searchResponse, searchUrl)
        
        json_response = json.loads(searchResponse.text)
        
        # Assert All instantiation
        allInstance = None
        try:
            allInstance = All.from_json(json_response)
        finally: 
            self.assertIsInstance(allInstance, All, f"Something went wrong at the All instance creation")
    
        # Assert that I can call the People endpoint and I get a SearchGeneral object
        searchInstance = None
        try:
            searchInstance = allInstance.getSearch('people',People)
        finally:
            self.assertIsInstance(searchInstance, SearchGeneral, f"After calling the All endpoint and accessing its People URL, it seems the returned data does not match the SearchGeneral specification")

        # Assert that we have a next page
        nextSearchInstance = searchInstance.getNext(People)
        self.assertIsNotNone(nextSearchInstance, f"It seems there is only one page of results for People results. This it not correct.")
       
        # Assert that results[2] is a People object - no need for instantiation, this was done at the SearchGeneral creation
        onePeopleInstance = nextSearchInstance.results[2]
        self.assertIsInstance(onePeopleInstance, People, f"Something went wrong when accessing the People results")
        
        # Assert that this is Chewbacca
        self.assertEqual(onePeopleInstance.name,"Chewbacca")
        
        # Prepare a new request to go to the Starships listed under this person
        searchUrl2 = onePeopleInstance.starships[0]
        searchResponse2 = requests.get(searchUrl2)
        
        # Assert request
        self.statusCodeAssertion(searchResponse2, searchUrl2)
        self.dataFormatAssertion(searchResponse2, searchUrl2)
        
        json_response2 = json.loads(searchResponse2.text)
        
        # Assert Starship instantiation
        starshipInstance = None
        try:
            starshipInstance = Starship.from_json(json_response2)
        finally: 
            self.assertIsInstance(starshipInstance, Starship, f"Something went wrong at the All instance creation")
            
        # Assert that this is the Millennium Falcon
        self.assertEqual(starshipInstance.name,"Millennium Falcon")
        
if __name__ == '__main__':
    unittest.main()
