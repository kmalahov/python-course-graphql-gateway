GraphQL API Gateway
===================

GraphQL API шлюз для взаимодействия с микросервисами.

Зависимости
===========
Требуемое ПО:

1. Docker для контейнеризации – |link_docker|

.. |link_docker| raw:: html

   <a href="https://www.docker.com" target="_blank">Docker Desktop</a>

2. Для работы с системой контроля версий – |link_git|

.. |link_git| raw:: html

   <a href="https://github.com/git-guides/install-git" target="_blank">Git</a>

3. IDE для работы с исходным кодом – |link_pycharm| (Опционально)

.. |link_pycharm| raw:: html

    <a href="https://www.jetbrains.com/ru-ru/pycharm/download" target="_blank">PyCharm</a>

Установка
=========
Clone the repository to your computer:

.. code:: bash

   git clone https://github.com/kmalahov/python-course-graphql-gateway

1. To configure the application copy `.env.sample` into `.env` file:

    .. code-block:: console

        cp .env.sample .env

    This file contains environment variables that will share their values
    across the application. The sample file (`.env.sample`) contains a
    set of variables with default values. So it can be configured
    depending on the environment.

2. Build the container using Docker Compose:

    .. code-block:: console

        docker compose build

    This command should be run from the root directory where `Dockerfile`
    is located. You also need to build the docker container again in case
    if you have updated `requirements.txt`.

3. To run the project inside the Docker container:

    .. code-block:: console

        docker compose up

    When containers are up server starts
    at http://0.0.0.0:8000/graphql. You can open it in your browser.


Использование
=============

Query example to request a list of favorite places:

    .. code-block:: graphql

        query {
          places {
            latitude
            longitude
            description
            city
            locality
          }
        }

Query example to request a list with pagination of favorite places:

    .. code-block:: graphql

        query {
          places (limit: 100, page: 1, size: 100){
            id
            latitude
            longitude
            description
            city
            locality
          }
        }

Query example to request a list of favorite places with countries information:

    .. code-block:: graphql

        query {
          places {
            latitude
            longitude
            description
            city
            locality
            country {
              name
              capital
              alpha2code
              alpha3code
              capital
              region
              subregion
              population
              latitude
              longitude
              demonym
              area
              numericCode
              flag
              currencies
              languages
            }
          }
        }

Query example to get specific favorite place:

    .. code-block:: graphql

        query{
          place(placeId:1) {
            id
            latitude
            longitude
            description
            city
            locality
          }
        }

Query example to create new favorite place:

    .. code-block:: graphql

        mutation {
          createPlace (
            latitude: 25.20485,
            longitude: 55.27078,
            description: "Nice food."
          ) {
            place {
              id
              latitude
              longitude
              description
              city
              locality
            }
            result
          }
        }

Query example to delete specific favorite place:

    .. code-block:: graphql

        mutation {
          deletePlace(placeId: 1) {
            result
          }
        }

Query example to create a favorite place:
    .. code-block:: graphql

        mutation {
          updatePlace (
            placeId: 1,
            latitude: 47.275503,
            longitude: -122.763093,
            description: "some description") {
              result
            }
        }

Автоматизация
=============

The project contains a special `Makefile` that provides shortcuts for
a set of commands:

1. Build the Docker container:

    .. code-block:: console

        make build

2. Generate Sphinx documentation run:

    .. code-block:: console

        make docs-html

3. Autoformat source code:

    .. code-block:: console

        make format

4. Static analysis (linters):

    .. code-block:: console

        make lint

5. Autotests:

    .. code-block:: console

        make test

   The test coverage report will be located at
   `src/htmlcov/index.html`. So you can estimate the quality of
   automated test coverage.

6. Run autoformat, linters and tests in one command:

    .. code-block:: console

        make all

    Run these commands from the source directory where `Makefile` is
    located.

Documentation
-------------

The project integrated with the
`Sphinx <https://www.sphinx-doc.org/en/master/>`__ documentation engine.
It allows the creation of documentation from source code. So the source
code should contain docstrings in
`reStructuredText <https://docutils.sourceforge.io/rst.html>`__ format.

To create HTML documentation run this command from the source directory
where `Makefile` is located:
    .. code-block:: console

        make docs-html

After generation documentation can be opened from a file
`docs/build/html/index.html`.


Тестирование
============


