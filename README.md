# AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Table of Content
- [Environment](#environment)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Examples of use](#examples-of-use)
- [Bugs](#bugs)
- [Authors](#authors)
- [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using Python3 (version 3.8.5)

## Installation
* Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console currently supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* `def reload(self)` - deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_amenity(self)` - Test that models/amenity.py conforms to PEP8
* `def test_pep8_conformance_test_amenity(self)` - Test that tests/test_models/test_amenity.py conforms to PEP8
* `def test_amenity_module_docstring(self)` - Test for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Test for the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Test for the city.py module docstring
* `def test_city_class_docstring(self)` - Test for the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_place(self)` - Test that models/place.py conforms to PEP8.
* `def test_pep8_conformance_test_place(self)` - Test that tests/test_models/test_place.py conforms to PEP8.
* `def test_place_module_docstring(self)` - Test for the place.py module docstring
* `def test_place_class_docstring(self)` - Test for the Place class docstring

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_review(self)` - Test that models/review.py conforms to PEP8
* `def test_pep8_conformance_test_review(self)` - Test that tests/test_models/test_review.py conforms to PEP8
* `def test_review_module_docstring(self)` - Test for the review.py module docstring
* `def test_review_class_docstring(self)` - Test for the Review class docstring

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_state(self)` - Test that models/state.py conforms to PEP8
* `def test_pep8_conformance_test_state(self)` - Test that tests/test_models/test_state.py conforms to PEP8
* `def test_state_module_docstring(self)` - Test for the state.py module docstring
* `def test_state_class_docstring(self)` - Test for the State class docstring

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8
* `def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_user_module_docstring(self)` - Test for the user.py module docstring
* `def test_user_class_docstring(self)` - Test for the User class docstring

## New Features

### AirBnB clone - RESTful API

This project focuses on building a RESTful API for the AirBnB clone using Python Flask. The API allows users to interact with the AirBnB clone application using HTTP requests.

#### Requirements

- Python Scripts:
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - The code should use the `PEP 8` style (version 1.7)
  - All files must be executable
  - The length of the files will be tested using `wc`
  - All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - A documentation is not a simple word, it's a real sentence explaining the purpose of the module, class, or method (the length will be verified)

- Python Unit Tests:
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files should end with a new line
  - All test files should be inside a folder `tests`
  - The tests should use the `unittest` module
  - All test files should be python files (extension: `.py`)
  - All test files and folders should start with `test_`
  - The file organization in the tests folder should be the same as the project: `tests/test_models/test_base_model.py`
  - All tests should be executed by using this command: `python3 -m unittest discover tests`
  - Tests can also be run file by file using this command: `python3 -m unittest tests/test_models/test_base_model.py`

#### API Endpoints

The following API endpoints are implemented:

- `GET /api/v1/status`: Retrieve the status of the API.
- `GET /api/v1/stats`: Retrieve the number of objects by type.
- `GET /api/v1/states`: Retrieve a list of all State objects.
- `GET /api/v1/states/<state_id>`: Retrieve a specific State object.
- `DELETE /api/v1/states/<state_id>`: Delete a specific State object.
- `POST /api/v1/states`: Create a new State object.
- `PUT /api/v1/states/<state_id>`: Update a specific State object.
- `GET /api/v1/cities`: Retrieve a list of all City objects.
- `GET /api/v1/cities/<city_id>`: Retrieve a specific City object.
- `DELETE /api/v1/cities/<city_id>`: Delete a specific City object.
- `POST /api/v1/states/<state_id>/cities`: Create a new City object linked to a State.
- `PUT /api/v1/cities/<city_id>`: Update a specific City object.
- `GET /api/v1/amenities`: Retrieve a list of all Amenity objects.
- `GET /api/v1/amenities/<amenity_id>`: Retrieve a specific Amenity object.
- `DELETE /api/v1/amenities/<amenity_id>`: Delete a specific Amenity object.
- `POST /api/v1/amenities`: Create a new Amenity object.
- `PUT /api/v1/amenities/<amenity_id>`: Update a specific Amenity object.
- `GET /api/v1/users`: Retrieve a list of all User objects.
- `GET /api/v1/users/<user_id>`: Retrieve a specific User object.
- `DELETE /api/v1/users/<user_id>`: Delete a specific User object.
- `POST /api/v1/users`: Create a new User object.
- `PUT /api/v1/users/<user_id>`: Update a specific User object.
- `GET /api/v1/cities/<city_id>/places`: Retrieve a list of all Place objects linked to a City.
- `GET /api/v1/places/<place_id>`: Retrieve a specific Place object.
- `DELETE /api/v1/places/<place_id>`: Delete a specific Place object.
- `POST /api/v1/cities/<city_id>/places`: Create a new Place object linked to a City.
- `PUT /api/v1/places/<place_id>`: Update a specific Place object.
- `GET /api/v1/places/<place_id>/reviews`: Retrieve a list of all Review objects linked to a Place.
- `GET /api/v1/reviews/<review_id>`: Retrieve a specific Review object.
- `DELETE /api/v1/reviews/<review_id>`: Delete a specific Review object.
- `POST /api/v1/places/<place_id>/reviews`: Create a new Review object linked to a Place.
- `PUT /api/v1/reviews/<review_id>`: Update a specific Review object.

#### Error Handling

The API handles errors gracefully and returns appropriate HTTP status codes and error messages in JSON format. The following errors are handled:

- 404 Not Found: Returned when a requested resource is not found.
- 400 Bad Request: Returned when the request is invalid or missing required parameters.

## Examples of Use

```bash
$ curl -X GET http://0.0.0.0:5000/api/v1/states
[
  {
    "__class__": "State", 
    "created_at": "2017-04-14T00:00:02", 
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99", 
    "name": "Louisiana", 
    "updated_at": "2017-04-14T00:00:02"
  }, 
  {
    "__class__": "State", 
    "created_at": "2017-04-14T16:21:42",
    "id": "1a9c29c7-e39c-4840-b5f9-74310b34f269",
    "name": "Arizona",
    "updated_at": "2017-04-14T16:21:42"
},
...
]
$ curl -X GET http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99
 {
    "class": "State",
    "created_at": "2017-04-14T00:00:02",
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99",
    "name": "Louisiana",
    "updated_at": "2017-04-14T00:00:02"
 }
$ curl -X POST http://0.0.0.0:5000/api/v1/states -H "Content-Type: application/json" -d '{"name": "California"}'
 {
    "class": "State",
    "created_at": "2017-04-15T01:30:27.557877",
    "id": "feadaa73-9e4b-4514-905b-8253f36b46f6",
    "name": "California",
    "updated_at": "2017-04-15T01:30:27.558081"
 }
$ curl -X PUT http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6 -H "Content-Type: application/json" -d '{"name": "California is so cool"}'
 {
    "class": "State",
    "created_at": "2017-04-15T01:30:28",
    "id": "feadaa73-9e4b-4514-905b-8253f36b46f6",
    "name": "California is so cool",
    "updated_at": "2017-04-15T01:51:08.044996"
 }
$ curl -X DELETE http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
 {}
```

## Bugs

No known bugs at this time.

## Authors
- Yassine Mtejjal [Github](https://github.com/Y4SS11N3)
- Anas Mouak - [Github](https://github.com/AnasMouak)
- Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)  
- Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)
- Jhoan Zamora - [Github](https://github.com/jzamora5) / [Twitter](https://twitter.com/JhoanZamora10)
- David Ovalle - [Github](https://github.com/Nukemenonai) / [Twitter](https://twitter.com/disartDave)

Second part of Airbnb: Joann Vuong

## License

Public Domain. No copy write protection.
