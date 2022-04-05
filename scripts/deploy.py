from brownie import FundMe, MockV3Aggregator, config, network

from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_addres = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_addres = MockV3Aggregator[-1].address

    print(account.balance)
    fund_me = FundMe.deploy(
        price_feed_addres,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
