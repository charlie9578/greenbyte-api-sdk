# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Organization(object):

    """Implementation of the 'Organization' model.

    An organization used for tasks and personnel.

    Attributes:
        organization_id (int): An id of an organization used for tasks and
            personnel.
        name (string): TODO: type description here.
        email (string): TODO: type description here.
        phone (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "organization_id":'organizationId',
        "name":'name',
        "email":'email',
        "phone":'phone'
    }

    def __init__(self,
                 organization_id=None,
                 name=None,
                 email=None,
                 phone=None):
        """Constructor for the Organization class"""

        # Initialize members of the class
        self.organization_id = organization_id
        self.name = name
        self.email = email
        self.phone = phone


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
        organization_id = dictionary.get('organizationId')
        name = dictionary.get('name')
        email = dictionary.get('email')
        phone = dictionary.get('phone')

        # Return an object of this model
        return cls(organization_id,
                   name,
                   email,
                   phone)


