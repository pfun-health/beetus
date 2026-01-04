# openapi_client.LlmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_scenario_llm_generate_scenario_post**](LlmApi.md#generate_scenario_llm_generate_scenario_post) | **POST** /llm/generate-scenario | Generate Scenario
[**translate_query_to_params_llm_translate_query_post**](LlmApi.md#translate_query_to_params_llm_translate_query_post) | **POST** /llm/translate-query | Translate Query To Params


# **generate_scenario_llm_generate_scenario_post**
> object generate_scenario_llm_generate_scenario_post(prompt=prompt)

Generate Scenario

Use VertexAI LLM endpoint to generate a realistic scenario (with hypothetical parameters).

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
    api_instance = openapi_client.LlmApi(api_client)
    prompt = '''
This person is mostly healthy but occasionally eats a late dinner.
''' # str |  (optional) (default to '''
This person is mostly healthy but occasionally eats a late dinner.
''')

    try:
        # Generate Scenario
        api_response = api_instance.generate_scenario_llm_generate_scenario_post(prompt=prompt)
        print("The response of LlmApi->generate_scenario_llm_generate_scenario_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LlmApi->generate_scenario_llm_generate_scenario_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt** | **str**|  | [optional] [default to &#39;&#39;&#39;
This person is mostly healthy but occasionally eats a late dinner.
&#39;&#39;&#39;]

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

# **translate_query_to_params_llm_translate_query_post**
> object translate_query_to_params_llm_translate_query_post(prompt=prompt)

Translate Query To Params

Use gemini to translate the given scenario to a set of pfun-cma-model parameters.

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
    api_instance = openapi_client.LlmApi(api_client)
    prompt = '''
This person is mostly healthy but occasionally eats a late dinner.
''' # str |  (optional) (default to '''
This person is mostly healthy but occasionally eats a late dinner.
''')

    try:
        # Translate Query To Params
        api_response = api_instance.translate_query_to_params_llm_translate_query_post(prompt=prompt)
        print("The response of LlmApi->translate_query_to_params_llm_translate_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LlmApi->translate_query_to_params_llm_translate_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt** | **str**|  | [optional] [default to &#39;&#39;&#39;
This person is mostly healthy but occasionally eats a late dinner.
&#39;&#39;&#39;]

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

