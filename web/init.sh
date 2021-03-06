sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py
sudo gunicorn -c /etc/gunicorn.d/django.py ask.wsgi:application -D
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo service nginx restart

sudo /etc/init.d/mysql start


mysql -uroot -e "CREATE DATABASE askappdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -uroot -e "CREATE USER 'askapp'@'localhost' IDENTIFIED BY 'passwrd123';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON askappdb.* TO 'askapp'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"

sudo python ~/web/ask/manage.py makemigrations qa
sudo python ~/web/ask/manage.py migrate