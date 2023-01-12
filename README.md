
# QA Coding Assignment

The goal of this assignment is to build an integration test for an API that provides information on the Star Wars movies (no knowledge of SW is required). The data needed will be queried from [SWAPI (Star Wars API)](https://swapi.dev/) which is an open testing API.

## Overview
The test should consist of a query where you can provide a search string and get matching results. You should then test the matching result end-points.

### Query endpoint
The test must query information using the following categories:
* All (default)
* People
* Planets
* Starships
* Vehicles

You should use the existing `/search` endpoints for each category (see: https://swapi.dev/documentation#search).
The default behaviour (All) should be to query all four search endpoints and check all results.

### Search results
Generally the useful information from the search response for a single entry is as follows:

```
{
  "count": 1,
    ...
  "results": [
    {
      "name": "Luke Skywalker",
        ...
      "films": [
        "http://swapi.dev/api/films/1/",
        "http://swapi.dev/api/films/2/",
        "http://swapi.dev/api/films/3/",
        "http://swapi.dev/api/films/6/"
      ],
        ...
      "url": "http://swapi.dev/api/people/1/"
    }
  ]
}
```


### Matching result end-point
Each search result entry should contain a URL that provides more detailed entry. Please add some test cases for these endpoints also.

## Technical details

## Requirements
The only strict requirement we pose is that the app is written in **python** unless expressly agreed otherwise. We recommend that you re-use code (wherever meaningful of course) and explain any decisions taken in a TESTME.md file.


### Project Setup
Please setup the test in a way that we can start it by simply running `test.sh` script.

### SWAPI
The [SWAPI](https://swapi.dev/) API is a free service and has a 10,000 requests per day rate limiting. Please make sure you don't abuse it.
Note that in some of the results the URLs returned start with `http` which is wrong and should be modified to `https` for them to work, make sure you handle this correctly.

### External Libraries
We don't mind if you use whatever external libraries you like.

### Estimation
You will see an open issue "Call for estimation". Please estimate by writing a comment  when you think the task will be ready before you start. We don't set any hard deadlines.
