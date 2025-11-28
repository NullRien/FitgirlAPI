import httpx
import re

BASE_URL = "https://fitgirl-repacks.site/"

class FitGirl:
    def __init__(self):
        pass

    @staticmethod
    def new_posts():
        try:
            response = httpx.get(BASE_URL)

            results = re.findall(r'<h1 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h1>', response.text)
            results = [i for i in results if "Upcoming Repacks" not in i]
            json_results = {"status": "Success", "results": []}

            for result in results:
                json_results["results"].append({"url": result[0], "title": result[1]})

            return json_results

        except Exception as e:
            return {"status": "Error", "message": str(e)}

    @staticmethod
    def search(query):
        try:
            response = httpx.get(BASE_URL + "?s=" + query)

            if "Sorry, but nothing matched your search terms. Please try again with some different keywords." in response.text:
                return {"status": "Error", "message": "No results found."}

            results = re.findall(r'<h1 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h1>', response.text)
            json_results = {"status": "Success", "results": []}

            for result in results:
                json_results["results"].append({"url": result[0], "title": result[1]})

            return json_results

        except Exception as e:
            return {"status": "Error", "message": str(e)}

    @staticmethod
    def download(query):
        try:
            response = httpx.get(BASE_URL + "?s=" + query)

            if "Sorry, but nothing matched your search terms. Please try again with some different keywords." in response.text:
                return {"status": "Error", "message": "No results found."}

            results = re.findall(r'<h1 class="entry-title"><a href="(.+?)" rel="bookmark">(.+?)</a></h1>', response.text)
            first_one = results[0][0]
            title_name = results[0][1]
            response = httpx.get(first_one)

            # Regex for download section URLs (inside su-spoiler-content)
            download_section_blocks = re.findall(r'<div class="su-spoiler-content[^>]*>(.*?)</div>', response.text, re.DOTALL)
            download_urls = []
            for block in download_section_blocks:
                download_urls += re.findall(r'href="([^"]+)"', block)

            # Regex for torrent section URLs (http, https, magnet)
            torrent_section = re.search(r'<h3>Download Mirrors \(Torrent\)</h3>(.+?)</ul>', response.text, re.DOTALL)
            torrent_urls = []
            if torrent_section:
                torrent_urls = re.findall(r'(https?://[^\s"\'<>]+|magnet:\?xt=urn:[^"\s\'<>]+)', torrent_section.group(1))

            json_results = {"status": "Success", "game": title_name, "download_urls": download_urls, "torrent_urls": torrent_urls}
            return json_results

        except Exception as e:
            return {"status": "Error", "message": str(e)}
