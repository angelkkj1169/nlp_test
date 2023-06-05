from google.oauth2 import service_account
from google.cloud import storage
from properties.cfg_parser import CfgParser
from properties.cfg_parser import UrlParser
import os

PRJ_ROOT = os.path.abspath(os.path.join(__file__, '..', '..'))
cfg = CfgParser(os.path.join(PRJ_ROOT, 'properties', 'config.cfg'))
url_cfg = UrlParser(os.path.join(PRJ_ROOT, 'properties', 'config.cfg'))

def getGCSClient():  
    # 서비스 계정 키의 파일 경로 설정
    key_path = cfg.gcs_key_path
    
    # 인증
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=[url_cfg.gcs_auth_url]
    )
    
    # # Access Token 생성
    # request = Request()
    # credentials.refresh(request)
    # access_token = credentials.token
    
    # Google Cloud Storage 클라이언트 생성
    client = storage.Client(credentials=credentials)
                                        
    return client