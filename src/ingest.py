import json

from src.opensea import Client as OpenseaClient

class AssetCollector():
    """
    AssetCollector probes an NFT marketplace and collects asset data. 
    """
    def __init__(self, marketplace="opensea"):
        self.marketplace = marketplace

    def collect(self, num=100):
        """
        Collects asset data from the specified marketplace.
        """
        if self.marketplace == "opensea":
            self.collect_opensea(num)
        else:
            raise Exception("Unknown marketplace: {}".format(self.marketplace))

    def collect_opensea(self, num):
        """
        Collects asset data from the OpenSea marketplace using the REST API.
        """
        client = OpenseaClient()
        collected = 0
        limit = 50
        assets = []
        while collected < num:
            res = client.get_assets(order_by="sale_date", order_direction="desc", offset=collected, limit=limit)
            assets += res["assets"]
            collected += len(res["assets"])
            print("Collected {} assets".format(collected))
        f = open("assets.json", "w+")
        json.dump(assets, f)
        f.close()
    