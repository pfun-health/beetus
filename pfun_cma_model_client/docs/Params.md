# Params


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**n** | **int** |  | [optional] [default to 1024]
**d** | **float** |  | [optional] [default to 0.0]
**taup** | **float** |  | [optional] [default to 1.0]
**taug** | **float** |  | [optional] [default to 1.0]
**b** | **float** |  | [optional] [default to 0.05]
**cm** | **float** |  | [optional] [default to 0.0]
**toff** | **float** |  | [optional] [default to 0.0]
**t_m** | **float** |  | [optional] 
**seed** | [**Seed**](Seed.md) |  | [optional] 
**eps** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.params import Params

# TODO update the JSON string below
json = "{}"
# create an instance of Params from a JSON string
params_instance = Params.from_json(json)
# print the JSON string representation of the object
print(Params.to_json())

# convert the object into a dict
params_dict = params_instance.to_dict()
# create an instance of Params from a dict
params_from_dict = Params.from_dict(params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


