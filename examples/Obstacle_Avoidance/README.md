# Obstacle Avoidance

An obstacle avoidance ROS 2 system connected to a Redis Broker with specifications:

```
Broker Name: MyBroker
Broker Type: Redis
Broker Host: domain.ddns.net
Broker Port: 5582
Broker Username: robot
Broker Password: r0b0t!
Broker db: 303
```

The model obstacle_avoidance.rbr could be obtained, running from terminal the transformation with the model obstacle_avoidance.xmi as an input, through the command:

```
sudo bash ~/rosbridge-generos-int/run.bash ~/generos ~/rosbridge-generos-int/examples/Obstacle_Avoidance/obstacle_avoidance.xmi ~/rosbridge-generos-int/examples/Obstacle_Avoidance/obstacle_avoidance.rbr redis domain.ddns.net 5582 robot r0b0t! 303
```
