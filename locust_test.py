import grpc
from models import nlp_server_pb2
from models import nlp_server_pb2_grpc
import time
from locust import User, TaskSet, task, events, between, stats, main, runners
import json
from datetime import datetime

class MyTasks(TaskSet):                 
    def on_start(self):
        #gRPC 채널 생성 및 스텁 생성
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = nlp_server_pb2_grpc.NLPServerStub(channel)

    @task(2)
    def getNlc(self):           
        start_time = time.time()     
        try:            
            # gRPC 서버에 요청                  
            response = self.stub.getNlc(nlp_server_pb2.nlcReq(searchType="S", query="추천요금제를 알려주세요", trid="vkZm2O48Bgy0NHSr9XuIGk7EDY5xJ6w1",
                                                 domain="고객센터", topN=3, sessionId="HTyY9wrfxZpdX0bBOEQ3mK7fW2D8bDHfGJ2CqO632R1xMQMckyheO3uW2UhqMvmgvbDHVULVmtMad5Bp", talkId="talkId1")) 
            print(response)       
        except Exception as e:            
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(request_type="grpc", name="getNlc", response_time=total_time, exception=e)   
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(request_type="grpc", name="getNlc", response_time=total_time, response_length=0)
            
    @task(1)
    def getItn(self):           
        start_time = time.time()     
        try:            
            # gRPC 서버에 요청                  
            response = self.stub.getItn(nlp_server_pb2.itnReq(searchType="S", sttQuery="텍스트로 변환된 사용자 음성 발화", trid="vkZm2O48Bgy0NHSr9XuIGk7EDY5xJ6w7",
                                                                    domain="domain", sessionId="gGVMvi0ipFY64QM2fkEqoEADB68TYLpHgdl7vN62wVlmQ5T4GZzOoR5PIniD0coYbO9aBsE7RpuEpwNO", talkId="talkId2"))
            print(response)       
        except Exception as e:            
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(request_type="grpc", name="getItn", response_time=total_time, exception=e)   
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request.fire(request_type="grpc", name="getItn", response_time=total_time, response_length=0)
                                                    
class MyUser(User):
    tasks = [MyTasks]  
    #wait_time으로 각 클라이언트가 일정 시간마다 요청하는 빈도를 조정할 수 있습니다.
    # wait_time = between(0.001, 0.001)
    wait_time = between(1, 2)