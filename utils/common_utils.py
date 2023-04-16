import json
import utils.common_variables as common_variables

STR_FILE_ENCODING = common_variables.STR_FILE_ENCODING

def load_json(str_path_json):
    
    with open(str_path_json, 'r', encoding=STR_FILE_ENCODING) as dict_json:
        str_data = json.load(dict_json)
    
    return str_data

def get_secret_settings(str_path_json):

    dict_json = load_json(str_path_json)
    
    str_naver_id = dict_json['Naver']['id']
    str_naver_password = dict_json['Naver']['password']

    dict_result = {}
    dict_result['str_naver_id'] = str_naver_id
    dict_result['str_naver_password'] = str_naver_password

    return dict_result