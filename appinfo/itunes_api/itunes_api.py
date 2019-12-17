import requests
import json

class iTunesApi:
    search_url = "https://itunes.apple.com/search?entity=software"

    def search_itunes_api(self, country_code, search_term):
        fullUrl = self.search_url + "&country=" + country_code + "&term=" + search_term
        response = requests.get(fullUrl)

        if response.status_code != 200:
            return response.status_code

        return response.json()