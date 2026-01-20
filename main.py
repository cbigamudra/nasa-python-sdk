from nasa import NasaClient

def run_demo():
    # Use DEMO_KEY or your own from api.nasa.gov
    client = NasaClient(api_key="DEMO_KEY")
    
    try:
        print("Fetching Astronomy Picture of the Day...")
        apod = client.get_apod()
        print(f"Title: {apod.title}")
        print(f"URL: {apod.url}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_demo()