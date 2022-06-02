from sets import Dynamodb,ExcelToJson
import json

if __name__ == "__main__":
    # try :

        o = ExcelToJson("MBG_products.xlsx")
        json_exl = o.getJson()
        tablename = 'service_table'
        a = Dynamodb()
        # a.create(tablename,'id')
        a.putitem(tablename,json_exl)