import json
from brownie import Bank, accounts

def main():
    address = '0x1BA2Af6eBB8181CD6F6c6BA69c41Ab968761Df17'
    bank_contract = Bank.at(address)

    bank_contract.deposit_funds({'from': accounts[1], 'value': 150})

    print("Balance of account 1: ", bank_contract.check_balance({'from': accounts[1]}))

    bank_contract.transfer_funds(accounts[2], 50, {'from': accounts[1]})

    print("Balance of account 1: ", bank_contract.check_balance({'from': accounts[1]}))
    print("Balance of account 2: ", bank_contract.check_balance({'from': accounts[2]}))

    bank_contract.withdraw_funds(50, {'from': accounts[1]})

    print("Balance of account 1: ", bank_contract.check_balance({'from': accounts[1]}));

    print("Blocks of account 1: ", bank_contract.get_blocks({'from': accounts[1]}))

