mapping = {
    "name": "products",
    "fields": [
        {
            "name" : "ProductID",
            "type" : "int32"
        },
        {
            "name" : "ProductName",
            "type" : "string"
        },
        {
            "name" : "ProductBrand",
            "type" : "string"
        },
        {
            "name" : "Gender",
            "type" : "string"
        },
        {
            "name" : "Price (INR)",
            "type" : "int32"
        },
        {
            "name" : "NumImages",
            "type" : "int32"
        },
        {
            "name" : "Description",
            "type" : "string"
        },
        {
            "name" : "PrimaryColor",
            "type" : "string"
        },
        {
            "name" : "DescriptionVector",
            "type" : "float[]",
            "embed": {
              "from": [
                "Description"
              ],
              "model_config": {
                "model_name": "ts/all-MiniLM-L12-v2"
              }
            }
        }
    ]
}
