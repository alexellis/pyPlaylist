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

	def get_stats(self):
		#{'playtime': '848', 'uptime': '2565'}
		#{'songid': '33', 'playlistlength': '1', 'playlist': '86', 'repeat': '0',
		#'consume': '0', 'mixrampdb': '0.000000', 'random': '0', 'state': 'play',
		# 'elapsed': '7.476', 'volume': '-1', 'single': '0', 'time': '7:0', 'song': '0', 'audio': '44100:16:2', 'bitrate': '128'}
		all = {}
		all.update(self.client.stats())
		all.update(self.client.status())

		stats = {}
		stats["elapsed"] = all["elapsed"] if all.has_key("elapsed") else "0"
		stats["state"] = all["state"] if all.has_key("state") else "stopped"
		stats["playtime"] = all["playtime"]
		stats["uptime"] = all["uptime"]
		stats["bitrate"] = all["bitrate"] if all.has_key('bitrate') else 0
		print stats
		return stats

	def get_playing(self):
		name = "unknown"
		val = self.client.currentsong()
		return val["name"] if val.has_key('name') else None

	def load(self,list):
		print "loading list", list
		self.client.clear()
		self.client.load(list)

	def play(self):
		self.client.play()

	def stop(self):
		self.client.stop()
