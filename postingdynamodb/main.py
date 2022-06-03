from sets import Dynamodb,ExcelToJson

if __name__ == "__main__":
    try :

        o = ExcelToJson("MBG_products.xlsx")
        json_exl = o.getJson()
        a = Dynamodb()
        # a.create(tablename,'id')
        a.putitem(json_exl)
    
    except Exception as e1:
        print(f"Generic error as {e1}")
    