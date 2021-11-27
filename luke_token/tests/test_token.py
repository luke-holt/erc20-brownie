import pytest
from brownie import LukeToken, accounts, config, network
from scripts.deploy_token import deploy_token, INITIAL_SUPPLY
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)


def test_token():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip
    token = deploy_token()
    account = get_account()
    # Act
    # Assert
    assert INITIAL_SUPPLY == token.balanceOf(account)
