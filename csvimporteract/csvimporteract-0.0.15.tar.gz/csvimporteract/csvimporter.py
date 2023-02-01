#-*- coding: utf-8 -*-
from sqlalchemy import create_engine
import pandas as pd
import os
import csv


def stackTodb(dataFrame, dbTableName):
    print(dataFrame)
    db_connection_str = 'mysql+pymysql://root:12345@127.0.0.1:3307/stackline'
    db_connection = create_engine(db_connection_str, encoding='utf-8')
    conn = db_connection.connect()

    dataFrame.to_sql(name=dbTableName, con=db_connection, if_exists='append', index=False)
    print("finished")

# CSV Cleaning
def csv_cleaning(csvFile, csv_folder_cleaned):
    file=open(csvFile,'r', encoding='latin1')
    targetFile = csv_folder_cleaned + "\\CLEANED_" + os.path.basename(csvFile)
    target=open(targetFile,'w', encoding='latin1')
    
    for line in file:
        target.write(line[:-1].rstrip(',') + "\n")

    file.close()
    target.close()

def csvCleaner(csv_folder, csv_folder_cleaned):
    fileList = os.listdir(csv_folder)

    for i in range(len(fileList)):
        csv_cleaning(csv_folder + "\\" + fileList[i], csv_folder_cleaned)
        print(fileList[i] + " is cleaned")

# CSV Encoding
def csv_encoding(csvFile, csv_folder_encoding):
    data = pd.read_csv(csvFile, encoding='utf-8')
    data.to_csv(csv_folder_encoding + "\\ENCOD_" + os.path.basename(csvFile), encoding='utf-8-sig', index = False)

def csvEncoder(csv_folder, csv_folder_encoding):
    fileList = os.listdir(csv_folder)

    for i in range(len(fileList)):
        csv_encoding(csv_folder + "\\" + fileList[i], csv_folder_encoding)
        print(fileList[i] + " is encoded")


def commonPreprocess(dataframe):
    # brand명 기준으로 이후 6글자 추출
    dataframe['brand'] = dataframe['brand'].str.lower()
    dataframe['title'] = dataframe['title'].str.lower()
    dataframe['product_name_1'] = dataframe.apply(lambda x: x['brand'] + ' ' + ' '.join(x['title'].split(x['brand'])[1].split()[:5]) if x['brand'] in x['title'] else '', axis=1)

    return dataframe

def commonPreprocess(dataframe):
    # brand명 기준으로 이후 6글자 추출
    dataframe['brand'] = dataframe['brand'].str.lower()
    dataframe['title'] = dataframe['title'].str.lower()
    try:
        dataframe['product_name_cut'] = dataframe.apply(lambda x: x['brand'] + ' ' + ' '.join(x['title'].split(x['brand'])[1].split()[:5]) if x['brand'] in x['title'] else '', axis=1)
    except Exception:
        pass

    return dataframe

def keywordPool(csv):
    pool = pd.read_csv(csv, sep=',', engine='python', encoding='latin-1')
    column = ["brand", "string", "product_name"]
    pool.columns = column

    poolList = {}
    #중복 제거한 브랜드 리스트
    brandList = pool.drop_duplicates(['brand'])['brand'].to_list()
    for i in range(len(brandList)):
        string = pool.loc[pool['brand'] == brandList[i]]
        # 브랜드 네임 : 키워드 풀
        poolList[brandList[i]] = string['string'].to_list()

    return poolList

def titleSummaryMaker(csv):
    pool = pd.read_csv(csv, sep=',', engine='python', encoding='latin-1')
    column = ["brand", "title_summary_temp", "title_summary"]
    pool.columns = column

    return pool[['title_summary_temp', 'title_summary']]


def csvImporter(csv_folder, csv_folder_encoding, csv_folder_cleaned, db_table_name):
    column_name = ["retailer_id", "retailer_name", "retailer_sku", "upc", "model_number", "title", "brand", "category", "subcategory", "week_id", "week_ending", "units_sold", "retail_sales", "retail_price", "conversion_rate", "total_traffic", "organic_traffic"]

    fileList = os.listdir(csv_folder_cleaned)
    for i in range(len(fileList)):

        dataframe = pd.read_csv(csv_folder_cleaned + "\\" + fileList[i], sep=',', engine='c', encoding='latin1')
        dataframe.columns = column_name
        dataframe.insert(0, "file_name", fileList[i][:-4], True)

        # commonPreprocess(dataframe)
        stackTodb(dataframe, db_table_name)
        

def addPoolColumn(dataframe, keyword_pool):

    pool = keywordPool(keyword_pool)
    title_mapping = titleSummaryMaker(keyword_pool)

    #키워드 풀에서 검색 후 포함되는 문자열은 리스트로 반환
    dataframe['title_summary_temp'] = dataframe.apply(lambda x: [i for i in pool.get(x['brand'], []) if i in x['title']], axis=1)
    dataframe['title_summary_temp'] = dataframe['title_summary_temp'].apply(lambda x: x if len(x) > 0 else '')

    #리스트 안에서 문자열이 가장 긴 값 리턴
    dataframe['title_summary_temp'] = dataframe['title_summary_temp'].apply(lambda x: max(x, key=lambda y: len(y)) if x else '')

    #키워드 분류로 한번 더 매핑
    final_df = pd.merge(dataframe, title_mapping, how='left', on='title_summary_temp')

    return final_df

