# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.api_helper import APIHelper
import greenbyteapi.models.user

class TaskComment(object):

    """Implementation of the 'TaskComment' model.

    A comment added to a task.

    Attributes:
        comment_id (int): The id of a task comment.
        text (string): TODO: type description here.
        timestamp_created (datetime): The timestamp when the comment was
            created (added to the task). The timestamp is in the time zone
            configured in the Greenbyte Platform without UTC offset.
        created_by (User): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "comment_id":'commentId',
        "text":'text',
        "timestamp_created":'timestampCreated',
        "created_by":'createdBy'
    }

    def __init__(self,
                 comment_id=None,
                 text=None,
                 timestamp_created=None,
                 created_by=None):
        """Constructor for the TaskComment class"""

        # Initialize members of the class
        self.comment_id = comment_id
        self.text = text
        self.timestamp_created = APIHelper.RFC3339DateTime(timestamp_created) if timestamp_created else None
        self.created_by = created_by


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
        comment_id = dictionary.get('commentId')
        text = dictionary.get('text')
        timestamp_created = APIHelper.RFC3339DateTime.from_value(dictionary.get("timestampCreated")).datetime if dictionary.get("timestampCreated") else None
        created_by = greenbyteapi.models.user.User.from_dictionary(dictionary.get('createdBy')) if dictionary.get('createdBy') else None

        # Return an object of this model
        return cls(comment_id,
                   text,
                   timestamp_created,
                   created_by)


