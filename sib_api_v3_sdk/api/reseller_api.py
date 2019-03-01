# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sib_api_v3_sdk.api_client import ApiClient


class ResellerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_credits(self, child_auth_key, add_credits, **kwargs):  # noqa: E501
        """Add Email and/or SMS credits to a specific child account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_credits(child_auth_key, add_credits, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param AddCredits add_credits: Values to post to add credit to a specific child account (required)
        :return: RemainingCreditModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_credits_with_http_info(child_auth_key, add_credits, **kwargs)  # noqa: E501
        else:
            (data) = self.add_credits_with_http_info(child_auth_key, add_credits, **kwargs)  # noqa: E501
            return data

    def add_credits_with_http_info(self, child_auth_key, add_credits, **kwargs):  # noqa: E501
        """Add Email and/or SMS credits to a specific child account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_credits_with_http_info(child_auth_key, add_credits, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param AddCredits add_credits: Values to post to add credit to a specific child account (required)
        :return: RemainingCreditModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['child_auth_key', 'add_credits']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_credits" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'child_auth_key' is set
        if ('child_auth_key' not in params or
                params['child_auth_key'] is None):
            raise ValueError("Missing the required parameter `child_auth_key` when calling `add_credits`")  # noqa: E501
        # verify the required parameter 'add_credits' is set
        if ('add_credits' not in params or
                params['add_credits'] is None):
            raise ValueError("Missing the required parameter `add_credits` when calling `add_credits`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'child_auth_key' in params:
            path_params['childAuthKey'] = params['child_auth_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add_credits' in params:
            body_params = params['add_credits']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children/{childAuthKey}/credits/add', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemainingCreditModel',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def associate_ip_to_child(self, child_auth_key, ip, **kwargs):  # noqa: E501
        """Associate a dedicated IP to the child  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.associate_ip_to_child(child_auth_key, ip, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param ManageIp ip: IP to associate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.associate_ip_to_child_with_http_info(child_auth_key, ip, **kwargs)  # noqa: E501
        else:
            (data) = self.associate_ip_to_child_with_http_info(child_auth_key, ip, **kwargs)  # noqa: E501
            return data

    def associate_ip_to_child_with_http_info(self, child_auth_key, ip, **kwargs):  # noqa: E501
        """Associate a dedicated IP to the child  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.associate_ip_to_child_with_http_info(child_auth_key, ip, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param ManageIp ip: IP to associate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['child_auth_key', 'ip']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method associate_ip_to_child" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'child_auth_key' is set
        if ('child_auth_key' not in params or
                params['child_auth_key'] is None):
            raise ValueError("Missing the required parameter `child_auth_key` when calling `associate_ip_to_child`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if ('ip' not in params or
                params['ip'] is None):
            raise ValueError("Missing the required parameter `ip` when calling `associate_ip_to_child`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'child_auth_key' in params:
            path_params['childAuthKey'] = params['child_auth_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ip' in params:
            body_params = params['ip']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children/{childAuthKey}/ips/associate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_reseller_child(self, **kwargs):  # noqa: E501
        """Creates a reseller child  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_reseller_child(async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateChild reseller_child: reseller child to add
        :return: CreateReseller
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_reseller_child_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_reseller_child_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_reseller_child_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a reseller child  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_reseller_child_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateChild reseller_child: reseller child to add
        :return: CreateReseller
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reseller_child']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_reseller_child" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reseller_child' in params:
            body_params = params['reseller_child']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateReseller',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_reseller_child(self, child_auth_key, **kwargs):  # noqa: E501
        """Deletes a single reseller child based on the childAuthKey supplied  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_reseller_child(child_auth_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_reseller_child_with_http_info(child_auth_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_reseller_child_with_http_info(child_auth_key, **kwargs)  # noqa: E501
            return data

    def delete_reseller_child_with_http_info(self, child_auth_key, **kwargs):  # noqa: E501
        """Deletes a single reseller child based on the childAuthKey supplied  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_reseller_child_with_http_info(child_auth_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['child_auth_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_reseller_child" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'child_auth_key' is set
        if ('child_auth_key' not in params or
                params['child_auth_key'] is None):
            raise ValueError("Missing the required parameter `child_auth_key` when calling `delete_reseller_child`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'child_auth_key' in params:
            path_params['childAuthKey'] = params['child_auth_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children/{childAuthKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dissociate_ip_from_child(self, child_auth_key, ip, **kwargs):  # noqa: E501
        """Dissociate a dedicated IP to the child  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dissociate_ip_from_child(child_auth_key, ip, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param ManageIp ip: IP to dissociate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.dissociate_ip_from_child_with_http_info(child_auth_key, ip, **kwargs)  # noqa: E501
        else:
            (data) = self.dissociate_ip_from_child_with_http_info(child_auth_key, ip, **kwargs)  # noqa: E501
            return data

    def dissociate_ip_from_child_with_http_info(self, child_auth_key, ip, **kwargs):  # noqa: E501
        """Dissociate a dedicated IP to the child  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.dissociate_ip_from_child_with_http_info(child_auth_key, ip, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param ManageIp ip: IP to dissociate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['child_auth_key', 'ip']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dissociate_ip_from_child" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'child_auth_key' is set
        if ('child_auth_key' not in params or
                params['child_auth_key'] is None):
            raise ValueError("Missing the required parameter `child_auth_key` when calling `dissociate_ip_from_child`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if ('ip' not in params or
                params['ip'] is None):
            raise ValueError("Missing the required parameter `ip` when calling `dissociate_ip_from_child`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'child_auth_key' in params:
            path_params['childAuthKey'] = params['child_auth_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ip' in params:
            body_params = params['ip']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children/{childAuthKey}/ips/dissociate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_child_info(self, child_auth_key, **kwargs):  # noqa: E501
        """Gets the info about a specific child account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_child_info(child_auth_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :return: GetChildInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_child_info_with_http_info(child_auth_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_child_info_with_http_info(child_auth_key, **kwargs)  # noqa: E501
            return data

    def get_child_info_with_http_info(self, child_auth_key, **kwargs):  # noqa: E501
        """Gets the info about a specific child account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_child_info_with_http_info(child_auth_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :return: GetChildInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['child_auth_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_child_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'child_auth_key' is set
        if ('child_auth_key' not in params or
                params['child_auth_key'] is None):
            raise ValueError("Missing the required parameter `child_auth_key` when calling `get_child_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'child_auth_key' in params:
            path_params['childAuthKey'] = params['child_auth_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children/{childAuthKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetChildInfo',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_reseller_childs(self, **kwargs):  # noqa: E501
        """Gets the list of all reseller&#39;s children accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_reseller_childs(async=True)
        >>> result = thread.get()

        :param async bool
        :return: GetChildrenList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_reseller_childs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_reseller_childs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_reseller_childs_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the list of all reseller&#39;s children accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_reseller_childs_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: GetChildrenList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reseller_childs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetChildrenList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_credits(self, child_auth_key, remove_credits, **kwargs):  # noqa: E501
        """Remove Email and/or SMS credits from a specific child account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_credits(child_auth_key, remove_credits, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param RemoveCredits remove_credits: Values to post to remove email or SMS credits from a specific child account (required)
        :return: RemainingCreditModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_credits_with_http_info(child_auth_key, remove_credits, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_credits_with_http_info(child_auth_key, remove_credits, **kwargs)  # noqa: E501
            return data

    def remove_credits_with_http_info(self, child_auth_key, remove_credits, **kwargs):  # noqa: E501
        """Remove Email and/or SMS credits from a specific child account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_credits_with_http_info(child_auth_key, remove_credits, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param RemoveCredits remove_credits: Values to post to remove email or SMS credits from a specific child account (required)
        :return: RemainingCreditModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['child_auth_key', 'remove_credits']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_credits" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'child_auth_key' is set
        if ('child_auth_key' not in params or
                params['child_auth_key'] is None):
            raise ValueError("Missing the required parameter `child_auth_key` when calling `remove_credits`")  # noqa: E501
        # verify the required parameter 'remove_credits' is set
        if ('remove_credits' not in params or
                params['remove_credits'] is None):
            raise ValueError("Missing the required parameter `remove_credits` when calling `remove_credits`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'child_auth_key' in params:
            path_params['childAuthKey'] = params['child_auth_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'remove_credits' in params:
            body_params = params['remove_credits']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children/{childAuthKey}/credits/remove', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RemainingCreditModel',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_reseller_child(self, child_auth_key, reseller_child, **kwargs):  # noqa: E501
        """Updates infos of reseller&#39;s child based on the childAuthKey supplied  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_reseller_child(child_auth_key, reseller_child, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param UpdateChild reseller_child: values to update in child profile (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_reseller_child_with_http_info(child_auth_key, reseller_child, **kwargs)  # noqa: E501
        else:
            (data) = self.update_reseller_child_with_http_info(child_auth_key, reseller_child, **kwargs)  # noqa: E501
            return data

    def update_reseller_child_with_http_info(self, child_auth_key, reseller_child, **kwargs):  # noqa: E501
        """Updates infos of reseller&#39;s child based on the childAuthKey supplied  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_reseller_child_with_http_info(child_auth_key, reseller_child, async=True)
        >>> result = thread.get()

        :param async bool
        :param str child_auth_key: auth key of reseller's child (required)
        :param UpdateChild reseller_child: values to update in child profile (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['child_auth_key', 'reseller_child']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_reseller_child" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'child_auth_key' is set
        if ('child_auth_key' not in params or
                params['child_auth_key'] is None):
            raise ValueError("Missing the required parameter `child_auth_key` when calling `update_reseller_child`")  # noqa: E501
        # verify the required parameter 'reseller_child' is set
        if ('reseller_child' not in params or
                params['reseller_child'] is None):
            raise ValueError("Missing the required parameter `reseller_child` when calling `update_reseller_child`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'child_auth_key' in params:
            path_params['childAuthKey'] = params['child_auth_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reseller_child' in params:
            body_params = params['reseller_child']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api-key', 'partner-key']  # noqa: E501

        return self.api_client.call_api(
            '/reseller/children/{childAuthKey}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
