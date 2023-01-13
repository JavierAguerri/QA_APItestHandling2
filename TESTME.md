# QA Coding Assignment - Notes from candidate

Hi! Thank you for the time you spent reviewing this.

Instructions:
 - Make sure python3 is installed in your machine
 - Navigate to the folder where test.sh is located
 - Run add execution permissions to test.sh
 - Execute this command: ./test.sh

What I did:
 - I created solid classes for the different endpoints (All, People, Planet... etc) and another for the search results (SearchGeneral). I think a good definition of the classes is key to code flexibility and maintenance. Also, the constructor method of the class takes a json dictionary and dumps it into the class. So everytime we are instantiating a class we are actually doing a "hidden" test: it will fail if the json data does not match the class specification (e.g. missing field).
 - I created auxiliary methods in the test class to encapsulate some parts.
 - 2 tests which check a search in general (response=OK, content=JSON, results returned match the expected class specification, amount of items as expected).
 Now that I am done with the exercise, I think it would make more sense to organize this test in another way. 
 I would test each aspect with a loop that iterates over different endpoints. For example:
   -- response=OK: Iterate over an array of different urls and check that all of them are OK
   -- content=JSON: Same as above
   -- results returned match the expected class specification: same as above, I would need an array of urls and an array of expected class to be matched by the returned JSON.
   -- amount of items as expected: same as expected.

 - 2 tests for All endpoint (general check similar to the ones above, and asserting that the people URL returns a Search object with People results). The first test could be covered by the previous point (reorganize testing of basic aspects). The second test here could be extended programatically to do the same with the rest of the endpoints (Films, Starships, etc)

 - Navigation tests. Check that I can move back and forth and there are more pages when expected. These tests can be further expanded to cover more endpoints and more complex scenarios.

 - Complex/exploratory test. Follow random paths and navigate through the API. This area could be expanded with as many tests as the team would be comfortable.

Things I would improve if I had to continue with this task:
 - More negative/failure tests. 
 - Better encapsulation at some points (endpointName, searchUrl, searchResponse)
 - Programatically test API requests to the urls provided in an All object, and checking that the returned objects are all SearchGeneral 
and inside each SearchGeneral there is the right object (People, Planet, Vehicle... etc)
 - Further testing complex cases (All->People(SearchGeneral)->Next->result[2]->Starships[0]->... and check we have the right object in hands
 - Encapsulate the steps at the exploratory testing, somehow. Unfortunately I do not have more time, but I feel that there could be a way to make it less "spaghettish"
 - When testing navigation, I would assert that the page URL parameter is correct too. 
 - additional methods for endpoint classes which instantiate their assigned elements, if any. For example, Planet class has two fields which are actually an array: films and residents (People). So it would look really neat to add methods which take a parameter (index of the array) and returned an instantiated Film or People, doing an API request in the "background". Or even we could do it without the parameter and return an array with all the films and people listed for the planet. This would make our classes very powerful.
 

The reason why I set such a long estimated time of arrival is because I am beginner with python and API testing, so I planned for several hours in order to deliver a decent solution. So I spent most of the time researching python and API testing documentation and tutorials.

I really enjoyed the exercise and the learning, so I would be happy to continue doing more stuff like this at Qredo!

Cheers,
Javier