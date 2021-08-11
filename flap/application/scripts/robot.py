#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#30ページもいらない説

import os
import datetime
import json

from time import sleep
from googleapiclient.discovery import build

GOOGLE_API_KEY          = "########"
CUSTOM_SEARCH_ENGINE_ID = "########"

DATA_DIR = 'data'

def makeDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def getSearchResponse(keyword):
    
    target_keyword = keyword
    
    today = datetime.datetime.today().strftime("%Y%m%d")
    timestamp = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    makeDir(DATA_DIR)

    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)

    page_limit = 3
    start_index = 1
    response = []
    for n_page in range(0, page_limit):
        try:
            sleep(1)
            response.append(service.cse().list(
                q=keyword,
                cx=CUSTOM_SEARCH_ENGINE_ID,
                lr='lang_ja',
                num=10,
                start=start_index
            ).execute())
            start_index = response[n_page].get("queries").get("nextPage")[0].get("startIndex")
        except Exception as e:
            print(e)
            break

    # レスポンスをjson形式で保存
    save_response_dir = os.path.join(DATA_DIR, 'response')
    makeDir(save_response_dir)
    out = {'snapshot_ymd': today, 'snapshot_timestamp': timestamp, 'response': []}
    out['response'] = response
    jsonstr = json.dumps(out, ensure_ascii=False)
    #with open(os.path.join(save_response_dir, 'response_' + today + '.json'), mode='w') as response_file:
        #response_file.write(jsonstr)

    #jsonのファイル名を日付からクエリにしておく        
    with open(os.path.join(save_response_dir, target_keyword + '.json'), mode='w') as response_file:
        response_file.write(jsonstr)

if __name__ == '__main__':

    target_keyword = input('検索したい語句を入力してください：')

    getSearchResponse(target_keyword)