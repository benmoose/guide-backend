# Guide Backend

### Setup

With [Docker installed](https://docs.docker.com/install/), start the
server with

```bash
$ docker-compose up
```

If this is the first time you're running the project, or you've removed
the containers, you'll need to run migrations first

```bash
$ docker-compose run db web python manage.py migrate --noinput
```

Run the test suite with

```bash
$ scripts/run-tests.sh
```

### Project Structure

#### Data Models

This project uses the concept of data models to encourage a clean
interface between application logic and the Django's database models.

All database models have a corresponding data model. The data model
contains the same information as the database model, but represented
is a way that is much easier to manipulate.

All data models contain classmethods to handle converting to and from
their corresponding database models. They also contain useful
constructor methods (e.g. `from_dict)`) which can help when constructing
models from HTTP requests. Data models are also responsible for
validating data (it should never be possible to call `to_db_model` on
a data model that contains incomplete or invalid data according to the
database model.
