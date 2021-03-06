# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from greenbyteapi.api_helper import APIHelper


class ConfigurationDataControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ConfigurationDataControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.configuration_data

    # Gets your system-wide configuration data.
    #
    #_🔐 This endpoint requires the **Configuration** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `configuration.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_configuration(self):

        # Perform the API call through the SDK function
        result = self.controller.get_configuration()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '[{"client":{"title":"Intro (Greenbyte AB)","tag":"intro","urlWeb":"https:/'
            '/intro.greenbyte.cloud/","urlApi":"https://intro.greenbyte.cloud/api/2.0/"}'
            ',"timeZone":{"title":"Europe/Stockholm","utcOffset":1,"utcOffsetDst":2,"dst'
            'TimestampStart":"2020-03-29T01:00:00","dstTimestampEnd":"2020-10-25T01:00:0'
            '0"},"dataSignals":{"availabilityTimeDataSignalId":430,"availabilityProducti'
            'onDataSignalId":445,"lostProductionDataSignalId":432,"performanceDataSignal'
            'Id":436}}]'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets your system-wide configuration data.
    #
    #_🔐 This endpoint requires the **Configuration** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `configuration.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_configuration_1(self):

        # Perform the API call through the SDK function
        result = self.controller.get_configuration()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

