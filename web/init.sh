
sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install python3.6
sudo rm /usr/bin/python3 && sudo ln -s /usr/bin/python3.6 /usr/bin/python3
curl "https://bootstrap.pypa.io/ez_setup.py" -o "ez_setup.py" && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python3 ez_setup.py && sudo python3 get-pip.py
sudo -H /usr/local/bin/pip3 install --upgrade django==3.1
wget https://www.sqlite.org/2019/sqlite-autoconf-3280000.tar.gz && tar zxvf sqlite-autoconf-3280000.tar.gz cd sqlite-autoconf-3280000
./configure
sudo make install
sudo LD_RUN_PATH=/usr/local/lib ./configure --enable-optimizations
export LD_LIBRARY_PATH="/usr/local/lib"
sudo rm /usr/bin/sqlite3 && sudo ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
sudo mkdir public
sudo mkdir uploads
cd public
sudo mkdir img
sudo mkdir css
sudo mkdir js
