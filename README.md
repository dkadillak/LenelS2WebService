# LenelS2WebService


## Functionality
* Returning a list of all created people 
```
GET /api/people
```
* Returning a list of people matching given first/last name => filter
```
GET /api/people?filter={filter}
```
* Returning person matching this id
```
GET / api/people/{id}
```
* Creating a person
```
POST /api/people
```
* Modifyin a person specified by a given id
```
PUT /api/people/{id}
```
* Removing a person
```
DELETE /api/people/{id}
```

### Person format
{
  "id": X,
  "first_name": "fname",
  "last_name": "lname"
}

## Running
```
$ ./script
```

## Assumptions
* A person's id field must be unique

## Built With
* Python 3.7.1 
* Django 2.1.4

