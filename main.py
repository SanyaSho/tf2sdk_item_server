from fastapi import FastAPI

from AuthTicketValidator import AuthTicketValidator
from CMsgSOCacheSubscribedSerializer import CMsgSOCacheSubscribedSerializer
from CMsgSOCacheSubscribedSerializerTest import CMsgSOCacheSubscribedSerializerTest
from ItemSchemaParser import ItemSchemaParser
from PlayerConstants import PlayerInfo

# Shared constants
from TFEnums import *

# Initialize AuthTicketValidator
atv = AuthTicketValidator()

# Initialize FastAPI
app = FastAPI()

# Initialize PlayerInfo (try to parse player_info.txt)
pi = PlayerInfo()

# Parse items_game.txt
isp = ItemSchemaParser()

gcmsgtest = CMsgSOCacheSubscribedSerializerTest( CMsgSOCacheSubscribedSerializer( isp, pi.PLAYER_STEAMID, pi.PLAYER_ACCNTID ) )
gcmsgtest.serialize_test_message()
token = gcmsgtest.serializer.get_message_as_base64()


## CLIENT-SIDE
@app.get( "/webapi/ISDK/GetInventory/v0001" )
def read_item( appid: int | None = None, ticket: str | None = None ):
	"""
	Purpose: Returns client-side gc message with player inventory, rank, quests, etc.

	:param appid: Game AppID
	:param ticket: Auth ticket (unique for each game start).
	:return: CLIENT-SIDE Player info
	"""

	if not appid:
		return { "result": EResult.k_EResultInvalidParam, "error": "no appid specified" }
	if not ticket:
		return { "result": EResult.k_EResultInvalidParam, "error": "no ticket specified" }

	(valid, ( steamid, account_id ), errcode) = atv.ValidatePlayerAuthTicket( ticket, pi )
	if not valid:
		return errcode

	return {
		"result": EResult.k_EResultOK,
		"steamid": str( steamid ), # tf_gc_client.cpp wants steamid to be string
		"version": 0, 
		"msg": token
	}

## SERVER-SIDE
@app.get( "/webapi/ISDK/GetEquipment/v0001" )
def read_item( appid: int | None = None, msg: str | None = None, ticket: str | None = None ):
	"""
	Purpose: Returns server-side gc message with player inventory only.
	"version" param is set.

	:param appid: Game AppID
	:param msg: CMsgAuthorizeServerItemRetrieval with all items retrieved from GetInventory stored as CUtlMemory<char>
	:param ticket: Auth ticket (unique for each game start). Taken from GetInventory.
	:return: SERVER-SIDE Player Info
	"""

	if not msg:
		return { "result": EResult.k_EResultInvalidParam, "error": "no msg specified" }
	if not appid:
		return { "result": EResult.k_EResultInvalidParam, "error": "no appid specified" }
	if not ticket:
		return { "result": EResult.k_EResultInvalidParam, "error": "no ticket specified" }

	(valid, ( steamid, account_id ), errcode) = atv.ValidatePlayerAuthTicket( ticket, pi )
	if not valid:
		return errcode

	return {
		"result": EResult.k_EResultOK,
		"steamid": str( steamid ), # same for tf_gc_server.cpp
		"version": 0,
		"msg": token
	}
