# CloudView Integration with Splunk  


## License
_**THIS SCRIPT IS PROVIDED TO YOU "AS IS."  TO THE EXTENT PERMITTED BY LAW, QUALYS HEREBY DISCLAIMS ALL WARRANTIES AND LIABILITY FOR THE PROVISION OR USE OF THIS SCRIPT.  IN NO EVENT SHALL THESE SCRIPTS BE DEEMED TO BE CLOUD SERVICES AS PROVIDED BY QUALYS**_

## Description 
Qualys CloudView is a solution for continuous inventory (CI) and assessment of your public cloud workloads (CSA). You can use this guide to integrate CloudView with Splunk and leverage Splunk for Cloud Security Assessment (CSA).

## Usage
You can utilize the power of scripted inputs to ingest CSA information by following below mentioned steps.

**1. Build a script file**
* Create a script file under one of the splunk allowed directories. Verify whether your environment variable $SPLUNK_HOME is set. 
    * $SPLUNK_HOME/bin/scripts 
    * $SPLUNK_HOME/etc/apps/search/bin 
    * $SPLUNK_HOME/etc/apps/splunk_instrumentation/bin 
    * $SPLUNK_HOME/etc/system/bin 
* Copy the contents from the Qualys GitHub for the script file. 
* Ensure to replace username, password and base url for Cloudview in the script file. 
* Make the file executable and change the owner and group to user splunk. 
* sudo chmod +x qualysCVDownload.py 
