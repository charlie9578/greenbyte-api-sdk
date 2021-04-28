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


class DataControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(DataControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.data

    # Gets authorized data signals for one or more devices.
    #
    #_🔐 This endpoint requires the **Data** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `datasignals.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_data_signals(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')

        # Perform the API call through the SDK function
        result = self.controller.get_data_signals(device_ids)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '[{"dataSignalId":1,"title":"Wind speed","type":"Wind speed","unit":"m/s","'
            'deviceType":{"deviceTypeId":1,"title":"Turbine"}},{"dataSignalId":5,"title"'
            ':"Power","type":"Power","unit":"kW","deviceType":{"deviceTypeId":1,"title":'
            '"Turbine"}}]'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets authorized data signals for one or more devices.
    #
    #_🔐 This endpoint requires the **Data** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `datasignals.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_data_signals_1(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')

        # Perform the API call through the SDK function
        result = self.controller.get_data_signals(device_ids)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets data for multiple devices and data signals in the given
    #resolution. The timestamps are in the time zone configured in the Greenbyte Platform.
    #Use the useUtc flag to get timestamps in UTC for all resolutions other than daily, weekly, monthly and yearly.
    #
    #_🔐 This endpoint requires the **Data** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `data.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_data(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        data_signal_ids = APIHelper.json_deserialize('[1,5]')
        timestamp_start = APIHelper.RFC3339DateTime.from_value('2020-01-01T00:00:00Z').datetime
        timestamp_end = APIHelper.RFC3339DateTime.from_value('2020-01-08T00:00:00Z').datetime
        use_utc = False
        resolution = '10minute'
        aggregate = 'device'
        aggregate_level = 0
        calculation = 'sum'

        # Perform the API call through the SDK function
        result = self.controller.get_data(device_ids, data_signal_ids, timestamp_start, timestamp_end, use_utc, resolution, aggregate, aggregate_level, calculation)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '[{"aggregate":"device","aggregateId":1,"aggregatePathNames":[],"deviceIds"'
            ':[1],"resolution":"hourly","calculation":"sum","dataSignal":{"dataSignalId"'
            ':1,"title":"Wind speed","unit":"m/s"},"data":{"2020-01-01T00:00:00":6.89,"2'
            '020-01-01T01:00:00":8.33}},{"aggregate":"device","aggregateId":1,"aggregate'
            'PathNames":[],"deviceIds":[1],"resolution":"hourly","calculation":"sum","da'
            'taSignal":{"dataSignalId":5,"title":"Power","unit":"kW"},"data":{"2020-01-0'
            '1T00:00:00":584.33,"2020-01-01T01:00:00":1014}}]'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets data for multiple devices and data signals in the given
    #resolution. The timestamps are in the time zone configured in the Greenbyte Platform.
    #Use the useUtc flag to get timestamps in UTC for all resolutions other than daily, weekly, monthly and yearly.
    #
    #_🔐 This endpoint requires the **Data** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `data.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_data_1(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        data_signal_ids = APIHelper.json_deserialize('[1,5]')
        timestamp_start = APIHelper.RFC3339DateTime.from_value('2020-01-01T00:00:00Z').datetime
        timestamp_end = APIHelper.RFC3339DateTime.from_value('2020-01-08T00:00:00Z').datetime
        use_utc = False
        resolution = '10minute'
        aggregate = 'device'
        aggregate_level = 0
        calculation = 'sum'

        # Perform the API call through the SDK function
        result = self.controller.get_data(device_ids, data_signal_ids, timestamp_start, timestamp_end, use_utc, resolution, aggregate, aggregate_level, calculation)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets the most recent data point for each
    #specified device and data signal. The timestamps are in UTC.
    #
    #_🔐 This endpoint requires the **Data** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `realtimedata.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_real_time_data(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        data_signal_ids = APIHelper.json_deserialize('[1,5]')
        aggregate = 'device'
        aggregate_level = 0
        calculation = 'sum'

        # Perform the API call through the SDK function
        result = self.controller.get_real_time_data(device_ids, data_signal_ids, aggregate, aggregate_level, calculation)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '[{"aggregate":"device","aggregateId":24,"aggregatePathNames":[],"deviceIds'
            '":[24],"calculation":"sum","dataSignal":{"dataSignalId":5,"title":"Power","'
            'unit":"kW"},"data":{"2020-03-17T12:50:02Z":2174}},{"aggregate":"device","ag'
            'gregateId":24,"aggregatePathNames":[],"deviceIds":[24],"calculation":"sum",'
            '"dataSignal":{"dataSignalId":1,"title":"Wind speed","unit":"m/s"},"data":{"'
            '2020-03-17T12:50:02Z":12.2}}]'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets the most recent data point for each
    #specified device and data signal. The timestamps are in UTC.
    #
    #_🔐 This endpoint requires the **Data** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `realtimedata.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_real_time_data_1(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        data_signal_ids = APIHelper.json_deserialize('[1,5]')
        aggregate = 'device'
        aggregate_level = 0
        calculation = 'sum'

        # Perform the API call through the SDK function
        result = self.controller.get_real_time_data(device_ids, data_signal_ids, aggregate, aggregate_level, calculation)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets signal data aggregated per availability contract category.
    #
    #_🔐 This endpoint requires the **Data** and **Statuses** endpoint permissions._
    #
    #_This request can also be made using the POST method, 
    #with a request to `datapercategory.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_data_per_category(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        data_signal_id = 248
        timestamp_start = APIHelper.RFC3339DateTime.from_value('2020-01-01T00:00:00Z').datetime
        timestamp_end = APIHelper.RFC3339DateTime.from_value('2020-01-08T00:00:00Z').datetime
        aggregate = 'device'
        aggregate_level = 0
        category = APIHelper.json_deserialize('["stop"]')

        # Perform the API call through the SDK function
        result = self.controller.get_data_per_category(device_ids, data_signal_id, timestamp_start, timestamp_end, aggregate, aggregate_level, category)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '{"dataSignal":{"dataSignalId":248,"title":"Lost Production (Contractual)",'
            '"unit":"kWh"},"calculation":"sum","data":[{"aggregateId":6,"aggregatePathNa'
            'mes":[],"deviceIds":[1,2,3],"contractTitle":"Vestas 1","categoryTitle":"Ici'
            'ng","categoryTime":"available","value":104.55,"duration":150},{"aggregateId'
            '":6,"aggregatePathNames":[],"deviceIds":[1,2,3],"contractTitle":"Vestas 1",'
            '"categoryTitle":"Utility","categoryTime":"excluded","value":73,"duration":5'
            '0.3}]}'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets signal data aggregated per availability contract category.
    #
    #_🔐 This endpoint requires the **Data** and **Statuses** endpoint permissions._
    #
    #_This request can also be made using the POST method, 
    #with a request to `datapercategory.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_data_per_category_1(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        data_signal_id = 248
        timestamp_start = APIHelper.RFC3339DateTime.from_value('2020-01-01T00:00:00Z').datetime
        timestamp_end = APIHelper.RFC3339DateTime.from_value('2020-01-08T00:00:00Z').datetime
        aggregate = 'device'
        aggregate_level = 0
        category = APIHelper.json_deserialize('["stop"]')

        # Perform the API call through the SDK function
        result = self.controller.get_data_per_category(device_ids, data_signal_id, timestamp_start, timestamp_end, aggregate, aggregate_level, category)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

