import configparser # python3

class CfgParser(object):
    def __init__(self, cfg_path):
        self.cfg_path = cfg_path
        try:
            self.config = configparser.ConfigParser()
            self.config.read(self.cfg_path) # config파일 읽기
        except Exception as e:
            print(e)
        
    @property
    def tlo_path(self):
        self._tlo_path = self.config.get('global', 'TLO_PATH')
        return self._tlo_path

    @property
    def log_path(self):
        self._log_path = self.config.get('global', 'LOG_PATH')
        return self._log_path

    @property
    def gcs_key_path(self):
        self._gcs_key_path = self.config.get('global', 'GCS_KEY_PATH')
        return self._gcs_key_path
    
class SettingParser(CfgParser):
    @property
    def time_limit(self):
        self._time_limit = self.config.get('setting', 'TIME_LIMIT')
        return self._time_limit

class UrlParser(CfgParser):
    @property
    def gcs_auth_url(self):
        self._gcs_auth_url = self.config.get('url', 'GCS_AUTH_URL')
        return self._gcs_auth_url
