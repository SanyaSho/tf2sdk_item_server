import struct

# Protobuf messages
from gcsdk_pb2 import *

class EconAttributeHelper:
	"""
	Helper class for easier work with item attributes
	"""

	attributes = None

	def __init__( self, attributes ):
		self.attributes = attributes

		if not self.attributes:
			print( "Warning! EconAttributeHelper was initialized without items_game.txt support! Attribute by name accessor will be unavailable." )


	# Utility functions
	def __check_if_attribute_is_valid_and_get_index( self, name: str ):
		if not self.attributes:
			return -1

		for i in self.attributes:
			if "name" in self.attributes[i] and self.attributes[i]["name"] == name or "attribute_class" in self.attributes[i] and self.attributes[i]["attribute_class"] == name:
				return int( i )

		print( f"Attribute '{name}' is not valid!" )
		return -1

	def get_attribute_name_by_index( self, attrib_index: int ):
		"""
		Get attribute name from index
		:param attrib_index: Attribute index from items_game.txt
		:type attrib_index: int
		:return: Attribute name
		:rtype: str
		"""

		_attrib_index = str( attrib_index )

		if _attrib_index in self.attributes:
			return self.attributes[_attrib_index]["name"]

		return None


	# Integer attribute
	def allocate_item_attribute_int_name( self, name: str, value: int ):
		"""
		:param name: Attribute name or class from items_game.txt
		:type name: int
		:param value: Attribute value
		:type value: int
		:return: CSOEconItemAttribute
		:rtype: CSOEconItemAttribute
		"""

		index = self.__check_if_attribute_is_valid_and_get_index( name )
		if index == -1:
			return None

		return self.allocate_item_attribute_int( index, value )

	def allocate_item_attribute_int( self, attrib_index: int, value: int ):
		"""
		:param attrib_index: Attribute index from items_game.txt
		:type attrib_index: int
		:param value: Attribute value
		:type value: int
		:return: CSOEconItemAttribute
		:rtype: CSOEconItemAttribute
		"""

		attrib = CSOEconItemAttribute()
		attrib.def_index = attrib_index

		attrib.value_bytes = struct.pack( "<i", value )

		return attrib


	# Float attribute
	def allocate_item_attribute_float_name( self, name: str, value: float ):
		"""
		:param name: Attribute name or class from items_game.txt
		:type name: float
		:param value: Attribute value
		:type value: float
		:return: CSOEconItemAttribute
		:rtype: CSOEconItemAttribute
		"""

		index = self.__check_if_attribute_is_valid_and_get_index( name )
		if index == -1:
			return None

		return self.allocate_item_attribute_float( index, value )

	def allocate_item_attribute_float( self, attrib_index: int, value: float ):
		"""
		:param attrib_index: Attribute index from items_game.txt
		:type attrib_index: int
		:param value: Attribute value
		:type value: float
		:return: CSOEconItemAttribute
		:rtype: CSOEconItemAttribute
		"""

		attrib = CSOEconItemAttribute()
		attrib.def_index = attrib_index

		attrib.value_bytes = struct.pack( "<f", value )

		return attrib


	# String attribute
	def allocate_item_attribute_string_name( self, name: str, value: str ):
		"""
		:param name: Attribute name or class from items_game.txt
		:type name: str
		:param value: Attribute value
		:type value: str
		:return: CSOEconItemAttribute
		:rtype: CSOEconItemAttribute
		"""

		index = self.__check_if_attribute_is_valid_and_get_index( name )
		if index == -1:
			return None

		return self.allocate_item_attribute_string( index, value )

	def allocate_item_attribute_string( self, attrib_index: int, value: str ):
		"""
		:param attrib_index: Attribute index from items_game.txt
		:type attrib_index: int
		:param value: Attribute value
		:type value: str
		:return: CSOEconItemAttribute
		:rtype: CSOEconItemAttribute
		"""

		attrib = CSOEconItemAttribute()
		attrib.def_index = attrib_index

		data = CAttribute_String()
		data.value = value
		attrib.value_bytes = data.SerializeToString()

		return attrib
