from sets import Dynamodb,ExcelToJson
import json

if __name__ == "__main__":
    # try :

        o = ExcelToJson("MBG_products.xlsx")
        json_exl = o.getJson()
        for dict in json_exl:
            print(dict['variants'])

        # a = Dynamodb()
        # tablename = 'service_table'
        # # a.create(tablename ,'id')
        # print(f"status code after posting data on dynamodb table : {a.putitem(tablename,json_exl )}")
        # a.putitem(tablename,list_dict )

    # except Exception as e1:
    #     print(f"generic error: {e1}")