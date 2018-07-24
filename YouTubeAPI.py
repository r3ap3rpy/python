from pprint import pprint
import requests
import os
import json


class YouTubeAPIException(Exception):
	""" Custom error exception for the YouTubeAPI class! """
	pass


class YouTubeAPI(object):
	__ChannelInfo = None
	__PlayLists = []
	__VideoLists = []
	def __init__(self, ChannelID, ChannelAPIKey):
		self.ChannelID = ChannelID
		self.ChannelAPIKey = ChannelAPIKey


	@property
	def ChannelName(self):
		if not self.__ChannelInfo:
			self.get_ChannelInfo()
		
		return self.__ChannelInfo['items'][0]['snippet']['title']


	@property
	def ChannelDescription(self):
		if not self.__ChannelInfo:
			self.get_ChannelInfo()
		
		return self.__ChannelInfo['items'][0]['snippet']['description']

	@property
	def ChannelCreationDate(self):
		if not self.__ChannelInfo:
			self.get_ChannelInfo()
		
		return self.__ChannelInfo['items'][0]['snippet']['publishedAt']

	@property
	def ChannelPlayLists(self):
		if not self.__PlayLists:
			self.get_PlayLists()
		
		return self.__PlayLists

	@property
	def ChannelVideos(self):
		if not self.__VideoLists:
			self.get_VideosFromPlaylists()

		return self.__VideoLists


	def get_ChannelInfo(self):
		self.__ChannelInfo = json.loads(requests.get(url="https://www.googleapis.com/youtube/v3/channels?part=snippet&id={}&key={}".format(self.ChannelID,self.ChannelAPIKey)).text)
		return self.__ChannelInfo

	def get_PlayLists(self):
		self.__PlayLists = []
		for item in json.loads(requests.get(url="https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={}&key={}".format(self.ChannelID,self.ChannelAPIKey)).text)['items']:
			self.__PlayLists.append({'Name':item['snippet']['title'],'ID':item['id'],'CreatedAt':item['snippet']['publishedAt'],'Description':item['snippet']['description']})

		return self.__PlayLists


	def get_VideosFromPlaylists(self, PlayList = None):
		self.__VideoLists = []

		if not self.__PlayLists:
			self.get_PlayLists()

		if PlayList is None:
			ToProcess = [(_['ID'],_['Name']) for _ in self.__PlayLists ]
		else:
			ToProcess = [(_['ID'],_['Name'])  for _ in self.__PlayLists if PlayList in (_['ID'],_['Name'])]

		if len(ToProcess) != 0:
			print('Playlist: {}'.format(ToProcess))
			for playlist in ToProcess:
				ItemsToProcess = []
				url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&key={}".format(playlist[0],self.ChannelAPIKey)
				PlaylistResponse = json.loads(requests.get(url=url).text)
				ItemsToProcess.append(PlaylistResponse['items'])
				while PlaylistResponse.get('nextPageToken'):
					url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&pageToken={}&playlistId={}&key={}".format(PlaylistResponse.get('nextPageToken'),playlist[0],self.ChannelAPIKey)
					PlaylistResponse = json.loads(requests.get(url=url).text)	
					ItemsToProcess.append(PlaylistResponse['items'])

				for kitem in ItemsToProcess:
					for jitem in kitem:	
						self.__VideoLists.append({'PlayList':playlist[1],'VideoName':jitem['snippet']['title'],'URL':("https://www.youtube.com/watch?v=" + jitem['snippet']['resourceId']['videoId']),'ID':jitem['snippet']['resourceId']['videoId'],'Description':jitem['snippet']['description'].replace('\n\n','<br>').replace('\n','<br>')})
			
			return self.__VideoLists			
		else:
			raise YouTubeAPIException('Could not get the videos from the specified playlist: {}, valid combo -> ({} or {})'.format(PlayList,','.join([_['Name'] for _ in self.__PlayLists]),','.join([_['ID'] for _ in self.__PlayLists])))


	def __repr__(self):
		return "{}(ChannelID = {}, ChannelAPIKey = {})".format(self.__class__.__name__, self.ChannelID, self.ChannelAPIKey)

	def __str__(self):
		return "{}(ChannelID = {}, ChannelAPIKey = {})".format(self.__class__.__name__, self.ChannelID, self.ChannelAPIKey)

	def __format__(self,r):
		return "{}(ChannelID = {}, ChannelAPIKey = {})".format(self.__class__.__name__, self.ChannelID, self.ChannelAPIKey)

CHNID = os.getenv('YTCHN')
CHAPI = os.getenv('YTAPI')

YT = YouTubeAPI(ChannelID = CHNID, ChannelAPIKey = CHAPI)

pprint(YT.ChannelName)
pprint(YT.ChannelDescription)
pprint(YT.ChannelCreationDate)
pprint(YT.ChannelPlayLists)
pprint(YT.ChannelVideos)
#for video in YT.get_VideosFromPlaylists():
#	print(video)