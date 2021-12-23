# avito_test
REST API application ...<br>

### Basic functionality:<br>
1.Web REST API<br>
2. ...<br>
3. ...<br>
4. Sent money from one client to another<br>


### Stack of technologies:<br>
-Python <br>
-FastApi<br>
-Docker <br>
-Database: Postgres <br>
-linter: Black<br>


### APIs endpoints:<br>
| requests | url | description  |
| ------- | --- | --- |
| GET | /clients/{client_id} |  information about a client |
| GET | /clients/all_operations/{client_id} | information about all operations for one client |
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
