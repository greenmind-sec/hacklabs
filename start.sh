

VAR_IPS="
172.18.18.10 lfi.hack.me \n
172.18.18.11 bruteforce.hack.me \n
172.18.18.12 heartblend.hack.me \n
172.18.18.13 juice-shop.hack.me \n
172.18.18.14 dvwa.hack.me \n
172.18.18.15 dsvw.hack.me \n
172.18.18.16 webgoat.hack.me \n
#172.18.18.17 javavulnerablelab.hack.me \n
#172.18.18.18 hackazon.hack.me
"

cp /etc/hosts /etc/hosts_BKP
echo $VAR_IPS >> /etc/hosts
docker-compose up -d
sleep 3
ping -c1 172.18.18.10
ping -c1 172.18.18.11
ping -c1 172.18.18.12
ping -c1 172.18.18.13
ping -c1 172.18.18.14
ping -c1 172.18.18.15
ping -c1 172.18.18.16
