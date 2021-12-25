# avito_test
REST API application: microservice for working with user balance (crediting funds, debiting funds, transferring funds from client to client, method for obtaining user balance). The service accepts and sends requests / responses in JSON format.<br>


### Stack of technologies:<br>
-Python <br>
-FastApi<br>
-Docker <br>
-Database: Postgres <br>
-Linter: Black<br>

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. The key features are: fast to code, based on the open standards for APIs, very high performance, minimize code duplication.

### Basic functionality:<br>
1. Web REST API<br>
2. Getting list of all clients and all operations from the database<br>
3. Creating new clients and all operations<br>
4. Getting information about any client or any operation by id <br>
5. Sending money from one client to another<br>
6. Getting client's balance in different currencies


### APIs endpoints:<br>
| requests | url | description  |
| ------- | --- | --- |
| GET | /clients/{client_id} |  information about a client |
| GET | /clients/all_operations/{client_id} | information about all operations for one client |
| GET | /clients/{client_id}/{currency} |  client's balance in different currencies |
| GET | /clients/{client_id}/{day} |  information about all operations for one user per day |
| POST | /clients | create new client |
| DELETE | /clients/{client_id} | delete a client |
| ------- | --- | --- |
| GET | /operations | information about all operations |
| GET | /operations/{operation_id} | information about one operation by id |
| POST | /operations | create new operation (operation can be 'income' or 'outcome' kind) |
| DELETE | /operations | delete an operation |
| POST | /operations/send_money/{user_id_from}/{user_id_to} | Sent money from one client to another |


## Installation
### Clone the repo:<br>

$ git clone https://github.com/SparklingAcidity/avito_test <br>
$ cd avito_test <br>

### Create virtualenv:<br>
$ virtualenv venv<br>
$ source venv/bin/activate<br>

### Docker run:
$ docker-compose up -d --build<br>

### Tests: <br>
$pytest


### API from the browser:
You can work on the API directly in your browser.<br>
You will see the automatic interactive API documentation (provided by Swagger UI).
http://127.0.0.1:8000/docs <br>


### Examples:<br>
All urls:<br>
![Screenshot](https://github.com/SparklingAcidity/avito_test/blob/master/img_for_readme/1.png) <br>
Create new operation: <br>
![Screenshot](https://github.com/SparklingAcidity/avito_test/blob/master/img_for_readme/2.png) <br>
Sent money from one client to another: <br>
![Screenshot](https://github.com/SparklingAcidity/avito_test/blob/master/img_for_readme/3.png) <br>
Get information about all operations for one client: <br>
![Screenshot](https://github.com/SparklingAcidity/avito_test/blob/master/img_for_readme/4.png)<br><br>
