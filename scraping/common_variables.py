import utils.common_utils as common_utils
import utils.common_variables as common_variables

STR_PATH_SECRET = common_variables.STR_PATH_SECRET

dict_secrets = common_utils.get_secret_settings(STR_PATH_SECRET)

STR_NAVER_ID = dict_secrets['str_naver_id']
STR_NAVER_PASSWORD = dict_secrets['str_naver_password']