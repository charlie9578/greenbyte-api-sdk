# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.api_helper import APIHelper
import greenbyteapi.models.site
import greenbyteapi.models.device_model
import greenbyteapi.models.turbine_type
import greenbyteapi.models.metadata_field

class Device(object):

    """Implementation of the 'Device' model.

    TODO: type model description here.

    Attributes:
        device_id (int): The id of a device.
        title (string): TODO: type description here.
        alt_title (string): An alternative title.
        identity (string): Device identification number.
        site (Site): The site where the device is located.
        device_type (string): The string representation of the device type.
        device_type_id (int): The id of a device type.
        parent_id (int): The id of the parent device, if any.
        child_ids (list of int): Ids of child devices, if any.
        device_model (DeviceModel): Information about the device manufacturer
            and model. Applies to devices of device type **other than**
            `Turbine`.
        turbine_type (TurbineType): Turbine type information (manufacturer and
            model). Only applies to devices of device type `Turbine`.
        max_power (int): The maximum power for a device.
        bidding_area (string): Only applies to Nordic countries and the UK.
        timestamp_start (datetime): The earliest timestamp device data is
            available for.
        latitude (string): The latitude of the device in the WGS84 system.
        longitude (string): The longitude of the device in the WGS84 system.
        elevation (string): The elevation of the device in meters above sea
            level.
        target_availability (float): The target availability for the device.
        metadata (list of MetadataField): A list of metadata fields and their
            values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id":'deviceId',
        "title":'title',
        "alt_title":'altTitle',
        "identity":'identity',
        "site":'site',
        "device_type":'deviceType',
        "device_type_id":'deviceTypeId',
        "parent_id":'parentId',
        "child_ids":'childIds',
        "device_model":'deviceModel',
        "turbine_type":'turbineType',
        "max_power":'maxPower',
        "bidding_area":'biddingArea',
        "timestamp_start":'timestampStart',
        "latitude":'latitude',
        "longitude":'longitude',
        "elevation":'elevation',
        "target_availability":'targetAvailability',
        "metadata":'metadata'
    }

    def __init__(self,
                 device_id=None,
                 title=None,
                 alt_title=None,
                 identity=None,
                 site=None,
                 device_type=None,
                 device_type_id=None,
                 parent_id=None,
                 child_ids=None,
                 device_model=None,
                 turbine_type=None,
                 max_power=None,
                 bidding_area=None,
                 timestamp_start=None,
                 latitude=None,
                 longitude=None,
                 elevation=None,
                 target_availability=None,
                 metadata=None):
        """Constructor for the Device class"""

        # Initialize members of the class
        self.device_id = device_id
        self.title = title
        self.alt_title = alt_title
        self.identity = identity
        self.site = site
        self.device_type = device_type
        self.device_type_id = device_type_id
        self.parent_id = parent_id
        self.child_ids = child_ids
        self.device_model = device_model
        self.turbine_type = turbine_type
        self.max_power = max_power
        self.bidding_area = bidding_area
        self.timestamp_start = APIHelper.RFC3339DateTime(timestamp_start) if timestamp_start else None
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.target_availability = target_availability
        self.metadata = metadata


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        device_id = dictionary.get('deviceId')
        title = dictionary.get('title')
        alt_title = dictionary.get('altTitle')
        identity = dictionary.get('identity')
        site = greenbyteapi.models.site.Site.from_dictionary(dictionary.get('site')) if dictionary.get('site') else None
        device_type = dictionary.get('deviceType')
        device_type_id = dictionary.get('deviceTypeId')
        parent_id = dictionary.get('parentId')
        child_ids = dictionary.get('childIds')
        device_model = greenbyteapi.models.device_model.DeviceModel.from_dictionary(dictionary.get('deviceModel')) if dictionary.get('deviceModel') else None
        turbine_type = greenbyteapi.models.turbine_type.TurbineType.from_dictionary(dictionary.get('turbineType')) if dictionary.get('turbineType') else None
        max_power = dictionary.get('maxPower')
        bidding_area = dictionary.get('biddingArea')
        timestamp_start = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampStart")).datetime if dictionary.get("timestampStart") else None
        latitude = dictionary.get('latitude')
        longitude = dictionary.get('longitude')
        elevation = dictionary.get('elevation')
        target_availability = dictionary.get('targetAvailability')
        metadata = None
        if dictionary.get('metadata') != None:
            metadata = list()
            for structure in dictionary.get('metadata'):
                metadata.append(greenbyteapi.models.metadata_field.MetadataField.from_dictionary(structure))

        # Return an object of this model
        return cls(device_id,
                   title,
                   alt_title,
                   identity,
                   site,
                   device_type,
                   device_type_id,
                   parent_id,
                   child_ids,
                   device_model,
                   turbine_type,
                   max_power,
                   bidding_area,
                   timestamp_start,
                   latitude,
                   longitude,
                   elevation,
                   target_availability,
                   metadata)


