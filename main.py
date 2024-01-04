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
            response = httpx.get(first_one)

            results = re.findall(r'<h3>Download Mirrors</h3>(.+?)</ul>', response.text, re.DOTALL)
            results = re.findall(r'<li><a href="(.+?)" target="_blank" rel="noopener">(.+?)</a>', results[0])

            json_results = {"status": "Success", "results": []}
            for result in results:
                json_results["results"].append({"url": result[0], "title": result[1]})

            return json_results

        except Exception as e:
            return {"status": "Error", "message": str(e)}
