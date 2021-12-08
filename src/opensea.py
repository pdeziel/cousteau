import requests

class Client:
    """
    REST client for interacting with the OpenSea API.
    """
    def __init__(self):
        self.base_url = "https://api.opensea.io/api/v1"

    def get_assets(self, **kwargs):
        """
        Get a page of assets from the API.
        """
        url = f"{self.base_url}/assets?"
        for k, v in kwargs.items():
            if url[-1] != "?":
                url += "&"
            url += f"{k}={v}"
        print(url)
        response = requests.request("GET", url)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        return response.json()