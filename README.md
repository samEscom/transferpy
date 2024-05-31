# Transferpy
Api of a code challenge to simulate a transfer between clients and beneficiaries

## Getting started

Make sure you have installed

- [Python 3.9+](https://www.python.org/downloads/)
- docker and docker-compose/compose

## Notes
Feel fre to use Transferpy.postman_collection.json file in Postman to get the endpoints collections

## Clone repo

```sh
git clone git@github.com:samEscom/transferpy.git transferpy
cd transferpy
```

## Build app in dev container, ready to use.
```sh
make app-dev
```
Sometimes the builder process fails.
This is a bug that I need to fix, the solution is to run this process again.

## Dev and run local

If you want a run and dev locally, you can use this action of a Makefile

```sh
make install-local
```

and run
```sh
make run-local
```

Sometimes this process fails.
This is a bug that I need to fix, the solution is to run this process again.


## How I know, the app is running correctly ?

![Captura desde 2024-05-31 11-59-50](https://github.com/samEscom/transferpy/assets/11033993/9077fffb-664c-41a0-867b-fda7c2786316)

At the terminal we are waiting for this output.

The API RUN on localhost on 8000 PORT

And we can use the health-check of the API


![Captura desde 2024-05-31 12-08-03](https://github.com/samEscom/transferpy/assets/11033993/64da04b9-deb9-4a33-9cc5-d6dff3906fed)


## Endpoints

### `POST /user/register`

This EP can register a new user.

#### body/json

```json
{
    "name": "Samuel",
    "email": "samuel.chavez@gmail.com",
    "password": "1234",
    "fullname": "John Doe",
    "address": "calle 1",
    "phone_number": "12345678"
}
```

#### Response

If the register is correctly the output expected is like this

```json
{
    "data": {
        "id": 1,
        "name": "Samuel",
        "email": "samuel.chavez@gmail.com",
        "phoneNumber": "12345678"
    },
    "time": "2024-05-31 16:24:37.842415"
}
```

### `POST /user/login`

This EP can login and get token.

#### body/json

```json
{
    "email": "samuel.chavez@gmail.com",
    "password": "1234"
}
```

#### Response

If the login is correctly the output and the token expected is like this

```json
{
    "data": {
        "token": "eyJhbVhfBzwizYw7xXYkG50aMT3vbs"
    },
    "time": "2024-05-31 18:35:44.895462"
}
```

Once we have a token ready, we can register a beneficiary

### `POST /beneficiary`

This EP can save a new beneficiary.


#### headers

```json
{
    "Authorization": "Bearer JWT_TOKEN"
}
```

#### body/json

```json
{
    "fullname": "John Doe",
    "genderId": 1,
    "relationshipId": 1,
    "dateOfBirthday": "1990-01-01"
}
```

#### What is a genderId or relationshipId ?

On database is a lookup.
the values expected on every field


Gender
![Captura desde 2024-05-31 13-21-34](https://github.com/samEscom/transferpy/assets/11033993/3e698e5d-9989-4628-abfb-33320c048e54)

Relationship

![Captura desde 2024-05-31 13-22-56](https://github.com/samEscom/transferpy/assets/11033993/49d32069-81ab-458b-befb-c851fe740815)



#### Response

The output expected is like this

```json
{
    "data": {
        "id": 1,
        "fullName": "John Doe",
        "dateOfBirthday": "1990-01-01",
        "gender": {
            "id": 1,
            "gender": "masculino"
        },
        "relationship": {
            "id": 1,
            "relationship": "esposo"
        },
        "isActive": 1,
        "createdAt": "2024-05-31 16:24:37.838758"
    },
    "time": "2024-05-31 16:25:21.649428"
}
```

### `POST /transfer`

This EP can save a new transfer.


#### headers

```json
{
    "Authorization": "Bearer JWT_TOKEN"
}
```

#### body/json

```json
{
    "beneficiaryId": 1,
    "amount": 120.99,
    "transferDate": "2024-06-04"
}
```

#### Response

The output expected is like this

```json
{
    "data": {
        "id": 2,
        "createdAt": "2024-05-31 18:35:44.893160",
        "amount": "120.99",
        "dateToTransfer": "2024-06-04",
        "status": 1
    },
    "time": "2024-05-31 18:45:19.265529"
}
```

#### What is a status ?

On database is a lookup, is the status of the transfer, (pendiente, completada, cancelada)
the values expected on every field

![Captura desde 2024-05-31 13-30-06](https://github.com/samEscom/transferpy/assets/11033993/c1343fa7-f295-41a9-bdb2-77bb8fbb4108)


### `GET /transfer/<int:transfer_id>`

This EP can get info of transfer.

#### headers

```json
{
    "Authorization": "Bearer JWT_TOKEN"
}
```

#### Response

The output expected of `GET /transfer` is a list of transfer

```json
{
    "data": [
        {
            "id": 1,
            "amount": "120.99",
            "status": {
                "id": 1,
                "desc": "pendiente"
            },
            "createdAt": "2024-05-31 16:25:21.644915",
            "dateToTransfer": "2024-06-04",
            "beneficiary": {
                "id": 1,
                "fullname": "John Doe"
            },
            "userOrigin": {
                "id": 1,
                "email": "samuel.chavez@gmail.com"
            },
            "isActive": 1
        },
        {
            "id": 2,
            "amount": "120.99",
            "status": {
                "id": 1,
                "desc": "pendiente"
            },
            "createdAt": "2024-05-31 18:35:44.893160",
            "dateToTransfer": "2024-06-04",
            "beneficiary": {
                "id": 1,
                "fullname": "John Doe"
            },
            "userOrigin": {
                "id": 1,
                "email": "samuel.chavez@gmail.com"
            },
            "isActive": 1
        }
    ],
    "time": "2024-05-31 18:52:29.128749"
}
```

The output expected of `GET /transfer/1` is only one transfer info


```json
{
    "data": {
            "id": 1,
            "amount": "120.99",
            "status": {
                "id": 1,
                "desc": "pendiente"
            },
            "createdAt": "2024-05-31 16:25:21.644915",
            "dateToTransfer": "2024-06-04",
            "beneficiary": {
                "id": 1,
                "fullname": "John Doe"
            },
            "userOrigin": {
                "id": 1,
                "email": "samuel.chavez@gmail.com"
            },
            "isActive": 1
        },
    "time": "2024-05-31 18:52:29.128749"
}
```

### `PATCH /transfer/<int:transfer_id>`

This EP can update info of transfer.

#### headers

```json
{
    "Authorization": "Bearer JWT_TOKEN"
}
```
### body/json
```json
{
    "beneficiaryId": 1,
    "amount": 120.99,
    "transferDate": "2024-06-04",
    "statusId": 2
}
```


#### Response

The output expected

```json
{
    "data": {
        "id": 1,
        "amount": "120.99",
        "status": {
            "id": 2,
            "desc": "completada"
        },
        "createdAt": "2024-05-31 16:25:21.644915",
        "dateToTransfer": "2024-06-04",
        "beneficiary": {
            "id": 1,
            "fullname": "John Doe"
        },
        "userOrigin": {
            "id": 1,
            "email": "samuel.chavez@gmail.com"
        },
        "isActive": 1
    },
    "time": "2024-05-31 19:00:52.260567"
}
```


### `DELETE /transfer/<int:transfer_id>`

This EP can deactivate the transfer (logic delete) `isActive=0`

#### headers

```json
{
    "Authorization": "Bearer JWT_TOKEN"
}
```

#### Response

The output expected

```json
{
    "data": {
        "isActive": 0
    },
    "time": "2024-05-31 19:11:25.017909"
}
```

## Database

If you want open the cli and make some queries on database 
![Captura desde 2024-05-31 13-16-29](https://github.com/samEscom/transferpy/assets/11033993/3e3bc3a6-a31b-4c41-afef-f8496d9c9e0c)




## Testing

To run all the  tests, execute:

```sh
make tests
```
This option use docker to run all tests

## Testing locally

To run your tests locally to can debug, execute:

```sh
make tests-local
```
You can change the scope of the tests you want to run with the variable `TEST`:

```sh
make tests-local TEST=tests/routes
```

To run one specific test function, run:
```sh
make tests-local TEST={test/file.py}::{specific_test}
```


## Coverage

Unfortunately, I didn't manage to finish the transfer endpoint tests. But I achieved 74% coverage

![Captura desde 2024-05-31 13-44-48](https://github.com/samEscom/transferpy/assets/11033993/067ddf06-89d3-4c05-b329-7f8a77633236)



## Validation and lint

To check your code against everything, run:


```sh
make lint
```

Some of the errors can be fixed automatically through:

```sh
make lint-fix
```

#### Contact

- Email: `sa5m.escom@gmail.com`