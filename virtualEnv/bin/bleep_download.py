import requests

import re

import os
from bs4 import BeautifulSoup



class BleepTrack:
	def __init__(self, album, title, index):
		self.album=album
		self.title=title
		i=str(index)
		self.padded_index="0"*(3-len(i))+i

	@property
	def url(self):
		return self.album.url_prefix+self.padded_index+'.mp3'

	





######### Aborted due to file dependencies....

