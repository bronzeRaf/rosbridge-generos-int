
# rosbridge-generos-int

A model to model transformation from a GeneROS model to a RosBridge one.

## Installing The Transformation:

### Automatic Install
In order to install and to run the transformation with its full capabilities you have to install some other software. It is highly recommended to use the official bash installer, to make sure all your libraries are set and up to date. Inside the folder you would like to install the transformation run:

```
$ wget https://raw.githubusercontent.com/bronzeRaf/rosbridge-generos-int/master/install.bash
$ sudo bash install.bash
```

You are done!

REMEMBER! You will need to install Generos too, to use the transformation. You can find instructions about Generos [here](https://github.com/bronzeRaf/generos/).

ALSO REMEMBER! You will also need to install ROS2 in your system to test your generated packages, but you still can generate them...
You can find ROS2 [here](https://index.ros.org/doc/ros2/Installation/Crystal/Linux-Install-Binary/ "Install ROS2").



## Running the Transformation:
To run the transformation you will need an XMI ROS2 model file. This model represents a ROS2 system and you can obtain this model from Generos. Therefor, you can obtain the RosBridge model running:

```
sudo bash path/to/run.bash path/to/generos path/to/model.xmi path/to/model.rbr broker_type broker_host broker_port broker_username broker_password broker_param
```

Replacing:
- "path/to/generos" with the absolute path to the installation folder of Generos
- "path/to/model.xmi" with the absolute path to the XMI model file
- "path/to/model.rbr" with the path you would like to save the generated model file
- "broker_type" with the broker type (redis or amqp)
- "broker_host" with the host of the broker
- "broker_port" with the port of the broker
- "broker_username" with the username of the broker
- "broker_password" with the password of the broker
- "broker_param" with the vhost (for amqp) or with the db (for redis) of the broker

Find your awesome RosBridge model in "path/to/model.rbr".

*NOTICE! This run script works with absolute paths. 

That's it, Enjoy!

