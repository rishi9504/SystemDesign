## What are database locks?
Shared Lock
Exclusive Lock
Update Lock
Schema Lock
Bulk Update Lock
Key Range Lock
Row Level Lock
Table Level Lock



## What is redis? Explain caching by Redis.


## How to improve API performance?
Pagination, async logging, caching, payload compression, connection pool

## What is a CI/CD Pipeline?

## Types of memory and storage----

## SQL Query execution Order?

## How to design effective and safe APIs?

Use resource names(nouns)
Use Plurals
Idempotency
Use versioning
Query after soft deletion
pagination
Sorting
Filtering
Secure Access
Resource cross reference
Add an item to a cart
Rate limit

## What is SSO? How do we use SSO?

## State system design acronyms.
CAP 
BASE
SOLID
KISS 

## What is availability and partition tolerance?

Availability and partition tolerance are two properties of a distributed system. The CAP theorem states that a distributed system can only provide two of the following properties at the same time: 
* Consistency: How well a system maintains a consistent and accurate view of data or state
* Availability: The ability to access a cluster even if a node in the cluster goes down
* Partition tolerance: The ability to continue functioning even if there is a communication break between two nodes

  
Availability is usually measured as uptime or reliability. It's critical for systems that provide mission-critical services or handle sensitive data. 
Partition tolerance refers to a system's ability to continue functioning despite network partitions or communication breakdowns between nodes. Network partitions happen when communication links between nodes fail, resulting in the system being split into multiple isolated sub-systems.

## Explain CAP with the available combinations.



Consistency means that data is the same across the cluster, so you can read or write from/to any node and get the same data.

Availability means the ability to access the cluster even if a node in the cluster goes down.

Partition tolerance means that the cluster continues to function even if there is a "partition" (communication break) between two nodes (both nodes are up, but can't communicate).

In order to get both availability and partition tolerance, you have to give up consistency. Consider if you have two nodes, X and Y, in a master-master setup. Now, there is a break between network communication between X and Y, so they can't sync updates. At this point you can either:

A) Allow the nodes to get out of sync (giving up consistency), or

B) Consider the cluster to be "down" (giving up availability)

All the combinations available are:

* CA - data is consistent between all nodes - as long as all nodes are online - and you can read/write from any node and be sure that the data is the same, but if you ever develop a partition between nodes, the data will be out of sync (and won't re-sync once the partition is resolved).
* CP - data is consistent between all nodes, and maintains partition tolerance (preventing data desync) by becoming unavailable when a node goes down.






## Other tips
- Memorize non-functional requirements and be quick at back of the envelope calculations. [Use this link](https://gist.github.com/mwakaba2/8ad25dda8c71fe529855994c70743733). QPS and Storage numbers are often more important than others. To arrive at QPS, go from DAU for Product -> DAU for feature -> Read/Write -> Seconds in the day -> QPS.
- Going for L4/E4/Intermediate role: Feel free to ask as many Qs to interviewer as you want. Going for L5/E5/Senior role: Lead the interview, make choices yourself, and provide justifications and just 'confirm' with interviewer you're on the right track.
- First provide a high level design overview with all components you would have, then deep dive into each component and why it is useful, what are its pros and cons.

nodes remain online even if they can't communicate with each other and will resync data once the partition is resolved, but you aren't guaranteed that all nodes will have the same data (either during or after the partition)
