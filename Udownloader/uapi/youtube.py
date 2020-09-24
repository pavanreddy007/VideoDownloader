from pytube import YouTube
def Download(videodata):

	SAVE_PATH = "F:/Coding/Youtube/"

	SAVE_PATH=SAVE_PATH+videodata[0]

	link=videodata[1]

	yt=YouTube(link)
	stream=yt.streams.first() 
	path=stream.download(SAVE_PATH)

	return(path)
