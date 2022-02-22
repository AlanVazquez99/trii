# Trii

![python]

## Content table
- [Target](#Target)
- [Solution](#Solution)
- [Requirements](#Requirements)
  - [Dependencies](#Dependencies)

<br/>

## Target
Choose a public api of your choice that has options for filtering. This api will be our data source.
Develop the following.
- An endpoint that consumes any public api and returns a list of data.
- The endpoint must have filters of the api that is being consumed, no more than 3 filters.
- An option should be added to download the information in a zip that contains the json.

<br/>

## Solution
It is basically a wrapper to the Rick & Morty public API (https://rickandmortyapi.com) It adds some extra features like filters, error handling, and downloading the data in ZIP format

<br/>

### Step 1:
<img src="out/Step 1.gif"/>

### Step 2:
<img src="out/Step 2.gif"/>


<br/>


## Requirements

> Python >= 3.9 

<br/>

### Dependencies

> [fastapi==0.74.1][fastapi] <br/>
> [pydantic==1.9.0][pydantic] <br/>
> [requests==2.27.1][requests] <br/>

<br/>


<!-- badges -->
[python]: https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white

<!-- links -->
[fastapi]: https://fastapi.tiangolo.com/
[pydantic]: https://pydantic-docs.helpmanual.io/
[requests]: https://docs.python-requests.org/en/latest/
