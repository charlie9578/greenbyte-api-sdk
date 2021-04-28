# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

class AggregateModeEnum(object):

    """Implementation of the 'AggregateMode' enum.

    How data is aggregated in the asset structure.

    Attributes:
        DEVICE: The data is aggregated by device.
        DEVICELEVEL: The data is aggregated by top-level device.
        SITE: The data is aggregated by site.
        PORTFOLIO: All data is aggregated into a single group.
        SITELEVEL: The data is aggregated by site hierarchy level. When this
            mode is used the parameter AggregateLevel controls down to which
            level in the hierarchy to aggregate.

    """

    DEVICE = 'device'

    DEVICELEVEL = 'deviceLevel'

    SITE = 'site'

    PORTFOLIO = 'portfolio'

    SITELEVEL = 'siteLevel'
