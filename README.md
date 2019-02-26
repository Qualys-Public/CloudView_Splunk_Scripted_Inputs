# CloudView Integration with Splunk  


## License
_**THIS SCRIPT IS PROVIDED TO YOU "AS IS."  TO THE EXTENT PERMITTED BY LAW, QUALYS HEREBY DISCLAIMS ALL WARRANTIES AND LIABILITY FOR THE PROVISION OR USE OF THIS SCRIPT.  IN NO EVENT SHALL THESE SCRIPTS BE DEEMED TO BE CLOUD SERVICES AS PROVIDED BY QUALYS**_

## Description 
Qualys CloudView is a solution for continuous inventory (CI) and assessment of your public cloud workloads (CSA). You can use this guide to integrate CloudView with Splunk and leverage Splunk for Cloud Security Assessment (CSA).

## Integration

### Usage
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

**2. Go to the Add New page**

   **By Splunk Home**
* Click the Add Data link in Splunk Home. 
* Click Monitor to monitor a script on the local machine, or Forward to forward data from a script on a remote machine. Splunk Web displays the "Add Data - Select Source" page. 
* In the left pane, locate and select Scripts.

   **By Splunk Settings**
* Click Settings in the upper right corner of Splunk Web. 
* Click Data Inputs. 
* Click Scripts. 
* Click New to add an input.

**3. Select the input source**
* In the Script Path drop down, select the path where the script resides. . Splunk Web updates the page to include a new drop-down list, "Script Name." 
* In the Script Name drop-down, select the script that you want to run. Splunk Web updates the page to populate the "Command" field with the script name. 
* In the Interval field, enter the amount of time (in seconds) that Splunk Enterprise should wait before invoking the script. You can schedule it to run daily or set up your own cron schedule. 
* Optionally, In the Source Name Override field, enter a new source name to override the default source value, if necessary. The default source name field is the path of your script file.  
* Click Next.

**4. Specify input settings**
* Select the source type for the script. You can choose Select to pick from the list of available source types on the local machine and select “json_no_timestamp”. 
* Select the "Searching and Reporting” as Application context for this input. 
* Set the Host name value. You have several choices for this setting. Example: Cloudview 
* Set the Index that Splunk Enterprise should send data to. Leave the value as "default", unless you have defined multiple indexes to handle different types of events. In addition to indexes for user data. 
* Click Review.

**5. Review your choices**
* Review the settings. 
* If they do not match what you want, click < to go back to the previous step in the wizard. Otherwise, click Submit.

**_Note: You can also add scripted inputs with inputs.conf file._**

### Searching & Reporting
This is how it looks once the script runs and data is populated. 

### Troubleshooting
Search for errors in Searching and Reporting app on your Splunk Enterprise using the query: 

```index="_internal" error qualysCVDownload.py```

or you can investigate the logs at _/opt/splunk/var/log/splunk/splunkd.log_

### Links 
For more information, refer the below links
* [Introduction to Scripted Inputs](https://docs.splunk.com/Documentation/Splunk/7.2.4/Data/Getdatafromscriptedinputs) 
* [Advanced Usage of Scripted Inputs](https://docs.splunk.com/Documentation/Splunk/7.2.4/AdvancedDev/ScriptSetup)
