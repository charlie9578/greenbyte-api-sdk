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


class AssetsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(AssetsControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.assets

    # Gets a list of devices that the API key has permissions for.
    #
    #_🔐 This endpoint requires the **Assets** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `devices.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_devices(self):
        # Parameters for the API call
        device_type_ids = APIHelper.json_deserialize('[1,2,3]')
        site_ids = APIHelper.json_deserialize('[1,2,3]')
        parent_ids = APIHelper.json_deserialize('[1,2,3]')
        fields = None
        page_size = 50
        page = 1
        use_utc = False

        # Perform the API call through the SDK function
        result = self.controller.get_devices(device_type_ids, site_ids, parent_ids, fields, page_size, page, use_utc)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '[{"deviceId":1121,"title":"Enerburg group A","altTitle":null,"identity":nu'
            'll,"site":{"siteId":7,"title":"Enerburg"},"deviceType":"Group","deviceTypeI'
            'd":10,"parentId":null,"childIds":[69,70],"deviceModel":null,"deviceModelId"'
            ':41,"manufacturer":"Generic group","model":"Generic","maxPower":0,"timestam'
            'pStart":"2013-10-01T02:00:00","latitude":"32.36431","longitude":"-88.7037",'
            '"elevation":"0","metadata":[]},{"deviceId":69,"title":"Enerburg 1","altTitl'
            'e":null,"identity":null,"site":{"siteId":7,"title":"Enerburg"},"deviceType"'
            ':"Turbine","deviceTypeId":1,"parentId":1121,"childIds":[],"deviceModel":nul'
            'l,"turbineType":{"turbineTypeId":1,"title":"Enercon E-82 E2 2.3MW","manufac'
            'turer":"Enercon","model":"E-82","controller":"CS82a","ratedPower":2300,"max'
            'RotorSpeed":18},"maxPower":2300,"biddingArea":null,"timestampStart":"2013-1'
            '0-01T02:00:00","latitude":"32.36431","longitude":"-88.7037","elevation":"0"'
            ',"targetAvailability":97,"metadata":[{"key":"Hub Height","value":"120"},{"k'
            'ey":"Direct Drive","value":"no"},{"key":"Blade Heating","value":"yes"}]},{"'
            'deviceId":70,"title":"Enerburg 2","altTitle":null,"identity":null,"site":{"'
            'siteId":7,"title":"Enerburg"},"deviceType":"Turbine","deviceTypeId":1,"pare'
            'ntId":1121,"childIds":[],"deviceModel":null,"turbineType":{"turbineTypeId":'
            '1,"title":"Enercon E-82 E2 2.3MW","manufacturer":"Enercon","model":"E-82","'
            'controller":"CS82a","ratedPower":2300,"maxRotorSpeed":18},"maxPower":2300,"'
            'biddingArea":null,"timestampStart":"2013-10-01T02:00:00","latitude":"32.360'
            '2","longitude":"-88.7194","elevation":"0","targetAvailability":null,"metada'
            'ta":[{"key":"Hub Height","value":"120"},{"key":"Direct Drive","value":"no"}'
            ',{"key":"Blade Heating","value":"yes"}]},{"deviceId":71,"title":"Enerburg 3'
            '","altTitle":null,"identity":null,"site":{"siteId":7,"title":"Enerburg"},"d'
            'eviceType":"Turbine","deviceModel":null,"parentId":null,"childIds":[],"devi'
            'ceTypeId":1,"turbineType":{"turbineTypeId":1,"title":"Enercon E-82 E2 2.3MW'
            '","manufacturer":"Enercon","model":"E-82","controller":"CS82a","ratedPower"'
            ':2300,"maxRotorSpeed":18},"maxPower":2300,"biddingArea":null,"timestampStar'
            't":"2013-10-01T02:00:00","latitude":"32.35697","longitude":"-88.7182","elev'
            'ation":"0","targetAvailability":null,"metadata":[]}]'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets a list of devices that the API key has permissions for.
    #
    #_🔐 This endpoint requires the **Assets** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `devices.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_devices_1(self):
        # Parameters for the API call
        device_type_ids = APIHelper.json_deserialize('[1,2,3]')
        site_ids = APIHelper.json_deserialize('[1,2,3]')
        parent_ids = APIHelper.json_deserialize('[1,2,3]')
        fields = None
        page_size = 50
        page = 1
        use_utc = False

        # Perform the API call through the SDK function
        result = self.controller.get_devices(device_type_ids, site_ids, parent_ids, fields, page_size, page, use_utc)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets a list of sites that the API key has permissions
    #for.
    #
    #_🔐 This endpoint requires the **Assets** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `sites.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_sites(self):
        # Parameters for the API call
        fields = APIHelper.json_deserialize('["siteId","title"]')
        page_size = 50
        page = 1

        # Perform the API call through the SDK function
        result = self.controller.get_sites(fields, page_size, page)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '[{"siteId":1,"title":"Wind farm 1","country":"Sweden","identity":"SE-WF1",'
            '"metadata":[{"key":"Address","value":"Wind Street 123"},{"key":"Phone","val'
            'ue":"555 123 456"}]},{"siteId":2,"title":"Solar site 1","country":"Spain","'
            'identity":"ES-SS1","metadata":[{"key":"Address","value":"Sun Street 456"},{'
            '"key":"Phone","value":"555 456 789"}]}]'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets a list of sites that the API key has permissions
    #for.
    #
    #_🔐 This endpoint requires the **Assets** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `sites.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_sites_1(self):
        # Parameters for the API call
        fields = APIHelper.json_deserialize('["siteId","title"]')
        page_size = 50
        page = 1

        # Perform the API call through the SDK function
        result = self.controller.get_sites(fields, page_size, page)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

    # Gets the default or learned power curves for wind turbines.
    #Other device types are not supported.
    #
    #_🔐 This endpoint requires the **PowerCurves** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `powercurves.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_power_curves(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        timestamp = dateutil.parser.parse('2020-01-01').date()
        learned = False

        # Perform the API call through the SDK function
        result = self.controller.get_power_curves(device_ids, timestamp, learned)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json; charset=utf-8'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))

        
        # Test whether the captured response is as we expected
        self.assertIsNotNone(result)
        expected_body = APIHelper.json_deserialize(
            '[{"deviceId":1,"title":"Enercon E-82 Noise mode 0","values":[{"windSpeed":'
            '1,"power":0},{"windSpeed":4,"power":88},{"windSpeed":5,"power":205},{"windS'
            'peed":6,"power":371},{"windSpeed":7,"power":601},{"windSpeed":8,"power":901'
            '},{"windSpeed":9,"power":1243},{"windSpeed":10,"power":1591},{"windSpeed":1'
            '1,"power":1876},{"windSpeed":12,"power":1979},{"windSpeed":13,"power":1999}'
            ',{"windSpeed":14,"power":2000},{"windSpeed":15,"power":2000},{"windSpeed":1'
            '6,"power":2000},{"windSpeed":17,"power":2000},{"windSpeed":18,"power":2000}'
            ',{"windSpeed":19,"power":2000},{"windSpeed":20,"power":2000},{"windSpeed":2'
            '1,"power":2000},{"windSpeed":22,"power":2000},{"windSpeed":23,"power":2000}'
            ',{"windSpeed":24,"power":2000},{"windSpeed":25,"power":2000}]}]'
            )
        received_body = APIHelper.json_deserialize(self.response_catcher.response.raw_body)
        self.assertTrue(TestHelper.match_body(expected_body, received_body))


    # Gets the default or learned power curves for wind turbines.
    #Other device types are not supported.
    #
    #_🔐 This endpoint requires the **PowerCurves** endpoint permission._
    #
    #_This request can also be made using the POST method, 
    #with a request to `powercurves.json` and 
    #a JSON request body instead of query parameters._
    #
    def test_test_get_power_curves_1(self):
        # Parameters for the API call
        device_ids = APIHelper.json_deserialize('[1,2,3]')
        timestamp = dateutil.parser.parse('2020-01-01').date()
        learned = False

        # Perform the API call through the SDK function
        result = self.controller.get_power_curves(device_ids, timestamp, learned)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 204)

