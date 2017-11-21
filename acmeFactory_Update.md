## Change notes: ##

* Disable the currently running service:

``` sudo systemctl disable sendTemps.service ```

* Backup the old code 

* Create a new directory to store the logs:

 ``` mkdir /home/pi/Projects/acmeFactory/logs ```

* Create the scheduled task

``` crontab -e ```

Add to the last line

```	*/5 * * * * /usr/bin/python3 /home/pi/Projects/acmeFactory/acmeSendTemp.py ```
