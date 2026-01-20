import json
import os
import requests
from datetime import date
from .models import ApodImage, Asteroid
from .exceptions import AuthenticationError, ResourceNotFoundError

class NasaClient:
    BASE_URL = "https://api.nasa.gov"

    def __init__(self, api_key: str = "DEMO_KEY", cache_file: str = "nasa_cache.json"):
        self.api_key = api_key
        self.cache_file = cache_file

    def _request(self, endpoint: str, params: dict = None):
        if params is None:
            params = {}
        params["api_key"] = self.api_key
        
        response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
        
        if response.status_code == 403:
            raise AuthenticationError("Invalid API Key provided.")
        if response.status_code == 404:
            raise ResourceNotFoundError("Space data not found.")
            
        response.raise_for_status()
        return response.json()

    def get_apod(self) -> ApodImage:
        today = str(date.today())

        # Cache Check
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                cached = json.load(f)
                if cached.get("date") == today:
                    return ApodImage(**cached)

        # API Fetch
        data = self._request("/planetary/apod")
        
        # Save to Cache
        clean_data = {
            "date": data.get("date"),
            "title": data.get("title"),
            "url": data.get("url"),
            "explanation": data.get("explanation")
        }
        with open(self.cache_file, 'w') as f:
            json.dump(clean_data, f)

        return ApodImage(**clean_data)