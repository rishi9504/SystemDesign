# What are database locks?
Database locks are mechanisms used in database management systems (DBMS) to manage concurrent access to data by multiple transactions or users. They ensure data consistency and integrity by preventing conflicts that can arise when multiple operations attempt to read, write, or modify the same data simultaneously. Locks help enforce **ACID (Atomicity, Consistency, Isolation, Durability)** properties of transactions.

### Types of Database Locks
Database locks can be categorized based on various criteria:

#### 1. **Locking Granularity**
   - **Row-Level Locks**: Restrict access to specific rows of a table.
   - **Table-Level Locks**: Restrict access to an entire table.
   - **Page-Level Locks**: Restrict access to a data page (a fixed-size chunk of data storage).
   - **Database-Level Locks**: Restrict access to the entire database.

#### 2. **Lock Modes**
   - **Shared Lock (S)**: Allows multiple transactions to read the same data concurrently but prevents writes. Typically used during read operations.
   - **Exclusive Lock (X)**: Prevents other transactions from reading or writing the data. Used for write operations.
   - **Update Lock (U)**: Prevents deadlocks by allowing only one transaction to prepare for an update. It transitions to an exclusive lock when the update is performed.

#### 3. **Duration**
   - **Short-Term Locks (Pessimistic)**: Held for the duration of a single operation.
   - **Long-Term Locks**: Held for the duration of a transaction.

#### 4. **Locking Mechanism**
   - **Pessimistic Locking**: Locks are acquired to prevent conflicts proactively. Transactions wait for locks to be released.
   - **Optimistic Locking**: No locks are used initially; conflicts are detected during the commit phase. Useful in low-contention environments.

---

### Common Scenarios Requiring Locks
- **Read-Write Conflicts**: Ensuring a transaction doesn't read stale or inconsistent data during a write operation.
- **Write-Write Conflicts**: Preventing multiple transactions from updating the same record simultaneously.
- **Deadlock Prevention**: Managing locks to avoid circular waits, which can halt transactions.

---

### Potential Issues with Locks
1. **Deadlocks**: Two or more transactions waiting for each other to release locks.
2. **Lock Contention**: Multiple transactions competing for the same resources, causing delays.
3. **Performance Overhead**: Managing locks incurs additional processing overhead.

Efficient database design and tuning are crucial to minimize lock contention and improve transaction throughput. Techniques like **lock escalation**, **partitioning**, and **indexing** can also reduce the impact of locks.




# What is redis? Explain caching by Redis.
### **What is Redis?**
Redis (Remote Dictionary Server) is an **open-source, in-memory data store** widely used as a cache, database, and message broker. It is designed for high performance, supporting a variety of data structures such as strings, hashes, lists, sets, sorted sets, and more. Redis is known for its speed, scalability, and versatility.

#### **Key Features of Redis**
1. **In-Memory Storage**: Data is stored in memory, making it extremely fast.
2. **Data Persistence**: Supports optional persistence through snapshots (RDB) or append-only files (AOF).
3. **Rich Data Types**: Handles complex data structures like lists, sets, and sorted sets.
4. **High Availability**: Supports replication and clustering for scalability and fault tolerance.
5. **Pub/Sub Messaging**: Built-in support for publish/subscribe messaging patterns.
6. **Atomic Operations**: Ensures data integrity with atomic execution of commands.

---

### **Caching by Redis**
Redis is extensively used for caching to improve application performance by storing frequently accessed or computationally expensive data in memory. This reduces the need to fetch data from slower sources, such as databases or external APIs.

#### **How Caching Works with Redis**
1. **Key-Value Pairs**: Cache data as key-value pairs where the key is a unique identifier, and the value is the data being cached.
   - Example: `{ "user:123": {"name": "Alice", "age": 30} }`
2. **TTL (Time-to-Live)**: Assign expiration times to cache entries to ensure data freshness and manage memory usage.
   - Example: `SET key value EX 60` (sets a key with a 60-second expiration).
3. **Read-Through Cache**: When data isn't found in Redis, the application fetches it from the database, stores it in Redis, and returns it to the user.
4. **Write-Through Cache**: Updates to the database automatically update the cache as well.
5. **Cache-aside Pattern**: The application interacts with Redis first. If the data isn't present, it's fetched from the database and written to Redis for future requests.

---

#### **Advantages of Using Redis for Caching**
1. **Performance**: Significantly reduces latency by serving data from memory.
2. **Scalability**: Redis can handle a large number of requests per second.
3. **Cost Efficiency**: Reduces load on primary databases or external systems.
4. **Data Expiry**: Automatic key expiration ensures the cache remains fresh and doesn't grow indefinitely.
5. **Flexibility**: Allows caching of different data formats and even complex objects.

---

#### **Use Cases for Redis Caching**
1. **Session Storage**: Storing user session data for fast retrieval in web applications.
2. **Database Query Results**: Caching results of expensive database queries.
3. **API Caching**: Storing responses from slow or rate-limited APIs.
4. **Frequently Accessed Configurations**: Storing configuration or reference data that changes infrequently.
5. **Content Delivery**: Caching static resources like images, CSS, or JSON data.

