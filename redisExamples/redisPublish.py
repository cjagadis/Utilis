import redis
import time
import json
import traceback


def pubAllocDealloc():

    try:
        # connect with Staging
        rp = redis.StrictRedis(host='35.193.241.194', port=6379,
                 password='7913511eca0b03a225a5d9cc60ce65800f3c37b059116898b189acbcd54cdcb6')                
        #p = rp.pubsub()                                                    

        print("Starting to Publish...")
        rp.publish('alloc-dealloc', 'rtmp_98405')                                
        print("Done")

    except Exception as e:
        print("!!!!!!!!!! EXCEPTION !!!!!!!!!")
        print(str(e))
        print(traceback.format_exc())

while 1:
    pubAllocDealloc()
    time.sleep(10)