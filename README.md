# Chatroom
Python sample project

pip install virtualenv

mkdir ChatApp

cd ChatApp

virtualenv chat-env

source chat-env/bin/activate

pip intsall django djangorestframework django-widget-tweaks

django-admin startproject ChatApp .

./manage.py makemigrations

./manage.py migrate

./manage.py runserver

./manage.py startapp chat

