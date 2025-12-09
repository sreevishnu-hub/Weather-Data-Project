# main.py
import os
import time
import json
from datetime import datetime
from weather_fetcher import WeatherFetcher
from s3_uploader import S3Uploader
from dotenv import load_dotenv

load_dotenv()


def run_once():
    # Load secrets from environment variables
    api_key = os.getenv('OPENWEATHER_API_KEY')
    bucket = os.getenv('AWS_S3_BUCKET')
    cities = os.getenv('CITIES', 'London,New York,Tokyo').split(',')

    if not api_key:
        print("ERROR: OPENWEATHER_API_KEY is missing in .env")
        return

    if not bucket:
        print("ERROR: AWS_S3_BUCKET is missing in .env")
        return

    fetcher = WeatherFetcher(api_key)
    uploader = S3Uploader(bucket)

    timestamp = datetime.utcnow().isoformat() + 'Z'

    for city in filter(None, [c.strip() for c in cities]):
        data = fetcher.fetch_city(city)
        if data is None:
            print(f"Failed to fetch weather for {city}")
            continue

        payload = {
            'city': city,
            'timestamp_utc': timestamp,
            'data': data,
        }

        key = f"{city.replace(' ', '_')}/{timestamp}.json"
        success = uploader.upload_json(payload, key)
        print(f"Uploaded {key}: {success}")


if __name__ == '__main__':
    run_once()
