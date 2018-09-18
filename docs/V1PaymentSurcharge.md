# V1PaymentSurcharge
> squareconnect.models.v1_payment_surcharge

### Description

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the surcharge. | [optional] 
**applied_money** | [**V1Money**](V1Money.md) | The amount of money applied to the order as a result of the surcharge. | [optional] 
**rate** | **str** | The amount of the surcharge as a percentage. The percentage is provided as a string representing the decimal equivalent of the percentage. For example, \&quot;0.7\&quot; corresponds to a 7% surcharge. Exactly one of rate or amount_money should be set. | [optional] 
**amount_money** | [**V1Money**](V1Money.md) | The amount of the surcharge as a Money object. Exactly one of rate or amount_money should be set. | [optional] 
**type** | **str** | Indicates the source of the surcharge. For example, if it was applied as an automatic gratuity for a large group. | [optional] 
**taxable** | **bool** | Indicates whether the surcharge is taxable. | [optional] 
**taxes** | [**list[V1PaymentTax]**](V1PaymentTax.md) | The list of taxes that should be applied to the surcharge. | [optional] 
**surcharge_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

