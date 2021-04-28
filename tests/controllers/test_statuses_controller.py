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


class StatusesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(StatusesControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.statuses

    # Gets statuses for multiple devices during the given time period.
    #The timestamps are in the time zone configured in the Greenbyte Platform.
    #Use the useUtc flag to get timestamps in UTC.
    #
    #_🔐 This endpoint requires the **Statuses** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `status.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_statuses(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        timestamp_start = APIHelper.RFC3339DateTime.from_value('2020-01-01T00:00:00Z').datetime
        timestamp_end = APIHelper.RFC3339DateTime.from_value('2020-01-08T00:00:00Z').datetime
        category = None
        lost_production_signal_id = 432
        fields = APIHelper.json_deserialize('["deviceId","message","lostProduction"]')
        sort_by = None
        sort_asc = False
        page_size = 50
        page = 1
        use_utc = False

        # Perform the API call through the SDK function
        result = self.controller.get_statuses(device_ids, timestamp_start, timestamp_end, category, lost_production_signal_id, fields, sort_by, sort_asc, page_size, page, use_utc)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Gets statuses for multiple devices during the given time period.
    #The timestamps are in the time zone configured in the Greenbyte Platform.
    #Use the useUtc flag to get timestamps in UTC.
    #
    #_🔐 This endpoint requires the **Statuses** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `status.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_statuses_1(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        timestamp_start = APIHelper.RFC3339DateTime.from_value('2020-01-01T00:00:00Z').datetime
        timestamp_end = APIHelper.RFC3339DateTime.from_value('2020-01-08T00:00:00Z').datetime
        category = None
        lost_production_signal_id = 432
        fields = APIHelper.json_deserialize('["deviceId","message","lostProduction"]')
        sort_by = None
        sort_asc = False
        page_size = 50
        page = 1
        use_utc = False

        # Perform the API call through the SDK function
        result = self.controller.get_statuses(device_ids, timestamp_start, timestamp_end, category, lost_production_signal_id, fields, sort_by, sort_asc, page_size, page, use_utc)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets active statuses for multiple devices.
    #The timestamps are in the time zone configured in the Greenbyte Platform.
    #Use the useUtc flag to get timestamps in UTC.
    #
    #_🔐 This endpoint requires the **Statuses** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `activestatus.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_active_statuses(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        category = None
        lost_production_signal_id = 432
        fields = APIHelper.json_deserialize('["deviceId","message","lostProduction"]')
        sort_by = None
        sort_asc = False
        page_size = 50
        page = 1
        use_utc = False

        # Perform the API call through the SDK function
        result = self.controller.get_active_statuses(device_ids, category, lost_production_signal_id, fields, sort_by, sort_asc, page_size, page, use_utc)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Gets active statuses for multiple devices.
    #The timestamps are in the time zone configured in the Greenbyte Platform.
    #Use the useUtc flag to get timestamps in UTC.
    #
    #_🔐 This endpoint requires the **Statuses** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `activestatus.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_active_statuses_1(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        category = None
        lost_production_signal_id = 432
        fields = APIHelper.json_deserialize('["deviceId","message","lostProduction"]')
        sort_by = None
        sort_asc = False
        page_size = 50
        page = 1
        use_utc = False

        # Perform the API call through the SDK function
        result = self.controller.get_active_statuses(device_ids, category, lost_production_signal_id, fields, sort_by, sort_asc, page_size, page, use_utc)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)
