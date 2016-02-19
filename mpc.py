from mpd import MPDClient

class Player:
	def __init__(self):
	    self.client = MPDClient()
	    self.client.connect("localhost", 6600)
	    self.client.timeout = 10
	    self.client.idletimeout = None 


	def quit(self):
	    self.client.close()
	    self.client.disconnect()

	def get_playlists(self):
	    val = self.client.listplaylists()
	    return val

	def get_playing(self):
		name = "unknown"
		val = self.client.playlistinfo()
		if(len(val)>0):
			print val[0]
			name = val[0]["name"]

		return name

	def load(self,list):
		print "loading list", list
		self.client.clear()
		self.client.load(list)

	def play(self):
		self.client.play()

	def stop(self):
		self.client.stop()