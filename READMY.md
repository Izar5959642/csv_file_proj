# Top Stories Analysis Project

This project fetches, analyzes, and plots data related to top stories from Hacker News. It performs the following tasks:

1. **Fetch and Save Top Stories**: Retrieves the latest top stories from Hacker News and saves them to a CSV file.
2. **Fetch Comments for Top Stories**: Collects comments related to the top stories and saves them to a CSV file.
3. **Analyze Data**: Analyzes the collected data to calculate statistics and plots the results.

## Files

- **`config_n.py`**: Configuration file containing URLs, file names, and parameters.
- **`fetch_save_top_story_n.py`**: Contains functions to fetch and save top stories and comments.
- **`analys_data_n.py`**: Contains functions to analyze data and plot results.
- **`main.py`**: Main script to execute the tasks of fetching, saving, and analyzing data.

## Configuration

Ensure that `config_n.py` contains the correct URLs and other settings:

```python
# URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
ITEM_URL_DATA_STORY = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty"
URL_COMMENT = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty"

# Names of the files
NAME_FILE_TOP_STORY = "Top_story_details.csv"
NAME_FILE_COMMENT = "Comment_data.csv"
NAME_FILE_ALNALYS_DATA = "Anlays_data.csv"

# Number of stories to read
NUM_OF_SORIES_TO_READ = 14

