# openapi_client.ParamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**default_params_params_default_get**](ParamsApi.md#default_params_params_default_get) | **GET** /params/default | Default Params
[**describe_params_params_describe_post**](ParamsApi.md#describe_params_params_describe_post) | **POST** /params/describe | Describe Params
[**params_schema_params_schema_get**](ParamsApi.md#params_schema_params_schema_get) | **GET** /params/schema | Params Schema
[**tabulate_params_params_tabulate_post**](ParamsApi.md#tabulate_params_params_tabulate_post) | **POST** /params/tabulate | Tabulate Params


# **default_params_params_default_get**
> object default_params_params_default_get()

Default Params

Get the default model parameters.

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
    api_instance = openapi_client.ParamsApi(api_client)

    try:
        # Default Params
        api_response = api_instance.default_params_params_default_get()
        print("The response of ParamsApi->default_params_params_default_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParamsApi->default_params_params_default_get: %s\n" % e)
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
    params (CMAModelParams | Mapping[str, Any]): The configuration parameters to describe.
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
    api_instance = openapi_client.ParamsApi(api_client)
    params = openapi_client.Params() # Params | 

    try:
        # Describe Params
        api_response = api_instance.describe_params_params_describe_post(params)
        print("The response of ParamsApi->describe_params_params_describe_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParamsApi->describe_params_params_describe_post: %s\n" % e)
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

# **params_schema_params_schema_get**
> object params_schema_params_schema_get()

Params Schema

Get the JSON schema for the model parameters.

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
    api_instance = openapi_client.ParamsApi(api_client)

    try:
        # Params Schema
        api_response = api_instance.params_schema_params_schema_get()
        print("The response of ParamsApi->params_schema_params_schema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParamsApi->params_schema_params_schema_get: %s\n" % e)
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

# **tabulate_params_params_tabulate_post**
> object tabulate_params_params_tabulate_post(params)

Tabulate Params

Generate a markdown table of a given (single) or set of parameters.

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
    api_instance = openapi_client.ParamsApi(api_client)
    params = openapi_client.Params() # Params | 

    try:
        # Tabulate Params
        api_response = api_instance.tabulate_params_params_tabulate_post(params)
        print("The response of ParamsApi->tabulate_params_params_tabulate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParamsApi->tabulate_params_params_tabulate_post: %s\n" % e)
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

