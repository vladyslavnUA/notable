# Challenge

How to run:
```
clone the repo
$ virtualenv env
$ source env/bin/activate

$ pip install -r requirement.txt
$ python manage.py runserver 8002
```

Head to http://localhost:8002/ for the API dashboard.

## List of all doctors
http://localhost:8002/doctors/

## List of appointments (create, update, search and filter available here)
http://localhost:8002/appointments/

## Delete an appointment
http://localhost:8002/apt/<uniqueID>
