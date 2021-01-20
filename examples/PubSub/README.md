# Publisher-Subscriber 

A simple publisher-subscriber ROS 2 system connected to a Redis Broker with specifications:

```
Broker Name: MyBroker
Broker Type: Redis
Broker Host: domain.ddns.net
Broker Port: 5582
Broker Username: robot
Broker Password: r0b0t!
Broker db: 303
```

The model pubsub.rbr could be obtained, running from terminal the transformation with the model pubsub.xmi as an input, through the command:

```
sudo bash ~/rosbridge-generos-int/run.bash ~/generos ~/rosbridge-generos-int/examples/PubSub/pubsub.xmi ~/rosbridge-generos-int/examples/PubSub/pubsub.rbr redis domain.ddns.net 5582 robot r0b0t! 303
```
