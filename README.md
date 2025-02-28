#### Install Xampp

```
chmod 755 xampp-linux-_-installer.run
sudo ./xampp-linux-_-installer.run
```

#### Install Python

```
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.13
python3 --version
python --version

or

tar -xf filename.tar.xz
cd extracted_directory_name
./configure
make
sudo make install
```

#### Install Django

```
sudo apt install python3-pip

==> run in project folder:
python3.13 -m venv myenv
source myenv/bin/activate
pip install --upgrade pip
pip install Django
django-admin --version
```

#### Create roject

```
django-admin startproject mysite
```

#### Create app

```
cd mysite
python manage.py startapp news
```

```python
# Generate migrations of app news
python manage.py makemigrations news

# Run migrations
python manage.py migrate
```

#### Run

```
python mysite/manage.py runserver
python mysite/manage.py runserver 8080
```

#### Step

Run migrations: `python manage.py migrate`
Create admin user: `python manage.py createsuperuser`

`source /home/nguyenloi/Desktop/demo-django/myenv/bin/activate`
`sudo apt-get install libmysqlclient-dev`
`pip install mysqlclient`

or

`pip install PyMySQL`

```python
# mysite/mysite/__init__.py
import pymysql
pymysql.install_as_MySQLdb()
```

Config database: mysite/mysite/settings.py

Filter with list_filter
Search with search_fields

#### Create model

Create models in mysite/news/models.py and Add app into mysite/mysite/settings.py
Add model to admin in mysite/news/admin.py

#### Create foreign key

`category = models.ForeignKey(Category, on_delete=models.CASCADE)`

#### Create requirement.txt

`pip freeze > requirements.txt`
