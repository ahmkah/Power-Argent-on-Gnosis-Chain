<h1 align="center"> Power Argent on Gnosis Chain </h1>

https://powerpool.notion.site/Launching-Gnosis-Client-6b96aa04804b45c1acd5654e7d166aed

https://powerpool.notion.site/Landing-Page-59ab36698b8e417db9be39bdd432a42f

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
We start the command in the stage at once in the screen, instead of "PORT1" type the port that you want to be ws, such as 8599 ... Wait a little, then exit the screen with CTRL+A and D.. To enter the screen again "screen -r nethermind" :

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

![image](https://github.com/ahmkah/Power-Argent-on-Gnosis-Chain/assets/99053148/5ccff0e1-3c97-45b3-9b02-357d37024282)

## STEP-3, Install Lighthouse (enter the commands one by one):

```console

screen -S lighthouse

curl -LO https://github.com/sigp/lighthouse/releases/download/v4.5.0/lighthouse-v4.5.0-x86_64-unknown-linux-gnu.tar.gz

tar -xvf lighthouse-v4.5.0-x86_64-unknown-linux-gnu.tar.gz

sudo cp lighthouse /usr/bin

rm -rf lighthouse lighthouse-v4.5.0-x86_64-unknown-linux-gnu.tar.gz
```
We start the command in the stage at once in the screen "PORT2, PORT3, PORT4" instead of typing the desired port, such as 6699 7799 8899 ... Wait a little, then exit the screen with CTRL+A and D.. The time to sync "screen -r lighthouse" to enter the screen again can exceed 24 hours!!!

```console
lighthouse beacon_node \
--network gnosis \
--debug-level info \
--datadir ~/gnosis-lh1 \
--execution-endpoints http://127.0.0.1:8551 \
--jwt-secrets /tmp/jwtsecret \
--enr-udp-port <PORT2> } \
--enr-tcp-port <PORT3>  \
--discovery-port <PORT4>  \
--checkpoint-sync-url https://checkpoint.gnosis.gateway.fm \
--disable-deposit-contract-sync
```

You will see something like this:
![image](https://github.com/ahmkah/Power-Argent-on-Gnosis-Chain/assets/99053148/86cc9b90-be88-4450-9b00-b265a79c60f8)

Some errors may pop out - ignore them. At the same time, your execution client will catch up:
![image](https://github.com/ahmkah/Power-Argent-on-Gnosis-Chain/assets/99053148/24749caf-5f66-449f-bd51-f91f52a0e4e8)

## STEP-4: Expose JSON RPC Port

To utilize the RPC endpoint (provided by your execution client) on an outside machine, enable port forwarding for port `8546` and use the following address: `ws://ip.of.your.server:8546`, replacing the phrase with the actual IP address of the PC your Nethermind client runs on.

If the **PowerAgent** is to be run on the same machine, it is not necessary to enable port forwarding.

## STEP-5 Power Argent Standalone Installation auto script:
