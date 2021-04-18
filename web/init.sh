sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
sudo /etc/init.d/mysql restart
#sudo mysql -uroot -e "CREATE DATABASE stepic_web;"
#sudo mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
#sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost';"
#sudo mysql -uroot -e "FLUSH PRIVILEGES;"

sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"

python3 manage.py makemigrations qa
python3 manage.py migrate