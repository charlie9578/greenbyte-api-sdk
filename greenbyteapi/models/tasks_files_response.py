# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.api_helper import APIHelper
import greenbyteapi.models.user

class TasksFilesResponse(object):

    """Implementation of the 'Tasks Files Response' model.

    TODO: type model description here.

    Attributes:
        file_id (int): The id of a file.
        file_name (string): TODO: type description here.
        timestamp_uploaded (datetime): The timestamp when the file was
            uploaded.
        uploaded_by (User): TODO: type description here.
        description (string): TODO: type description here.
        category (CategoryEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "file_id":'fileId',
        "file_name":'fileName',
        "timestamp_uploaded":'timestampUploaded',
        "uploaded_by":'uploadedBy',
        "description":'description',
        "category":'category'
    }

    def __init__(self,
                 file_id=None,
                 file_name=None,
                 timestamp_uploaded=None,
                 uploaded_by=None,
                 description=None,
                 category=None):
        """Constructor for the TasksFilesResponse class"""

        # Initialize members of the class
        self.file_id = file_id
        self.file_name = file_name
        self.timestamp_uploaded = APIHelper.RFC3339DateTime(timestamp_uploaded) if timestamp_uploaded else None
        self.uploaded_by = uploaded_by
        self.description = description
        self.category = category


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
        file_id = dictionary.get('fileId')
        file_name = dictionary.get('fileName')
        timestamp_uploaded = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampUploaded")).datetime if dictionary.get("timestampUploaded") else None
        uploaded_by = greenbyteapi.models.user.User.from_dictionary(dictionary.get('uploadedBy')) if dictionary.get('uploadedBy') else None
        description = dictionary.get('description')
        category = dictionary.get('category')

        # Return an object of this model
        return cls(file_id,
                   file_name,
                   timestamp_uploaded,
                   uploaded_by,
                   description,
                   category)


