# -*- coding: utf-8 -*-

"""
    greenbyteapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from greenbyteapi.api_helper import APIHelper
from greenbyteapi.configuration import Configuration
from greenbyteapi.controllers.base_controller import BaseController
from greenbyteapi.http.auth.custom_header_auth import CustomHeaderAuth
from greenbyteapi.models.device import Device
from greenbyteapi.models.site_with_data import SiteWithData
from greenbyteapi.models.power_curve import PowerCurve
from greenbyteapi.exceptions.problem_details_exception import ProblemDetailsException
from greenbyteapi.exceptions.api_exception import APIException

class AssetsController(BaseController):

    """A Controller to access Endpoints in the greenbyteapi API."""


    def get_devices(self,
                    device_type_ids=None,
                    site_ids=None,
                    parent_ids=None,
                    fields=None,
                    page_size=50,
                    page=1,
                    use_utc=False):
        """Does a GET request to /devices.

        Gets a list of devices that the API key has permissions for.
        _🔐 This endpoint requires the **Assets** endpoint permission._
        _This request can also be made using the POST method, 
        with a request to `devices.json` and 
        a JSON request body instead of query parameters._

        Args:
            device_type_ids (list of int, optional): Only include devices of
                these types. Examples: * 1 - Wind turbine * 2 - Production
                meter * 3 - Met mast * 4 - Inverter * 10 - Device group * 11 -
                Grid meter * 12 - Combiner box * 23 - String * 27 - Virtual
                Meteo Sensor
            site_ids (list of int, optional): Only include devices at these
                sites.
            parent_ids (list of int, optional): Only include devices with
                these parent devices.
            fields (list of string, optional): Which fields to include in the
                response. Valid fields are those defined in the `Device`
                schema (See Response Type). By default all fields are
                included.
            page_size (int, optional): The number of items to return per
                page.
            page (int, optional): Which page to return when the number of
                items exceed the page size.
            use_utc (bool, optional): Set to true to get timestamps in UTC.

        Returns:
            list of Device: Response from the API. A list of devices with
                associated metadata.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/devices'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'deviceTypeIds': device_type_ids,
            'siteIds': site_ids,
            'parentIds': parent_ids,
            'fields': fields,
            'pageSize': page_size,
            'page': page,
            'useUtc': use_utc
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ProblemDetailsException('The request cannot be fulfilled due to bad syntax.', _context)
        elif _context.response.status_code == 401:
            raise APIException('The request is missing a valid API key. ', _context)
        elif _context.response.status_code == 403:
            raise APIException('One of the following: * The API key does not authorize access to the requested endpoint because of a missing endpoint permission. * The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. ', _context)
        elif _context.response.status_code == 405:
            raise APIException('The HTTP method is not allowed for the endpoint.', _context)
        elif _context.response.status_code == 429:
            raise ProblemDetailsException('The API key has been used in too many requests in a given amount of time. The following headers will be set in the response: * `X-Rate-Limit-Limit` – The rate limit period (for example   "1m", "12h", or "1d"). * `X-Rate-Limit-Remaining` – The remaining number of requests   for this period. * `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601   format) when the remaining number of requests resets.  The limit is currently 1,000 requests/minute per API key and IP address. ', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Device.from_dictionary)

    def get_sites(self,
                  fields=None,
                  page_size=50,
                  page=1):
        """Does a GET request to /sites.

        Gets a list of sites that the API key has permissions
        for.
        _🔐 This endpoint requires the **Assets** endpoint permission._
        _This request can also be made using the POST method, 
        with a request to `sites.json` and 
        a JSON request body instead of query parameters._

        Args:
            fields (list of string, optional): Which fields to include in the
                response. Valid fields are those defined in the `SiteWithData`
                schema (See Response Type). By default all fields are
                included.
            page_size (int, optional): The number of items to return per
                page.
            page (int, optional): Which page to return when the number of
                items exceed the page size.

        Returns:
            list of SiteWithData: Response from the API. A list of sites with
                associated metadata.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/sites'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'fields': fields,
            'pageSize': page_size,
            'page': page
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ProblemDetailsException('The request cannot be fulfilled due to bad syntax.', _context)
        elif _context.response.status_code == 401:
            raise APIException('The request is missing a valid API key. ', _context)
        elif _context.response.status_code == 403:
            raise APIException('One of the following: * The API key does not authorize access to the requested endpoint because of a missing endpoint permission. * The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. ', _context)
        elif _context.response.status_code == 405:
            raise APIException('The HTTP method is not allowed for the endpoint.', _context)
        elif _context.response.status_code == 429:
            raise ProblemDetailsException('The API key has been used in too many requests in a given amount of time. The following headers will be set in the response: * `X-Rate-Limit-Limit` – The rate limit period (for example   "1m", "12h", or "1d"). * `X-Rate-Limit-Remaining` – The remaining number of requests   for this period. * `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601   format) when the remaining number of requests resets.  The limit is currently 1,000 requests/minute per API key and IP address. ', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, SiteWithData.from_dictionary)

    def get_power_curves(self,
                         device_ids,
                         timestamp=None,
                         learned=False):
        """Does a GET request to /powercurves.

        Gets the default or learned power curves for wind turbines.
        Other device types are not supported.
        _🔐 This endpoint requires the **PowerCurves** endpoint permission._
        _This request can also be made using the POST method, 
        with a request to `powercurves.json` and 
        a JSON request body instead of query parameters._

        Args:
            device_ids (list of int): What devices to get power curves for.
                Only wind turbines are supported.
            timestamp (date, optional): The date for which to get power
                curves. The default is the current date.
            learned (bool, optional): Whether to get learned power curves
                instead of default power curves.

        Returns:
            list of PowerCurve: Response from the API. A list of objects
                containing device ids and associated power curves.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/powercurves'
        _query_builder = Configuration.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'deviceIds': device_ids,
            'timestamp': timestamp,
            'learned': learned
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ProblemDetailsException('The request cannot be fulfilled due to bad syntax.', _context)
        elif _context.response.status_code == 401:
            raise APIException('The request is missing a valid API key. ', _context)
        elif _context.response.status_code == 403:
            raise APIException('One of the following: * The API key does not authorize access to the requested endpoint because of a missing endpoint permission. * The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. ', _context)
        elif _context.response.status_code == 405:
            raise APIException('The HTTP method is not allowed for the endpoint.', _context)
        elif _context.response.status_code == 429:
            raise ProblemDetailsException('The API key has been used in too many requests in a given amount of time. The following headers will be set in the response: * `X-Rate-Limit-Limit` – The rate limit period (for example   "1m", "12h", or "1d"). * `X-Rate-Limit-Remaining` – The remaining number of requests   for this period. * `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601   format) when the remaining number of requests resets.  The limit is currently 1,000 requests/minute per API key and IP address. ', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, PowerCurve.from_dictionary)
