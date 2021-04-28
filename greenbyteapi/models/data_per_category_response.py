# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import greenbyteapi.models.data_signal
import greenbyteapi.models.data_per_category_item

class DataPerCategoryResponse(object):

    """Implementation of the 'DataPerCategoryResponse' model.

    An object containing data grouped by contract category and aggregate.

    Attributes:
        data_signal (DataSignal): A data signal.
        calculation (CalculationModeEnum): Which operation to use when
            aggregating data.
        data (list of DataPerCategoryItem): A list of objects: one per
            combination of * aggregate * contract category

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data_signal":'dataSignal',
        "calculation":'calculation',
        "data":'data'
    }

    def __init__(self,
                 data_signal=None,
                 calculation=None,
                 data=None):
        """Constructor for the DataPerCategoryResponse class"""

        # Initialize members of the class
        self.data_signal = data_signal
        self.calculation = calculation
        self.data = data


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
        data_signal = greenbyteapi.models.data_signal.DataSignal.from_dictionary(dictionary.get('dataSignal')) if dictionary.get('dataSignal') else None
        calculation = dictionary.get('calculation')
        data = None
        if dictionary.get('data') != None:
            data = list()
            for structure in dictionary.get('data'):
                data.append(greenbyteapi.models.data_per_category_item.DataPerCategoryItem.from_dictionary(structure))

        # Return an object of this model
        return cls(data_signal,
                   calculation,
                   data)

