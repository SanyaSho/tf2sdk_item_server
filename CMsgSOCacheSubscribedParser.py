# Protobuf messages
from gcsdk_pb2 import *

# Shared constants
from TFEnums import *

class CMsgSOCacheSubscribedParser:
	logfile = None

	def __init__( self, logfile: str = None ):
		if logfile is not None:
			self.logfile = open( logfile, "w" )

	def parse( self, data ):
		msg = CMsgSOCacheSubscribed()
		msg.ParseFromString( data )

		self.__log_and_print( f"owner: {msg.owner}" )

		#print( f"objects: {msg.objects}" )
		for i, obj in enumerate( msg.objects ):
			self.__log_and_print( f"\nObject {i + 1}" )
			self.__log_and_print( f"id: {obj.type_id}" )
			for j in obj.object_data:
				if obj.type_id == EEconTypeID.k_EEconTypeItemPresetInstance:
					data = CSOClassPresetClientData()
					data.ParseFromString( j )

					self.__parse_CSOClassPresetClientData( data )
				elif obj.type_id == EEconTypeID.k_EEconTypeItem:
					data = CSOEconItem()
					data.ParseFromString( j )

					self.__parse_CSOEconItem( data )
				elif obj.type_id == EEconTypeID.k_EEconTypeGameAccountClient:
					data = CSOEconGameAccountClient()
					data.ParseFromString( j )

					self.__parse_CSOEconGameAccountClient( data )
				elif obj.type_id == EEconTypeID.k_EEconTypeDuelSummary:
					data = CSOTFDuelSummary()
					data.ParseFromString( j )

					self.__parse_CSOTFDuelSummary( data )
				elif obj.type_id == EEconTypeID.k_EEconTypeMapContribution:
					data = CSOTFMapContribution()
					data.ParseFromString( j )

					self.__parse_CSOTFMapContribution( data )
				elif obj.type_id == EEconTypeID.k_EEConTypeLadderData:
					data = CSOTFLadderPlayerStats()
					data.ParseFromString( j )

					self.__parse_CSOTFLadderPlayerStats( data )
				elif obj.type_id == EGCTFProtoObjectTypes.k_EProtoObjectTFRatingData:
					data = CSOTFRatingData()
					data.ParseFromString( j )

					self.__parse_CSOTFRatingData( data )
				elif obj.type_id == EEconTypeID.k_EEconTypeQuestMapNode:
					data = CSOQuestMapNode()
					data.ParseFromString( j )

					self.__parse_CSOQuestMapNode( data )
				elif obj.type_id == EEconTypeID.k_EEConTypeQuest:
					data = CSOQuest()
					data.ParseFromString( j )

					self.__parse_CSOQuest( data )
				elif obj.type_id == EEconTypeID.k_EEconTypeQuestMapRewardPurchase:
					data = CSOQuestMapRewardPurchase()
					data.ParseFromString( j )

					self.__parse_CSOQuestMapRewardPurchase( data )
				elif obj.type_id == EEconTypeID.k_EEconTypePlayerInfo:
					data = CSOTFPlayerInfo()
					data.ParseFromString( j )

					self.__parse_CSOTFPlayerInfo( data )
				elif obj.type_id == EEconTypeID.k_EEConTypeMatchResultPlayerInfo:
					data = CSOTFMatchResultPlayerStats()
					data.ParseFromString( j )

					self.__parse_CSOTFMatchResultPlayerStats( data )
				else:
					self.__log_and_print( f"data: {j}" )

		self.__log_and_print( f"version: {msg.version}" )
		data = CMsgSOIDOwner()
		data.ParseFromString( msg.owner_soid.SerializeToString() )
		self.__parse_CMsgSOIDOwner( data )
		self.__log_and_print( f"service_id: {msg.service_id}" )
		self.__log_and_print( f"service_list: {msg.service_list}" )
		self.__log_and_print( f"sync_version: {msg.sync_version}" )


	#
	# Utility functions
	#
	def __log_and_print( self, msg ):
		if self.logfile is not None:
			self.logfile.write( msg )
			self.logfile.write( "\n" )

		print( msg )

	#
	# Private packet parsers
	#

	def __parse_CSOClassPresetClientData( self, data: CSOClassPresetClientData ):
		self.__log_and_print( "CLASS PRESET DATA (36):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" class_id: {data.class_id}" )
		self.__log_and_print( f" active_preset_id: {data.active_preset_id}" )

	# Helper for __parse_CSOEconItem
	def __parse_CSOEconItemAttribute( self, msgid: int, data: CSOEconItemAttribute ):
		self.__log_and_print( f" ITEM ATTRIBUTE {msgid}:" )
		self.__log_and_print( f"  def_index: {data.def_index}" )
		self.__log_and_print( f"  value: {data.value}" )
		self.__log_and_print( f"  value_bytes: {data.value_bytes}" )

	# Helper for __parse_CSOEconItem
	def __parse_CSOEconItemEquipped( self, msgid: int, data: CSOEconItemEquipped ):
		self.__log_and_print( f" ITEM EQUIPPED STATE {msgid}:" )
		self.__log_and_print( f"  new_class: {data.new_class}" )
		self.__log_and_print( f"  new_slot: {data.new_slot}" )

	def __parse_CSOEconItem( self, data: CSOEconItem ):
		self.__log_and_print( "ITEM (1):" )
		self.__log_and_print( f" id: {data.id}" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" inventory: {data.inventory}" )
		self.__log_and_print( f" def_index: {data.def_index}" )
		self.__log_and_print( f" quantity: {data.quantity}" )
		self.__log_and_print( f" level: {data.level}" )
		self.__log_and_print( f" quality: {data.quality}" )
		self.__log_and_print( f" flags: {data.flags}" )
		self.__log_and_print( f" origin: {data.origin}" )
		self.__log_and_print( f" custom_name: {data.custom_name}" )
		self.__log_and_print( f" custom_desc: {data.custom_desc}" )
		#self.__log_and_print( f" attribute: {data.attribute}" ) # CSOEconItemAttribute
		self.__log_and_print( f" attribute:" )
		for i, obj in enumerate( data.attribute ):
			self.__parse_CSOEconItemAttribute( i, obj )
		self.__log_and_print( f" interior_item: {data.interior_item}" ) # CSOEconItem
		self.__log_and_print( f" in_use: {data.in_use}" )
		self.__log_and_print( f" style: {data.style}" )
		self.__log_and_print( f" original_id: {data.original_id}" )
		self.__log_and_print( f" contains_equipped_state: {data.contains_equipped_state}" )
		#self.__log_and_print( f" equipped_state: {data.equipped_state}" ) # CSOEconItemEquipped
		self.__log_and_print( f" equipped_state:" )
		for i, obj in enumerate( data.equipped_state ):
			self.__parse_CSOEconItemEquipped( i, obj )
		self.__log_and_print( f" contains_equipped_state_v2: {data.contains_equipped_state_v2}" )

	def __parse_CSOEconGameAccountClient( self, data: CSOEconGameAccountClient ):
		self.__log_and_print( "GAME ACCOUNT DATA (CLIENT) (7):" )
		self.__log_and_print( f" additional_backpack_slots: {data.additional_backpack_slots}" )
		self.__log_and_print( f" trial_account: {data.trial_account}" )
		self.__log_and_print( f" need_to_choose_most_helpful_friend: {data.need_to_choose_most_helpful_friend}" )
		self.__log_and_print( f" in_coaches_list: {data.in_coaches_list}" )
		self.__log_and_print( f" trade_ban_expiration: {data.trade_ban_expiration}" )
		self.__log_and_print( f" duel_ban_expiration: {data.duel_ban_expiration}" )
		self.__log_and_print( f" preview_item_def: {data.preview_item_def}" )
		self.__log_and_print( f" phone_verified: {data.phone_verified}" )
		self.__log_and_print( f" skill_rating_6v6: {data.skill_rating_6v6}" )
		self.__log_and_print( f" skill_rating_9v9: {data.skill_rating_9v9}" )
		self.__log_and_print( f" competitive_access: {data.competitive_access}" )
		self.__log_and_print( f" matchmaking_ranked_ban_expiration: {data.matchmaking_ranked_ban_expiration}" )
		self.__log_and_print( f" matchmaking_ranked_low_priority_expiration: {data.matchmaking_ranked_low_priority_expiration}" )
		self.__log_and_print( f" matchmaking_ranked_ban_last_duration: {data.matchmaking_ranked_ban_last_duration}" )
		self.__log_and_print( f" matchmaking_ranked_low_priority_last_duration: {data.matchmaking_ranked_low_priority_last_duration}" )
		self.__log_and_print( f" matchmaking_casual_ban_expiration: {data.matchmaking_casual_ban_expiration}" )
		self.__log_and_print( f" matchmaking_casual_low_priority_expiration: {data.matchmaking_casual_low_priority_expiration}" )
		self.__log_and_print( f" matchmaking_casual_ban_last_duration: {data.matchmaking_casual_ban_last_duration}" )
		self.__log_and_print( f" matchmaking_casual_low_priority_last_duration: {data.matchmaking_casual_low_priority_last_duration}" )
		self.__log_and_print( f" phone_identifying: {data.phone_identifying}" )
		self.__log_and_print( f" disable_party_quest_progress: {data.disable_party_quest_progress}" )
		self.__log_and_print( f" quest_reward_credits: {data.quest_reward_credits}" )
		self.__log_and_print( f" matchmaking_last_casual_excessive_reports_auto_ban_time: {data.matchmaking_last_casual_excessive_reports_auto_ban_time}" )
		self.__log_and_print( f" matchmaking_last_comp_excessive_reports_auto_ban_time: {data.matchmaking_last_comp_excessive_reports_auto_ban_time}" )

	def __parse_CSOTFDuelSummary( self, data: CSOTFDuelSummary ):
		self.__log_and_print( "DUEL SUMMARY (19):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" duel_wins: {data.duel_wins}" )
		self.__log_and_print( f" duel_losses: {data.duel_losses}" )
		self.__log_and_print( f" last_duel_account_id: {data.last_duel_account_id}" )
		self.__log_and_print( f" last_duel_timestamp: {data.last_duel_timestamp}" )
		self.__log_and_print( f" last_duel_status: {data.last_duel_status}" )

	def __parse_CSOTFMapContribution( self, data: CSOTFMapContribution ):
		self.__log_and_print( "MAP CONTRIBUTION (28):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" def_index: {data.def_index}" )
		self.__log_and_print( f" contribution_level: {data.contribution_level}" )

	def __parse_CSOTFLadderPlayerStats( self, data: CSOTFLadderPlayerStats ):
		self.__log_and_print( "CSGO MM STATS (39):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" match_group: {data.match_group}" )
		self.__log_and_print( f" season_id: {data.season_id}" )
		self.__log_and_print( f" games: {data.games}" )
		self.__log_and_print( f" score: {data.score}" )
		self.__log_and_print( f" kills: {data.kills}" )
		self.__log_and_print( f" deaths: {data.deaths}" )
		self.__log_and_print( f" damage: {data.damage}" )
		self.__log_and_print( f" healing: {data.healing}" )
		self.__log_and_print( f" support: {data.support}" )
		self.__log_and_print( f" score_bronze: {data.score_bronze}" )
		self.__log_and_print( f" score_silver: {data.score_silver}" )
		self.__log_and_print( f" score_gold: {data.score_gold}" )
		self.__log_and_print( f" kills_bronze: {data.kills_bronze}" )
		self.__log_and_print( f" kills_silver: {data.kills_silver}" )
		self.__log_and_print( f" kills_gold: {data.kills_gold}" )
		self.__log_and_print( f" damage_bronze: {data.damage_bronze}" )
		self.__log_and_print( f" damage_silver: {data.damage_silver}" )
		self.__log_and_print( f" damage_gold: {data.damage_gold}" )
		self.__log_and_print( f" healing_bronze: {data.healing_bronze}" )
		self.__log_and_print( f" healing_silver: {data.healing_silver}" )
		self.__log_and_print( f" healing_gold: {data.healing_gold}" )
		self.__log_and_print( f" support_bronze: {data.support_bronze}" )
		self.__log_and_print( f" support_silver: {data.support_silver}" )
		self.__log_and_print( f" support_gold: {data.support_gold}" )

	def __parse_CSOTFRatingData( self, data: CSOTFRatingData ):
		self.__log_and_print( "RATING DATA (2007):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" rating_type: {data.rating_type}" )
		self.__log_and_print( f" rating_primary: {data.rating_primary}" )
		self.__log_and_print( f" rating_secondary: {data.rating_secondary}" )
		self.__log_and_print( f" rating_tertiary: {data.rating_tertiary}" )

	def __parse_CSOQuestMapNode( self, data: CSOQuestMapNode ):
		self.__log_and_print( "QUEST MAP NODE (44):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" defindex: {data.defindex}" )
		self.__log_and_print( f" node_id: {data.node_id}" )
		self.__log_and_print( f" star_0_earned: {data.star_0_earned}" )
		self.__log_and_print( f" star_1_earned: {data.star_1_earned}" )
		self.__log_and_print( f" star_2_earned: {data.star_2_earned}" )
		self.__log_and_print( f" loot_claimed: {data.loot_claimed}" )
		self.__log_and_print( f" selected_quest_def: {data.selected_quest_def}" )
		self.__log_and_print( f" map_cycle: {data.map_cycle}" )

	def __parse_CSOQuest( self, data: CSOQuest ):
		self.__log_and_print( "QUEST DATA (45):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" quest_id: {data.quest_id}" )
		self.__log_and_print( f" defindex: {data.defindex}" )
		self.__log_and_print( f" active: {data.active}" )
		self.__log_and_print( f" points_0: {data.points_0}" )
		self.__log_and_print( f" points_1: {data.points_1}" )
		self.__log_and_print( f" points_2: {data.points_2}" )
		self.__log_and_print( f" quest_map_node_source_id: {data.quest_map_node_source_id}" )
		self.__log_and_print( f" map_cycle: {data.map_cycle}" )

	def __parse_CSOQuestMapRewardPurchase( self, data: CSOQuestMapRewardPurchase ):
		self.__log_and_print( "QUEST MAP REWARD PURCHASE (46):" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" defindex: {data.defindex}" )
		self.__log_and_print( f" count: {data.count}" )
		self.__log_and_print( f" map_cycle: {data.map_cycle}" )
		self.__log_and_print( f" purchase_id: {data.purchase_id}" )

	def __parse_CSOTFPlayerInfo( self, data: CSOTFPlayerInfo ):
		self.__log_and_print( "PLAYER INFO (2):" )
		self.__log_and_print( f" num_new_users_helped: {data.num_new_users_helped}" )

	def __parse_CSOTFMatchResultPlayerStats( self, data: CSOTFMatchResultPlayerStats ):
		self.__log_and_print( "COMPETITIVE MATCH STATS (40):" )
		self.__log_and_print( f" match_id: {data.match_id}" )
		self.__log_and_print( f" account_id: {data.account_id}" )
		self.__log_and_print( f" match_group: {data.match_group}" )
		self.__log_and_print( f" endtime: {data.endtime}" )
		self.__log_and_print( f" season_id: {data.season_id}" )
		self.__log_and_print( f" status: {data.status}" )
		self.__log_and_print( f" original_party_id: {data.original_party_id}" )
		self.__log_and_print( f" team: {data.team}" )
		self.__log_and_print( f" score: {data.score}" )
		self.__log_and_print( f" ping: {data.ping}" )
		self.__log_and_print( f" flags: {data.flags}" )
		self.__log_and_print( f" display_rating: {data.display_rating}" )
		self.__log_and_print( f" display_rating_change: {data.display_rating_change}" )
		self.__log_and_print( f" rank: {data.rank}" )
		self.__log_and_print( f" classes_played: {data.classes_played}" )
		self.__log_and_print( f" kills: {data.kills}" )
		self.__log_and_print( f" deaths: {data.deaths}" )
		self.__log_and_print( f" damage: {data.damage}" )
		self.__log_and_print( f" healing: {data.healing}" )
		self.__log_and_print( f" support: {data.support}" )
		self.__log_and_print( f" score_medal: {data.score_medal}" )
		self.__log_and_print( f" kills_medal: {data.kills_medal}" )
		self.__log_and_print( f" damage_medal: {data.damage_medal}" )
		self.__log_and_print( f" healing_medal: {data.healing_medal}" )
		self.__log_and_print( f" support_medal: {data.support_medal}" )
		self.__log_and_print( f" map_index: {data.map_index}" )
		self.__log_and_print( f" winning_team: {data.winning_team}" )

	def __parse_CMsgSOIDOwner( self, data: CMsgSOIDOwner ):
		self.__log_and_print( "CMsgSOIDOwner:" )
		self.__log_and_print( f" type: {data.type}" )
		self.__log_and_print( f" id: {data.id}" )
