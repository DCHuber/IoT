Blue Tooth Low Energy Setup
======

Using the python library from Ian Harvey - [Bluepy](https://github.com/IanHarvey/bluepy) to scan for btle devices


Libray Installation
------------
For python library:

To install the current released version, on most Debian-based systems:

    $ sudo apt-get install python-pip libglib2.0-dev
    $ sudo pip install bluepy
    

For Python 3, you may need to use `pip3`:

    $ sudo apt-get install python3-pip libglib2.0-dev
    $ sudo pip3 install bluepy


Once installed you can download and run the [testBLE.py](https://github.com/DCHuber/IoT/blob/master/btle/testBLE.py) code to see if it is working

    $ sudo python3 testBLE.py
    
Code Installation
------------
Finally, download and configure the scanner code [btleScanner.py](https://github.com/DCHuber/IoT/blob/master/btle/btleScanner.py) to run as a cron job on your system.  

  #Create entry in the cron task manager
    $ crontab -e     -- first time you may need to specify editor.  Choose the default [2] nano
    
  #add the following line, which will run each minute.  Edit paths if you are storing the code elsewhere
    * * * * * sudo /usr/bin/python3 /home/pi/Projects/bluePy/btleScanner.py
    
  #To save the file, press Ctrl-X  followed by Y for yes   followed by `Enter`

To view the logging data in real time, you can use the `tail` command:

    $ tail -f <path to log file>    ie:  tail -f Projects/bluePy/logs/btlescan.csv


