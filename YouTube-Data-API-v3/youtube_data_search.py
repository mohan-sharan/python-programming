from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "ENTER YOUR DEVELOPER KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=25, order="relevance", token=None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    location=location,
    locationRadius=location_radius).execute()

    title = []
    videoId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    videos = []

    for search_result in search_response.get("items", []):
    	if search_result["id"]["kind"] == "youtube#video":

            title.append(search_result['snippet']['title'])

            videoId.append(search_result['id']['videoId'])

            video_response = youtube.videos().list(part='statistics, snippet, recordingDetails', id=search_result['id']['videoId']).execute()

            viewCount.append(video_response['items'][0]['statistics']['viewCount'])
            likeCount.append(video_response['items'][0]['statistics']['likeCount'])
            dislikeCount.append(video_response['items'][0]['statistics']['dislikeCount'])

    #print("VIDEO TITLE\n", title)
    #print("VIDEO ID\n", videoId)
    #print("VIEW COUNT\n", viewCount)
    #print("LIKE COUNT\n", likeCount)
    #print("DISLIKE COUNT\n", dislikeCount)

    search_dict = {'VIDEO TITLE':title, 'VIDEO ID':videoId, "VIEW COUNT":viewCount, "LIKE COUNT": likeCount, "DISLIKE COUNT": dislikeCount}
    return search_dict