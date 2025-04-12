import vdf

class ItemSchemaParser:
	items_game = None

	def __init__( self ):
		try:
			self.items_game = vdf.load( open( "scripts/items/items_game.txt", "r" ) )["items_game"]
		except:
			print( "Failed to serialize items_game.txt!" )

	def get_qualities( self ):
		return self.items_game["qualities"] if self.items_game else []

	def get_all_items( self ):
		return self.items_game["items"] if self.items_game else []

	def get_all_attributes( self ):
		return self.items_game["attributes"] if self.items_game else []

	def get_cosmetic_unusual_effects( self ):
		return self.items_game["attribute_controlled_attached_particles"]["cosmetic_unusual_effects"] if self.items_game else []

	def get_weapon_unusual_effects( self ):
		return self.items_game["attribute_controlled_attached_particles"]["weapon_unusual_effects"] if self.items_game else []

	#def get_killstreak_eyeglows( self ):
	#	return self.items_game["attribute_controlled_attached_particles"]["killstreak_eyeglows"] if self.items_game else []
