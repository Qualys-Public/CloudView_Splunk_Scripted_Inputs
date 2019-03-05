import json
import os

username = "REPLACE_ME_QUALYS_USERNAME"
password = "REPLACE_ME_QUALYS_PASSWORD"
BASEURL = "REPLACE_ME_BASE_URL"
accountID = REPLACE_ME_ACCOUNT_ID
kurl = 'curl -k -s -u {}:{} -H "X-Requested-With:Curl" -H "Accept: application/json" -X "GET"  "{}/cloudview-api/rest/1.5/aws/evaluations/{}"'.format(username, password,BASEURL,accountID)
eval = os.popen(kurl).read()
evalcontent = json.loads(eval)['content']

for i in  range (len(evalcontent)):
        cid = int(evalcontent[i]["controlId"])
        qurl = 'curl -k -s -u {}:{} -H "X-Requested-With:Curl" -H "Accept: application/json" -X "GET"  "{}/cloudview-api/rest/1.5/aws/evaluations/{}/resources/{}"'.format(username, password,BASEURL,accountID,cid)
        result = os.popen(qurl).read()
        resourceevaluation = json.loads(result)
        count = len(resourceevaluation['content'])
        for j in range(count):
                resourcecontent = resourceevaluation['content'][j]
                resourcecontent["controlName"] = evalcontent[i]["controlName"]
                resourcecontent["controlId"] = evalcontent[i]["controlId"]
                print ((json.dumps(resourcecontent)))
