# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import greenbyteapi.models.organization
import greenbyteapi.models.personnel_qualification
import greenbyteapi.models.personnel_site_induction

class Personnel(object):

    """Implementation of the 'Personnel' model.

    A person in the personnel list.

    Attributes:
        personnel_id (int): The id of a person in the personnel list.
        first_name (string): TODO: type description here.
        last_name (string): TODO: type description here.
        email (string): TODO: type description here.
        phone (string): TODO: type description here.
        mobile (string): TODO: type description here.
        organization (Organization): An organization used for tasks and
            personnel.
        qualifications (list of PersonnelQualification): TODO: type
            description here.
        site_inductions (list of PersonnelSiteInduction): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "personnel_id":'personnelId',
        "first_name":'firstName',
        "last_name":'lastName',
        "email":'email',
        "phone":'phone',
        "mobile":'mobile',
        "organization":'organization',
        "qualifications":'qualifications',
        "site_inductions":'siteInductions'
    }

    def __init__(self,
                 personnel_id=None,
                 first_name=None,
                 last_name=None,
                 email=None,
                 phone=None,
                 mobile=None,
                 organization=None,
                 qualifications=None,
                 site_inductions=None):
        """Constructor for the Personnel class"""

        # Initialize members of the class
        self.personnel_id = personnel_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.mobile = mobile
        self.organization = organization
        self.qualifications = qualifications
        self.site_inductions = site_inductions


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
        email = dictionary.get('email')
        phone = dictionary.get('phone')
        mobile = dictionary.get('mobile')
        organization = greenbyteapi.models.organization.Organization.from_dictionary(dictionary.get('organization')) if dictionary.get('organization') else None
        qualifications = None
        if dictionary.get('qualifications') != None:
            qualifications = list()
            for structure in dictionary.get('qualifications'):
                qualifications.append(greenbyteapi.models.personnel_qualification.PersonnelQualification.from_dictionary(structure))
        site_inductions = None
        if dictionary.get('siteInductions') != None:
            site_inductions = list()
            for structure in dictionary.get('siteInductions'):
                site_inductions.append(greenbyteapi.models.personnel_site_induction.PersonnelSiteInduction.from_dictionary(structure))

        # Return an object of this model
        return cls(personnel_id,
                   first_name,
                   last_name,
                   email,
                   phone,
                   mobile,
                   organization,
                   qualifications,
                   site_inductions)


