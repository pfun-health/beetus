# openapi_client.DexcomApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_callback_dexcom_auth_callback_get**](DexcomApi.md#auth_callback_dexcom_auth_callback_get) | **GET** /dexcom/auth/callback | Auth Callback
[**get_devices_dexcom_users_self_devices_get**](DexcomApi.md#get_devices_dexcom_users_self_devices_get) | **GET** /dexcom/users/self/devices | Get Devices
[**get_egvs_dexcom_users_self_egvs_get**](DexcomApi.md#get_egvs_dexcom_users_self_egvs_get) | **GET** /dexcom/users/self/egvs | Get Egvs
[**get_token_dexcom_token_post**](DexcomApi.md#get_token_dexcom_token_post) | **POST** /dexcom/token | Get Token
[**test_dexcom_route_dexcom_test_get**](DexcomApi.md#test_dexcom_route_dexcom_test_get) | **GET** /dexcom/test | Test Dexcom Route


# **auth_callback_dexcom_auth_callback_get**
> object auth_callback_dexcom_auth_callback_get()

Auth Callback

Dexcom authorization callback.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DexcomApi(api_client)

    try:
        # Auth Callback
        api_response = api_instance.auth_callback_dexcom_auth_callback_get()
        print("The response of DexcomApi->auth_callback_dexcom_auth_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DexcomApi->auth_callback_dexcom_auth_callback_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_dexcom_users_self_devices_get**
> object get_devices_dexcom_users_self_devices_get()

Get Devices

Proxy endpoint for fetching device data.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DexcomApi(api_client)

    try:
        # Get Devices
        api_response = api_instance.get_devices_dexcom_users_self_devices_get()
        print("The response of DexcomApi->get_devices_dexcom_users_self_devices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DexcomApi->get_devices_dexcom_users_self_devices_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_egvs_dexcom_users_self_egvs_get**
> object get_egvs_dexcom_users_self_egvs_get()

Get Egvs

Proxy endpoint for fetching EGV data.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DexcomApi(api_client)

    try:
        # Get Egvs
        api_response = api_instance.get_egvs_dexcom_users_self_egvs_get()
        print("The response of DexcomApi->get_egvs_dexcom_users_self_egvs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DexcomApi->get_egvs_dexcom_users_self_egvs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_dexcom_token_post**
> object get_token_dexcom_token_post(body)

Get Token

Exchange authorization code for an access token.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DexcomApi(api_client)
    body = None # object | 

    try:
        # Get Token
        api_response = api_instance.get_token_dexcom_token_post(body)
        print("The response of DexcomApi->get_token_dexcom_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DexcomApi->get_token_dexcom_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_dexcom_route_dexcom_test_get**
> object test_dexcom_route_dexcom_test_get()

Test Dexcom Route

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DexcomApi(api_client)

    try:
        # Test Dexcom Route
        api_response = api_instance.test_dexcom_route_dexcom_test_get()
        print("The response of DexcomApi->test_dexcom_route_dexcom_test_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DexcomApi->test_dexcom_route_dexcom_test_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

