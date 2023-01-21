import csv,json
from xml.dom import minidom
import random
from decimal import Decimal
from faker import Faker
import string 
import datetime 
import time
import pandas as pd

RECORD_COUNT = 100000
fake = Faker()
response=[]

def create_json_file(response):
    with open('data.json', 'w') as fp: 
        json.dump(response, fp, indent=4,default=str) 
        
def create_csv_file(response):
    df = pd.DataFrame(response)  
    df.to_csv('data.csv',index=False) 

def gen_name_gender_email():
   gender = 'M' if random.randint(0,1) == 0 else 'F'
   first = fake.first_name_male() if gender=='M' else fake.first_name_female()
   last = fake.last_name()
   full= first +' '+last 
   email=fake.email()
   return {'gender':gender,'first_name':first,'last_name':first,'full_name':full,'email':email}

# Random Date
def gen_date(p_startyear=None,p_format=None):
    l_startyear = 1980
    l_format="%m/%d/%Y"
    if p_startyear:
        l_startyear=p_startyear
    if p_format:
        l_format = p_format
    sd=fake.date_between_dates(date_start=datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d"), date_end=datetime.datetime.now())
    return sd.strftime(l_format)

def get_phone():
    return fake.phone_number() 


def get_int(p_precision=None):
    if p_precision:
        return random.randint(int('1'+'0'*(p_precision-1)),int('9'*p_precision))
    else:
        return random.randint(0,10)
gid=None
def get_int_seq(start_seq):
    global gid
    if gid:
        pass
    else:
        gid=start_seq-1        
    gid+=1
    return gid


def get_decimal(p_precision=None):
    if p_precision:
        return str(get_int(int(str(p_precision)[0:str(p_precision).find('.')]))) +'.'+ str(get_int(int(str(p_precision)[int(str(p_precision).find('.'))+1:])))

def random_datetime(p_startyear=None):
    l_startyear=1980
    if p_startyear:
        l_startyear=p_startyear
    return datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d") + datetime.timedelta(
        seconds=random.randint(0, int((datetime.datetime.now() - datetime.datetime.strptime(str(l_startyear)+"-01-01", "%Y-%m-%d")).total_seconds())),
    )

def random_timestamp():
    return random_datetime().strftime("%H:%M:%S:")+str(random.randint(100000,999999))

def get_ssn():
    return fake.ssn()

def get_credit_score(start_seq=None):
    return random.randint(100,800)

# def get_loan_amount(start_seq=None):
#     return random.randint(10000,30000)

def get_loan_amount(p_precision=None):
    if p_precision ==None:
        p_precision=2
    return round(random.uniform(10000.00,30000.00),p_precision)

def create_data(col_info, output_format=None, output_style=None):
    header=[]
    data=[]
    for c in range(1000):
        row={}
        for column in col_info:
            if column['field_descriptor'][0]=='first_name' or column['field_descriptor'][0]=='last_name' or column['field_descriptor'][0]=='gender'or column['field_descriptor'][0]=='full_name':
                row[column['col']]=gen_name_gender_email()[column['field_descriptor'][0]]
            elif column['field_descriptor'][1]:
                a= column['field_descriptor'][0](column['field_descriptor'][1])
                row[column['col']]=a
            else:
                a= column['field_descriptor'][0]()
                row[column['col']]=a
        data.append(row)
    return data


array=[
    #    {'col':'customer_first_name','field_descriptor':['first_name',None]},
    #    {'col':'customer_last_name','field_descriptor':['last_name',None]},
       {'col':'customer_id','field_descriptor':[get_int_seq,1]},
       {'col':'customer_name','field_descriptor':['full_name',None]},
    #    {'col':'gender','field_descriptor':['gender',None]},
       {'col':'application_date','field_descriptor':[gen_date,2022]},       
       {'col':'customer_creditscore','field_descriptor':[get_credit_score,1]},
       {'col':'customer_req_loanamount','field_descriptor':[get_loan_amount,2]}]
output=['json','csv']
data=create_data(array)
print(type(data))
# print(json.dumps(data,indent=4))
create_json_file(data)
create_csv_file(data)