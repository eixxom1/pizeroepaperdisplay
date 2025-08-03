


### 🔐 What is SCP ?

**SCP** is a command-line tool that lets you securely copy files **between computers** using **SSH**.    
<sub>(not the SCP Foundation /ref)</sub>

### Why i need this in our Project
If you use a Pi Zero (2 W) Which is already underpowered, You wouldnt want to run Pi-Connect on it, Because it would use resources and it would increase Power draw,
I am trying to have minimal Power draw on it, And SCP uses less Power because the SSH Service is already running most of the Times.



### 📝 What you need

* SSH access to the remote server
* SCP installed (comes pre-installed on Linux/macOS; for Windows, use PowerShell or install OpenSSH)



###  1. Copy a File **From Local to Remote**

```bash
scp /path/to/local/file.txt username@remote_ip:/path/to/remote/
```

 Example:

```bash
scp myfile.txt pi@192.168.1.42:/home/pi/
```



###  2. Copy a File **From Remote to Local**

```bash
scp username@remote_ip:/path/to/remote/file.txt /path/to/local/
```

 Example:

```bash
scp pi@192.168.1.42:/home/pi/myfile.txt ~/Downloads/
```



###  3. Copy a **Directory** (add `-r` for recursive)

```bash
scp -r /path/to/local/folder username@remote_ip:/path/to/remote/
```

 Example:

```bash
scp -r myfolder pi@192.168.1.42:/home/pi/
```
You could also use the Hostname

```bash
scp -r myfolder pi@pizero:/home/pi/
```



###  Tips

* Default port is `22`. To use a different port (e.g., 2222):

```bash
scp -P 2222 file.txt user@host:/path/
```

* Use `~` to refer to home directory:

```bash
scp file.txt user@host:~/Documents/
```

