
import redis
import time
import traceback


def redisCheck():
    print("in redisCheck")
    try:
        # connect with Staging
        rp = redis.StrictRedis(host='35.193.241.194', port=6379,
                 password='7913511eca0b03a225a5d9cc60ce65800f3c37b059116898b189acbcd54cdcb6')                
        p = rp.pubsub()                                                                
        p.subscribe('alloc-dealloc')                                                 
        PAUSE = True

        while PAUSE:                                                                
            print("Waiting For redisStarter...")
            message = p.get_message()                                              
            if message:
                command = message['data']                                           

                if command == b'rtmp_98405':                                             
                    PAUSE = False                                                   

            time.sleep(1)

        print("Permission to start...")

    except Exception as e:
        print("!!!!!!!!!! EXCEPTION !!!!!!!!!")
        print(str(e))
        print(traceback.format_exc())

redisCheck()