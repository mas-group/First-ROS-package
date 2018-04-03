# Ros commands

## Messages
### Look at all messages available
```
rosmsg list
```

### Look at the definition of a single message type
```
rosmsg show message_type
```
For example
```
rosmsg show turtlesim/pose
```

## Topics
### Look at all topics being published
```
rostopic list
```
### Get information about a topic (who subscribes, who published, whats the message type?)
```
rostopic info topic_name
```

### Print all the messages from one topic
```
rostopic echo topic_name
```
