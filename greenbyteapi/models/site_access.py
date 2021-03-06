# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.api_helper import APIHelper
import greenbyteapi.models.site_access_personnel

class SiteAccess(object):

    """Implementation of the 'SiteAccess' model.

    A site access.

    Attributes:
        site_access_id (int): The id of a site access.
        site_id (int): The id of a site.
        device_ids (list of int): Device ids associated with the site access.
        task_ids (list of int): Task ids associated with the site access.
        site_access_personnel (list of SiteAccessPersonnel): Personnel
            associated with the site access.
        timestamp_start (datetime): The timestamp when the site access is/was
            planned to start. The timestamp is in the time zone configured in
            the Greenbyte Platform without UTC offset.
        timestamp_end_expected (datetime): The timestamp when the site access
            is/was planned to end. The timestamp is in the time zone
            configured in the Greenbyte Platform without UTC offset.
        timestamp_end (datetime): The timestamp when the site access actually
            ended. The timestamp is in the time zone configured in the
            Greenbyte Platform without UTC offset.
        log_on_comment (string): A comment for when logging on to the site.
        log_off_comment (string): A comment for when logging off from the
            site.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "site_access_id":'siteAccessId',
        "site_id":'siteId',
        "device_ids":'deviceIds',
        "task_ids":'taskIds',
        "site_access_personnel":'siteAccessPersonnel',
        "timestamp_start":'timestampStart',
        "timestamp_end_expected":'timestampEndExpected',
        "timestamp_end":'timestampEnd',
        "log_on_comment":'logOnComment',
        "log_off_comment":'logOffComment'
    }

    def __init__(self,
                 site_access_id=None,
                 site_id=None,
                 device_ids=None,
                 task_ids=None,
                 site_access_personnel=None,
                 timestamp_start=None,
                 timestamp_end_expected=None,
                 timestamp_end=None,
                 log_on_comment=None,
                 log_off_comment=None):
        """Constructor for the SiteAccess class"""

        # Initialize members of the class
        self.site_access_id = site_access_id
        self.site_id = site_id
        self.device_ids = device_ids
        self.task_ids = task_ids
        self.site_access_personnel = site_access_personnel
        self.timestamp_start = APIHelper.RFC3339DateTime(timestamp_start) if timestamp_start else None
        self.timestamp_end_expected = APIHelper.RFC3339DateTime(timestamp_end_expected) if timestamp_end_expected else None
        self.timestamp_end = APIHelper.RFC3339DateTime(timestamp_end) if timestamp_end else None
        self.log_on_comment = log_on_comment
        self.log_off_comment = log_off_comment


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
        site_access_id = dictionary.get('siteAccessId')
        site_id = dictionary.get('siteId')
        device_ids = dictionary.get('deviceIds')
        task_ids = dictionary.get('taskIds')
        site_access_personnel = None
        if dictionary.get('siteAccessPersonnel') != None:
            site_access_personnel = list()
            for structure in dictionary.get('siteAccessPersonnel'):
                site_access_personnel.append(greenbyteapi.models.site_access_personnel.SiteAccessPersonnel.from_dictionary(structure))
        timestamp_start = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampStart")).datetime if dictionary.get("timestampStart") else None
        timestamp_end_expected = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampEndExpected")).datetime if dictionary.get("timestampEndExpected") else None
        timestamp_end = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampEnd")).datetime if dictionary.get("timestampEnd") else None
        log_on_comment = dictionary.get('logOnComment')
        log_off_comment = dictionary.get('logOffComment')

        # Return an object of this model
        return cls(site_access_id,
                   site_id,
                   device_ids,
                   task_ids,
                   site_access_personnel,
                   timestamp_start,
                   timestamp_end_expected,
                   timestamp_end,
                   log_on_comment,
                   log_off_comment)


