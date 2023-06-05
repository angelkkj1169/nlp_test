from models import nlp_server_pb2
import json
import os  
from auth import gcs_auth
from loggings import tlo
from loggings.svc_log import SvcLogger
import time

tlo_cls = tlo.Tlo() 
svcLogger = SvcLogger()
logger = svcLogger.get_logger() 
         
def getNlc(request, context):
    tlo_msg = {} 
    tlo_msg['trid'] =  request.trid 
    tlo_msg['search_type'] =  request.searchType           
    tlo_msg['session_id'] = request.sessionId 
    tlo_msg['talk_id'] =  request.talkId 
    tlo_msg['query'] =  request.query   

    try:
        tlo_msg['nlc_req_time'] = tlo.get_request_time() # NLC_REQ_TIME NLC 요청시간
        #NLC 엔진 연동 관련 로직이 들어갈 예정
        tlo_msg['nlc_rsp_time'] = tlo.get_request_time() # NLC_RSP_TIME NLC 응답시간
        tlo_msg['nlc_rsp'] = "20000000"      # NLC_RSP NLC 응답 결과코드
        tlo_msg['nlc_text'] = "[요금제] 갤럭시 버즈 팩" # NLC_RSP NLC 응답 결과코드
        tlo_msg['result_code'] = '20000000'   
        tlo_cls.set_tlo_messages(tlo_msg)
        
        resultCode = "0000"
        domain = "고객센터"   
        topAnswer = 100280 
        topScore = 0.01659
        intentName = "[요금제] 갤럭시 버즈 팩"            
        answerList = []          
        answerList.append({"answer":100280, "score":0.01120, "intent":"[요금제]"}) 
        answerList.append({"answer":100272, "score":0.0145, "intent":"[단말기]"})
        answerList.append({"answer":89, "score":0.0647, "intent":"[청구요금]"})
              
    except Exception:
        resultCode = "9999"
        logger.error('##### NLC 연동중 에러가 발생했습니다.')
        logger.error('##### SYSTEM ERROR: %s', resultCode, exc_info=True)
 
        tlo_msg['nlc_rsp_time'] = tlo.get_request_time() # NLC_RSP_TIME NLC 응답시간
        tlo_msg['nlc_rsp'] = "40000000"      # NLC_RSP NLC 응답 결과코드
        tlo_msg['result_code'] = '40000001'
        tlo_cls.set_tlo_messages(tlo_msg)
        return nlp_server_pb2.nlcRes(resultCode=resultCode)
    
    return nlp_server_pb2.nlcRes(resultCode=resultCode, domain=domain, topAnswer=topAnswer,
                            topScore=topScore, intentName=intentName, answerList=answerList)
 

def reqSimulation(request, context): 
    tlo_msg = {} 
    tlo_msg['result_code'] = '22222222'
    tlo_cls.set_tlo_messages(tlo_msg)
    
         
    resultCode = "200"
    domain = "고객센터" 
    algorithm = "NLC"     
    topAnswer = 100280 
    topScore = 0.01659
    matched = False
    defaultScore = 0.75
    multiIScore = 0.5
    intentName = "[요금제] 갤럭시 버즈 팩"            
    answerList = []          
    answerList.append({"answer":100280, "score":0.01120, "intent":"[요금제]"}) 
    answerList.append({"answer":100272, "score":0.0145, "intent":"[단말기]"})
    answerList.append({"answer":89, "score":0.0647, "intent":"[청구요금]"})  
    return nlp_server_pb2.simulationRes(resultCode=resultCode, domain=domain, algorithm=algorithm,
                                        topAnswer=topAnswer,topScore=topScore, matched=matched,
                                        defaultScore=defaultScore, multiIScore=multiIScore, intentName=intentName, answerList=answerList)
                  
def getItn(request, context):
    tlo_msg = {} 
    tlo_msg['result_code'] = '33333333'
    tlo_cls.set_tlo_messages(tlo_msg)
                                  
    resultCode = "200"
    domain = "쇼핑상담"   
    sttQuery = "아이폰십사 오구요금제 가입" 
    normQuery = "아이폰 14 59 요금제 가입"
    itnclsCode = True         
    return nlp_server_pb2.itnRes(resultCode=resultCode, domain=domain, sttQuery=sttQuery,
                                normQuery=normQuery, itnclsCode=itnclsCode)   

                               
def getModelList(request, context):                 
    # # Google Cloud Storage 클라이언트 생성
    client = gcs_auth.getGCSClient()
                    
    # 클라이언트로부터 받아온 버킷 이름 설정
    bucket_name = request.bucketName
        
    # 버킷 객체 가져오기
    bucket = client.bucket(bucket_name)

    # 버킷 안에 있는 객체(파일/폴더) 모든 목록을 조회     
    blobs = bucket.list_blobs() 
                    
    # 클라이언트에 보낼 list 생성
    resList = []   

    # GCS API에서 받아온 값(파일경로, 파일 생성 날짜)과 json파일 안에 있는 값을 합쳐서 생성한 json 객체를 list에 담음
    for blob in blobs:   
                                                                                            
        if blob.name.endswith('.bin'): #blob 객체가 모델인 경우
            newJson = {}             
            directory_name = os.path.dirname(blob.name)             
            config = bucket.blob(directory_name+"/config.json") #각 모델폴더 안에 있는 config.json의 이름이 동일하다고 가정할 때만 사용가능
            content = config.download_as_string() #불러온 json 파일 읽기
            json_content = json.loads(content)                                                                                                    
        
            for key, value in json_content.items():                                                       
                newJson[key] = value
            
            newJson["uploadDate"] = blob.time_created.strftime('%Y-%m-%d %H:%M:%S')
            newJson["path"] = blob.name + " ("+str(blob.size)+"b)"                                            
            resList.append(newJson)
                                                    
    resultCode = "200"
    resultMessage = "성공"     
    # 클라이언트로 list 전달                                              
    return nlp_server_pb2.getModelRes(resultCode=resultCode, resultMessage=resultMessage, modelList=resList)

 
 
 
 
 