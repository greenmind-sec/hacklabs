# HackLabs
Labs for hacking using docker.

## Install hacklabs

### Build project
For install hacklabs.
```sh
docker-compose build --no-cache
```
[![asciicast](https://asciinema.org/a/JfI3giuTl2xhqDzALJmaoYDcd.png)](https://asciinema.org/a/JfI3giuTl2xhqDzALJmaoYDcd)

### Up Lab
Start labs
```sh
sudo docker-compose up -d
```
[![asciicast](https://asciinema.org/a/ggSwhfCaaBWtu8EleqXnaU4uN.png)](https://asciinema.org/a/ggSwhfCaaBWtu8EleqXnaU4uN)

Or using **script.sh** and redirect domain.
```sh
sudo python3 hacklabs.py
```
[![asciicast](https://asciinema.org/a/KWCa7SAnFgKxbIQPH5LRB1NzI.png)](https://asciinema.org/a/KWCa7SAnFgKxbIQPH5LRB1NzI)

### Stop Lab
Stop project
```sh
sudo python3 hacklabs.py
```

### Check Domain
Check domain ip.

Domain used is **hack.me**.
```sh
cat /etc/hosts
```

[![asciicast](https://asciinema.org/a/GTVCzRIGfmhptW1jX070livBJ.png)](https://asciinema.org/a/GTVCzRIGfmhptW1jX070livBJ)
