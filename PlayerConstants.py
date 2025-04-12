# Define your SteamID / AccountID here. You can find both here "https://steamdb.info/calculator".

import json

class PlayerInfo:
	PLAYER_STEAMID = 0
	PLAYER_ACCNTID = 0

	def __init__( self ):
		self.parse_player_info()

	def parse_player_info( self ):
		try:
			json_info = json.load( open( "scripts/player_info.json", "r" ) )

			if "steamid" not in json_info or "account_id" not in json_info:
				return

			self.PLAYER_STEAMID = int( json_info["steamid"] )
			self.PLAYER_ACCNTID = int( json_info["account_id"] )

			print( f"SteamID: {self.PLAYER_STEAMID} / AccountID: {self.PLAYER_ACCNTID}" )
		except:
			print( "Malformed player_info.txt!" )