## Change notes: ##

* Disable the currently running service:

  ``` sudo systemctl disable sendTemps.service ```

* Backup the old code 

* Create a new directory to store the logs
  
  ``` mkdir /home/pi/Projects/acmeFactory/logs ```

* Create the scheduled task by runing the crontab command - the first time might have you select an editor - I use nano
  
  ``` crontab -e ```
  
  Add to the last line
  
    ```	*/5 * * * * /usr/bin/python3 /home/pi/Projects/acmeFactory/acmeSendTemp.py ```
     
* If you want to see if everything is working you can run this command
  
  ```tail -f /home/pi/Projects/acmeFactory/logs/temp.log```

