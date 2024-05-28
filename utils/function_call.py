function_call = [
  {
    "type": "function",
    "function": {
      "name": "itemize_receipt",
      "description": "Itemize a receipt from an image",
      "parameters": {
        "type": "object",
        "properties": {
            "vendor": {
                "type": "string",
                "description": "Name of vendor",
            },
            "date": {
                "type": "string",
                "format": "date",
                "description": "Date of purchase",
            },
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of item",
                        },
                        "price": {
                            "type": "number",
                            "description": "Price of item",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity of item",
                        },
                        "category": {
                            "type": "string",
                            "description": "Category of item",
                            "enum": ["take-out", "meal", "groceries", "clothing", "electronics", "supplies", "other"],
                        },
                    },
                },
                "description": "List of items purchased",
            },
            "payment_method": {
                "type": "string",
                "description": "Payment method",
                "enum": ["cash", "credit", "debit", "mobile", "other"],
            },
        },
        "required": ["vendor","date","items","payment_method"],
      },
    }
  }
]