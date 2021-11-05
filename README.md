# TourMe

![](web_static/static/images/tourme_logo.png)

This is our Portfolio Project, concluding our Foundations Year at Holberton School

## Project Description



**Deployed Site**
[]()

**Landing Page**
[Landing Page-Site]()

**Girum**
- [linkedin]()
- [final project blog]()

**Fkadeal**
- [linkedin]()
- [final project blog]()

**Vincent**
- [linkedin]()
- [final project blog]()

### functionality

---

## installation

this project works was built using ubuntu 19.10 but can be tested using ubuntu 14.04. 

#### requirements

- [mysql](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04) database software administrator
- [sqlalchemy](https://docs.sqlalchemy.org/en/13/intro.html#installation)
- [python3](https://docs.python-guide.org/starting/install3/linux/)
- flask ([installation](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask), no need to install `virtualenv`)
- [pip3](https://askubuntu.com/questions/778052/installing-pip3-for-python3-on-ubuntu-16-04-lts-using-a-proxy)
- [flask-login](https://flask-login.readthedocs.io/en/latest/)

#### getting started

Git clone <project>

cd Tourme

Activate virtual environment

- pip install Flask
- pip install SQLAlchemy
- pip install flask-login

- [Install mysqlclient](https://askubuntu.com/a/1331893)

## Connect to the MySQL database with your dummy credetials
- [Creating a new MySQL database user](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)


make all python files executable

## To run the main app:
```
chmod u+x app.py

./app.py
```

in your browser type the following url: http://0.0.0.0:5000/

---

## To rollback the database:
```
chmod u+x rollback_db.py

./db/rollback_db.py
```

## To reload the database and prepopulate the users table by default:
```
./db/db_reload.py
```
## To create all the tables for the 1st time:
```
./db/db_engine.py
```



### usage

Once you get the local server running, the site will be connected automatically to the database. On the welcome page you can see the names of the tour guides and posts as well. You can now create an account or log-in if you have already registered. after you log in you can now create posts and access tour-guides, hire a tour-guide message a tour-guide, share your experiences with a blog post. More features to be are progresivley being added.
### contributing

## screenshot

## data modeling

![]()

## license

## authors
* Girum- [github]()   
* Fkadeal- [github](https://github.com/fkadeal) 
* Vincent - [Github]() 
