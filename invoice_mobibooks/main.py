from sets import PostInvoiceToMobibooks
from sets import InvoiceData

if __name__ == "__main__":
    # try:
        a = InvoiceData()
        prepare_invoice =a.prepre_invoice({
        "orderline": {
        "_sa_instance_state": None,
        "start_on": "2022-05-05 00:00:00",
        "invno": None,
        "id": 4011,
        "product_id": 30,
        "finish_on": None,
        "invoice_date": None,
        "session": "B",
        "is_paused": False,
        "upd_on": "2021-12-09 13:59:18",
        "qty": 1,
        "sale_val": 350,
        "upd_by": "AppSync",
        "weight": 1,
        "taxmethod": "GST5OUTPUT",
        "package_num": "",
        "comment": "",
        "kitchen_id": 2,
        "order_id": 105,
        "subscription_id": 260
        },
        "kitchen": {
        "_sa_instance_state": None,
        "display_name": "Vibrant kitchen - Gachibowli",
        "name": "VIBRANTKITCHENGACHIBOWLI",
        "id": 2,
        "status": "A"
        },
        "subscription": {
        "_sa_instance_state": None,
        "finish_date": "2022-05-11 00:00:00",
        "id": 260,
        "customer_id": 42,
        "L_balance": 0,
        "status": "A",
        "cartitem_id": "fca70bea-0c31-42ba-aa4f-9a2828d9c046",
        "upd_on": "2021-12-09 13:59:16",
        "upd_by": "AppSync",
        "start_date": "2022-05-05 00:00:00",
        "product_id": 30,
        "B_balance": 0,
        "D_balance": 0,
        "plan_duration": None,
        "cart_id": "7fed647b-a2c3-45e6-bae2-4daaf5438edf"
        },
        "customer": {
        "_sa_instance_state": None,
        "display_name": "MG test3",
        "id": 42,
        "status": "A",
        "upd_on": "2021-11-26 13:10:10",
        "name": "MGTEST3",
        "mobile": "9876598765",
        "upd_by": "AppSync"
        },
        "weight": 1,
        "product": [
        {
        "_sa_instance_state": None,
        "name": "SALADMS",
        "sale_price": 0,
        "id": 30,
        "category": "Salads",
        "display_name": "Salad - MS",
        "status": "A",
        "qty": 1,
        "sale_val": 350,
        "uom": "NOS"
        }
        ],
        "cust_id": "42",
        "id": 16594,
        "start_date": "2022-05-05 00:00:00",
        "delivery_address": "MG test3\n room no 123\n jublie enclave\n road no1\n near htex\n Hyderabad\n Telangana\n 500034\n ",
        "is_paused": False,
        "subscription_id": 260,
        "upd_on": "2021-12-17 06:07:23",
        "upd_by": "Admin",
        "finish_date": "2021-12-17 00:00:00",
        "event_type": "PD",
        "meal_type": "B",
        "comments": "",
        "status": "S",
        "area_code": None,
        "sed_id": "f3aa2fee-3a24-42cb-b270-11a534717d2b"
        }

        )
        # print(f"invoice : {prepare_invoice}")
        b = PostInvoiceToMobibooks()
        b.consume_one_handler(prepare_invoice)

    # except Exception as e1:
    #     print(f"generic error : {e1}")