import os
import time
from properties.cfg_parser import CfgParser, UrlParser
from datetime import datetime
from pytz import timezone

PRJ_ROOT = os.path.abspath(os.path.join(__file__, '..', '..'))
cfg = CfgParser(os.path.join(PRJ_ROOT, 'properties', 'config.cfg'))
url_cfg = UrlParser(os.path.join(PRJ_ROOT, 'properties', 'config.cfg'))

# 당일 service로그 파일 생성
def create_slog_file():   
    log_path = PRJ_ROOT + cfg.log_path + 'nlc.' + str(datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d")) + '.log'
    with open(log_path, 'w'):
        pass

# 당일 날짜를 폴더명으로 통합통계 폴더 생성
def create_folder_job():
    tlo_path = cfg.tlo_path
    abs_path = PRJ_ROOT + os.path.join(tlo_path, str(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d")))
    
    if not os.path.isdir(abs_path):
        try:
            os.makedirs(abs_path, 0o777) # drwxrwxrwx--모든권한 부여
        except:
            pass

# 통합통계 로그 5분마다 생성
def create_log_file():
    tlo_path = cfg.tlo_path
    dir_path = PRJ_ROOT + os.path.join(tlo_path, str(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d")))

    per_min = divmod(int(datetime.now(timezone('Asia/Seoul')).strftime("%M")), 5)
    if per_min[1] == 0:
        current_min = "%02d" % int(datetime.now(timezone('Asia/Seoul')).strftime("%M"))
        if current_min == 5:
            current_min = '05'
    else:
        current_min = per_min[0] * 5 + 5
        if current_min == 60:
            current_min = '00'
            time.sleep(10) # 로그생성이 59분에 되어 10초 휴면
        if len(str(current_min)) == 1:
            current_min = '0' + str(current_min)

    logfile_name = str('nlc.' + 'tlo.' + datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H")) + str(current_min) + '.log' 
    abs_path = PRJ_ROOT + os.path.join(tlo_path, str(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d")), logfile_name)
  
    if not os.path.isdir(dir_path):
        try:
            os.makedirs(dir_path, 0o777) # drwxrwxrwx--모든권한 부여
        except:
            pass

    with open(abs_path, 'w'):
        pass

