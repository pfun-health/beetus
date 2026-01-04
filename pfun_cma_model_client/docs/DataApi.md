# openapi_client.DataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sample_dataset_data_sample_download_get**](DataApi.md#get_sample_dataset_data_sample_download_get) | **GET** /data/sample/download | Get Sample Dataset
[**stream_sample_dataset_data_sample_stream_get**](DataApi.md#stream_sample_dataset_data_sample_stream_get) | **GET** /data/sample/stream | Stream Sample Dataset


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
    api_instance = openapi_client.DataApi(api_client)
    nrows = 23 # int |  (optional) (default to 23)

    try:
        # Get Sample Dataset
        api_response = api_instance.get_sample_dataset_data_sample_download_get(nrows=nrows)
        print("The response of DataApi->get_sample_dataset_data_sample_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->get_sample_dataset_data_sample_download_get: %s\n" % e)
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
    api_instance = openapi_client.DataApi(api_client)
    pct0 = 0.0 # float |  (optional) (default to 0.0)
    nrows = -1 # int |  (optional) (default to -1)

    try:
        # Stream Sample Dataset
        api_response = api_instance.stream_sample_dataset_data_sample_stream_get(pct0=pct0, nrows=nrows)
        print("The response of DataApi->stream_sample_dataset_data_sample_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->stream_sample_dataset_data_sample_stream_get: %s\n" % e)
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

