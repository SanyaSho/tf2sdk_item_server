import random

# Shared constants
from TFEnums import *

class CMsgSOCacheSubscribedSerializerTest:
	serializer = None

	def __init__( self, serializer ):
		self.serializer = serializer

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

		# Shitty values. Must start with 1
		id = 1
		slot = 1


		def add_item_with_custom_texture( id: int = 1, slot: int = 1, itemid: int = -1, quality: int = EEconItemQuality.AE_NORMAL, ctlo: int = -1, cthi: int = -1 ):
			if itemid == -1 or ctlo == -1 or cthi == -1:
				return

			sign_attribs = [
				self.serializer.attrib_helper.allocate_item_attribute_int_name( "custom texture lo", ctlo ),
				self.serializer.attrib_helper.allocate_item_attribute_int_name( "custom texture hi", cthi )
			]

			self.serializer.add_item_to_inventory(
				{
					"id": id, "slot": slot, "def_index": itemid,
					"quality": quality,
					"attributes": sign_attribs
				}
			)

			# Must increment this everytime you touch the inventory
			id += 1
			slot += 1
			return id, slot

		# Add "Genuine Conscientious Objector" and "Genuine Photo Badge" to the inventory with custom texture
		#(id, slot) = add_item_with_custom_texture( id, slot, 474, EEconItemQuality.AE_RARITY1, 378690501, 469905498 )
		#(id, slot) = add_item_with_custom_texture( id, slot, 623, EEconItemQuality.AE_RARITY1, 378690501, 469905498 )


		def add_item_with_paintkit( id: int = 1, slot: int = 1, itemid: int = -1 ):
			paintkit_attribs = [
				#self.serializer.attrib_helper.allocate_item_attribute_int_name( "paintkit_proto_def_index",	144 ),
				#self.serializer.attrib_helper.allocate_item_attribute_int_name( "set_item_texture_wear",	1053609165 ),
				#self.serializer.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_lo",	687649116 ),
				#self.serializer.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_hi",	320889421 )

				# Dragon Slayer War Paint (Factory New) #(seed: 1634437561148735688)
				self.serializer.attrib_helper.allocate_item_attribute_int_name( "paintkit_proto_def_index",	390 ),		# 834
				self.serializer.attrib_helper.allocate_item_attribute_int_name( "set_item_texture_wear",	1045220557 ),	# 725
				#self.serializer.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_lo",	1607696584 ),	# 866
				#self.serializer.attrib_helper.allocate_item_attribute_int_name( "custom_paintkit_seed_hi",	380547149 )	# 867
			]

			self.serializer.add_item_to_inventory(
				{
					"id": id, "slot": slot, "def_index": itemid,
					"attributes": paintkit_attribs
				}
			)

			# Must increment this everytime you touch the inventory
			id += 1
			slot += 1
			return id, slot

		# Add Rocket Launcher with a paintkit applied
		#(id, slot) = add_item_with_paintkit( id, slot, 205 )


		def give_some_painted_weapons( id: int = 1, slot: int = 1, itemid: int = 1, max: int = 1 ):
			for paint in range( max ):
				attributes = [
					self.serializer.attrib_helper.allocate_item_attribute_int_name( "paintkit_proto_def_index",	paint )
				]

				self.serializer.add_item_to_inventory(
					{
						"id": id, "slot": slot, "def_index": itemid,
						"attributes": attributes
					}
				)

				# Must increment this everytime you touch the inventory
				id += 1
				slot += 1

			return id, slot

		#(id, slot) = give_some_painted_weapons( id, slot, 205, 512 )


		def give_all_taunts( id: int = 1, slot: int = 1 ):
			for i in self.serializer.isp.get_all_items():
				item = self.serializer.isp.get_all_items()[i]

				if ("prefab" in item and "taunt" in item["prefab"]) or ("taunt" in item) or ("item_slot" in item and "taunt" in item["item_slot"]):
					self.serializer.add_item_to_inventory(
						{
							"id": id, "slot": slot, "def_index": i
						}
					)

					# Must increment this everytime you touch the inventory
					id += 1
					slot += 1

			return id, slot

		#(id, slot) = give_all_taunts( id, slot )


		def give_valve_rocket_launcher( id: int = 1, slot: int = 1 ):
			# taken from TF2C b4 items_game.txt
			valve_rocket_launcher_attributes = [
				# Unusual Effect: Flying Bits
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "attach particle effect",	2.0 ),

				# +1009900% damage bonus
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "damage bonus",		10100.0 ),

				# +109900% clip size
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "clip size bonus",		1100.0 ),

				# +75% faster firing speed
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "fire rate bonus",		0.25 ),

				# On Hit: Gain up to +250 health
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "heal on hit for slowfire",	250.0 ),

				# On Kill: 10 seconds of 100% critical chance
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "critboost on kill",		10.0 ),

				# +50% projectile speed
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "Projectile speed increased",	1.5 ),

				# +100% faster move speed on wearer
				self.serializer.attrib_helper.allocate_item_attribute_float_name( "move speed bonus",		2.0 ),
			]

			valve_rocket_launcher_equipped_on = [
				#self.serializer.add_item_to_class( ETFClass.TF_CLASS_SOLDIER, loadout_positions_t.LOADOUT_POSITION_PRIMARY )
			]

			self.serializer.add_item_to_inventory(
				{
					"id": id, "slot": slot, "def_index": 18,
					"level": EEconConstants.MAX_ITEM_LEVEL, "quality": EEconItemQuality.AE_DEVELOPER,
					"attributes": valve_rocket_launcher_attributes, "equipped_on": valve_rocket_launcher_equipped_on
				}
			)

			# Must increment this everytime you touch the inventory
			id += 1
			slot += 1
			return id, slot

		(id, slot) = give_valve_rocket_launcher( id, slot )


		def give_item_with_all_qualities( item: int, id: int = 1, slot: int = 1 ):
			for quality in range( EEconItemQuality.AE_MAX_TYPES ):
				self.serializer.add_item_to_inventory(
					{
						"id": id, "slot": slot, "def_index": item,
						"level": EEconConstants.MAX_ITEM_LEVEL, "quality": quality
					}
				)

				# Must increment this everytime you touch the inventory
				id += 1
				slot += 1

			return id, slot

		#(id, slot) = give_item_with_all_qualities( 18, id, slot )
		#(id, slot) = give_item_with_all_qualities( 1071, id, slot )


		def give_item_with_unusual_effect( item: int, effect_list: dict, id: int = 1, slot: int = 1 ):
			for i in effect_list:
				effect_attributes = [
					self.serializer.attrib_helper.allocate_item_attribute_float_name( "attach particle effect",	float( i ) ),
					self.serializer.attrib_helper.allocate_item_attribute_string_name( "custom name attr",		f"Effect: {i}" )
				]

				self.serializer.add_item_to_inventory(
					{
						"id": id, "slot": slot, "def_index": item,
						"level": EEconConstants.MAX_ITEM_LEVEL, "quality": EEconItemQuality.AE_UNUSUAL,
						"attributes": effect_attributes
					}
				)

				# Must increment this everytime you touch the inventory
				id += 1
				slot += 1

			return id, slot

		#(id, slot) = give_item_with_unusual_effect( 125, self.serializer.isp.get_cosmetic_unusual_effects(), id, slot )
		##(id, slot) = give_item_with_unusual_effect( 125, self.serializer.isp.get_killstreak_eyeglows(), id, slot )
		#(id, slot) = give_item_with_unusual_effect( 13, self.serializer.isp.get_weapon_unusual_effects(), id, slot )


		def give_australium_item( item: int, id: int = 1, slot: int = 1 ):
			# https://forums.alliedmods.net/showthread.php?t=141962&page=121
			australium_attributes = [
				#"2027 ; 1 ; 2022 ; 1 ; 542 ; 1"
				self.serializer.attrib_helper.allocate_item_attribute_int_name( "is australium item",	1 ),
				self.serializer.attrib_helper.allocate_item_attribute_int_name( "loot rarity",		1 ),
				self.serializer.attrib_helper.allocate_item_attribute_int_name( "item style override",	1 )
			]
			self.serializer.add_item_to_inventory(
				{
					"id": id, "slot": slot, "def_index": item,
					"quality": EEconItemQuality.AE_STRANGE,
					"attributes": australium_attributes
				}
			)

			# Must increment this everytime you touch the inventory
			id += 1
			slot += 1
			return id, slot

		#(id, slot) = give_australium_item( 200, id, slot )
		#(id, slot) = give_australium_item( 205, id, slot )


		def give_all_items( id: int = 1, slot: int = 1 ):
			def get_random_item_level():
				return random.randrange( EEconConstants.MIN_ITEM_LEVEL, EEconConstants.MAX_ITEM_LEVEL, 1 )

			def get_quality_from_schema_string( quality: str ):
				return int( self.serializer.isp.get_qualities()[quality]["value"] ) if quality in self.serializer.isp.get_qualities() else EEconItemQuality.AE_NORMAL

			for i in self.serializer.isp.get_all_items():
				if i == "default":
					continue

				item = self.serializer.isp.get_all_items()[i]

				if "prefab" in item and "tournament_medal" in item["prefab"]:
					continue

				#slot_banlist = [ "hat" ]
				#if "item_slot" in item and item["item_slot"] in slot_banlist:
				#	continue

				#prefab_banlist = [ "base_hat", "hat", "tournament_medal" ]
				#if "prefab" in item:
				#	for j in item["prefab"].split( " " ):
				#		if j in prefab_banlist:
				#			continue

				quality = get_quality_from_schema_string( item["item_quality"] ) if "item_quality" in item else EEconItemQuality.AE_NORMAL

				attributes = [
					#self.serializer.attrib_helper.allocate_item_attribute_string_name( "custom desc attr", f"EconID: {i}" )
				]

				self.serializer.add_item_to_inventory(
					{
						"id": id, "slot": slot, "def_index": int( i ),
						"level": get_random_item_level(), "quality": quality,
						"attributes": attributes
					}
				)

				# Must increment this everytime you touch the inventory
				id += 1
				slot += 1

			return id, slot

		#(id, slot) = give_all_items( id, slot )


		print( f"Total items added: {id - 1}, used slots: {slot - 1}" )


		# Append player info
		self.serializer.add_client_info(
			{ "additional_backpack_slots": EEconConstants.MAX_NUM_BACKPACK_SLOTS }
		)


		# CASUAL: Level: 150 Tier: 8
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_12v12_Rank,				150,		0,		0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_12v12_Rank_PlayerAcknowledged,	150,		0,		0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_XP,					10000000,	0,		0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_Casual_XP_PlayerAcknowledged,		10000000,	0,		0 )

		# COMPETITIVE: Rank: Death Merchant, Wins: 10, Games played: 10, MMR: 1000000000
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_Rank,					13,		10,		10 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_Rank_PlayerAcknowledged,			13,		10,		10 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_GLICKO,					1000000000,	0,		0 )
		self.serializer.add_matchmaking_rating_data( EMMRating.k_nMMRating_6v6_GLICKO_PlayerAcknowledged,		1000000000,	0,		0 )


		#self.serializer.dump_message()
