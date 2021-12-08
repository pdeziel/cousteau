from src.ingest import AssetCollector

def run():
    scraper = AssetCollector()
    scraper.collect()

if __name__ == "__main__":
    run()