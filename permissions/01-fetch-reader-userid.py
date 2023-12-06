import asyncio
import json
import os

import py_nillion_client as nillion


async def main():
    with open(os.environ["NILLION_CONFIG"], "r") as fh:
        config = json.load(fh)

    # Path to the user keys
    reader_userkey_path = config["YOUR_READERKEY_PATH_HERE"]

    # Path to the node key generated in previous step
    nodekey_path = config["YOUR_NODEKEY_PATH_HERE"]

    # Bootnode multiadress from from run-local-cluster output
    bootnodes = [config["YOUR_BOOTNODE_MULTIADDRESS_HERE"]]

    # This is the cluster id from run-local-cluster output
    cluster_id = config["YOUR_CLUSTER_ID_HERE"]

    nodekey = nillion.NodeKey.from_file(nodekey_path)
    payments_config = nillion.PaymentsConfig(
        config["YOUR_BLOCKCHAIN_RPC_ENDPOINT"],
        config["YOUR_WALLET_PRIVATE_KEY"],
        int(config["YOUR_CHAIN_ID"]),
        config["YOUR_PAYMENTS_SC_ADDRESS"],
        config["YOUR_BLINDING_FACTORS_MANAGER_SC_ADDRESS"],
    )

    reader = nillion.NillionClient(
        nodekey,
        bootnodes,
        nillion.ConnectionMode.relay(),
        nillion.UserKey.from_file(reader_userkey_path),
        payments_config,
    )

    print(reader.user_id())


asyncio.run(main())
