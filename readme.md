sudo apt install libpq-dev python3-dev

You also need to install PostgreSQL

sudo -u postgres psql
postgres=# create database mydb;
postgres=# create user myuser with encrypted password 'mypass';
postgres=# grant all privileges on database mydb to myuser;

python manage.py migrate
python manage.py createsuperuser

Resetting postgres-db:
psql -d mydb
\c postgres
 DROP DATABASE mydb;
 create database mydb;

 {
	"username": "blue_dinosaur",
	"password": "SecurePassword1234"
}

admin
1234

- restart postgres
sudo service postgresql start

source ./byte-liferpg/.venv/bin/activate