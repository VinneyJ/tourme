##To Run this app
git clone 

cd Tourme

Activate virtual environment

pip install Flask
pip install SQLAlchemy
pip install flask-login


make all python files executable

#To run the main app:
```
chmod u+x app.py

./app.py
```

#To rollback the database:
```
chmod u+x rollback_db.py

./rollback_db.py
```

#To reload the database and prepopulate the users table by default:
```
./db_reload.py
```
#To create all the tables for the 1st time:
```
./db_engine.py
```



