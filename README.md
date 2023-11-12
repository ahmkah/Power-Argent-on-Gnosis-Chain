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

Generate JWT secret file by executing the following command:
```console
openssl rand -hex 32 | tr -d "\n" > "/tmp/jwtsecret"
```
```console
sudo apt-get install curl screen zip wget
```

```console

screen -S nethermind

sudo apt-get install libsnappy-dev

wget https://github.com/NethermindEth/nethermind/releases/download/1.20.4/nethermind-1.20.4-d06ec791-linux-x64.zip

unzip nethermind-1.20.4-d06ec791-linux-x64.zip

rm -rf nethermind-1.20.4-d06ec791-linux-x64.zip
```
We start the command in the stage at once in the screen, instead of <PORT1>, type the port that you want to be ws, such as 8599 ... Wait a little, then exit the screen with CTRL+A and D.. To enter the screen again "screen -r nethermind" :

```console

./Nethermind.Runner \
--config gnosis \
--Init.WebSocketsEnabled true \
--JsonRpc.Enabled true \
--JsonRpc.EnabledModules "eth,net,web3,subscribe" \
--JsonRpc.WebSocketsPort <PORT1> \
--JsonRpc.Host 0.0.0.0 \
--JsonRpc.JwtSecretFile /tmp/jwtsecret \
--baseDbPath ~/nethermindDb \
--JsonRpc.Timeout 120000 \
--Sync.FastSync true
```






