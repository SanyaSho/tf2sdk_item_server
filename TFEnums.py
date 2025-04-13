class EResult:
	"""
	Copied from steamclientpublic.h
	"""

	k_EResultOK							= 1
	k_EResultFail							= 2
	k_EResultNoConnection						= 3
	k_EResultInvalidParam						= 8
	k_EResultNotLoggedOn						= 21


class EMMRating:
	"""
	Copied from tf_matchmaking_shared.h
	"""

	k_nMMRating_Invalid						= -1

	k_nMMRating_6v6_DRILLO						= 0
	k_nMMRating_6v6_DRILLO_PlayerAcknowledged			= 1
	k_nMMRating_6v6_GLICKO						= 2
	k_nMMRating_12v12_DRILLO					= 3
	k_nMMRating_Casual_12v12_GLICKO					= 4
	k_nMMRating_Casual_XP						= 5
	k_nMMRating_Casual_XP_PlayerAcknowledged			= 6
	k_nMMRating_6v6_Rank						= 7
	k_nMMRating_6v6_Rank_PlayerAcknowledged				= 8
	k_nMMRating_Casual_12v12_Rank					= 9
	k_nMMRating_Casual_12v12_Rank_PlayerAcknowledged		= 10
	k_nMMRating_6v6_GLICKO_PlayerAcknowledged			= 11
	k_nMMRating_Comp_12v12_Rank					= 12
	k_nMMRating_Comp_12v12_Rank_PlayerAcknowledged			= 13
	k_nMMRating_Comp_12v12_GLICKO					= 14
	k_nMMRating_Comp_12v12_GLICKO_PlayerAcknowledged		= 15


class EEconItemQuality:
	"""
	Copied from econ_item_constants.h
	"""

	AE_UNDEFINED							= -1		# Invalid

	AE_NORMAL							= 0		# Normal
	AE_RARITY1							= 1		# Genuine
	AE_RARITY2							= 2		# Customized
	AE_VINTAGE							= 3		# Vintage
	AE_RARITY3							= 4		# Artisan
	AE_UNUSUAL							= 5		# Unusual
	AE_UNIQUE							= 6		# Unique
	AE_COMMUNITY							= 7		# Community
	AE_DEVELOPER							= 8		# Valve
	AE_SELFMADE							= 9		# Self-Made
	AE_CUSTOMIZED							= 10		# Customized
	AE_STRANGE							= 11		# Strange
	AE_COMPLETED							= 12		# Completed
	AE_HAUNTED							= 13		# Haunted
	AE_COLLECTORS							= 14		# Collector's
	AE_PAINTKITWEAPON						= 15		# Decorated Weapon

	AE_RARITY_DEFAULT						= 16		# Stock
	AE_RARITY_COMMON						= 17		# Civilian
	AE_RARITY_UNCOMMON						= 18		# Freelance
	AE_RARITY_RARE							= 19		# Mercenary
	AE_RARITY_MYTHICAL						= 20		# Commando
	AE_RARITY_LEGENDARY						= 21		# Assassin
	AE_RARITY_ANCIENT						= 22		# Elite

	AE_MAX_TYPES							= AE_RARITY_ANCIENT + 1
	AE_DEPRECATED_UNIQUE						= 3


class ETFClass:
	"""
	Copied from tf_shareddefs.h
	"""

	TF_CLASS_SCOUT							= 1
	TF_CLASS_SNIPER							= 2
	TF_CLASS_SOLDIER						= 3
	TF_CLASS_DEMOMAN						= 4
	TF_CLASS_MEDIC							= 5
	TF_CLASS_HEAVYWEAPONS						= 6
	TF_CLASS_PYRO							= 7
	TF_CLASS_SPY							= 8
	TF_CLASS_ENGINEER						= 9
	TF_CLASS_CIVILIAN						= 10


class ETFLoadoutPreset:
	TF_LOADOUT_PRESET_A						= 0
	TF_LOADOUT_PRESET_B						= 1
	TF_LOADOUT_PRESET_C						= 2
	TF_LOADOUT_PRESET_D						= 3

	MIN_PRESETS							= TF_LOADOUT_PRESET_A
	MAX_PRESETS							= TF_LOADOUT_PRESET_D + 1


class loadout_positions_t:
	"""
	Copied from tf_item_constants.h
	"""

	LOADOUT_POSITION_INVALID					= -1

	# Weapons & Equipment
	LOADOUT_POSITION_PRIMARY					= 0
	LOADOUT_POSITION_SECONDARY					= 1
	LOADOUT_POSITION_MELEE						= 2
	LOADOUT_POSITION_UTILITY					= 3
	LOADOUT_POSITION_BUILDING					= 4
	LOADOUT_POSITION_PDA						= 5
	LOADOUT_POSITION_PDA2						= 6

	# Wearables. If you add new wearable slots, make sure you add them to IsWearableSlot() below this.
	LOADOUT_POSITION_HEAD						= 7
	LOADOUT_POSITION_MISC						= 8

	# other
	LOADOUT_POSITION_ACTION						= 9

	# More wearables, yay!
	LOADOUT_POSITION_MISC2						= 10

	# taunts
	LOADOUT_POSITION_TAUNT						= 11
	LOADOUT_POSITION_TAUNT2						= 12
	LOADOUT_POSITION_TAUNT3						= 13
	LOADOUT_POSITION_TAUNT4						= 14
	LOADOUT_POSITION_TAUNT5						= 15
	LOADOUT_POSITION_TAUNT6						= 16
	LOADOUT_POSITION_TAUNT7						= 17
	LOADOUT_POSITION_TAUNT8						= 18


