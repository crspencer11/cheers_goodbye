import requests

class Orders:
    def __init__(self, restaurant_id, token):
        self.base_url = "https://toast-api-server/orders/v2"
        self.headers = {
            "Toast-Restaurant-External-ID": restaurant_id,
            "Authorization": f"Bearer {token}"
        }

    def fetch_orders_bulk(self, business_date, start_date, end_date, page=0, page_size=0):
        url = f"{self.base_url}/ordersBulk"
        query = {
            "businessDate": business_date,
            "startDate": start_date,
            "endDate": end_date,
            "page": str(page),
            "pageSize": str(page_size)
        }
        response = requests.get(url, headers=self.headers, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# example response from bulk order call
"""
[
  {
    "guid": "string",
    "entityType": "string",
    "externalId": "string",
    "openedDate": "2019-08-24T14:15:22Z",
    "modifiedDate": "2019-08-24T14:15:22Z",
    "promisedDate": "2019-08-24T14:15:22Z",
    "diningOption": {
      "guid": "string",
      "entityType": "string",
      "externalId": "string"
    },
    "checks": [
      {
        "guid": "string",
        "entityType": "string",
        "externalId": "string",
        "createdDate": "2019-08-24T14:15:22Z",
        "openedDate": "2019-08-24T14:15:22Z",
        "closedDate": "2019-08-24T14:15:22Z",
        "modifiedDate": "2019-08-24T14:15:22Z",
        "deletedDate": "2019-08-24T14:15:22Z",
        "deleted": true,
        "selections": [
          {
            "guid": "string",
            "entityType": "string",
            "externalId": "string",
            "item": {
              "guid": "string",
              "entityType": "string",
              "multiLocationId": "string",
              "externalId": "string"
            },
            "itemGroup": {
              "guid": "string",
              "entityType": "string",
              "multiLocationId": "string",
              "externalId": "string"
            },
            "optionGroup": {
              "guid": "string",
              "entityType": "string",
              "multiLocationId": "string",
              "externalId": "string"
            },
            "preModifier": {
              "guid": "string",
              "entityType": "string",
              "multiLocationId": "string",
              "externalId": "string"
            },
            "quantity": 0,
            "seatNumber": 0,
            "unitOfMeasure": "NONE",
            "selectionType": "NONE",
            "salesCategory": {
              "guid": "string",
              "entityType": "string",
              "multiLocationId": "string",
              "externalId": "string"
            },
            "appliedDiscounts": [
              {
                "guid": null,
                "entityType": null,
                "externalId": null,
                "name": null,
                "discountAmount": null,
                "nonTaxDiscountAmount": null,
                "discount": null,
                "triggers": [],
                "approver": null,
                "processingState": null,
                "appliedDiscountReason": null,
                "loyaltyDetails": null,
                "comboItems": [],
                "appliedPromoCode": null,
                "discountType": null,
                "discountPercent": null
              }
            ],
            "deferred": true,
            "preDiscountPrice": 0,
            "price": 0,
            "tax": 0,
            "voided": true,
            "voidDate": "2019-08-24T14:15:22Z",
            "voidBusinessDate": 0,
            "voidReason": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "refundDetails": {
              "refundAmount": 0,
              "taxRefundAmount": 0,
              "refundTransaction": {
                "guid": null,
                "entityType": null
              }
            },
            "displayName": "string",
            "createdDate": "2019-08-24T14:15:22Z",
            "modifiedDate": "2019-08-24T14:15:22Z",
            "modifiers": [
              {}
            ],
            "fulfillmentStatus": "NEW",
            "taxInclusion": "INCLUDED",
            "appliedTaxes": [
              {
                "guid": null,
                "entityType": null,
                "taxRate": null,
                "name": null,
                "rate": null,
                "taxAmount": null,
                "type": null,
                "facilitatorCollectAndRemitTax": null,
                "displayName": null,
                "jurisdiction": null,
                "jurisdictionType": null
              }
            ],
            "diningOption": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "openPriceAmount": 0,
            "receiptLinePrice": 0,
            "optionGroupPricingMode": "INCLUDED",
            "externalPriceAmount": 0
          }
        ],
        "customer": {
          "guid": "string",
          "entityType": "string",
          "firstName": "string",
          "lastName": "string",
          "phone": "string",
          "phoneCountryCode": "string",
          "email": "string"
        },
        "appliedLoyaltyInfo": {
          "guid": "string",
          "entityType": "string",
          "loyaltyIdentifier": "string",
          "maskedLoyaltyIdentifier": "string",
          "vendor": "TOAST",
          "accrualFamilyGuid": "string",
          "accrualText": "string"
        },
        "taxExempt": false,
        "displayNumber": "string",
        "appliedServiceCharges": [
          {
            "guid": "string",
            "entityType": "string",
            "externalId": "string",
            "chargeAmount": 0,
            "serviceCharge": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "chargeType": "FIXED",
            "name": "string",
            "delivery": true,
            "takeout": true,
            "dineIn": true,
            "gratuity": true,
            "taxable": true,
            "appliedTaxes": [
              {
                "guid": null,
                "entityType": null,
                "taxRate": null,
                "name": null,
                "rate": null,
                "taxAmount": null,
                "type": null,
                "facilitatorCollectAndRemitTax": null,
                "displayName": null,
                "jurisdiction": null,
                "jurisdictionType": null
              }
            ],
            "serviceChargeCalculation": "PRE_DISCOUNT",
            "refundDetails": {
              "refundAmount": 0,
              "taxRefundAmount": 0,
              "refundTransaction": {
                "guid": null,
                "entityType": null
              }
            },
            "serviceChargeCategory": "SERVICE_CHARGE",
            "paymentGuid": "string"
          }
        ],
        "amount": 0,
        "taxAmount": 0,
        "totalAmount": 0,
        "payments": [
          {
            "guid": "string",
            "entityType": "string",
            "externalId": "string",
            "paidDate": "2019-08-24T14:15:22Z",
            "paidBusinessDate": 0,
            "type": "CASH",
            "cardEntryMode": "SWIPED",
            "amount": 0,
            "tipAmount": 0,
            "amountTendered": 0,
            "cardType": "VISA",
            "last4Digits": "string",
            "originalProcessingFee": 0,
            "server": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "cashDrawer": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "refundStatus": "NONE",
            "refund": {
              "refundAmount": 0,
              "tipRefundAmount": 0,
              "refundDate": "2019-08-24T14:15:22Z",
              "refundBusinessDate": 0,
              "refundTransaction": {
                "guid": null,
                "entityType": null
              }
            },
            "paymentStatus": "OPEN",
            "voidInfo": {
              "voidUser": {
                "guid": null,
                "entityType": null,
                "externalId": null
              },
              "voidApprover": {
                "guid": null,
                "entityType": null,
                "externalId": null
              },
              "voidDate": "2019-08-24T14:15:22Z",
              "voidBusinessDate": 0,
              "voidReason": {
                "guid": null,
                "entityType": null,
                "externalId": null
              }
            },
            "houseAccount": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "otherPayment": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "createdDevice": {
              "id": "string"
            },
            "lastModifiedDevice": {
              "id": "string"
            },
            "mcaRepaymentAmount": 0,
            "cardPaymentId": "string",
            "orderGuid": "string",
            "checkGuid": "string",
            "tenderTransactionGuid": "string"
          }
        ],
        "tabName": "string",
        "paymentStatus": "OPEN",
        "appliedDiscounts": [
          {
            "guid": "string",
            "entityType": "string",
            "externalId": "string",
            "name": "string",
            "discountAmount": 0,
            "nonTaxDiscountAmount": 0,
            "discount": {
              "guid": "string",
              "entityType": "string"
            },
            "triggers": [
              {
                "selection": null,
                "quantity": null
              }
            ],
            "approver": {
              "guid": "string",
              "entityType": "string",
              "externalId": "string"
            },
            "processingState": "PENDING_APPLIED",
            "appliedDiscountReason": {
              "name": "string",
              "description": "string",
              "comment": "string",
              "discountReason": {
                "guid": null,
                "entityType": null
              }
            },
            "loyaltyDetails": {
              "vendor": "TOAST",
              "referenceId": "string"
            },
            "comboItems": [
              {
                "guid": null,
                "entityType": null,
                "externalId": null
              }
            ],
            "appliedPromoCode": "string",
            "discountType": "BOGO",
            "discountPercent": 0
          }
        ],
        "voided": true,
        "voidDate": "2019-08-24T14:15:22Z",
        "voidBusinessDate": 0,
        "paidDate": "2019-08-24T14:15:22Z",
        "createdDevice": {
          "id": "string"
        },
        "lastModifiedDevice": {
          "id": "string"
        },
        "duration": 0
      }
    ],
    "table": {
      "guid": "string",
      "entityType": "string",
      "externalId": "string"
    },
    "serviceArea": {
      "guid": "string",
      "entityType": "string",
      "externalId": "string"
    },
    "restaurantService": {
      "guid": "string",
      "entityType": "string",
      "externalId": "string"
    },
    "revenueCenter": {
      "guid": "string",
      "entityType": "string",
      "externalId": "string"
    },
    "source": "string",
    "duration": 0,
    "deliveryInfo": {
      "address1": "string",
      "address2": "string",
      "city": "string",
      "administrativeArea": "string",
      "state": "string",
      "zipCode": "string",
      "country": "string",
      "latitude": 0,
      "longitude": 0,
      "notes": "string",
      "deliveredDate": "2019-08-24T14:15:22Z",
      "dispatchedDate": "2019-08-24T14:15:22Z",
      "deliveryEmployee": {
        "guid": "string",
        "entityType": "string",
        "externalId": "string"
      },
      "deliveryState": "PENDING"
    },
    "requiredPrepTime": "string",
    "estimatedFulfillmentDate": "2019-08-24T14:15:22Z",
    "numberOfGuests": 0,
    "voided": true,
    "voidDate": "2019-08-24T14:15:22Z",
    "voidBusinessDate": 0,
    "paidDate": "2019-08-24T14:15:22Z",
    "closedDate": "2019-08-24T14:15:22Z",
    "deletedDate": "2019-08-24T14:15:22Z",
    "deleted": true,
    "businessDate": 0,
    "server": {
      "guid": "string",
      "entityType": "string",
      "externalId": "string"
    },
    "pricingFeatures": [
      "TAXESV2"
    ],
    "approvalStatus": "NEEDS_APPROVAL",
    "guestOrderStatus": "string",
    "createdDevice": {
      "id": "string"
    },
    "createdDate": "2019-08-24T14:15:22Z",
    "initialDate": 0,
    "lastModifiedDevice": {
      "id": "string"
    },
    "curbsidePickupInfo": {
      "guid": "string",
      "entityType": "string",
      "transportColor": "string",
      "transportDescription": "string",
      "notes": "string"
    },
    "deliveryServiceInfo": {
      "guid": "string",
      "entityType": "string",
      "providerId": "string",
      "providerName": "string",
      "driverName": "string",
      "driverPhoneNumber": "string",
      "providerInfo": "string",
      "originalQuotedDeliveryDate": "string"
    },
    "marketplaceFacilitatorTaxInfo": {
      "facilitatorCollectAndRemitTaxOrder": true,
      "taxes": [
        {
          "guid": "string",
          "entityType": "string",
          "taxRate": {
            "guid": "string",
            "entityType": "string"
          },
          "name": "string",
          "rate": 0,
          "taxAmount": 0,
          "type": "PERCENT",
          "facilitatorCollectAndRemitTax": true,
          "displayName": "string",
          "jurisdiction": "string",
          "jurisdictionType": "string"
        }
      ]
    },
    "createdInTestMode": true,
    "appliedPackagingInfo": {
      "guid": "string",
      "entityType": "string",
      "appliedPackagingItems": [
        {
          "guid": "string",
          "entityType": "string",
          "itemConfigId": "string",
          "inclusion": "YES",
          "itemTypes": [
            "string"
          ],
          "guestDisplayName": "string"
        }
      ]
    },
    "excessFood": true,
    "displayNumber": "string"
  }
]
"""
