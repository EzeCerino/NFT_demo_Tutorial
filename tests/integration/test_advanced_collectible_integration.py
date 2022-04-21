from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIROMENTES,
    get_account,
    get_contract,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from brownie import network
import pytest
import time


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTES:
        pytest.skip()
    advanced_collectible, creating_tx = deploy_and_create()
    time.sleep(120)
    assert advanced_collectible.tokenCounter() == 1