class EEconConstants:
	"""
	Copied from econ_item_constants.h
	"""

	# Standard/default backpack size
	DEFAULT_NUM_BACKPACK_SLOTS					= 300
	DEFAULT_NUM_BACKPACK_SLOTS_FREE_TRIAL_ACCOUNT			= 50
	MAX_NUM_BACKPACK_SLOTS						= 4000
	MAX_NUM_FULL_BACKPACK_SLOTS					= MAX_NUM_BACKPACK_SLOTS - DEFAULT_NUM_BACKPACK_SLOTS

	# Current item level range
	MIN_ITEM_LEVEL							= 0
	MAX_ITEM_LEVEL							= 100

	# Maximum number of attributes allowed on a single item
	MAX_ATTRIBUTES_PER_ITEM						= 20


class EEconTypeID:
	"""
	Copied from econ_item_constants.h
	"""

	k_EEconTypeItemPresetInstance					= 36
	k_EEconTypeItem							= 1
	k_EEconTypeGameAccountClient					= 7
	k_EEconTypeDuelSummary						= 19
	k_EEconTypeMapContribution					= 28
	k_EEConTypeLadderData						= 39
	k_EEconTypeQuestMapNode						= 44
	k_EEConTypeQuest						= 45
	k_EEconTypeQuestMapRewardPurchase				= 46
	k_EEconTypePlayerInfo						= 2
	k_EEConTypeMatchResultPlayerInfo				= 40


class EGCTFProtoObjectTypes:
	"""
	Copied from tf_gcmessages.h
	"""

	k_EProtoObjectTypesGameBase					= 2000
	k_EProtoObjectTFRatingData					= k_EProtoObjectTypesGameBase + 7


class EEconItemFlags:
	"""
	Copied from econ_item_constants.h
	"""

	kEconItemFlag_CannotTrade					= 1 << 0
	kEconItemFlag_CannotBeUsedInCrafting				= 1 << 1
	kEconItemFlag_CanBeTradedByFreeAccounts				= 1 << 2
	kEconItemFlag_NonEconomy					= 1 << 3	# used for items that are meant to not interact in the economy -- these can't be traded, gift-wrapped, crafted, etc.
	kEconItemFlag_PurchasedAfterStoreCraftabilityChanges2012	= 1 << 4	# cosmetic items coming from the store are now usable in crafting; this flag is set on all items purchased from the store after this change was made

#ifdef CLIENT_DLL
#ifdef TF_CLIENT_DLL
	kEconItemFlagClient_ForceBlueTeam				= 1 << 5
#endif // TF_CLIENT_DLL
	kEconItemFlagClient_StoreItem					= 1 << 6
	kEconItemFlagClient_Preview					= 1 << 7	# only set on the client; means "this item is being previewed"
#endif // CLIENT_DLL


class EEconItemOrigin:
	"""
	Copied from econ_item_constants.h
	"""

	kEconItemOrigin_Invalid						= -1		# should never be stored in the DB! used to indicate "invalid" for in-memory objects only

	kEconItemOrigin_Drop						= 0
	kEconItemOrigin_Achievement					= 1
	kEconItemOrigin_Purchased					= 2
	kEconItemOrigin_Traded						= 3
	kEconItemOrigin_Crafted						= 4
	kEconItemOrigin_StorePromotion					= 5
	kEconItemOrigin_Gifted						= 6
	kEconItemOrigin_SupportGranted					= 7
	kEconItemOrigin_FoundInCrate					= 8
	kEconItemOrigin_Earned						= 9
	kEconItemOrigin_ThirdPartyPromotion				= 10
	kEconItemOrigin_GiftWrapped					= 11
	kEconItemOrigin_HalloweenDrop					= 12
	kEconItemOrigin_PackageItem					= 13
	kEconItemOrigin_Foreign						= 14
	kEconItemOrigin_CDKey						= 15
	kEconItemOrigin_CollectionReward				= 16
	kEconItemOrigin_PreviewItem					= 17
	kEconItemOrigin_SteamWorkshopContribution			= 18
	kEconItemOrigin_PeriodicScoreReward				= 19
	kEconItemOrigin_MvMMissionCompletionReward			= 20		# includes loot from both "mission completed" and "tour completed" events
	kEconItemOrigin_MvMSquadSurplusReward				= 21
	kEconItemOrigin_RecipeOutput					= 22
	kEconItemOrigin_QuestDrop					= 23
	kEconItemOrigin_QuestLoanerItem					= 24
	kEconItemOrigin_TradeUp						= 25
	kEconItemOrigin_ViralCompetitiveBetaPassSpread			= 26
	kEconItemOrigin_CYOABloodMoneyPurchase				= 27
	kEconItemOrigin_Paintkit					= 28
	kEconItemOrigin_UntradableFreeContractReward			= 29
