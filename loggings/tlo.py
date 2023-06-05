import re, os
import time, math, datetime
from datetime import datetime
from pytz import timezone

# microtime값을 11자리로 잘라 역수를 구함.
# @return: string
def seq_id():
    uniq_mc = '%f%d' % math.modf(time.time())
    uniq_seq = uniq_mc[2:10]
    tmp_seq = '%.3f' % round(float(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S.%f")), 4)
    seq_id = tmp_seq.replace('.', '') + uniq_seq[::-1]
    return seq_id

def get_request_time():
    tmp_request = a = '%.3f' % round(float(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S.%f")), 4)
    return tmp_request.replace('.', '')

def get_logtime():
    return str(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S"))

def get_nlc_time():
    return str(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H%M%S"))

def get_tlo_log_name():
    per_min = divmod(int(datetime.now(timezone('Asia/Seoul')).strftime("%M")), 5)
    if per_min[1] == 0:
        current_min = "%02d" % int(datetime.now(timezone('Asia/Seoul')).strftime("%M"))
        if current_min == 5:
            current_min = '05'
    else:
        current_min = per_min[0] * 5
        if current_min == 0:
            current_min = '00'
        if len(str(current_min)) == 1:
            current_min = '0' + str(current_min)

    logfile_name = str('nlc.' + 'tlo.' + datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d%H")) + str(current_min) + '.log'
    return logfile_name

def get_tlo_path(tlo_path):
    abs_path = os.path.join(tlo_path, str(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d")))

    if not os.path.isdir(abs_path):
        try:
            os.makedirs(abs_path, 0o777) # drwxrwxrwx--모든권한 부여
        except:
            pass
    return abs_path

class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance

class Tlo(metaclass=SingletonType):        
    # SEQ_ID=%(seq_id)s|LOG_TIME=%(asctime)s|REQ_TIME=%(asctime)s|LOG_TYPE=SVVC|MIN=null|
    def __init__(self):
        seq_id = ""
        self._log_time = "LOG_TIME=|"
        self._log_type = "LOG_TYPE=SVC|"
        self._sid = "SID=|"
        self._result_code = "RESULT_CODE=|"
        self._req_time = "REQ_TIME=|"
        self._rsp_time = "RSP_TIME=|"
        self._client_ip = "CLIENT_IP=|"
        self._dev_info = "DEV_INFO=|"
        self._os_info = "OS_INFO=|"
        self._nw_info = "NW_INFO=|"
        self._svc_name = "SVC_NAME=CHAT|"
        self._dev_model = "DEV_MODEL=|"
        self._carrier_type = "CARRIER_TYPE=|"
        self._session_id = "SESSION_ID|"
        self._talk_id = "TALK_ID=|"
        self._req_url = "REQ_URL=|"
        self._search_type = "SEARCH_TYPE=|"
        self._query = "QUERY=|"
        self._trid = "TRID=|"
        self._nlc_req_time = "NLC_REQ_TIME=|"
        self._nlc_rsp_time = "NLC_RSP_TIME=|"
        self._nlc_rsp = "NLC_RSP=|"
        self._svr_type = "SVR_TYPE=|" 
        self._nlc_result = "NLC_RESULT=|"
        self._nlc_text = "NLC_TEXT=|"
        self._r1 = "R1=|"
        self._r2 = "R2=|"
        self._r3 = "R3=|"
        self._r4 = "R4=|"
        self._r5 = "R5="

    def set_tlo_messages(self, argv):
        for field, value in argv.items():
            setter = 'self.' + field + ' = \'' + str(value) + '\''
            exec(setter) # 문자열로 표현된 문을 인수로 받아 파이썬 컴파일 코드로 변환

    def get_tlo_messages(self):
        self.rsp_time = get_request_time()
        tlo_message = self.seq_id + self.log_time + self.log_type + self.sid + self.result_code + self.req_time + self.rsp_time \
        + self.client_ip + self.dev_info + self.os_info + self.nw_info + self.svc_name + self.dev_model + self.carrier_type + self.session_id \
        + self.talk_id + self.req_url + self.search_type + self.query + self.trid + self.nlc_req_time + self.nlc_rsp_time \
        + self.nlc_rsp + self.svr_type + self.nlc_result + self.nlc_text \
        + self.r1 + self.r2 + self.r3 + self.r4 + self.r5 
        
        # regex 정규 표현식 사용
        # re.sub(정규 표현식, 치환 문자, 대상 문자열)
        return re.sub(r'\|$', '', tlo_message) # r --> escape문자 그대로 출력

    def clear(self):
        self.__init__()

    @property # @property: getter값 읽어오는 역할 (property 이름으로 접근 가능)
    def seq_id(self):
        return self._seq_id
    @seq_id.setter # property.setter: 값을 지정하는 역할
    def seq_id(self, value):
        self._seq_id = "SEQ_ID=%s|" % value
        
    @property
    def log_time(self):
        return self._log_time
    @log_time.setter
    def log_time(self, value):
        self._log_time = "LOG_TIME=%s|" % value
        
    @property
    def req_time(self):
        return self._req_time
    @req_time.setter
    def req_time(self, value):
        self._req_time = "REQ_TIME=%s|" % value
        
    @property
    def log_type(self):
        return self._log_type
    @log_type.setter
    def log_type(self, value):
        self._log_type = value
        
    @property
    def result_code(self):
        return self._result_code
    @result_code.setter
    def result_code(self, value):
        self._result_code = "RESULT_CODE=%s|" % value
        
    @property
    def rsp_time(self):
        return self._rsp_time
    @rsp_time.setter
    def rsp_time(self, value):
        self._rsp_time = "RSP_TIME=%s|" % value
           
    @property
    def sid(self): # dvic MAC
        return self._sid
    @sid.setter
    def sid(self, value):
        self._sid = "SID=%s|" % value
        
    @property
    def client_ip(self):
        return self._client_ip
    @client_ip.setter
    def client_ip(self, value):
        self._client_ip = "CLIENT_IP=%s|" % value
        
    @property
    def dev_info(self):
        return self._dev_info
    @dev_info.setter
    def dev_info(self, value):
        self._dev_info = "DEV_INFO=%s|" % value
        
    @property
    def os_info(self):
        return self._os_info
    @os_info.setter
    def os_info(self, value):
        self._os_info = "OS_INFO=%s|" % value
        
    @property
    def nw_info(self):
        return self._nw_info
    @nw_info.setter
    def nw_info(self, value):
        self._nw_info = "NW_INFO=%s|" % value
        
    @property
    def svc_name(self):
        return self._svc_name
    @svc_name.setter
    def svc_name(self, value):
        self._svc_name = "SVC_NAME=%s|" % value
        
    @property
    def dev_model(self):
        return self._dev_model
    @dev_model.setter
    def dev_model(self, value):
        self._dev_model = "DEV_MODEL=%s|" % value
        
    @property
    def carrier_type(self):
        return self._carrier_type
    @carrier_type.setter
    def carrier_type(self, value):
        self._carrier_type = "CARRIER_TYPE=%s|" % value
                         
    @property
    def session_id(self):
        return self._session_id
    @session_id.setter
    def session_id(self, value):
        self._session_id = "SESSION_ID=%s|" % value
            
    @property
    def talk_id(self):
        return self._talk_id
    @talk_id.setter
    def talk_id(self, value):
        self._talk_id = "TALK_ID=%s|" % value
             
    @property
    def req_url(self):
        return self._req_url
    @req_url.setter
    def req_url(self, value):
        self._req_url = "REQ_URL=%s|" % value
             
    @property
    def search_type(self):
        return self._search_type
    @search_type.setter
    def search_type(self, value):
        self._search_type = "SEARCH_TYPE=%s|" % value
        
    @property
    def query(self):
        return self._query
    @query.setter
    def query(self, value):
        self._query = "QUERY=%s|" % value
        
    @property
    def trid(self):
        return self._trid
    @trid.setter
    def trid(self, value):
        self._trid = "TRID=%s|" % value
        
    @property
    def nlc_req_time(self):
        return self._nlc_req_time
    @nlc_req_time.setter
    def nlc_req_time(self, value):
        self._nlc_req_time = "NLC_REQ_TIME=%s|" % value
        
    @property
    def nlc_rsp_time(self):
        return self._nlc_rsp_time
    @nlc_rsp_time.setter
    def nlc_rsp_time(self, value):
        self._nlc_rsp_time = "NLC_RSP_TIME=%s|" % value
        
    @property
    def nlc_rsp(self):
        return self._nlc_rsp
    @nlc_rsp.setter
    def nlc_rsp(self, value):
        self._nlc_rsp = "NLC_RSP=%s|" % value
        
    @property
    def svr_type(self):
        return self._svr_type
    @svr_type.setter
    def svr_type(self, value):
        self._svr_type = "SVR_TYPE=%s|" % value
        
    @property
    def nlc_result(self):
        return self._nlc_result
    @nlc_result.setter
    def nlc_result(self, value):
        self._nlc_result = "NLC_RESULT=%s|" % value   

    @property
    def nlc_text(self):
        return self._nlc_text
    @nlc_text.setter
    def nlc_text(self, value):
        self._nlc_text = "NLC_TEXT=%s|" % value  

    # 예비필드
    @property
    def r1(self):
        return self._r1
    @r1.setter
    def r1(self, value):
        self._r1 = "R1=%s|" % value

    @property
    def r2(self):
        return self._r2
    @r2.setter
    def r2(self, value):
        self._r2 = "R2=%s|" % value

    @property
    def r3(self):
        return self._r3
    @r3.setter
    def r3(self, value):
        self._r3 = "R3=%s|" % value

    @property
    def r4(self):
        return self._r4
    @r4.setter
    def r4(self, value):
        self._r4 = "R4=%s|" % value

    @property
    def r5(self):
        return self._r5
    @r5.setter
    def r5(self, value):
        self._r5 = "R5=%s|" % value
  
if __name__ == "__main__":
    tcls = Tlo()
    tcls.seq_id = seq_id()
    #tcls.reserve1 = 'test'

    a = {'log_time': get_logtime(), 'seq_id':seq_id()}
    tcls.set_tlo_messages(a)
    print(tcls.get_tlo_messages)
    





    
