# openapi_client.DemoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**demo_data_stream_demo_data_stream_get**](DemoApi.md#demo_data_stream_demo_data_stream_get) | **GET** /demo/data-stream | Demo Data Stream
[**demo_dexcom_demo_dexcom_get**](DemoApi.md#demo_dexcom_demo_dexcom_get) | **GET** /demo/dexcom | Demo Dexcom
[**demo_gemini_demo_gemini_get**](DemoApi.md#demo_gemini_demo_gemini_get) | **GET** /demo/gemini | Demo Gemini
[**demo_run_at_time_demo_run_at_time_get**](DemoApi.md#demo_run_at_time_demo_run_at_time_get) | **GET** /demo/run-at-time | Demo Run At Time
[**demo_webgl_demo_webgl_demo_get**](DemoApi.md#demo_webgl_demo_webgl_demo_get) | **GET** /demo/webgl-demo | Demo Webgl


# **demo_data_stream_demo_data_stream_get**
> object demo_data_stream_demo_data_stream_get()

Demo Data Stream

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
    api_instance = openapi_client.DemoApi(api_client)

    try:
        # Demo Data Stream
        api_response = api_instance.demo_data_stream_demo_data_stream_get()
        print("The response of DemoApi->demo_data_stream_demo_data_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->demo_data_stream_demo_data_stream_get: %s\n" % e)
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

# **demo_dexcom_demo_dexcom_get**
> object demo_dexcom_demo_dexcom_get()

Demo Dexcom

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
    api_instance = openapi_client.DemoApi(api_client)

    try:
        # Demo Dexcom
        api_response = api_instance.demo_dexcom_demo_dexcom_get()
        print("The response of DemoApi->demo_dexcom_demo_dexcom_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->demo_dexcom_demo_dexcom_get: %s\n" % e)
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

# **demo_gemini_demo_gemini_get**
> object demo_gemini_demo_gemini_get()

Demo Gemini

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
    api_instance = openapi_client.DemoApi(api_client)

    try:
        # Demo Gemini
        api_response = api_instance.demo_gemini_demo_gemini_get()
        print("The response of DemoApi->demo_gemini_demo_gemini_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->demo_gemini_demo_gemini_get: %s\n" % e)
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

# **demo_run_at_time_demo_run_at_time_get**
> object demo_run_at_time_demo_run_at_time_get()

Demo Run At Time

Demo UI endpoint to run the model at a specific time (using websockets).

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
    api_instance = openapi_client.DemoApi(api_client)

    try:
        # Demo Run At Time
        api_response = api_instance.demo_run_at_time_demo_run_at_time_get()
        print("The response of DemoApi->demo_run_at_time_demo_run_at_time_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->demo_run_at_time_demo_run_at_time_get: %s\n" % e)
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

# **demo_webgl_demo_webgl_demo_get**
> object demo_webgl_demo_webgl_demo_get()

Demo Webgl

Demo UI endpoint for the WebGL-based real-time plot.

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
    api_instance = openapi_client.DemoApi(api_client)

    try:
        # Demo Webgl
        api_response = api_instance.demo_webgl_demo_webgl_demo_get()
        print("The response of DemoApi->demo_webgl_demo_webgl_demo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DemoApi->demo_webgl_demo_webgl_demo_get: %s\n" % e)
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

