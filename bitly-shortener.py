import os
import requests
import json
import argparse
from tinydb import TinyDB, Query
from dotenv import load_dotenv



def cache_to_db(data):
	db.insert(data)


def check_link_in_cache(link):
	query = Query()
	cached_link =  db.search(query.long_link == link)
	if cached_link:
		return cached_link[0].get('short_link')


def check_clicks(link, token):
	url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks'
	response = requests.get(url, json={'units':-1},
	headers=authorization_headers)
	response_json = response.json()
	link_clicks = response_json.get('link_clicks')
	if link_clicks:
		clicks = link_clicks[0].get('clicks')
		return f'Total clicks for this link: {clicks}'
	else:
		return 'There is no clicks for this link'


def shorten_link(link, token):
	url = 'https://api-ssl.bitly.com/v4/shorten'
	response = requests.post(url, json={'long_url':link},
	headers=authorization_headers)
	response_json = response.json()
	short_link = response_json.get('id')
	cache_to_db({'long_link':link,
	'short_link':short_link})
	return short_link


def check_link(link):
	if check_link_in_cache(link):
		print(check_link_in_cache(link))
	elif 'bit.ly' in link:
		if 'http://bit.ly' in link:
			link = link.split('//')[1]
		print(check_clicks(link, token))
	else:
		if 'http://' in link:
			print(shorten_link(link, token))
		else:
			print('This is not a valid link.')


if __name__ == '__main__':
	load_dotenv()
	db_name = os.getenv('CACHE_DB')
	db = TinyDB(db_name)
	token = os.getenv('BITLY_TOKEN')
	authorization_headers = {
		'Authorization':f'Bearer {token}'}
	parser = argparse.ArgumentParser()
	parser.add_argument("link",
	help="shorten the link or return clicks",
	nargs=1)
	args = parser.parse_args()
	link = args.link[0]
	check_link(link)
