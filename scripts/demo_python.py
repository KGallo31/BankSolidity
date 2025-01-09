import json
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

json_file_path = open('build/contracts/Bank.json')
data = json.load(json_file_path)

abi = data['abi']

address = '0x3756422A0434aec18cD2b817B4f58EdCA9fa12C8'
contract = w3.eth.contract(address=address, abi=abi)

print(contract)

print(w3.is_connected())

most_recent_block = w3.eth.block_number

print(most_recent_block)    

list_of_accounts = w3.eth.accounts

print(list_of_accounts)

list_of_block_number = contract.functions.get_blocks().call({'from': list_of_accounts[0]})
for block_num in list_of_block_number:
    current_block = w3.eth.get_block(block_num)
    trans = w3.eth.get_transaction(current_block['transactions'][0])
    input_from_block = contract.decode_function_input(trans.input)
    if '<Function deposit_funds()>' in str(input_from_block):
        print('Amount of funds that were deposited were:', trans.value)
    elif '<Function withdraw_funds(uint256)>' in str(input_from_block):
        print('Amount of funds that were withdrawn were:', trans.value)
    elif '<Function transfer_funds(address,uint256)>' in str(input_from_block):
        funds_transfered = input_from_block[1]['_funds']
        receiving_address = input_from_block[1]['receiving_address']
        print('funds were trasnfered to the address of: ', receiving_address, 'for the amount of: ', funds_transfered)
# byte_value = bytes.fromhex(block2['hash'])
# print(byte_value)

# print(block2['transactions'][0])
# trans = w3.eth.get_transaction(block2['transactions'][0])
# print(trans)
# print(contract.decode_function_input(trans))
# print(blocks)
# for num in blocks:
    # print(num)

# contract.functions.deposit_funds().transact({'from': list_of_accounts[0], 'value': 100})
# balance = contract.functions.check_balance().call({'from': list_of_accounts[0]})
# print('Current balance after depositing funds: ', balance)

# contract.functions.transfer_funds(list_of_accounts[1],50).transact({'from': list_of_accounts[0]})
# balance = contract.functions.check_balance().call({'from': list_of_accounts[0]})

# print('Current balance after transfering funds: ', balance)


