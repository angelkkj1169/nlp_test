import logging
from exception import error
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("interceptor")  # 로거 생성

class Counter:
    def __init__(self, value=0):
        self.value = value
        
    def increment(self, delta=1):
        if self.value == 10: 
            error.getError("00000000", "서버의 동시 접속자 수는 10명까지입니다.")      
        self.value += delta        
        logger.info("현재 접속중인 사용자: "+ str(self.value)) 
                    
    def decrement(self, delta=1):
        self.value -= delta  
        logger.info("현재 접속중인 사용자: "+ str(self.value))