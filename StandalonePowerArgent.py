import time
import yaml
import hexbytes as hb
import copy
import os
import sys
def modifyCompose(path, number):
    path = path+'/docker-compose.yaml'
    path = path.replace('//', '/')
    with open (path, 'r') as file:
        compose = yaml.safe_load(file)
        compose['services'][str(number)] = copy.deepcopy(compose['services']['bot'])
        del compose['services']['bot']
    with open (path, 'w') as file:
        yaml.dump(compose, file)
def makeConfig(path, datasource, graphUrl, network, rpc, agentAddress, workerAddress, workerPass = 'admin', maxPriorityFeePerGas = 6000000, acceptMax = True, accrueReward = True, 
              resendBlocks = 4, resendPrice = 1000, resendMax = 4, priorityAdd = 100, maxDelay = 10, minSuccess = 3):
    path = path+'/main.yaml'
    path = path.replace('//', '/')
    if isinstance(workerAddress, int):
        workerAddress = hb.HexBytes(workerAddress).hex()
    if isinstance(agentAddress, int):
        agentAddress = hb.HexBytes(agentAddress).hex()
    with open (path, 'w') as file:
        config = {'networks': {'data_source': 'network',
  'enabled': [network],
  'details': {network: {'rpc': rpc,
    'max_priority_fee_per_gas': maxPriorityFeePerGas,
    'agents': {agentAddress: {'executor': 'pga',
      'keeper_worker_address': workerAddress,
      'key_pass': workerPass,
      'accept_max_base_fee_limit': acceptMax,
      'accrue_reward': accrueReward,
      'tx_resend_or_drop_after_blocks': resendBlocks,
      'tx_resend_max_gas_price_gwei': resendPrice,
      'tx_resend_max_attempts': resendMax,
      'gas_price_priority_add_gwei': priorityAdd,
      'max_block_delay': maxDelay,
      'resolve_min_success_count': minSuccess}}}}}}
        if datasource == 'subgraph':
            config['networks']['details'][network]['data_source'] = 'subgraph'
            config['networks']['details'][network]['subgraph_url'] = graphUrl
        yaml.dump(config, file)
workerName = sys.argv[1]
agentAddr = sys.argv[2]
datasource = sys.argv[3]
graphUrl = sys.argv[4]
workerPk = sys.argv[5]
workerPassword = sys.argv[6]
workerAddress = sys.argv[7]
rpc = sys.argv[8]
chain = sys.argv[9]

filesAndFolders = os.listdir(os.getcwd())
if workerName in filesAndFolders:
    print(f'Worker {workerName} already exists')
else:
    os.system(f'mkdir {workerName}')
    os.chdir(f'{workerName}')
    os.system('git clone https://github.com/eitelvolkerts/poweragent-standalone.git')
    os.chdir('poweragent-standalone')
    os.system('npm i')
    os.system(f'node jsongen.js {workerPk} {workerPassword}')
    modifyCompose(os.getcwd(), workerName)
    makeConfig(
        os.getcwd()+'/config',
        datasource,
        graphUrl,
        chain,
        rpc,
        agentAddr,
        workerAddress,
        workerPassword,
    )
    os.system('docker compose up -d')
    os.chdir('../..')
    print(os.getcwd())
    print(f'Set worker {workerName} up')