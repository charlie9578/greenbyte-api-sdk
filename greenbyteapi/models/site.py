# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Site(object):

    """Implementation of the 'Site' model.

    TODO: type model description here.

    Attributes:
        site_id (int): The id of a site.
        title (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "site_id":'siteId',
        "title":'title'
    }

    def __init__(self,
                 site_id=None,
                 title=None):
        """Constructor for the Site class"""

        # Initialize members of the class
        self.site_id = site_id
        self.title = title


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
        site_id = dictionary.get('siteId')
        title = dictionary.get('title')

        # Return an object of this model
        return cls(site_id,
                   title)


