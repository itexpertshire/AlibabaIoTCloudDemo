from aliyunsdkcore import client
from aliyunsdkiot.request.v20170420 import RegistDeviceRequest
from aliyunsdkiot.request.v20170420 import PubRequest

accessKeyId = 'LTAIqo5BFYdWSvZD'
accessKeySecret = 'kS2ezP0t81QHBwSTciUQybGxmwrHQP'
clt = client.AcsClient(accessKeyId, accessKeySecret, 'cn-shanghai')
productKey = 'a1hbm0FZrDs'
deviceName = 'VWyNtvJbQCi9D0PIovfmrg'
topicName = '/'+productKey+'/'+deviceName+'/update'

import time
from w1thermsensor import W1ThermSensor


###sensor = W1ThermSensor()

###while True:
###    temperature = sensor.get_temperature()
###    print("The temperature is %s celsius" % temperature)
###    time.sleep(1)
###
request = PubRequest.PubRequest()
request.set_accept_format('json') # Set the response format. The default is XML.
request.set_ProductKey(productKey)
request.set_TopicFullName(topicName) #Full name of the topic to which the messages are sent.
request.set_MessageContent('eyAidGVtcGVyYXR1cmUiIDogMjYgfQ==') #hello world Base64 String
request.set_Qos(0)
result = clt.do_action_with_exception(request)
print 'result : ' + result
