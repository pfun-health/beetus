# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fit_model_to_data_model_fit_post**](DefaultApi.md#fit_model_to_data_model_fit_post) | **POST** /model/fit | Fit Model To Data
[**health_check_health_get**](DefaultApi.md#health_check_health_get) | **GET** /health | Health Check
[**health_check_run_at_time_health_ws_run_at_time_get**](DefaultApi.md#health_check_run_at_time_health_ws_run_at_time_get) | **GET** /health/ws/run-at-time | Health Check Run At Time
[**root_get**](DefaultApi.md#root_get) | **GET** / | Root
[**run_at_time_route_model_run_at_time_post**](DefaultApi.md#run_at_time_route_model_run_at_time_post) | **POST** /model/run-at-time | Run At Time Route
[**run_at_time_stream_route_model_run_at_time_stream_post**](DefaultApi.md#run_at_time_stream_route_model_run_at_time_stream_post) | **POST** /model/run-at-time/stream | Run At Time Stream Route
[**run_model_model_run_post**](DefaultApi.md#run_model_model_run_post) | **POST** /model/run | Run Model


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

