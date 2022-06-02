from sets import Dynamodb,ExcelToJson
import json

if __name__ == "__main__":
    # try :

        o = ExcelToJson("MBG_products.xlsx")
        json_exl = o.getJson()
        a = Dynamodb()
        # a.create(tablename,'id')
        a.putitem(json_exl)