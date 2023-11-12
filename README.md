# Power-Argent-on-Gnosis-Chain

## Hardware requirements
```console
CPU: 4 Cores
RAM: 16 GB
SSD: 300 GB
Ubuntu 20.04 or 22.04
```
## STEP-1, Let's update our server:
```console
sudo apt-get update && sudo apt-get upgrade -y
```

## STEP-2, Install Nethermind clients (enter the commands one by one):

## ``IMPORTANT! Do not forget to forward ports: 30303 and  9000 on your router or digital hosting! Otherwise, your nodes will not be discoverable and will not sync!``

/ Generate JWT secret file by executing the following command:
```console
openssl rand -hex 32 | tr -d "\n" > "/tmp/jwtsecret"
```

