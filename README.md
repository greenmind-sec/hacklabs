# HackLabs
Labs for hacking using docker.

## Install hacklabs

### Install Docker
Install Docker.
```sh
https://docs.docker.com/engine/install/
```
> Install docker in ubuntu: https://docs.docker.com/engine/install/ubuntu/

### Install python3 pip
Install pip3 for python.
```sh
apt-get install python3-pip
```
> Using apt install

### Install requirements.txt
Install libs **docker-compose** and **python_hosts**.
```sh
pip3 install -r requirements.txt
```

### Execution permission
Granting execution permission for hacklabs
```sh
chmod +x hacklabs.py
```

## Start and Stop

### Up Lab
Start labs
```sh
sudo ./hacklabs.py
```
![Start HackLabs](https://i.imgur.com/RuiRGW5.png)

Check labs IPS.

![Check Hosts](https://i.imgur.com/f8HHhkT.png)

### Stop Lab
Stop project
```sh
sudo ./hacklabs.py
```
![Stop HackLabs](https://i.imgur.com/QZpxwhK.png)
