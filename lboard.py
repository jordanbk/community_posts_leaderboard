import os
import logging
import dataiku
import pandas as pd
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Read recipe inputs
messages_users_filtered_by_month_by_author_login_sorted = dataiku.Dataset("messages_users_filtered_by_month_by_author_login_sorted")
messages_users_filtered_by_month_by_author_login_sorted_df = messages_users_filtered_by_month_by_author_login_sorted.get_dataframe()

count_df = messages_users_filtered_by_month_by_author_login_sorted_df # For this sample code, simply copy input to output

# Read Kudos:
messages_users_filtered_by_month_by_author_login_kudos = dataiku.Dataset("messages_users_filtered_by_month_by_author_login_kudos")
messages_users_filtered_by_month_by_author_login_kudos_df = messages_users_filtered_by_month_by_author_login_kudos.get_dataframe()

kudos_df = messages_users_filtered_by_month_by_author_login_kudos_df

# Read Solutions:
messages_users_filtered_by_month_by_author_login_solutions = dataiku.Dataset("messages_users_filtered_by_month_by_author_login_solutions")
messages_users_filtered_by_month_by_author_login_solutions_df = messages_users_filtered_by_month_by_author_login_solutions.get_dataframe()

solutions_df = messages_users_filtered_by_month_by_author_login_solutions_df

#top count posters
top_count_poster1 = count_df['email'].iloc[0]
top_count_poster2 = count_df['email'].iloc[1]
top_count_poster3 = count_df['email'].iloc[2]

#top solutions posters
top_solution_poster1 = solutions_df['email'].iloc[0]
top_solution_poster2 = solutions_df['email'].iloc[1]
top_solution_poster3 = solutions_df['email'].iloc[2]

#top kudos posters
top_kudos_poster1 = kudos_df['email'].iloc[0]
top_kudos_poster2 = kudos_df['email'].iloc[1]
top_kudos_poster3 = kudos_df['email'].iloc[2]


dataiku.get_custom_variables()
project = dataiku.api_client().get_project(dataiku.default_project_key())
vars = project.get_variables()

client = WebClient(token="xoxb-")
logger = logging.getLogger(__name__)

channel_id="C057Y8V04E8"
token = "xoxb-token"

#lookup user by email --------------------------------------------------------------
try:
    
    result1 = client.users_lookupByEmail(
        token=token,
        email=top_count_poster1
    )
    logger.info(result1)

except SlackApiError:
    logger.error("Error getting top_count_poster email address")

# https://api.slack.com/methods/users.lookupByEmail
top_poster1 = result1['user']['id']

try:
    
    result2 = client.users_lookupByEmail(
        token=token,
        email=top_count_poster2
    )
    logger.info(result2)

except SlackApiError:
    logger.error("Error getting top_count_poster email address")

# https://api.slack.com/methods/users.lookupByEmail
top_poster2 = result2['user']['id']

try:
    
    result3 = client.users_lookupByEmail(
        token=token,
        email=top_count_poster3
    )
    logger.info(result3)

except SlackApiError:
    logger.error("Error getting top_count_poster email address")

# https://api.slack.com/methods/users.lookupByEmail
top_poster3 = result3['user']['id']

# top solutions --------------------------------------------------------------
try:
    
    result4 = client.users_lookupByEmail(
        token=token,
        email=top_solution_poster1
    )
    logger.info(result4)

except SlackApiError:
    logger.error("Error getting top_solution_poster email address")
    
top_solution1 = result4['user']['id']

try:
    
    result5 = client.users_lookupByEmail(
        token=token,
        email=top_solution_poster2
    )
    logger.info(result5)

except SlackApiError:
    logger.error("Error getting top_solution_poster email address")
    
top_solution2 = result5['user']['id']

try:
    
    result6 = client.users_lookupByEmail(
        token=token,
        email=top_solution_poster3
    )
    logger.info(result6)

except SlackApiError:
    logger.error("Error getting top_solution_poster email address")
    
top_solution3 = result6['user']['id']

# top kudos --------------------------------------------------------------
try:
    
    result7 = client.users_lookupByEmail(
        token=token,
        email=top_kudos_poster1
    )
    logger.info(result7)

except SlackApiError:
    logger.error("Error getting top_solution_poster email address")
    
top_kudos1 = result7['user']['id']

try:
    
    result8 = client.users_lookupByEmail(
        token=token,
        email=top_kudos_poster2
    )
    logger.info(result8)

except SlackApiError:
    logger.error("Error getting top_solution_poster email address")
    
top_kudos2 = result8['user']['id']

try:
    
    result9 = client.users_lookupByEmail(
        token=token,
        email=top_kudos_poster3
    )
    logger.info(result9)

except SlackApiError:
    logger.error("Error getting top_solution_poster email address")
    
top_kudos3 = result9['user']['id']

#define/set vars
vars['standard']['top_count_poster1']=top_poster1
vars['standard']['top_count_poster2']=top_poster2
vars['standard']['top_count_poster3']=top_poster3

vars['standard']['top_solution_poster1']=top_solution1
vars['standard']['top_solution_poster2']=top_solution2
vars['standard']['top_solution_poster3']=top_solution3

vars['standard']['top_kudos_poster1']=top_kudos1
vars['standard']['top_kudos_poster2']=top_kudos2
vars['standard']['top_kudos_poster3']=top_kudos3


project.set_variables(vars)
