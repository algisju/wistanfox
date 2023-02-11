from pytube import YouTube

# Set the URL of the video you want to download
url = "https://www.youtube.com/watch?v=dYrPjYuJK7M"

# Create a YouTube object
yt = YouTube(url)

#print(yt.streams.get_by_resolution)

resolution = "720p"

# Get the first video stream available with the desired resolution
video = yt.streams.filter(res=resolution).first()
# Get the first video stream available
#video = yt.streams.first()

# Download the video to the current directory
video.download(filename="marais.mp4")