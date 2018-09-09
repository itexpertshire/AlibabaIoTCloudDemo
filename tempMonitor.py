from aliyunsdkcore import client
from aliyunsdkiot.request.v20170420 import RegistDeviceRequest
from aliyunsdkiot.request.v20170420 import PubRequest
import time
import base64
from w1thermsensor import W1ThermSensor


accessKeyId = 'LTAIqo5BFYdWSvZD'
accessKeySecret = 'kS2ezP0t81QHBwSTciUQybGxmwrHQP'
clt = client.AcsClient(accessKeyId, accessKeySecret, 'cn-shanghai')
productKey = 'a1hbm0FZrDs'
deviceName = 'VWyNtvJbQCi9D0PIovfmrg'
topicName = '/'+productKey+'/'+deviceName+'/update'


request = PubRequest.PubRequest()
request.set_accept_format('json') # Set the response format. The default is XML.
request.set_ProductKey(productKey)
request.set_TopicFullName(topicName) #Full name of the topic to which the messages are sent.


sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    timevalue = time.time()
    print ("time %s" %timevalue)
    print("The temperature is %s celsius" % temperature)    
    message = "{ 'temperature': %s, 'time': %s }" % (temperature,timevalue)
    print (base64.urlsafe_b64encode(message)) 
    request.set_MessageContent(base64.urlsafe_b64encode(message)) #JSON message Base64 String
    request.set_Qos(0)
    result = clt.do_action_with_exception(request)
    print 'result : ' + result
    time.sleep(60)
