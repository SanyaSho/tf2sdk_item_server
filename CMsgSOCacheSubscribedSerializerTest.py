import random

from CMsgSOCacheSubscribedSerializer import CMsgSOCacheSubscribedSerializer
from ItemSchemaParser import ItemSchemaParser
from EconAttributeHelper import EconAttributeHelper

# Shared constants
from TFEnums import *

class CMsgSOCacheSubscribedSerializerTest:
	serializer: CMsgSOCacheSubscribedSerializer = None

	last_id = 1
	last_slot = 1

	isp: ItemSchemaParser = None
	attrib_helper: EconAttributeHelper = None

	def __init__( self, isp: ItemSchemaParser, serializer: CMsgSOCacheSubscribedSerializer ):
		self.serializer = serializer

		self.isp = isp
		self.attrib_helper = EconAttributeHelper( self.isp.get_all_attributes() )

	def get_random_item_level( self ):
		return random.randrange( EEconConstants.MIN_ITEM_LEVEL, EEconConstants.MAX_ITEM_LEVEL, 1 )

	def get_quality_from_schema_string( self, quality: str ):
		return int( self.isp.get_qualities()[quality]["value"] ) if quality in self.isp.get_qualities() else EEconItemQuality.AE_NORMAL

	def add_item_to_inventory( self, item_data: dict ):
		item_data.update( { "id": self.last_id, "slot": self.last_slot } )

		self.serializer.add_item_to_inventory( item_data )

		self.last_id += 1
		self.last_slot += 1

	def serialize_test_message( self ):
		# Set default active loadout preset for each class
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_SCOUT,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_SNIPER,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_SOLDIER,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_DEMOMAN,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_MEDIC,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_HEAVYWEAPONS,	ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_PYRO,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_SPY,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )
		self.serializer.add_class_loadout_preset( ETFClass.TF_CLASS_ENGINEER,		ETFLoadoutPreset.TF_LOADOUT_PRESET_A )


		def add_item_with_custom_texture( itemid: int = -1, quality: int = EEconItemQuality.AE_NORMAL, ctlo: int = -1, cthi: int = -1 ):
			if itemid == -1 or ctlo == -1 or cthi == -1:
				return

			sign_attribs = [
				self.attrib_helper.allocate_item_attribute_int_name( "custom texture lo", ctlo ),
				self.attrib_helper.allocate_item_attribute_int_name( "custom texture hi", cthi )
			]

			self.add_item_to_inventory(
				{
					"def_index": itemid,
					"quality": quality,
					"attributes": sign_attribs
				}
			)

		# Add "Genuine Conscientious Objector" and "Valve Photo Badge" to the inventory with custom texture
		#add_item_with_custom_texture( 474, EEconItemQuality.AE_RARITY1, 378690501, 469905498 )
		#add_item_with_custom_texture( 623, EEconItemQuality.AE_DEVELOPER, 378690501, 469905498 )


		def add_item_with_paintkit( itemid: int = -1 ):
			paintkit_attribs = [
				#self.attrib_helper.allocate_item_attribute_int_name( "paintkit_proto_def_index",	144 ),
				#self.attrib_helper.allocate_item_attribute_int_name( "set_item_texture_wear",		1053609165 ),
				#self.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_lo",	687649116 ),
				#self.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_hi",	320889421 )

				# Dragon Slayer War Paint (Factory New) #(seed: 1634437561148735688)
				self.attrib_helper.allocate_item_attribute_int_name( "paintkit_proto_def_index",	390 ),		# 834
				self.attrib_helper.allocate_item_attribute_int_name( "set_item_texture_wear",	1045220557 ),	# 725
				#self.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_lo",	1607696584 ),	# 866
				#self.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_hi",	380547149 )	# 867
			]

			self.add_item_to_inventory(
				{
					"def_index": itemid,
					"attributes": paintkit_attribs
				}
			)


		# Add Rocket Launcher with a paintkit applied
		#add_item_with_paintkit( 205 )


		def give_some_painted_weapons( itemid: int = 1, max: int = 1 ):
			for paint in range( max ):
				attributes = [
					self.attrib_helper.allocate_item_attribute_int_name( "paintkit_proto_def_index",	paint )
				]

				self.add_item_to_inventory(
					{
						"def_index": itemid,
						"attributes": attributes
					}
				)

		#give_some_painted_weapons( 205, 512 )


		def give_all_taunts():
			for i in self.isp.get_all_items():
				item = self.isp.get_all_items()[i]

				if ("prefab" in item and "taunt" in item["prefab"]) or ("taunt" in item) or ("item_slot" in item and "taunt" in item["item_slot"]):
					self.serializer.add_item_to_inventory(
						{
							"def_index": i
						}
					)

		#give_all_taunts()


		def give_valve_rocket_launcher():
			# taken from TF2C b4 items_game.txt
			valve_rocket_launcher_attributes = [
				# Unusual Effect: Flying Bits
				self.attrib_helper.allocate_item_attribute_float_name( "attach particle effect",		2.0 ),

				# +1009900% damage bonus
				self.attrib_helper.allocate_item_attribute_float_name( "damage bonus",			10100.0 ),

				# +109900% clip size
				self.attrib_helper.allocate_item_attribute_float_name( "clip size bonus",			1100.0 ),

				# +75% faster firing speed
				self.attrib_helper.allocate_item_attribute_float_name( "fire rate bonus",			0.25 ),

				# On Hit: Gain up to +250 health
				self.attrib_helper.allocate_item_attribute_float_name( "heal on hit for slowfire",	250.0 ),

				# On Kill: 10 seconds of 100% critical chance
				self.attrib_helper.allocate_item_attribute_float_name( "critboost on kill",		10.0 ),

				# +50% projectile speed
				self.attrib_helper.allocate_item_attribute_float_name( "Projectile speed increased",	1.5 ),

				# +100% faster move speed on wearer
				self.attrib_helper.allocate_item_attribute_float_name( "move speed bonus",		2.0 ),
			]

			valve_rocket_launcher_equipped_on = [
				#self.serializer.add_item_to_class( ETFClass.TF_CLASS_SOLDIER, loadout_positions_t.LOADOUT_POSITION_PRIMARY )
			]

			self.add_item_to_inventory(
				{
					"def_index": 18,
					"level": EEconConstants.MAX_ITEM_LEVEL, "quality": EEconItemQuality.AE_DEVELOPER,
					"attributes": valve_rocket_launcher_attributes, "equipped_on": valve_rocket_launcher_equipped_on
				}
			)

		give_valve_rocket_launcher()


		def give_item_with_all_qualities( item: int ):
			for quality in range( EEconItemQuality.AE_MAX_TYPES ):
				self.add_item_to_inventory(
					{
						"def_index": item,
						"level": EEconConstants.MAX_ITEM_LEVEL, "quality": quality
					}
				)

		#give_item_with_all_qualities( 18 )
		#give_item_with_all_qualities( 1071 )


		def give_item_with_unusual_effect( item: int, effect_list: dict ):
			for i in effect_list:
				effect_attributes = [
					self.attrib_helper.allocate_item_attribute_float_name( "attach particle effect",		float( i ) ),
					self.attrib_helper.allocate_item_attribute_string_name( "custom name attr",		f"Effect: {i}" )
				]

				self.add_item_to_inventory(
					{
						"def_index": item,
						"level": EEconConstants.MAX_ITEM_LEVEL, "quality": EEconItemQuality.AE_UNUSUAL,
						"attributes": effect_attributes
					}
				)

		#give_item_with_unusual_effect( 125, self.isp.get_cosmetic_unusual_effects() )
		##give_item_with_unusual_effect( 125, self.isp.get_killstreak_eyeglows() )
		#give_item_with_unusual_effect( 13, self.isp.get_weapon_unusual_effects() )


		def give_australium_item( item: int ):
			# https://forums.alliedmods.net/showthread.php?t=141962&page=121
			australium_attributes = [
				#"2027 ; 1 ; 2022 ; 1 ; 542 ; 1"
				self.attrib_helper.allocate_item_attribute_int_name( "is australium item",	1 ),
				self.attrib_helper.allocate_item_attribute_int_name( "loot rarity",		1 ),
				self.attrib_helper.allocate_item_attribute_int_name( "item style override",	1 )
			]
			self.add_item_to_inventory(
				{
					"def_index": item,
					"quality": EEconItemQuality.AE_STRANGE,
					"attributes": australium_attributes
				}
			)

		#give_australium_item( 200 )
		#give_australium_item( 205 )


		def give_all_items():
			for i in self.isp.get_all_items():
				if i == "default":
					continue

				item = self.isp.get_all_items()[i]

				if "prefab" in item and "tournament_medal" in item["prefab"]:
					continue

				quality = self.get_quality_from_schema_string( item["item_quality"] ) if "item_quality" in item else EEconItemQuality.AE_NORMAL

				attributes = [
					#self.attrib_helper.allocate_item_attribute_string_name( "custom desc attr", f"EconID: {i}" )
				]

				self.add_item_to_inventory(
					{
						"def_index": int( i ),
						"level": self.get_random_item_level(), "quality": quality,
						"attributes": attributes
					}
				)

		#give_all_items()


		# Add the "World Traveler's Hat"
		self.add_item_to_inventory( { "def_index": 1899, "level": 20, "quality": EEconItemQuality.AE_UNIQUE } )


		print( f"Total items added: {self.last_id - 1}, used slots: {self.last_slot - 1}" )


		# Append player info
		self.serializer.add_client_info(
			{ "additional_backpack_slots": EEconConstants.MAX_NUM_FULL_BACKPACK_SLOTS }
		)


		# Add max contribution level for each map token (used by World Traveler's Hat)
		for def_index in self.isp.get_all_items():
			item = self.isp.get_all_items()[def_index]

			if "prefab" not in item or "map_token" not in item["prefab"]:
				continue

			self.serializer.add_map_contribution_data( int( def_index ), random.randrange( 0, 200, 25 ) )


		# CASUAL: Level: 150 Tier: 8
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_12v12_Rank,				150,	0,	0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_12v12_Rank_PlayerAcknowledged,	150,	0,	0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_XP,					10000000,	0,	0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_XP_PlayerAcknowledged,		10000000,	0,	0 )

		# COMPETITIVE: Rank: Death Merchant, Wins: 10, Games played: 10, MMR: 1000000000
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_Rank,					13,		10,	10 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_Rank_PlayerAcknowledged,			13,		10,	10 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_GLICKO,					1000000000,	0,	0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_GLICKO_PlayerAcknowledged,		1000000000,	0,	0 )


		#self.serializer.dump_message()
