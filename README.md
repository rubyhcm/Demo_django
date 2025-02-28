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

#### Run

```
python mysite/manage.py runserver
python mysite/manage.py runserver 8080
```

#### Step

Run migrations: `python manage.py migrate`
Create admin user: `python manage.py createsuperuser`
