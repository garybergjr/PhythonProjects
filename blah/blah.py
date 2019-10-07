response = tb_pages.update_item(
    Key={
        'idPages': item['idPages'],
        'urlz': item['urlz']
    },
    UpdateExpression="SET var1InTable= :var1, var2InTable= :var2,var3InTable= :var3",
    ExpressionAttributeValues={
        ':var1': var1String,
        ':var2': var2StrList,
        ':var3': var3NewString
    },
    ReturnValues="UPDATED_NEW"

)
