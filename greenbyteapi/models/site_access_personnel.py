# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.api_helper import APIHelper

class SiteAccessPersonnel(object):

    """Implementation of the 'SiteAccessPersonnel' model.

    Site access personnel.

    Attributes:
        personnel_id (int): The id of a person in the personnel list.
        first_name (string): TODO: type description here.
        last_name (string): TODO: type description here.
        company (string): TODO: type description here.
        phone_number (string): TODO: type description here.
        vehicle_registration (string): TODO: type description here.
        comment (string): TODO: type description here.
        timestamp_start (datetime): TODO: type description here.
        timestamp_end (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "personnel_id":'personnelId',
        "first_name":'firstName',
        "last_name":'lastName',
        "company":'company',
        "phone_number":'phoneNumber',
        "vehicle_registration":'vehicleRegistration',
        "comment":'comment',
        "timestamp_start":'timestampStart',
        "timestamp_end":'timestampEnd'
    }

    def __init__(self,
                 personnel_id=None,
                 first_name=None,
                 last_name=None,
                 company=None,
                 phone_number=None,
                 vehicle_registration=None,
                 comment=None,
                 timestamp_start=None,
                 timestamp_end=None):
        """Constructor for the SiteAccessPersonnel class"""

        # Initialize members of the class
        self.personnel_id = personnel_id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.phone_number = phone_number
        self.vehicle_registration = vehicle_registration
        self.comment = comment
        self.timestamp_start = APIHelper.RFC3339DateTime(timestamp_start) if timestamp_start else None
        self.timestamp_end = APIHelper.RFC3339DateTime(timestamp_end) if timestamp_end else None


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
        personnel_id = dictionary.get('personnelId')
        first_name = dictionary.get('firstName')
        last_name = dictionary.get('lastName')
        company = dictionary.get('company')
        phone_number = dictionary.get('phoneNumber')
        vehicle_registration = dictionary.get('vehicleRegistration')
        comment = dictionary.get('comment')
        timestamp_start = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampStart")).datetime if dictionary.get("timestampStart") else None
        timestamp_end = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampEnd")).datetime if dictionary.get("timestampEnd") else None

        # Return an object of this model
        return cls(personnel_id,
                   first_name,
                   last_name,
                   company,
                   phone_number,
                   vehicle_registration,
                   comment,
                   timestamp_start,
                   timestamp_end)


