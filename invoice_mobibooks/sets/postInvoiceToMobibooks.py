
# import uuid
import os
from .mobibooks import Mobibooks
from .booksexceptions import BooksException
# from datetime import datetime

class PostInvoiceToMobibooks:

    def __init__(self):
        self.loc = os.environ.get('MOBI_LOCATION')
        self.user = os.environ.get('MOBI_USER')
        self.password = os.environ.get('MOBI_PASSWORD')
        self.host = os.environ.get('MOBI_HOST')
        self.cust = os.environ.get('MOBI_CUSTOMER')
        
    def consume_one_handler(self,invoice=None):
        """takes None, returns connection
        py:function::

        Args:
            None

        Returns:
            a.login(connection): connection established after operation
        """
        # connect to mobibibooks
        # print('connect to mobibooks')
        # print(f"(location:{self.loc},user: {self.user},paswsord: {self.password}, host: {self.host},customer : {self.cust})")
        obj = Mobibooks(self.host,self.user,self.password,self.loc,self.cust)

        # login
        obj.login()
        print(f"session created")
        
        #for inv in invoice:
            # post and print Invoice
        print('----BEFORE POSTING AN INVOICE-----')
        # print(inv)
        resp = obj.post('invoice/',invoice,'inv')
        print('invoice_response-{}'.format(resp))
        return resp
        # if 'id' in resp:
        #     unique_key = str(uuid.uuid4())
        #     print_inv = {"unique_key":unique_key,"manualid":"VI-"+datetime.now().strftime("%m/%d/%Y%H:%M:%S")}
        #     print_resp = o.post('invoice/{}/printInvoice/'.format(resp['id']),print_inv,'inv')
        #     print('Print_invoice_response-{}'.format(print_resp))
        #     return print_resp
    
                #download inovice url : http://139.59.3.114/act/inv/invoice/downloadinvoice/?v_id=372944115&tx_type=IV&is_browser=1
