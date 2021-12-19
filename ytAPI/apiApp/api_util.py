from .models import Videos
from ytAPI import settings
from datetime import datetime, timedelta

from googleapiclient.discovery import build
from apiclient.errors import HttpError

# Function for fetching videos from YouTube API
def fetch_videos():

    # Fetch the keys from settings file
    available_apikeys = settings.API_KEYS                   
    current_time = datetime.now()                 
    
    # Since we need to get the posts which were posted 5 minutes from current_time
    req_time = current_time - timedelta(minutes=5)
    
    # flag variable ensures the successful fetching of the videos.
    flag=False
    for apikey in available_apikeys:
        try:
            # For more details : https://developers.google.com/youtube/v3/quickstart/python
            # Youtube API call 
            youtube = build("youtube", "v3", developerKey=apikey)
           
            # Calling instance for 'football' query 
            req = youtube.search().list(q="football",part="snippet", order="date",maxResults=50, publishedAfter=(req_time.replace(microsecond=0).isoformat()+'Z') )
            # Executing response 
            response = req.execute()

            flag=True
            for obj in response['items']:
                title = obj['snippet']['title']
                description = obj['snippet']['description']
                publishingDateTime = obj['snippet']['publishedAt']
                thumbnailsUrl = obj['snippet']['thumbnails']['default']['url']
                channelTitle = obj['snippet']['channelTitle']

                # Saving the details in the Videos model
                Videos.objects.create(title=title, description=description,publishingDateTime=publishingDateTime, thumbnailsUrl=thumbnailsUrl,channelTitle=channelTitle)

        # If the quota for an api key is not exceeded keep on using the same key
        except HttpError as er:
            err_code = er.resp.status
            if not(err_code == 400 or err_code == 403):
                break

        if flag:
            break