# Obstacle Avoidance

A simple obstacle avoidance ROS 2 system connected to a AMQP Broker with specifications:

```
Broker Name: MyBroker
Broker Type: AMQP
Broker Host: domain.ddns.net
Broker Port: 1312
Broker Username: arob
Broker Password: 1234
Broker vhost: /
```

The model obstacle_avoidance.rbr could be obtained, running from terminal the transformation with the model obstacle_avoidance.xmi as an input, through the command:

```
sudo bash ~/rosbridge-generos-int/run.bash ~/generos ~/rosbridge-generos-int/examples/Obstacle_Avoidance/obstacle_avoidance.xmi ~/rosbridge-generos-int/examples/Obstacle_Avoidance/obstacle_avoidance.rbr amqp domain.ddns.net 1312 arob 1234 /
```
