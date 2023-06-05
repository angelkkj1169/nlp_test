import logging
import grpc
from models import nlp_server_pb2
from models import nlp_server_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = nlp_server_pb2_grpc.NLPServerStub(channel)

#챗봇이나 관리도구에서 요청을 한다고 가정하고 만든 호출용 클라이언트
def run(): 
    rpcInput = input("getNlc/getModelList/reqSimulation/getItn(N/M/S/I): ")  
    if rpcInput == "N":
        getNlc()
    elif rpcInput == "M":
        getModelList()
    elif rpcInput == "S":
        reqSimulation()
    elif rpcInput == "I":
        getItn()         
    else:
        print("잘못된 입력입니다.")

def getNlc():     
    response = stub.getNlc(nlp_server_pb2.nlcReq(searchType="S", query="추천요금제를 알려주세요", trid="vkZm2O48Bgy0NHSr9XuIGk7EDY5xJ6w1",
                                                 domain="고객센터", topN=3, sessionId="HTyY9wrfxZpdX0bBOEQ3mK7fW2D8bDHfGJ2CqO632R1xMQMckyheO3uW2UhqMvmgvbDHVULVmtMad5Bp", talkId="talkId1"))               
    #서버에서 받아온 결과를 출력
    print(response)

         
def reqSimulation():     
    response = stub.reqSimulation(nlp_server_pb2.simulationReq(searchType="S", query="추천요금제를 알려주세요 시뮬레이션",
                                                               trid="vkZm2O48Bgy0NHSr9XuIGk7EDY5xJ6w1", domain="고객센터", topN=3))               
    #서버에서 받아온 결과를 출력
    print(response) 
   
def getItn():     
    response = stub.getItn(nlp_server_pb2.itnReq(searchType="S", sttQuery="텍스트로 변환된 사용자 음성 발화", trid="vkZm2O48Bgy0NHSr9XuIGk7EDY5xJ6w7",
                                                        domain="domain", sessionId="gGVMvi0ipFY64QM2fkEqoEADB68TYLpHgdl7vN62wVlmQ5T4GZzOoR5PIniD0coYbO9aBsE7RpuEpwNO", talkId="talkId2"))                  
    #서버에서 받아온 결과를 출력   
    print(response) 

             
def getModelList():        
    # proto 파일에 저장된 규격으로 bucketName get_gcs_test를 서버에 전달
    response = stub.getModelList(nlp_server_pb2.getModelReq(bucketName="get_gcs_test"))         

    modelList = response.modelList
    for index, obj in enumerate(modelList):
        print("받아온 json 파일의 내용" +str(index+1)+": \n" + str(obj))

               
if __name__ == '__main__':
    logging.basicConfig()
    run()
    