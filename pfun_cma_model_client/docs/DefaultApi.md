# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**default_params_params_default_get**](DefaultApi.md#default_params_params_default_get) | **GET** /params/default | Default Params
[**demo_data_stream_demo_data_stream_get**](DefaultApi.md#demo_data_stream_demo_data_stream_get) | **GET** /demo/data-stream | Demo Data Stream
[**demo_dexcom_demo_dexcom_get**](DefaultApi.md#demo_dexcom_demo_dexcom_get) | **GET** /demo/dexcom | Demo Dexcom
[**demo_gemini_demo_gemini_get**](DefaultApi.md#demo_gemini_demo_gemini_get) | **GET** /demo/gemini | Demo Gemini
[**demo_rolling_window_demo_rolling_window_demo_get**](DefaultApi.md#demo_rolling_window_demo_rolling_window_demo_get) | **GET** /demo/rolling-window-demo | Demo Rolling Window
[**demo_run_at_time_demo_run_at_time_get**](DefaultApi.md#demo_run_at_time_demo_run_at_time_get) | **GET** /demo/run-at-time | Demo Run At Time
[**demo_webgl_demo_webgl_demo_get**](DefaultApi.md#demo_webgl_demo_webgl_demo_get) | **GET** /demo/webgl-demo | Demo Webgl
[**describe_params_params_describe_post**](DefaultApi.md#describe_params_params_describe_post) | **POST** /params/describe | Describe Params
[**fit_model_to_data_model_fit_post**](DefaultApi.md#fit_model_to_data_model_fit_post) | **POST** /model/fit | Fit Model To Data
[**get_sample_dataset_data_sample_download_get**](DefaultApi.md#get_sample_dataset_data_sample_download_get) | **GET** /data/sample/download | Get Sample Dataset
[**health_check_health_get**](DefaultApi.md#health_check_health_get) | **GET** /health | Health Check
[**health_check_run_at_time_health_ws_run_at_time_get**](DefaultApi.md#health_check_run_at_time_health_ws_run_at_time_get) | **GET** /health/ws/run-at-time | Health Check Run At Time
[**params_schema_params_schema_get**](DefaultApi.md#params_schema_params_schema_get) | **GET** /params/schema | Params Schema
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**run_at_time_route_model_run_at_time_post**](DefaultApi.md#run_at_time_route_model_run_at_time_post) | **POST** /model/run-at-time | Run At Time Route
[**run_at_time_stream_route_model_run_at_time_stream_post**](DefaultApi.md#run_at_time_stream_route_model_run_at_time_stream_post) | **POST** /model/run-at-time/stream | Run At Time Stream Route
[**run_model_model_run_post**](DefaultApi.md#run_model_model_run_post) | **POST** /model/run | Run Model
[**stream_sample_dataset_data_sample_stream_get**](DefaultApi.md#stream_sample_dataset_data_sample_stream_get) | **GET** /data/sample/stream | Stream Sample Dataset
[**tabulate_params_params_tabulate_post**](DefaultApi.md#tabulate_params_params_tabulate_post) | **POST** /params/tabulate | Tabulate Params
[**translate_model_results_by_language_translate_results_post**](DefaultApi.md#translate_model_results_by_language_translate_results_post) | **POST** /translate-results | Translate Model Results By Language


# **default_params_params_default_get**
> object default_params_params_default_get()

Default Params

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Default Params
        api_response = api_instance.default_params_params_default_get()
        print("The response of DefaultApi->default_params_params_default_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->default_params_params_default_get: %s\n" % e)
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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Demo Data Stream
        api_response = api_instance.demo_data_stream_demo_data_stream_get()
        print("The response of DefaultApi->demo_data_stream_demo_data_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->demo_data_stream_demo_data_stream_get: %s\n" % e)
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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Demo Dexcom
        api_response = api_instance.demo_dexcom_demo_dexcom_get()
        print("The response of DefaultApi->demo_dexcom_demo_dexcom_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->demo_dexcom_demo_dexcom_get: %s\n" % e)
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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Demo Gemini
        api_response = api_instance.demo_gemini_demo_gemini_get()
        print("The response of DefaultApi->demo_gemini_demo_gemini_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->demo_gemini_demo_gemini_get: %s\n" % e)
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

# **demo_rolling_window_demo_rolling_window_demo_get**
> object demo_rolling_window_demo_rolling_window_demo_get()

Demo Rolling Window

Demo UI endpoint for the Rolling Window real-time plot.

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Demo Rolling Window
        api_response = api_instance.demo_rolling_window_demo_rolling_window_demo_get()
        print("The response of DefaultApi->demo_rolling_window_demo_rolling_window_demo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->demo_rolling_window_demo_rolling_window_demo_get: %s\n" % e)
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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Demo Run At Time
        api_response = api_instance.demo_run_at_time_demo_run_at_time_get()
        print("The response of DefaultApi->demo_run_at_time_demo_run_at_time_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->demo_run_at_time_demo_run_at_time_get: %s\n" % e)
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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Demo Webgl
        api_response = api_instance.demo_webgl_demo_webgl_demo_get()
        print("The response of DefaultApi->demo_webgl_demo_webgl_demo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->demo_webgl_demo_webgl_demo_get: %s\n" % e)
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

# **describe_params_params_describe_post**
> object describe_params_params_describe_post(params)

Describe Params

Describe a given (single) or set of parameters using CMAModelParams.describe and generate_qualitative_descriptor.
Args:
    config (Optional[BoundedCMAModelParams | Mapping]): The configuration parameters to describe.
Returns:
    dict: Dictionary of parameter descriptions and qualitative descriptors.

### Example


```python
import openapi_client
from openapi_client.models.params import Params
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
    api_instance = openapi_client.DefaultApi(api_client)
    params = openapi_client.Params() # Params | 

    try:
        # Describe Params
        api_response = api_instance.describe_params_params_describe_post(params)
        print("The response of DefaultApi->describe_params_params_describe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->describe_params_params_describe_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**Params**](Params.md)|  | 

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

# **fit_model_to_data_model_fit_post**
> object fit_model_to_data_model_fit_post(body_fit_model_to_data_model_fit_post)

Fit Model To Data

### Example


```python
import openapi_client
from openapi_client.models.body_fit_model_to_data_model_fit_post import BodyFitModelToDataModelFitPost
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
    api_instance = openapi_client.DefaultApi(api_client)
    body_fit_model_to_data_model_fit_post = openapi_client.BodyFitModelToDataModelFitPost() # BodyFitModelToDataModelFitPost | 

    try:
        # Fit Model To Data
        api_response = api_instance.fit_model_to_data_model_fit_post(body_fit_model_to_data_model_fit_post)
        print("The response of DefaultApi->fit_model_to_data_model_fit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->fit_model_to_data_model_fit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_fit_model_to_data_model_fit_post** | [**BodyFitModelToDataModelFitPost**](BodyFitModelToDataModelFitPost.md)|  | 

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

# **get_sample_dataset_data_sample_download_get**
> object get_sample_dataset_data_sample_download_get(nrows=nrows)

Get Sample Dataset

(slow) Download the sample dataset with optional row limit.

Args:
    request (Request): The FastAPI request object.
    nrows (int): The number of rows to return. If -1, return the full dataset.

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
    api_instance = openapi_client.DefaultApi(api_client)
    nrows = 23 # int |  (optional) (default to 23)

    try:
        # Get Sample Dataset
        api_response = api_instance.get_sample_dataset_data_sample_download_get(nrows=nrows)
        print("The response of DefaultApi->get_sample_dataset_data_sample_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sample_dataset_data_sample_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nrows** | **int**|  | [optional] [default to 23]

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_health_get**
> object health_check_health_get()

Health Check

Health check endpoint.

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_health_get()
        print("The response of DefaultApi->health_check_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_health_get: %s\n" % e)
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

# **health_check_run_at_time_health_ws_run_at_time_get**
> object health_check_run_at_time_health_ws_run_at_time_get()

Health Check Run At Time

Health check endpoint for the 'run-at-time' WebSocket functionality.

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Health Check Run At Time
        api_response = api_instance.health_check_run_at_time_health_ws_run_at_time_get()
        print("The response of DefaultApi->health_check_run_at_time_health_ws_run_at_time_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_run_at_time_health_ws_run_at_time_get: %s\n" % e)
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

# **params_schema_params_schema_get**
> object params_schema_params_schema_get()

Params Schema

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Params Schema
        api_response = api_instance.params_schema_params_schema_get()
        print("The response of DefaultApi->params_schema_params_schema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->params_schema_params_schema_get: %s\n" % e)
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

# **root_get**
> object root_get()

Root

Root endpoint to display the homepage.

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
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root_get()
        print("The response of DefaultApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root_get: %s\n" % e)
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

# **run_at_time_route_model_run_at_time_post**
> object run_at_time_route_model_run_at_time_post(t0, t1, n, cma_model_params=cma_model_params)

Run At Time Route

Run the CMA model at a specific time.

Parameters:
- t0 (float | int): The start time (in decimal hours).
- t1 (float | int): The end time (in decimal hours).
- n (int): The number of samples.
- config (CMAModelParams): The model configuration parameters.

### Example


```python
import openapi_client
from openapi_client.models.cma_model_params import CMAModelParams
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
    api_instance = openapi_client.DefaultApi(api_client)
    t0 = openapi_client.T0() # T0 | 
    t1 = openapi_client.T1() # T1 | 
    n = 56 # int | 
    cma_model_params = openapi_client.CMAModelParams() # CMAModelParams |  (optional)

    try:
        # Run At Time Route
        api_response = api_instance.run_at_time_route_model_run_at_time_post(t0, t1, n, cma_model_params=cma_model_params)
        print("The response of DefaultApi->run_at_time_route_model_run_at_time_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_at_time_route_model_run_at_time_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t0** | [**T0**](.md)|  | 
 **t1** | [**T1**](.md)|  | 
 **n** | **int**|  | 
 **cma_model_params** | [**CMAModelParams**](CMAModelParams.md)|  | [optional] 

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

# **run_at_time_stream_route_model_run_at_time_stream_post**
> object run_at_time_stream_route_model_run_at_time_stream_post(t0, t1, n, cma_model_params=cma_model_params)

Run At Time Stream Route

Streaming version of the run-at-time route.

### Example


```python
import openapi_client
from openapi_client.models.cma_model_params import CMAModelParams
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
    api_instance = openapi_client.DefaultApi(api_client)
    t0 = openapi_client.T01() # T01 | 
    t1 = openapi_client.T11() # T11 | 
    n = 56 # int | 
    cma_model_params = openapi_client.CMAModelParams() # CMAModelParams |  (optional)

    try:
        # Run At Time Stream Route
        api_response = api_instance.run_at_time_stream_route_model_run_at_time_stream_post(t0, t1, n, cma_model_params=cma_model_params)
        print("The response of DefaultApi->run_at_time_stream_route_model_run_at_time_stream_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_at_time_stream_route_model_run_at_time_stream_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t0** | [**T01**](.md)|  | 
 **t1** | [**T11**](.md)|  | 
 **n** | **int**|  | 
 **cma_model_params** | [**CMAModelParams**](CMAModelParams.md)|  | [optional] 

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

# **run_model_model_run_post**
> object run_model_model_run_post(config=config)

Run Model

Runs the CMA model.

### Example


```python
import openapi_client
from openapi_client.models.cma_model_params import CMAModelParams
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
    api_instance = openapi_client.DefaultApi(api_client)
    config = openapi_client.CMAModelParams() # CMAModelParams |  (optional)

    try:
        # Run Model
        api_response = api_instance.run_model_model_run_post(config=config)
        print("The response of DefaultApi->run_model_model_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->run_model_model_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**CMAModelParams**](.md)|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_sample_dataset_data_sample_stream_get**
> object stream_sample_dataset_data_sample_stream_get(pct0=pct0, nrows=nrows)

Stream Sample Dataset

(fast) Stream the sample dataset with optional row limit.
Args:
    request (Request): The FastAPI request object.
    pct0 (float): The relative location to start in the dataset [0.0, 1.0].
    nrows (int): The number of rows to include in the stream. If -1, stream the full dataset.

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
    api_instance = openapi_client.DefaultApi(api_client)
    pct0 = 0.0 # float |  (optional) (default to 0.0)
    nrows = -1 # int |  (optional) (default to -1)

    try:
        # Stream Sample Dataset
        api_response = api_instance.stream_sample_dataset_data_sample_stream_get(pct0=pct0, nrows=nrows)
        print("The response of DefaultApi->stream_sample_dataset_data_sample_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stream_sample_dataset_data_sample_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pct0** | **float**|  | [optional] [default to 0.0]
 **nrows** | **int**|  | [optional] [default to -1]

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tabulate_params_params_tabulate_post**
> object tabulate_params_params_tabulate_post(params)

Tabulate Params

Generate a markdown table of a given (single) or set of parameters using CMAModelParams.generate_markdown_table.
Args:
    config (Optional[BoundedCMAModelParams | Mapping]): The configuration parameters to describe.
Returns:
    dict: Dictionary of parameter descriptions and qualitative descriptors.

### Example


```python
import openapi_client
from openapi_client.models.params import Params
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
    api_instance = openapi_client.DefaultApi(api_client)
    params = openapi_client.Params() # Params | 

    try:
        # Tabulate Params
        api_response = api_instance.tabulate_params_params_tabulate_post(params)
        print("The response of DefaultApi->tabulate_params_params_tabulate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tabulate_params_params_tabulate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**Params**](Params.md)|  | 

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

# **translate_model_results_by_language_translate_results_post**
> object translate_model_results_by_language_translate_results_post(from_lang, body)

Translate Model Results By Language

Translate model results between Python and JavaScript formats.

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
    api_instance = openapi_client.DefaultApi(api_client)
    from_lang = 'from_lang_example' # str | 
    body = None # object | 

    try:
        # Translate Model Results By Language
        api_response = api_instance.translate_model_results_by_language_translate_results_post(from_lang, body)
        print("The response of DefaultApi->translate_model_results_by_language_translate_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->translate_model_results_by_language_translate_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_lang** | **str**|  | 
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

