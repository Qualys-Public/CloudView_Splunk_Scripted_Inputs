import json
import os

username = "REPLACE_ME_QUALYS_USERNAME"
password = "REPLACE_ME_QUALYS_PASSWORD"
BASEURL = "REPLACE_ME_BASE_URL"
accountID = REPLACE_ME_ACCOUNT_ID
kurl = 'curl -k -s -u {}:{} -H "X-Requested-With:Curl" -H "Accept: application/json" -X "GET"  "{}/cloudview-api/rest/1.5/aws/evaluations/{}"'.format(username, password,BASEURL,accountID)
eval = os.popen(kurl).read()
count = len(json.loads(eval)['content'])

for i in  range (1,count):
        qurl = 'curl -k -s -u {}:{} -H "X-Requested-With:Curl" -H "Accept: application/json" -X "GET"  "{}/cloudview-api/rest/1.5/aws/evaluations/{}/resources/{}"'.format(username, password,BASEURL,accountID,i)
        result = os.popen(qurl).read()
        abc = json.loads(result)
        for i in range(len(abc['content'])):
                test = abc['content'][i]
                print ((json.dumps(test)))
