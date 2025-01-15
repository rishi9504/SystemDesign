## Vectorized processing in DataBases

## encoding (also known as serialization or marshalling)

## decoding (parsing, deserialization, unmarshalling).

## Protocol Buffers

## Thrift

## Avro

## writer and reader schema in Avro

## RPC Framework

## asynchronous message-passing systems

- message brokers are used as follows: one process sends a message to a named
queue or topic, and the broker ensures that the message is delivered to one or more
consumers of or subscribers to that queue or topic. There can be many producers and
many consumers on the same topic.

- A key design goal of a service-oriented/microservices architecture is to make the
application easier to change and maintain by making services independently deploya‐
ble and evolvable

- REST is not a protocol, but rather a design philosophy that builds upon the principles
of HTTP. It emphasizes simple data formats, using URLs for identifying
resources and using HTTP features for cache control, authentication, and content
type negotiation

## Shared memory architecture
## Shared disk architecture
## Shared nothing architecture
## semi-synchronous config
## read-after-write consistency, also known as read-your-writes consistency


- Replication means keeping a copy of the same data on multiple machines that are
connected via a network
-  three popular algorithms for replicating changes
between nodes: single-leader, multi-leader, and leaderless replication

- Every write to the database needs to be processed by every replica; otherwise, the rep‐
licas would no longer contain the same data. The most common solution for this is
called leader-based replication (also known as active/passive or master–slave replica‐
tion)
- An important detail of a replicated system is whether the replication happens syn‐
chronously or asynchronously.

- Handling a failure of the leader is trickier: one of the followers needs to be promoted
to be the new leader, clients need to be reconfigured to send their writes to the new
leader, and the other followers need to start consuming data changes from the new
leader. This process is called failover




















