'''
    Example to show that  system
    command can be called 
    in pyton.
    with OS package, you can call any  command
    but the output goes to standard out
    with os.popen().read(), the out put can be 
    captured as a  string array
    with subprocess.check_output, the output is a
    byte array
    with  os.popen().readlines(), a list is returned
    each line is a list and the output is easily parsed
'''

import os
import subprocess

ret = subprocess.check_output("ps aux",shell=True)
#print(type(ret))


#ret1 = os.system("gcloud --quiet compute ssh --ssh-key-file=~/.ssh/compute_engine  jagadish@demo4 --zone us-central1-c --command 'cd /home && ls -l'")

#ret2 = os.system("gcloud compute images list")
#print(type(ret2))

out = os.popen('ps').read()
#print(type(out))
#print(out[0:9])

#output = os.popen('ps').readlines()
#print(type(output))
#for l in  output:
#    print(l)

img = os.popen('gcloud compute images list').readlines()
print(type(img))
print(len(img))
print(len(img[0]))
print(type(img[0]))
text = img[1]
text = text.split()
print(text)
print(text[0])
imgKV = {}
k = 0
'''
for i in img:
    imgKV[i[0]] = [img[1], img[2], img[3]]
    print(str(img[k][0]))
    k = k + 1
'''
