valid_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
    },
    "userId": {
      "type": "string"
    },
    "resourceId": {
      "type": "string"
    },
    "resourceName": {
        "type": "string"
    },
    "adOfferId": {
        "type": "string"
    },
    "adOfferTitle": {
        "type": "string"
    },
    "integrationCode": {
        "type": "string"
    },
    "trackingUrl": {
        "type": "string"
    },
    "status": {
        "type": "string"
    },
    "startDate": {
        "type": "string"
    },
    "endDate": {
        "oneOf": [
            {"type": "string"},
            {"type": "null"},
        ]
    },
    "createdAt": {
        "type": "string"
    },
    "active": {
        "type": "boolean"
    },
  },
  "required": ["id", "userId", "resourceId", "resourceName", "adOfferId",
               "adOfferTitle", "integrationCode", "trackingUrl", "status",
               "startDate", "endDate", "createdAt", "active"
               ]
}