from analys_data_n import *
from fetch_save_top_story_n import *
from config_n import*

# URL for fetching top stories
topstories_url = TOP_STORIES_URL

# Fetch and save top stories
Fetch_and_Save_Top_Stories(topstories_url)

# Fetch and save comments for top stories
Fetch_Comments_for_Top_Stories()



# Analyze and save data and plot the result
analys_data()