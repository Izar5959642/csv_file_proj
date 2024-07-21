import csv 
import pandas as pd # for read from csv file

from config_n import *
from fetch_save_top_story_n import *
import matplotlib.pyplot as plt



def analys_data():

    """
    Reads the top story CSV file, calculates statistics (average, max, min scores, and comment statistics),
    and saves the results to another CSV file.

    Returns:
        None
    """

    # Read top story file 
    top_stories_df = pd.read_csv(NAME_FILE_TOP_STORY)

    # Get from top story file list of score and list of num of comments
    score_list = top_stories_df['Score'].tolist()
    num_comment_list = top_stories_df['Number of Comments'].tolist()

    # Average / others stats
    avg_score = sum(score_list) / len(score_list)
    max_score = max(score_list)
    min_score = min(score_list)
    total_comments = len(num_comment_list)
    total_sum_comments = sum(num_comment_list)
    avg_comment = total_sum_comments / total_comments

    # Insert the stats value into list
    list_avg = [avg_score, max_score, min_score,  avg_comment, total_sum_comments]

    # Insert the list stats into csv file
    with open(NAME_FILE_ALNALYS_DATA, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        names_list = ['Average Score','Max score', 'Min score', 'Average commanets\n per stories', 'Total comments sum']
        # Write lists on csv file 
        csv_writer.writerow(names_list)
        csv_writer.writerow(list_avg)
        print (f"Average data saved at {NAME_FILE_ALNALYS_DATA} file")
        
        # Plot the list on plt screen
        plot_stats(names_list, list_avg)

    return




def plot_stats(name_list, value_list):
    """
    Arguments:
        name_list = list of names of the stats
        value_list = list of the average / other stats value

    the function print on the screen the result

    return:
        None
    """
    color_list = ['green','blue','skyblue',  'purple', 'purple']

    plt.figure(figsize=(50, 50))
    plt.bar(name_list, value_list, color = color_list)

    plt.xlabel('Name of Stats')
    plt.ylabel('Values')
    plt.title('Stats')
    plt.show()
    return