By using Redis for caching, applications can achieve **lower latency**, **higher throughput**, and **better user experiences**, especially in high-traffic systems.

## How to improve API performance?
### **1. Pagination**
Pagination is the process of dividing large datasets into smaller, manageable chunks (pages) that can be fetched or displayed incrementally. It is commonly used in APIs to limit the number of records returned in a single response, enhancing performance and user experience.

- **How It Works**:
  - Clients specify parameters such as page number (`page`) and page size (`limit`) in the API request.
  - Example: `GET /api/products?page=2&limit=10` returns 10 products starting from the 11th.

- **Types of Pagination**:
  - **Offset-Based Pagination**: Uses offset and limit values (e.g., `offset=10&limit=10`).
  - **Cursor-Based Pagination**: Uses a cursor to fetch the next page (e.g., `cursor=abc123`).
  - **Keyset Pagination**: Fetches results based on a specific field value (e.g., `id > 100`).

- **Benefits**:
  - Reduces the load on servers and clients.
  - Improves response times.
  - Enhances usability for large datasets.

---

### **2. Async Logging**
Async (Asynchronous) logging refers to logging operations performed in a non-blocking manner. Instead of writing logs synchronously (which could delay API processing), logs are queued and processed asynchronously in the background.

- **How It Works**:
  - Log messages are placed in an in-memory queue.
  - A separate thread or process consumes the queue and writes logs to the appropriate destination (file, database, monitoring tool).

- **Benefits**:
  - Improves API performance by reducing latency caused by synchronous logging.
  - Prevents application bottlenecks during high traffic.

- **Common Libraries**:
  - Java: Logback, Log4j with async appenders.
  - Python: `concurrent.futures`, `logging.handlers.QueueHandler`.

---

### **3. Caching**
Caching in APIs involves temporarily storing frequently accessed data in a faster storage layer (e.g., memory) to reduce the need for repetitive and expensive data retrieval operations.

- **How It Works**:
  - Cached data is stored using key-value pairs.
  - When a client requests data, the API checks the cache first before querying the database.

- **Types of Caching**:
  - **In-Memory Caching**: Uses tools like Redis, Memcached.
  - **Browser Caching**: Sets HTTP headers like `Cache-Control` or `ETag`.
  - **Distributed Caching**: Used in large-scale applications for sharing caches across multiple servers.

- **Benefits**:
  - Reduces response time.
  - Minimizes server load and database queries.
  - Improves scalability.

---

### **4. Payload Compression**
Payload compression is the process of reducing the size of data (payload) sent over the network in API requests and responses. This reduces bandwidth usage and improves response times.

- **How It Works**:
  - Compression algorithms like Gzip or Brotli compress the payload.
  - The client indicates support for compression via the `Accept-Encoding` header.
  - The server compresses the response if the client supports it and includes the `Content-Encoding` header.

- **Benefits**:
  - Faster data transmission.
  - Reduced bandwidth costs.
  - Better performance for large payloads like JSON or XML.

- **Example**:
  - **Request Header**: `Accept-Encoding: gzip, deflate`
  - **Response Header**: `Content-Encoding: gzip`

---

### **5. Connection Pool**
A connection pool is a collection of reusable database or network connections maintained to serve API requests efficiently. Instead of creating a new connection for each request, connections are reused, reducing overhead.

- **How It Works**:
  - When an API requires a connection (e.g., to a database), it fetches one from the pool.
  - After the request is processed, the connection is returned to the pool for reuse.

- **Benefits**:
  - Reduces latency by avoiding the cost of establishing connections repeatedly.
  - Improves resource utilization and scalability.
  - Helps manage connection limits imposed by external systems (e.g., databases).

- **Common Libraries**:
  - Java: HikariCP, Apache DBCP.
  - Python: SQLAlchemy connection pooling.

---

By implementing these concepts effectively, APIs can achieve higher performance, scalability, and reliability, catering to modern application demands.

## What is a CI/CD Pipeline?

## Types of memory and storage----

## SQL Query execution Order?

## How to design effective and safe APIs?

- Use resource names(nouns)
- Use Plurals
- Idempotency
- Use versioning
- Query after soft deletion
- pagination
- Sorting
- Filtering
- Secure Access
- Resource cross reference
- Add an item to a cart
- Rate limit

## What is SSO? How do we use SSO?

## Describe following terms:

- Throughput
- Response time
- Latency
- Tail latencies
- Service level Objectives (SLO)
- Service Level Agreement (SLA)
- Tail Latency Amplification
- Scaling up
- Scaling down
- Shared nothing Architecture



## Three design principle for System Designs:
- Operability
- Simplicity
- Evolvability

## Possible symptoms of complexity:
page 43 ddia

# Functional requirements
- what should the app do
- data storage
- data retrieval
- data search
- data processing

# types of data models
- relational models
- network models
- hiearchial models


# ployglot persistence

# impedence mismatch

# How exaactly indexing work in the databases

# Twitter arch for assembling home timeline


## What is load parameter in System?

## What is fan out in System Design?



## State system design acronyms.
- CAP 
- BASE
- SOLID
- KISS 

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
