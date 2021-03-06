# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import greenbyteapi.models.client_configuration
import greenbyteapi.models.time_zone_configuration
import greenbyteapi.models.data_signal_configuration

class ConfigurationItem(object):

    """Implementation of the 'ConfigurationItem' model.

    Your configuration data.

    Attributes:
        client (ClientConfiguration): General configuration data.
        time_zone (TimeZoneConfiguration): The time zone configuration.
        data_signals (DataSignalConfiguration): Your data signal
            configuration. These only apply to wind devices.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client":'client',
        "time_zone":'timeZone',
        "data_signals":'dataSignals'
    }

    def __init__(self,
                 client=None,
                 time_zone=None,
                 data_signals=None):
        """Constructor for the ConfigurationItem class"""

        # Initialize members of the class
        self.client = client
        self.time_zone = time_zone
        self.data_signals = data_signals


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
        client = greenbyteapi.models.client_configuration.ClientConfiguration.from_dictionary(dictionary.get('client')) if dictionary.get('client') else None
        time_zone = greenbyteapi.models.time_zone_configuration.TimeZoneConfiguration.from_dictionary(dictionary.get('timeZone')) if dictionary.get('timeZone') else None
        data_signals = greenbyteapi.models.data_signal_configuration.DataSignalConfiguration.from_dictionary(dictionary.get('dataSignals')) if dictionary.get('dataSignals') else None

        # Return an object of this model
        return cls(client,
                   time_zone,
                   data_signals)


