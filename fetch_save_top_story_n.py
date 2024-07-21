import requests
import csv 
from config_n import *
import pandas as pd

def Fetch_and_Save_Top_Stories(topstories_url ):
    """
    Fetches top stories from the given URL, extracts details for each story,
    and saves them to a CSV file.

    Args:
        topstories_url (str): The URL to fetch top stories from.

    Returns:
        None
    """


    response = requests.get(topstories_url)
    name_csv_file = NAME_FILE_TOP_STORY
    item_url = ITEM_URL_DATA_STORY

    # Open top story 
    if response.status_code == 200:
        story_ids = response.json()
        story_ids = story_ids[:NUM_OF_SORIES_TO_READ]
        with open(name_csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # write the frist row , the header
            csv_writer.writerow(['Story Id', 'Title', 'URL', 'Score', 'By', 'Time', 'Descendants', 'Number of Comments','Top comment level'])

            list_id_comment = []
            # loop through the 10 frist top story IDs
            for story_id in story_ids:
                item_response = requests.get(item_url.format(story_id))
               
               # Open data of story 
                if item_response.status_code == 200:
                    # Get the items
                    item_data = item_response.json()

                    list_of_comment_id = item_data.get('kids', [])
                    top_comment_level = list_of_comment_id[0] if list_of_comment_id else "No comments"

                    if top_comment_level != "No comments":
                        list_id_comment.append(top_comment_level)

                    # Make a list from the attribute of the class
                    story_details = [
                        item_data.get('id', ''),
                        item_data.get('title', ''),
                        item_data.get('url', ''),
                        item_data.get('score', ''),
                        item_data.get('by', ''),
                        item_data.get('time', ''),
                        item_data.get('descendants', ''),
                        len(item_data.get('kids', [])),
                        top_comment_level
                    ]
                    # Insert the list into csv file
                    csv_writer.writerow(story_details)

            print (f"Data saved to {name_csv_file}")
    else:
        print ("Faild to retrive data")



def get_top_comment_id():
    """
    Reads the top story CSV file and extracts the IDs of the top comments.

    Returns:
        list: A list of top comment IDs.
    """

    top_sories_df = pd.read_csv(NAME_FILE_TOP_STORY)
    top_comment = top_sories_df['Top comment level'].tolist()
    return top_comment

def Fetch_Comments_for_Top_Stories():
    """
    Fetches comments for the top stories, extracts details for each comment,
    and saves them to a CSV file.

    Returns:
        None
    """

    list_comment = get_top_comment_id ()

    url_commant = URL_COMMENT
    name_file = NAME_FILE_COMMENT

    with open(name_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Comment Id', 'By', 'Perent' ,'Time', 'Text'])
       
        for id_comment in list_comment:
            item_respons = requests.get(url_commant.format(id_comment))

            if item_respons.status_code == 200:
                # Get the items
                item_data = item_respons.json()
                # Make a list from the attribute of the class
                story_details = [
                            item_data.get('id', ''),
                            item_data.get('by', ''),
                            item_data.get('parent', ''),
                            item_data.get('time', ''),
                            item_data.get('text', ''),
                        ]
                # Insert the list into csv file
                csv_writer.writerow(story_details)
            else:
                print ("Faild in write comment data")
                return
    print(f"Comment data write in {name_file} file")
    return
    