Bluetooth Low Energy Setup
======

Using the python library from Ian Harvey - [Bluepy](https://github.com/IanHarvey/bluepy) to scan for btle devices


Libray Installation
------------
For python library:

To install the current released version, on most Debian-based systems:

For Python 3, which I assume you are using in my examples, you may need to use `pip3`:

    $ sudo apt-get install python3-pip libglib2.0-dev
    $ sudo pip3 install bluepy

    
Code Installation
------------

Once installed you can download and run the [testBLE.py](https://github.com/DCHuber/IoT/blob/master/btle/testBLE.py) code to see if it is working

    $ sudo python3 testBLE.py
    
Finally, download and configure the scanner code [btleScanner.py](https://github.com/DCHuber/IoT/blob/master/btle/btleScanner.py) to run as a cron job on your system.  

 1. Create the folders needed to host the code
 
        $ mkdir Projects/bluePy
        $ mkdir Projects/bluePy/logs
        
 2.  Download the code referenced above and place it in the `/Projects/bluePy` folder
 
 3. Edit the `nodeID` field to use your devices local btle MAC address.   To get the address, execute the command:
        
        $ hciconfig
     
    Copy the MAC address and edit it to remove the ":" and lower case the letters:  ie: "b827eb01c055"
 
 4. Schedule the code to run once a minute by creating an entry in the cron task manager
   
        $ crontab -e     #NOTE: first time you may need to specify editor.  Choose the default [2] nano

    Add the following line at the end of the file.  If you created your directories in a different path than what is recommended in Step 1, edit the paths
 
        * * * * * sudo /usr/bin/python3 /home/pi/Projects/bluePy/btleScanner.py
    
  #To save the file, press Ctrl-X  followed by `Y` for yes   followed by `Enter`

 5. To view the logging data in real time, you can use the `tail` command:

        $ tail -f <path to log file>    ie:  $ tail -f Projects/bluePy/logs/btlescan.csv


