from brownie import LukeToken, network, config
from scripts.helpful_scripts import get_account, get_contract


# 1B tokens
INITIAL_SUPPLY = 1000000000


def deploy_token():
    account = get_account()
    token = LukeToken.deploy(INITIAL_SUPPLY, {"from": account})
    print("Token deployed!")
    return token


def main():
    pass
