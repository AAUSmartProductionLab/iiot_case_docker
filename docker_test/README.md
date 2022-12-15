# IIoT Box Start-up guide (docker version)

This guide will describe the step-by-step process to set up the IIoT Box on the shopfloor.

---

## Installation & Setup
This section will contain go through the installation and setup of the docker containers for the IIoT box.

### Prerequisites


A version of Ubuntu compatible with Raspberry Pi has to be installed. This can be installed using the Raspberry Pi Imager [Link](https://www.raspberrypi.com/software/).

The next step is to install docker which can be done through the guide that can be found here [Link](https://docs.docker.com/engine/install/ubuntu/)(Ubuntu).

Once docker is installed, we need to install the docker-compose plugin. This can be done through this [Link](https://docs.docker.com/compose/install/linux/#install-using-the-repository).

There are sometimes permission issues with running docker-compose. Run the following commands in a terminal to ensure the permissions are the place:
``` 
$ sudo groupadd docker

$ sudo usermod -aG docker $USER

$ newgrp docker
```
Once this is installed the docker installation can be tested using the following command: 
```
$ sudo docker run hello-world
```

Next git has to be installed such that the repository can be cloned and used to run the docker-compose file.

```
$ sudo apt install git
```
With git installed we can now download this repository to a desired folder. Simply run the following command:

```
git clone https://github.com/AAUSmartProductionLab/iiot_case_docker.git
```
### Setting up the device with the iiot container stack


---
## Initial Steps



1. Create node-red flows + credentials that are relevant to the demo.
2. Create image from raspAP so a wifi can be automatically setup.
3. Make sure all files are in the necessary folders such that the docker-compose directory is readable and understandable.
4. Change python code to something useful, such that it can be used in the future.
5. Add FOTA to the ESP's such that it'll be easy to edit code in the future.
6. 
