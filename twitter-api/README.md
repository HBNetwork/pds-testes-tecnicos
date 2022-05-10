# Back-end Assessment

[Project](https://docs.google.com/document/d/1AjLtZa3x741EPa4pPSUuoUTb8tLiRXGtNbrs8YLhXkY/edit?usp=sharing)

# Application

### How to get start

First of all you need **docker** and **docker-compose** installed on your machine.

You can follow this [tutorial](https://docs.docker.com/compose/install/)

After that you can start the application running

```console
docker-compose up --build
```

:information_source: You don't have to create a .env file, for now the enviroment variables are hard coded on docker-compose to you get started fast.

### Using the application

So, you can use the application oppening the api docs that uses swagger.

In your browser open `http://localhost:8000/api/docs`

There you can see all the endpoints and test.

:information_source: **The database is populated with random data**.
:warning: **Atention you will be always the user with id 1**.

### Test with coverage

To test the application run

```console
docker-compose exec app pytest --cov=.
```