# Publisher-Subscriber 

A simple server-client ROS 2 system connected to a Redis Broker with specifications:

```
Broker Name: MyBroker
Broker Type: Redis
Broker Host: domain.ddns.net
Broker Port: 22
Broker Username: myrobot
Broker Password: myr0b0t1!
Broker db: 902
```

The model serverclient.rbr could be obtained, running from terminal the transformation with the model serverclient.xmi as an input, through the command:

```
sudo bash ~/rosbridge-generos-int/run.bash ~/generos ~/rosbridge-generos-int/examples/ServerClient/serverclient.xmi ~/rosbridge-generos-int/examples/ServerClient/serverclient.rbr redis domain.ddns.net 22 myrobot myr0b0t1! 902
```