def csvPreprocess(csv_folder, csv_folder_cleaned, csv_folder_encoding):
    # csv 줄밀림 정제
    csvEncoder(csv_folder, csv_folder_encoding)
    csvCleaner(csv_folder, csv_folder_cleaned)
    

def csvImporter_NEW(csv_folder, csv_folder_cleaned, csv_folder_encoding, keyword_pool):
    column_name = ["retailer_id", "retailer_name", "retailer_sku", "upc", "model_number", "title", "brand", "category", "subcategory", "week_id", "week_ending", "units_sold", "retail_sales", "retail_price", "conversion_rate", "total_traffic", "organic_traffic"]
    
    # 키워드 풀 가져오기
    pool = keywordPool(keyword_pool)
    title_mapping = titleSummaryMaker(keyword_pool)

    fileList = os.listdir(csv_folder_cleaned)
    for i in range(len(fileList)):
        dataframe = pd.read_csv(csv_folder_cleaned + "\\" + fileList[i], sep=',', engine='python', encoding='latin-1')
        dataframe.columns = column_name
        
        #파일명 제일 앞단에 삽입
        dataframe.insert(0, "file_name", fileList[i][:-4], True)
        
        # csv 파일 내 브랜드, 타이틀명 소문자 변경
        dataframe['brand'] = dataframe['brand'].str.lower()
        dataframe['title'] = dataframe['title'].str.lower()

        ##### no pool
        if "Laptops" in fileList[i]:
            db_table_name = 'tb_stackline_laptops'
            # commonPreprocess(dataframe)
            stackTodb(dataframe, db_table_name)

        if "Earbud" in fileList[i]:
            db_table_name = 'tb_stackline_earbuds'
            # commonPreprocess(dataframe)
            stackTodb(dataframe, db_table_name)

        ##### pool
        if "Watches" in fileList[i]:
            db_table_name = 'tb_stackline_watches'
            stackTodb(addPoolColumn(db_table_name), db_table_name)

        if "Tablets" in fileList[i]:
            db_table_name = 'tb_stackline_tablets'
            stackTodb(addPoolColumn(db_table_name), db_table_name)

        if "Phones" in fileList[i]:
            db_table_name = 'tb_stackline_smartphones'
            stackTodb(addPoolColumn(db_table_name), db_table_name)


def keywordCheck(csv_folder, csv_folder_cleaned, csv_folder_encoding, pool_check_folder, keyword_pool):
    column_name = ["retailer_id", "retailer_name", "retailer_sku", "upc", "model_number", "title", "brand", "category", "subcategory", "week_id", "week_ending", "units_sold", "retail_sales", "retail_price", "conversion_rate", "total_traffic", "organic_traffic"]

    # 키워드 풀 가져오기
    pool = keywordPool(keyword_pool)
    title_mapping = titleSummaryMaker(keyword_pool)

    fileList = os.listdir(csv_folder_cleaned)
    for i in range(len(fileList)):
        dataframe = pd.read_csv(csv_folder_cleaned + "\\" + fileList[i], sep=',', engine='c', encoding='latin-1')
        dataframe.columns = column_name
        
        #파일명 제일 앞단에 삽입
        dataframe.insert(0, "file_name", fileList[i][:-4], True)

        # csv 파일 내 브랜드, 타이틀명 소문자 변경
        dataframe['brand'] = dataframe['brand'].str.lower()
        dataframe['title'] = dataframe['title'].str.lower()

        # sales unit / retail sales 컬럼 추가
        check_frame = dataframe[['brand', 'title', 'units_sold', 'retail_sales']].groupby(by=['brand', 'title'], as_index=False).sum()

        # 키워드 풀과 겹치는 스트링 반환 
        check_frame['title_summary_list'] = check_frame.apply(lambda x: [i for i in pool.get(x['brand'], []) if i in x['title']], axis=1)
        check_frame['title_summary_list'] = check_frame['title_summary_list'].apply(lambda x: x if len(x) > 0 else '')
             
        # 리스트 중 가장 문자열이 긴 값 리턴
        check_frame['title_summary_temp'] = check_frame['title_summary_list'].apply(lambda x: max(x, key=lambda y: len(y)) if x else '')
        
        #키워드 분류로 한번 더 매핑
        final_df = pd.merge(check_frame, title_mapping, how='left', on='title_summary_temp')

        #pool 폴더로 검수용 파일 반환
        final_df.to_csv(pool_check_folder + "\\Keyword_Check_" + fileList[i], sep=',', na_rep='', encoding='utf-8-sig', index = False)
        print(fileList[i] + "is created")


# if __name__ == "__main__":
# #     db_table_name = 'tb_stackline_dataset'
#     csv_folder = "csvFolder"
#     csv_folder_cleaned = "csvFolder_cleaned"
#     keyword_pool = "csvimporteract\\tablet_phone_pool.csv"
     
# #     csvImporter(csv_folder, csv_folder_cleaned, db_table_name)

#     csvImporter_NEW(csv_folder, csv_folder_cleaned, keyword_pool)