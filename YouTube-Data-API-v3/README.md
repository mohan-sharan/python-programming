## _SEARCH BY KEYWORD - Dude Perfect_

![dude_perfect](https://user-images.githubusercontent.com/36114089/45137246-6c389800-b16d-11e8-92ee-dac45ddb57f9.png)

### _YouTube Data API V3_
YouTube Data API v3 is an API that provides access to YouTube data, such as videos, playlists, and channels.

**STEPS:**
- pip install --upgrade google-api-python-client
- pip install --upgrade oauth2client
- Create a new project in Google Developers Console (https://console.developers.google.com/apis/library) and enable YouTube Data API v3.
- The "Create Credentials" button is clicked and the API key (For Example: AIzaSyB_MTBisQ1LH0ydNnTAorR2r-LWEl3oe-k) is obtained. 
- Copy the API key and paste it under DEVELOPER_KEY in "youtube_data_search.py"
- "youtube_data_search.py" is placed in a working directory. 
- Open ipython. The code in "youtube_search_results.py" is typed to analyze the view count, the number of likes and dislikes of few videos from the YouTube channel "Dude Perfect".
- The figure below shows a bar chart plot of the number of views and likes for few videos:

![youtube_search_results dude perfect](https://user-images.githubusercontent.com/36114089/45139744-6b583400-b176-11e8-99b5-add3fcb518ca.PNG)
