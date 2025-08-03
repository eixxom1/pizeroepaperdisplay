Guide for Auto-Starting Something in Linux



##  Full `rc.local` Setup for `FILE.py`

###  Step 1: Check or Create `/etc/rc.local`

#### If it **doesn't exist**, create it:

```bash
sudo nano /etc/rc.local
```

Paste the following content:

```bash
#!/bin/sh -e
# Start FILE.py script at boot
/usr/bin/python /home/YOUR-DIRECTORY-TO-THE-FILE.PY/ &
exit 0
```

> Replace `/usr/bin/python` with the exact path if needed (check with `which python`).



###  Step 2: Make it executable

```bash
sudo chmod +x /etc/rc.local
```



###  Step 3: Create the systemd service for `rc.local`

If it doesn't already exist, create:

```bash
sudo nano /etc/systemd/system/rc-local.service
```

Paste this:

```ini
[Unit]
Description=/etc/rc.local compatibility
ConditionPathExists=/etc/rc.local
After=network.target

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
RemainAfterExit=yes
GuessMainPID=no

[Install]
WantedBy=multi-user.target
```



###  Step 4: Enable the service

```bash
sudo systemctl enable rc-local
sudo systemctl start rc-local
```



###  Step 5: Reboot and test

```bash
sudo reboot
```

After booting, your `FILE.py` script should run automatically.



###  Optional: Debug tip

If it's not working:

* Check if your script runs manually first:

  ```bash
  /usr/bin/python /home/YOUR-DIRECTORY-TO-THE-FILE.PY/
  ```

* Add debug output to `/tmp`:
  In `/etc/rc.local`, change the line to:

  ```bash
  /usr/bin/python /home/YOUR-DIRECTORY-TO-THE-FILE.PY/ >> /tmp/YOUR-LOG-NAME.log 2>&1 &
  ```

This logs output and errors to `c`.

###  Tips


  Start the Service Immediatly
  ```bash  	
sudo systemctl start rc-local
  ```

  Stops the Service 
  ```bash  	
sudo systemctl stop rc-local
  ```

  Restarts the Service 
  ```bash  	
sudo systemctl restart rc-local
  ```

  Enables the Service at Boot
  ```bash  	
sudo systemctl enable rc-local
  ```
 (i have no idea why enable is blue)
 
  Disables the Service at Boot
  ```bash  	
sudo systemctl disable rc-local
  ```

  Status of the Service
  ```bash  	
sudo systemctl status rc-local
  ```


You have to rename ``` /home/YOUR-DIRECTORY-TO-THE-FILE.PY/ ``` to the name of your File, and ``` /tmp/YOUR-LOG-NAME.log ``` to the Name you want your Log to be.
