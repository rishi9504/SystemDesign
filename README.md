# SystemDesign
All things related to system design.

## What is availability and partition tolerance?

Availability and partition tolerance are two properties of a distributed system. The CAP theorem states that a distributed system can only provide two of the following properties at the same time: 
* Consistency: How well a system maintains a consistent and accurate view of data or state
* Availability: The ability to access a cluster even if a node in the cluster goes down
* Partition tolerance: The ability to continue functioning even if there is a communication break between two nodes

  
Availability is usually measured as uptime or reliability. It's critical for systems that provide mission-critical services or handle sensitive data. 
Partition tolerance refers to a system's ability to continue functioning despite network partitions or communication breakdowns between nodes. Network partitions happen when communication links between nodes fail, resulting in the system being split into multiple isolated sub-systems.
