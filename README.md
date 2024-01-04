# FitGirl Repacks API

This is a Python API designed to interact with the FitGirl Repacks website (https://fitgirl-repacks.site/), a popular source for free game repacks. The API provides functionality to retrieve new posts, search for specific games, and obtain download links.

## Features

1. **New Posts:**
   - Retrieves the latest game posts from FitGirl Repacks.
   - Returns a JSON object containing the URLs and titles of the latest games.

2. **Search:**
   - Searches for games based on the provided query.
   - Returns a JSON object with the URLs and titles of the matching games.

3. **Download:**
   - Retrieves download links for a specific game.
   - Returns a JSON object with download URLs and titles.

## Installation

Before using the API, make sure to install httpx. You can install it using the following command:

```bash
pip install httpx
```

## Usage

1. **New Posts:**
   ```python
   from fitgirl_api import FitGirl

   new_posts = FitGirl.new_posts()
   print(new_posts)
   ```

2. **Search:**
   ```python
   from fitgirl_api import FitGirl

   search_results = FitGirl.search("your_query_here")
   print(search_results)
   ```

3. **Download:**
   ```python
   from fitgirl_api import FitGirl

   download_links = FitGirl.download("your_query_here")
   print(download_links)
   ```

## Notes

- This API uses either the `httpx` lbrary.
- In case of errors, the API returns a JSON object with the status and an error message.

Feel free to explore and integrate this API into your projects to enhance your experience with FitGirl Repacks. For more information on FitGirl Repacks, visit their official website: [FitGirl Repacks](https://fitgirl-repacks.site/).
