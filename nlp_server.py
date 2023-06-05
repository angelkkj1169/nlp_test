from concurrent import futures
import logging
import grpc
from models import nlp_server_pb2_grpc
from interceptor import interceptor
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import job
from service import nlp_service

sched = BackgroundScheduler(timezone='Asia/Seoul')
                                
class NLPServer(nlp_server_pb2_grpc.NLPServerServicer):
 	
    def getNlc(self, request, context):                               
        return nlp_service.getNlc(request, context)
                                          
    def getModelList(self, request, context):
        return nlp_service.getModelList(request, context)
    
    def reqSimulation(self, request, context):
        return nlp_service.reqSimulation(request, context)
    
    def getItn(self, request, context):
        return nlp_service.getItn(request, context)
    
               
# 스케줄러 실행 
@sched.scheduled_job('cron', second='0', minute='0', hour='0', id='create_folder_job')
def create_folder_job():
    job.create_folder_job()

@sched.scheduled_job('cron', second='0', minute='0', hour='0', id='create_slog_file')
def create_slog_file():
    job.create_slog_file()

@sched.scheduled_job('cron', minute='*/5', id='create_log_file')
def create_log_file():
    job.create_log_file()
    
sched.start()       
                       
def serve():
    # 서버 및 사용할 인터셉터 클래스 정의
    interceptors = [interceptor.LoggingInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(), interceptors=interceptors)
         
    # 위에서 정의한 서버를 지정
    nlp_server_pb2_grpc.add_NLPServerServicer_to_server(NLPServer(), server)

    # 포트 50051로 연결
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()