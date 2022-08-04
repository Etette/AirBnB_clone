# AirBnB Clone - The Console
Project is carried out by Emmanuel Effiong and Gbenga Ogunmefun

## Project Description

The main objective of this project is to clone the AirBnB website.
First part is to create all classes for AirBnB(`User`, `City`, `Place`) that inherits from a `BaseModel`
Create an abstracted storage engine and 
validate all classes and the storage engine.

## Command Intepreter
* Create a new object (e.g: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

### Functionalities of the console

`create:` Create a new object (User/Place)
`update:` Update attributes of an object
`show:` Prints the string representation of an instance based on the class name and id
`all:` Prints all string representation of all instances.
`EOF:` method to EOF to exit with. (CTRL D)
`emptyline:` an empty line + ENTER shouldn't execute anything.
`destroy:` Deletes an instance based on the class name and id.
`quit:` Quit command to exit the program

## How to use

### In interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### In non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$
```

## Directory and File Descriptions

`models` - Contains all models used in the project
`models/engine/file_storage.py` - Used for serialization and deserialization of python objects to and from a Json file.
`models/base_model.py` - Base class for all models.
`models/city.py, amenity.py, place.py, review.py, state.py, user.py` - Entities that inherit from the Base class.
`console.py` - The command line intepreter.
`AUTHORS` - Contributors on this project.
