# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import dateutil.parser

class Recurrence(object):

    """Implementation of the 'Recurrence' model.

    Recurrence settings for the task. To calculate when the
    task is recurring, use the `timestampStart` field and
    then add to it multiples of the specified interval; the
    `intervalType` field determines if the task is recurring
    on daily, weekly, monthly, or yearly basis.
    If the task is not recurring, this field is null.
    **Note:** Only the main (first) task in a recurring
    series have recurrence settings. For the other tasks in
    the series, the field `mainTaskId` can be used to find
    it.

    Attributes:
        interval (int): The interval with which the task repeats.
        interval_type (IntervalTypeEnum): The type of with which the task
            repeats.
        date_end (date): When the recurring task series ends (exclusive).  The
            end date is **not** included in the recurring task series: for
            example, to have a task series occur until and including the last
            day of March 2020, set `dateEnd` to "2020-04-01".

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interval":'interval',
        "interval_type":'intervalType',
        "date_end":'dateEnd'
    }

    def __init__(self,
                 interval=None,
                 interval_type=None,
                 date_end=None):
        """Constructor for the Recurrence class"""

        # Initialize members of the class
        self.interval = interval
        self.interval_type = interval_type
        self.date_end = date_end


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
        interval = dictionary.get('interval')
        interval_type = dictionary.get('intervalType')
        date_end = dateutil.parser.parse(dictionary.get('dateEnd')).date() if dictionary.get('dateEnd') else None

        # Return an object of this model
        return cls(interval,
                   interval_type,
                   date_end)


