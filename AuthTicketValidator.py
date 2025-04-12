from PlayerConstants import PlayerInfo

class AuthTicketValidator:
	#valid_tickets = {}

	def __init__( self ):
		print( "AuthTicketValidator" )

	def ValidatePlayerAuthTicket( self, ticket, temppi: PlayerInfo ):
		# TODO: Must call https://partner.steamgames.com/doc/webapi/ISteamUserAuth#AuthenticateUserTicket to get user's SteamID

		return True, ( temppi.PLAYER_STEAMID, temppi.PLAYER_ACCNTID ), {}

		#if ticket in valid_tickets:
		#	return True, valid_tickets[ticket], {}

		#return False, "0", { "result": EResult.k_EResultNotLoggedOn, "error": "steamauth failed", "steam_errorcode": EResult.k_EResultNoConnection, "steam_errordesc": "Invalid parameter", "identity": "tf2sdk" }
