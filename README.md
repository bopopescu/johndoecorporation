# John Doe Corp.

A simple CRUD (Create, Read, Update, and Delete ) employee management webapp written in Flask.

####This webapp allows:

* Users to register and login as employees

* Admin to create, update, and delete departments and roles

* Admin to assign employees to a department and assign them roles

* Admin to view all employees and their details

####To run the code:

1. `$ sudo /usr/local/mysql/support-files/mysql.server start`

2. `$ /usr/local/mysql/bin/mysql -uroot -p`

3. `(venv) $ export FLASK_CONFIG=development`

4. `(venv) $ export FLASK_APP=run.py`

5. `(venv) $ flask run`

6. Go to `http://127.0.0.1:5000/`