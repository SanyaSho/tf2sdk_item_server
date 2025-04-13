import base64

# Protobuf messages
from gcsdk_pb2 import *

# Shared constants
from TFEnums import *

# For dump_message()
from CMsgSOCacheSubscribedParser import CMsgSOCacheSubscribedParser

def clamp( val: int, min: int, max: int ):
	if val > max:
		return max
	elif val < min:
		return min

	return val

class CMsgSOCacheSubscribedSerializer:
	msg: CMsgSOCacheSubscribed

	steamid: int
	account_id: int

	def __init__( self, owner_steamid: int, owner_account_id: int ):
		"""
		:param owner_steamid: User's SteamID
		:param owner_account_id: User's AccountID
		"""

		if owner_steamid == 0 or owner_account_id == 0:
			print( "SteamID / AccountID is invalid! See PlayerConstants.py" )
			return

		print( f"Initialized CMsgSOCacheSubscribedSerializer for {owner_steamid} / {owner_account_id}" )

		self.msg = CMsgSOCacheSubscribed()
		self.msg.owner = owner_steamid

		self.steamid = owner_steamid
		self.account_id = owner_account_id

	# Class presets (MSGID: 36)
	def add_class_loadout_preset( self, class_id: int, active_preset_id: int ):
		"""
		:param class_id: Class ID (See ETFClass)
		:type class_id: int
		:param active_preset_id: Preset ID (See ETFLoadoutPreset)
		:type active_preset_id: int
		"""

		active_preset_id = clamp( active_preset_id, ETFLoadoutPreset.MIN_PRESETS, ETFLoadoutPreset.MAX_PRESETS )

		preset = self.generate_object_if_not_exists( EEconTypeID.k_EEconTypeItemPresetInstance )

		data = CSOClassPresetClientData()
		data.account_id = self.account_id
		data.class_id = class_id
		data.active_preset_id = active_preset_id

		preset.object_data.append( data.SerializeToString() )

	def add_class_loadout_preset_array( self, preset_info: list ):
		"""
		:param preset_info: List of { "class_id": CLASS, "active_preset_id": PRESET }
		:type preset_info: list
		"""

		for preset in preset_info:
			class_id = preset["class_id"]
			active_preset_id = preset["active_preset_id"]

			self.add_class_loadout_preset( class_id, active_preset_id )


	# Helper for add_item_to_inventory
	def add_item_to_class( self, class_id: int, slot_id: int ):
		"""
		:param class_id: Class ID (See ETFClass)
		:param slot_id: Slot (See loadout_positions_t)
		:return: CSOEconItemEquipped
		:rtype: CSOEconItemEquipped
		"""

		data = CSOEconItemEquipped()
		data.new_class = class_id
		data.new_slot = slot_id
		return data

	# Inventory (MSGID: 1)
	def add_item_to_inventory( self, item_data: dict ):
		"""
		:param item_data: Information about item
		:type item_data: dict
		"""

		if "id" not in item_data or "slot" not in item_data or "def_index" not in item_data:
			print( "Invalid item!" )
			return

		item = self.generate_object_if_not_exists( EEconTypeID.k_EEconTypeItem )

		data = CSOEconItem()

		# Item ID
		data.id = item_data["id"]

		# Item Owner
		data.account_id = self.account_id

		# App managed int representing inventory placement
		data.inventory = item_data["slot"]

		# Item definition index (from items_game.txt)
		data.def_index = item_data["def_index"]

		# Item Level
		data.level = item_data["level"] if "level" in item_data else EEconConstants.MIN_ITEM_LEVEL

		# Item quality (rarity)
		data.quality = item_data["quality"] if "quality" in item_data else EEconItemQuality.AE_NORMAL

		# Flags (EEconItemFlags)
		data.flags = item_data["flags"] if "flags" in item_data else 0

		# Origin (EEconItemOrigin)
		data.origin = item_data["origin"] if "origin" in item_data else EEconItemOrigin.kEconItemOrigin_Drop

		# Custom name. Can be done with attribute.
		if "custom_name" in item_data:
			data.custom_name = item_data["custom_name"]

		# Custom desc. Can be done with attribute.
		if "custom_desc" in item_data:
			data.custom_desc = item_data["custom_desc"]

		# Item attributes
		if "attributes" in item_data:
			for i in range( 0, len( item_data["attributes"] ) ):
				if i >= EEconConstants.MAX_ATTRIBUTES_PER_ITEM:
					print( f"Item {item_data["def_index"]} has more than {EEconConstants.MAX_ATTRIBUTES_PER_ITEM} attributes!" )
					continue

				attribute = item_data["attributes"][i]

				if attribute is None: # skip invalid attributes
					continue

				data.attribute.append( attribute )

		# ?
		if "interior_item" in item_data:
			data.interior_item = item_data["interior_item"]

		# Is this item in use? (ie., being used as part of a cross-game trade)
		data.in_use = item_data["in_use"] if "in_use" in item_data else False

		# Style
		data.style = item_data["style"] if "style" in item_data else 0

		# ?
		if "original_id" in item_data:
			data.original_id = item_data["original_id"]

		data.contains_equipped_state = False # DEPRECATED

		if "equipped_on" in item_data:
			for i in item_data["equipped_on"]:
				if i is None:
					continue

				data.equipped_state.append( i )

		data.contains_equipped_state_v2 = True

		item.object_data.append( data.SerializeToString() )

	# Client info (MSGID: 7)
	def add_client_info( self, client_info: dict ):
		"""
		:param client_info: Information about client
		:type client_info: dict
		"""

		info = self.generate_object_if_not_exists( EEconTypeID.k_EEconTypeGameAccountClient )

		data = CSOEconGameAccountClient()
		data.additional_backpack_slots = client_info["additional_backpack_slots"] if "additional_backpack_slots" in client_info else EEconConstants.MAX_NUM_FULL_BACKPACK_SLOTS
		data.competitive_access = True
		data.phone_identifying = True

		info.object_data.append( data.SerializeToString() )

	# 19

	# Map contributions (MSGID: 28)
	def add_map_contribution_data( self, map_def_index: int, contribution_level: int ):
		mapcontrib = self.generate_object_if_not_exists( EEconTypeID.k_EEconTypeMapContribution )

		data = CSOTFMapContribution()
		data.account_id = self.account_id
		data.def_index = map_def_index
		data.contribution_level = contribution_level

		mapcontrib.object_data.append( data.SerializeToString() )

	# 39

	# Matchmaking rating (MSGID: 2007)
	def add_matchmaking_rating_data( self, rating_type: EMMRating, rating_primary: int, rating_secondary: int, rating_tertiary: int ):
		"""
		:param rating_type: Rating type (See EMMRating)
		:type rating_type: EMMRating
		"""

		stats = self.generate_object_if_not_exists( EGCTFProtoObjectTypes.k_EProtoObjectTFRatingData )

		data = CSOTFRatingData()
		data.account_id = self.account_id
		data.rating_type = rating_type
		data.rating_primary = rating_primary
		data.rating_secondary = rating_secondary
		data.rating_tertiary = rating_tertiary

		stats.object_data.append( data.SerializeToString() )

	# 44
	# 45
	# 46
	# 2
	# 40

	#
	# Utility functions
	#
	def generate_object_if_not_exists( self, type_id: int ):
		obj = self.get_object_by_type_id( type_id )
		if not obj:
			obj = self.msg.objects.add()
			obj.type_id = type_id

		return obj

	def get_object_by_type_id( self, type_id: int ):
		for obj in self.msg.objects:
			if obj.type_id == type_id:
				return obj

		return None

	def get_message_as_base64( self ):
		"""
		Returns CMsgSOCacheSubscribed encoded with Base64
		:return: Base64 string
		:rtype: str
		"""

		data = self.msg.SerializeToString()
		b64data = base64.b64encode( data )
		return b64data.decode( "utf-8" )

	def dump_message( self ):
		parser = CMsgSOCacheSubscribedParser()
		parser.parse( self.msg.SerializeToString() )
