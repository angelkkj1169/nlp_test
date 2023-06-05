from grpc_interceptor import ServerInterceptor
from connection_manager import counter
from loggings.svc_log import SvcLogger
from loggings import tlo
from properties.cfg_parser import CfgParser
from datetime import datetime
from pytz import timezone
import loggings.tlo_writer as tlo_writer
import os

PRJ_ROOT = os.path.abspath(os.path.join(__file__, '..', '..'))
public_cfg = CfgParser(os.path.join(PRJ_ROOT, 'properties', 'config.cfg'))  
tlo_path = PRJ_ROOT + public_cfg.tlo_path
counter = counter.Counter()
tlo_cls = tlo.Tlo()
log_file = PRJ_ROOT + public_cfg.log_path + 'nlc.' + str(datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d"))+'.log'
svcLogger = SvcLogger('svc_logger', log_file)
logger = svcLogger.get_logger()
        
# 서버 인터셉터 클래스 정의
class LoggingInterceptor(ServerInterceptor):
       
    def intercept(self, method, request, context, method_name):
        tlo_cls.clear()
            
        #methodName의 이름은 proto파일 규격에 따름
        methodName = method_name.rsplit('/', 1)[-1]
                                             
        logger.info(f'####### start {methodName}() method....')
         
        #여기부턴 tlo 작성과정 
        request_time = tlo.get_request_time()
        client_ip = context.peer()
        tlo_msg = {}
        tlo_msg['seq_id'] = tlo.seq_id() #tlo 고유 id
        tlo_msg['req_time'] = request_time #서비스 전체 요청 발생 시간  
        tlo_msg['client_ip'] = client_ip 
            
        # SVR_TYPE: chatbot, admin, itn
        if methodName == 'getNlc':
            tlo_msg['svr_type'] = "chatbot"    
        elif methodName == 'getItn':
            tlo_msg['svr_type'] = "itn" 
        else:
            tlo_msg['svr_type'] = "admin" 

        counter.increment()            
  
        # try:
            # 이 코드를 기준으로 위에는 서버가 클라이언트의 요청을 받기 전에 필요한 코드를,
            # 아래에는 클라이언트가 서버의 응답을 받기 전에 필요한 코드를 작성하면 됨            
        response = method(request, context)   
        print(response.resultCode)
        
        counter.decrement() 
        if response.resultCode == "0000":
            tlo_msg['rsp_time'] = tlo.get_request_time() #서비스 전체 응답 완료 시간       
            tlo_msg['log_time'] = tlo.get_logtime() #로그를 파일에 WRITE하는 시점 시간
            logger.info(f'####### end {methodName}() method....')
            log_write(tlo_msg)        
            return response
        else: 
            tlo_msg['rsp_time'] = tlo.get_request_time() #서비스 전체 응답 완료 시간       
            tlo_msg['log_time'] = tlo.get_logtime() #로그를 파일에 WRITE하는 시점 시간
            logger.info(f'####### end {methodName}() method....')
            log_write(tlo_msg)   
            return response
        
        # TLO로그는 하나의 클라이언트 요청당 하나만 생기고, 결과가 정상이든 에러든 무조건 하나씩 생성된다.
        # 1XXXXXXX 정보
        # 2XXXXXXX 성공
        # 3XXXXXXX 클라이언트 에러
        # 4XXXXXXX 서버에러(서비스)
        # 5XXXXXXX 서버에러(연동)
                           
def log_write(tlo_msg):
    tlo_cls.set_tlo_messages(tlo_msg)
    tlo_input_msg = tlo_cls.get_tlo_messages()
    tlo_abs_path = tlo.get_tlo_path(tlo_path)
    tlo_file_name = tlo.get_tlo_log_name()
    tlo_file = tlo_writer.MultiLog(os.path.join(tlo_abs_path, tlo_file_name), tlo_file_name, None)
    tlo_file.info(tlo_input_msg)
    tlo_writer.EndMultiLog(tlo_file_name) 
    
    