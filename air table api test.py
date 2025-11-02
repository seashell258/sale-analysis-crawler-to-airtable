
import requests
import pandas as pd
import json

def create_headers():
    headers = {
    'Authorization': 'Bearer ' + str(personal_access_token),
    'Content-Type': 'application/json',
    }
    return headers


base_table_api_url = 'https://api.airtable.com/v0/{}/{}'.format(base_id, table_id)

# 列出全部資料
headers = create_headers()
response = requests.get(base_table_api_url, headers=headers)
#print(response.content)

import requests
import pandas as pd
import json

#獲取每一行資料的id
headers = create_headers()
response = requests.get(base_table_api_url, headers=headers)
table_record_ids = []
for i in response.json().get('records'):
    id = i.get('id')
    table_record_ids.append(id)

#print(table_record_ids)

#刪除全部資料
for record in table_record_ids:
    response = requests.delete(base_table_api_url + '/' + record, headers=headers)
    #print(response)


# 讀"xlsx" 然後上傳。 但不會自動把xlsx資料的欄位名稱與airtable的欄位名稱配對。
#所以現在要自己去airtable裡面設定好資料的欄位名稱。 

df = pd.read_excel("cerebro_result.9999.xlsx")
result = df.to_json(orient="records")
parsed = json.loads(result)


for i in parsed:
    temp_json = {'fields' : i}
    records = [temp_json]
    data = {'records' : records}
    response = requests.post(base_table_api_url, headers=headers, json=data)
    print(response.content)


