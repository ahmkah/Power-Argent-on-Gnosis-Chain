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
```console
sudo ufw status

sudo ufw allow 53
sudo ufw allow 22
sudo ufw allow 9000
sudo ufw allow 30303

sudo ufw status enable
```


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
sudo ufw allow 8546

```

```console

./Nethermind.Runner \
--config gnosis \
--Init.WebSocketsEnabled true \
--JsonRpc.Enabled true \
--JsonRpc.EnabledModules "eth,net,web3,subscribe" \
--JsonRpc.WebSocketsPort 8546 \
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
We start the command in the stage at once in the screen "PORT1, PORT2, PORT3" instead of typing the desired port, such as 6699 7799 8899 ... Wait a little, then exit the screen with CTRL+A and D.. The time to sync "screen -r lighthouse" to enter the screen again can exceed 24 hours!!!

```console
sudo ufw allow PORT3

```

```console
lighthouse beacon_node \
--network gnosis \
--debug-level info \
--datadir ~/gnosis-lh1 \
--execution-endpoints http://127.0.0.1:8551 \
--jwt-secrets /tmp/jwtsecret \
--enr-udp-port <PORT1> } \
--enr-tcp-port <PORT2>  \
--discovery-port <PORT3>  \
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

## STEP-5 Power Argent Standalone Installation (enter the commands one by one):

```console
sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt install docker-ce docker-ce-cli containerd.io

sudo systemctl start docker
sudo systemctl enable docker

docker --version

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version

```

```console
sudo apt install git
sudo apt install nodejs
sudo apt install npm
```

```console
git clone https://github.com/eitelvolkerts/poweragent-standalone
cd poweragent-standalone
npm i
```
At this stage, if you are going to work with the same admin address and worker, you just need to move the backup file to the corresponding keys file using an application such as winscp, if you are going to create a new worker, skip this section!!!
UTC--2023-08-18T09-32-40.364Z--8ccf, from which we received the PowerArgent backup..... our file with a Winscp-style application
![image](https://github.com/ahmkah/Power-Argent-on-Gnosis-Chain/assets/99053148/253ebca1-ee45-4d04-8a0e-0b4f1c84e4b5)

if you want to create a new worker, use this command, if you have made a move, skip this part!!!
```console
node jsongen.js ${YOUR_WORKER_PRIVATE_KEY} ${A_PASSWORD_OF_YOUR_CHOICE}
```

``main.yaml`` editing. Now open the file below and just change your worker address '<WORKER_ADDRESS_FOR_WHICH_YOU_GENERATED_THE_KEYFILE>' and password '<PASSWORD_SPECIFIED_AT_KEYFILE_GENERATION>'. CTRL + X , y enter to save and exit.

```console
nano config/main.yaml
```

```console
networks:
    data_source: network
    enabled:
      - gnosis
    details:
      gnosis:
        rpc: '${YOUR_RPC}'
        max_priority_fee_per_gas: 6000000
        agents:
          '0x071412e301C2087A4DAA055CF4aFa2683cE1e499':
            executor: pga
            keeper_worker_address: '<WORKER_ADDRESS_FOR_WHICH_YOU_GENERATED_THE_KEYFILE>'
            key_pass: '<PASSWORD_SPECIFIED_AT_KEYFILE_GENERATION>'
            accept_max_base_fee_limit: true
            accrue_reward: true
            tx_resend_or_drop_after_blocks: 4
            tx_resend_max_gas_price_gwei: 1000
            tx_resend_max_attempts: 4
            gas_price_priority_add_gwei: 100
            # data_source: subgraph
            # subgraph_url: https://api.studio.thegraph.com/query/44364/ppav2-rd-sepolia-b11/version/latest
            max_block_delay: 10
            resolve_min_success_count: 3

```

## STEP-6 Power Argent Standalone Launch : 

To get the ${CONTAINER_NAME}, execute docker ps and find the container id. If you changed the name of the container, use it instead.

```console
docker pull powerpool/power-agent-node
docker compose up -d
docker logs -f ${CONTAINER_NAME}

```

Update (In the folder with the docker-compose.yaml file run)

```console
docker compose down --rmi local
docker pull eitelvolkerts/pagentv2
docker compose up -d

```
Stop (In the folder with the docker-compose.yaml file run)

```console
docker compose down --rmi local

```



