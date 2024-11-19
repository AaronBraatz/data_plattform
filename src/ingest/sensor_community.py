"""Load data from sensor.community."""
from pathlib import Path
from tqdm import tqdm
import requests
from lxml import html
import re

from src.minio import load_file_to_bucket, BUCKET_SENSOR_COMMUNITY

BASE_URL = 'https://archive.sensor.community/'
DATE_PATTERN = r'\d{4}-\d\d-\d\d'
FILE_PATTERN = r'\d{4}-\d\d-\d\d.+\.csv'

def get_sub_urls(base_url: str, pattern: str) -> list[str]:
    response = requests.get(base_url)
    tree = html.fromstring(response.content)
    urls = tree.xpath('//table//tr/td/a/@href')
    return [url for url in urls if re.match(pattern, url)]


def main():
    for day_url in get_sub_urls(BASE_URL, DATE_PATTERN):
        print(f'Loading for this date: {day_url}')

        for file_url in tqdm(get_sub_urls(BASE_URL + day_url, FILE_PATTERN), ):
            # print(f'Loading this file: {file_url}')

            load_file_to_bucket(
                file_url=BASE_URL + day_url + file_url,
                file_path=Path(day_url, file_url),
                bucket_name=BUCKET_SENSOR_COMMUNITY,
            )


if __name__ == '__main__':
    main()