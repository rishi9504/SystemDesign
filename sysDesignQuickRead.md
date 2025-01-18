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

A **CI/CD pipeline** (Continuous Integration/Continuous Deployment or Continuous Delivery pipeline) is a series of automated processes used to build, test, and deploy software applications. It enables developers to deliver code changes more frequently, reliably, and efficiently.

### **Key Concepts in CI/CD**
1. **Continuous Integration (CI)**:
   - Developers integrate code into a shared repository multiple times a day.
   - Automated tools validate the code by running build and test processes.
   - Goal: Catch and resolve errors early in the development cycle.

2. **Continuous Delivery (CD)**:
   - Ensures that the application is always in a deployable state.
   - After successful CI, code changes are automatically prepared for deployment.
   - Deployment to production is triggered manually but is streamlined.

3. **Continuous Deployment**:
   - Extends continuous delivery by automating the deployment to production.
   - Every successful code change is automatically deployed without manual intervention.

---

### **Stages of a CI/CD Pipeline**
A typical CI/CD pipeline involves the following stages:

1. **Source Stage**:
   - Monitors the version control system (e.g., Git) for code changes.
   - Triggers the pipeline when new code is pushed to the repository.

2. **Build Stage**:
   - Compiles the source code into executable artifacts.
   - Ensures that the application can be built successfully.

3. **Test Stage**:
   - Runs automated tests (unit tests, integration tests, and end-to-end tests).
   - Validates functionality, performance, and security.
   - Prevents faulty code from progressing further.

4. **Release Stage**:
   - Packages the built artifacts for deployment (e.g., Docker images, JAR files).
   - May include creating environment-specific configurations.

5. **Deploy Stage**:
   - Deploys the application to different environments (e.g., staging, production).
   - Uses tools like Kubernetes, Terraform, or cloud services for automated deployment.

6. **Monitoring Stage** (Post-Deployment):
   - Tracks application performance and error logs in production.
   - Detects issues early and triggers alerts for rollback or fixes.

---

### **Benefits of a CI/CD Pipeline**
1. **Faster Development Cycles**:
   - Automates repetitive tasks like testing and deployment, enabling faster code releases.
2. **Improved Code Quality**:
   - Automated testing ensures bugs are caught early.
3. **Consistent Deployments**:
   - Reduces human errors by standardizing the deployment process.
4. **Increased Collaboration**:
   - Encourages team members to integrate and test their work frequently.
5. **Reduced Risks**:
   - Incremental updates lower the chance of introducing major issues in production.

---

### **Tools for CI/CD Pipelines**
- **CI Tools**:
  - Jenkins, GitHub Actions, GitLab CI/CD, CircleCI, Travis CI.
  
- **Build Tools**:
  - Maven, Gradle, Webpack.
  
- **Testing Tools**:
  - JUnit, Selenium, Postman, Jest.

- **Deployment Tools**:
  - Kubernetes, Docker, AWS CodePipeline, Terraform.

---

By automating and streamlining the process from code changes to deployment, a CI/CD pipeline empowers development teams to deliver high-quality software quickly and efficiently.


## Types of memory and storage

Memory and storage in computing are fundamental components used to manage and retain data. They differ in speed, purpose, and volatility. Here's an overview of the types of memory and storage:

---

### **1. Memory (Primary Storage)**
Memory refers to the temporary storage that a computer uses to run programs and process data. It is typically volatile, meaning data is lost when the power is turned off.

#### **Types of Memory**
1. **Random Access Memory (RAM)**:
   - **Description**: Fast, temporary storage used to store data that the CPU needs during operation.
   - **Types**:
     - **Dynamic RAM (DRAM)**: Most common; needs periodic refreshing to retain data.
     - **Static RAM (SRAM)**: Faster and more expensive than DRAM; used for cache memory.
   - **Use Cases**: Running applications, operating systems, and temporary data storage.

2. **Read-Only Memory (ROM)**:
   - **Description**: Non-volatile memory that stores firmware or data permanently.
   - **Types**:
     - **PROM**: Programmable ROM that can be written once.
     - **EPROM**: Erasable Programmable ROM, erasable with UV light.
     - **EEPROM**: Electrically Erasable Programmable ROM, erasable using electricity.
   - **Use Cases**: Storing BIOS or firmware.

3. **Cache Memory**:
   - **Description**: High-speed memory located near or inside the CPU.
   - **Levels**: L1, L2, L3 (closer to CPU = faster, smaller in size).
   - **Use Cases**: Storing frequently accessed CPU instructions and data.

4. **Virtual Memory**:
   - **Description**: Disk space used as an extension of RAM when physical RAM is insufficient.
   - **Use Cases**: Supporting large applications or multitasking when RAM is full.

---

### **2. Storage (Secondary Storage)**
Storage refers to non-volatile memory used for long-term data retention, even when the computer is turned off.

#### **Types of Storage**
1. **Hard Disk Drives (HDDs)**:
   - **Description**: Magnetic storage device with spinning platters.
   - **Characteristics**: Large capacity, slower than SSDs, more affordable.
   - **Use Cases**: Storing operating systems, applications, and files.

2. **Solid-State Drives (SSDs)**:
   - **Description**: Storage device with no moving parts; uses NAND flash memory.
   - **Characteristics**: Faster, more durable, and more expensive than HDDs.
   - **Use Cases**: Boot drives, performance-critical applications.

3. **Hybrid Drives (SSHDs)**:
   - **Description**: Combines HDD and SSD features, using SSD for frequently accessed data.
   - **Use Cases**: Mid-performance and cost-conscious storage solutions.

4. **Optical Storage**:
   - **Examples**: CDs, DVDs, Blu-ray discs.
   - **Characteristics**: Uses lasers to read/write data; low capacity compared to modern storage.
   - **Use Cases**: Media distribution, backups.

5. **Flash Storage**:
   - **Examples**: USB drives, memory cards (SD cards).
   - **Characteristics**: Portable, fast, and durable.
   - **Use Cases**: Portable storage, cameras, mobile devices.

6. **Network Attached Storage (NAS)**:
   - **Description**: Storage accessible over a network.
   - **Characteristics**: Provides centralized storage for multiple users.
   - **Use Cases**: File sharing, backups, media servers.

7. **Cloud Storage**:
   - **Description**: Data stored on remote servers accessed via the internet.
   - **Examples**: Google Drive, AWS S3, Dropbox.
   - **Use Cases**: File sharing, backups, scalable storage.

---

### **3. Memory vs. Storage**
| **Aspect**            | **Memory (e.g., RAM)**                   | **Storage (e.g., HDD, SSD)**               |
|------------------------|------------------------------------------|--------------------------------------------|
| **Purpose**            | Temporary data for processing           | Long-term data retention                   |
| **Volatility**         | Volatile (data lost on power-off)        | Non-volatile (data persists)               |
| **Speed**              | Much faster                            | Slower                                     |
| **Capacity**           | Smaller (e.g., 8–64 GB)                | Larger (e.g., 256 GB–several TB)           |
| **Cost**               | Higher per GB                          | Lower per GB                               |

---

Understanding the different types of memory and storage is crucial for selecting the right components for specific use cases, such as performance optimization, data retention, or cost efficiency.

## SQL Query execution Order

### **SQL Query Execution Order**

In SQL, the execution order of a query defines the sequence in which different clauses are processed to retrieve and manipulate data. Although queries are written in a specific syntactical order, the SQL engine processes them in a logical order.

---

### **SQL Query Syntax Order**
When writing a SQL query, the standard syntax order is as follows:
```sql
SELECT [DISTINCT] column1, column2, ...
FROM table_name
JOIN table_name
ON condition
WHERE condition
GROUP BY column
HAVING condition
ORDER BY column
LIMIT number;
```

However, this is **not** the order in which the query is executed.

---

### **Logical Execution Order**
The SQL query is executed in the following order, step by step:

1. **FROM**:
   - The query starts by identifying the tables or views specified in the `FROM` clause.
   - If multiple tables are joined, this step resolves joins, applies any join conditions, and creates a working data set.

2. **ON** (for JOIN operations):
   - If the query involves joins, the `ON` clause is applied to filter the rows while combining tables.
   - This happens as part of the `FROM` processing.

3. **WHERE**:
   - After the base data set is created, the `WHERE` clause filters rows based on specified conditions.
   - Rows that do not meet the condition are excluded.
   - **Key Point**: Aggregate functions (e.g., `SUM`, `COUNT`) cannot be used in the `WHERE` clause.

4. **GROUP BY**:
   - Groups the filtered data into subsets based on one or more columns.
   - This is necessary when using aggregate functions like `SUM`, `AVG`, `COUNT`, etc.
   - **Key Point**: Only columns in the `GROUP BY` clause or aggregate functions can appear in the `SELECT` clause.

5. **HAVING**:
   - Filters grouped data based on conditions applied to aggregate functions or grouped columns.
   - **Key Point**: Unlike `WHERE`, `HAVING` works on grouped data rather than individual rows.

6. **SELECT**:
   - Specifies the columns to include in the output.
   - If the `DISTINCT` keyword is used, duplicate rows are removed at this stage.

7. **ORDER BY**:
   - Sorts the final result set based on one or more columns, in ascending (`ASC`) or descending (`DESC`) order.
   - **Key Point**: Sorting is applied after all filtering and aggregation.

8. **LIMIT**:
   - Restricts the number of rows returned in the result set.
   - Typically used to implement pagination or retrieve a sample of data.

---

### **Example Query Execution**

#### Query:
```sql
SELECT department, COUNT(employee_id) AS employee_count
FROM employees
WHERE salary > 50000
GROUP BY department
HAVING COUNT(employee_id) > 5
ORDER BY employee_count DESC
LIMIT 10;
```

#### Execution Steps:
1. **FROM**: The `employees` table is selected.
2. **WHERE**: Rows where `salary > 50000` are filtered.
3. **GROUP BY**: Remaining rows are grouped by `department`.
4. **HAVING**: Groups with `COUNT(employee_id) > 5` are filtered.
5. **SELECT**: `department` and `COUNT(employee_id)` are included in the result.
6. **ORDER BY**: Results are sorted by `employee_count` in descending order.
7. **LIMIT**: The first 10 rows of the sorted result are returned.

---

### **Execution Flow Visualization**
```plaintext
1. FROM → 2. ON → 3. WHERE → 4. GROUP BY → 5. HAVING → 6. SELECT → 7. ORDER BY → 8. LIMIT
```

---


- The `SELECT` clause is **logically executed last** but written early in query syntax.
- The `WHERE` clause filters rows before aggregation, while `HAVING` filters rows after aggregation.
- Understanding this logical execution order helps in debugging queries, optimizing performance, and avoiding errors.

## How to design effective and safe APIs?

Designing effective and safe APIs involves a combination of good architectural practices, attention to security, and ensuring a user-friendly interface. Here’s a comprehensive guide:

---

### **1. Principles of Effective API Design**

#### **a. Clear and Consistent Design**
- Use **RESTful principles** or other appropriate paradigms (GraphQL, gRPC) based on use cases.
- Use consistent naming conventions (e.g., `camelCase` for JSON fields).
- Follow HTTP standards:
  - Use proper HTTP verbs: `GET` for reading, `POST` for creating, `PUT`/`PATCH` for updating, `DELETE` for deletion.
  - Use appropriate HTTP status codes: `200 OK`, `400 Bad Request`, `401 Unauthorized`, `500 Internal Server Error`, etc.

#### **b. Versioning**
- Maintain backward compatibility by versioning APIs (e.g., `/v1/resource`).
- Prefer URI-based versioning or use headers for version negotiation.

#### **c. Documentation**
- Provide comprehensive and interactive documentation (e.g., Swagger/OpenAPI).
- Include examples, error codes, and expected responses.
- Keep documentation updated with changes.

#### **d. Simplify Usage**
- Avoid overloading endpoints with too many responsibilities.
- Provide filters, sorting, pagination, and search functionality to improve usability.
  - Example: `GET /products?sort=price&filter=category:electronics&page=2`.

#### **e. Provide Meaningful Responses**
- Use JSON or XML (typically JSON) for structured data.
- Include helpful error messages and response metadata (e.g., pagination info).

---

### **2. Principles of Safe API Design**

#### **a. Authentication and Authorization**
- Use secure methods for authentication:
  - **OAuth 2.0** or **JWT (JSON Web Tokens)** for user authentication.
  - API keys for service-to-service communication.
- Enforce role-based access control (RBAC) and least privilege.

#### **b. Rate Limiting and Throttling**
- Prevent abuse with rate limits and quotas.
  - Example: Allow 100 requests per minute per user.
- Return `429 Too Many Requests` when the limit is exceeded.

#### **c. Data Validation and Sanitization**
- Validate and sanitize user input to prevent injection attacks (SQL injection, XSS).
- Use libraries or frameworks for input validation.

#### **d. Use HTTPS**
- Enforce HTTPS to encrypt data in transit and prevent eavesdropping or MITM attacks.
- Redirect HTTP requests to HTTPS.

#### **e. Error Handling**
- Avoid leaking sensitive information in error responses.
- Return generic error messages (`500 Internal Server Error`) for server-side issues while logging detailed errors internally.

#### **f. Secure Sensitive Data**
- Mask sensitive data in responses (e.g., hide full credit card numbers).
- Avoid logging sensitive data like passwords, API keys, or tokens.

#### **g. Prevent Over-Exposure**
- Implement **principle of least privilege**:
  - Restrict access to only the required data.
  - Use fields filtering: `GET /users?fields=id,name`.

#### **h. Implement CORS Policies**
- Configure Cross-Origin Resource Sharing (CORS) policies to restrict which domains can access your API.
  - Example: Allow trusted origins while blocking others.

#### **i. Secure File Uploads**
- Validate uploaded file types and sizes.
- Store files securely, avoiding execution of untrusted content.

---

### **3. Best Practices for Scalability and Reliability**

#### **a. Idempotency**
- Ensure idempotency of `PUT`, `DELETE`, and non-modifying actions (e.g., retries do not cause unexpected behavior).

#### **b. Use Caching**
- Leverage caching mechanisms:
  - **Client-side caching**: Use `Cache-Control` and `ETag` headers.
  - **Server-side caching**: Use tools like Redis or CDN for frequently accessed data.

#### **c. Design for Failure**
- Implement retries with exponential backoff for network errors.
- Provide circuit breakers to avoid cascading failures.

#### **d. API Monitoring**
- Monitor usage and performance through tools like Prometheus, Datadog, or New Relic.
- Log requests and responses, but exclude sensitive information.

#### **e. Asynchronous Processing**
- Offload long-running operations to asynchronous processing systems (e.g., queues or background jobs).

---

### **4. Testing and Iteration**

#### **a. Automated Testing**
- Use unit, integration, and end-to-end tests for your API.
- Validate responses, status codes, and data correctness.

#### **b. Mock APIs**
- Use mock servers during development and testing phases to simulate API behavior.

#### **c. Feedback Loops**
- Gather feedback from developers to improve usability.
- Iterate based on user needs and performance data.

---

### **5. API Lifecycle Management**
- **Deprecation Policy**: Announce deprecations well in advance, providing a migration guide.
- **Backward Compatibility**: Avoid breaking changes unless a new version is released.
- **Monitoring & Analytics**: Track API usage patterns to detect issues and optimize performance.

---

### **6. Example: Well-Designed API Endpoint**
#### **Request**:
```http
GET /users?filter=active:true&page=1&limit=10
Host: api.example.com
Authorization: Bearer <token>
Accept: application/json
```

#### **Response**:
```json
{
  "data": [
    { "id": 1, "name": "Alice", "status": "active" },
    { "id": 2, "name": "Bob", "status": "active" }
  ],
  "meta": {
    "page": 1,
    "limit": 10,
    "total_pages": 5,
    "total_records": 50
  }
}
```

---

By following these principles, you can design APIs that are **user-friendly**, **secure**, **scalable**, and **maintainable** for long-term success.

## What is SSE? How do we use SSE?

### **What is SSE (Server-Sent Events)?**

**Server-Sent Events (SSE)** is a standard protocol that allows a server to send real-time updates to a client over a single HTTP connection. Unlike WebSockets, which enable bi-directional communication, SSE is unidirectional — data flows from the server to the client only.

SSE is ideal for scenarios where the server needs to push real-time updates to clients, such as:
- Live score updates.
- Notifications or alerts.
- Streaming data (e.g., stock prices, logs).

---

### **How SSE Works**
1. **Client Requests Updates**:
   - The client makes an HTTP `GET` request to the server to establish a connection.
2. **Server Sends Updates**:
   - The server keeps the connection open and sends updates in the form of text/event-stream data.
3. **Client Receives Updates**:
   - The client listens for incoming updates and processes them.

---

### **Key Features of SSE**
1. **Text-Based Protocol**:
   - Data is sent in plain text format with a specific structure.
2. **Automatic Reconnection**:
   - The client automatically attempts to reconnect if the connection is lost.
3. **Event Filtering**:
   - Events can be assigned names, and the client can listen to specific events.

---

### **Using SSE**

#### **Server-Side Implementation**
The server must:
- Set the `Content-Type` header to `text/event-stream`.
- Send data in a specific format.
- Keep the connection open.

**Example: Node.js Server with SSE**
```javascript
const http = require('http');

http.createServer((req, res) => {
  if (req.url === '/events') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive'
    });

    // Send initial event
    res.write('data: Welcome to SSE\n\n');

    // Send periodic updates
    const interval = setInterval(() => {
      const message = `data: Current time is ${new Date().toISOString()}\n\n`;
      res.write(message);
    }, 1000);

    // Cleanup on client disconnect
    req.on('close', () => {
      clearInterval(interval);
    });
  } else {
    res.writeHead(404);
    res.end();
  }
}).listen(3000, () => console.log('Server running on http://localhost:3000'));
```

---

#### **Client-Side Implementation**
The client uses the **EventSource API** to listen for server-sent events.

**Example: HTML/JavaScript Client**
```html
<!DOCTYPE html>
<html>
<head>
  <title>SSE Example</title>
</head>
<body>
  <h1>Server-Sent Events</h1>
  <div id="updates"></div>

  <script>
    const eventSource = new EventSource('/events');

    // Listen for default events
    eventSource.onmessage = (event) => {
      const updates = document.getElementById('updates');
      updates.innerHTML += `<p>${event.data}</p>`;
    };

    // Handle errors
    eventSource.onerror = () => {
      console.error('Error with SSE connection.');
      eventSource.close();
    };
  </script>
</body>
</html>
```

---

### **SSE Data Format**
The server sends messages in the following format:
```plaintext
id: 1         // Optional: Event ID for reconnection.
event: update // Optional: Event name.
data: Hello, World! // Required: Actual event data.

\n // Blank line indicates the end of the message.
```

**Example of SSE Data Stream**:
```plaintext
id: 1
event: news
data: {"title": "Breaking News", "content": "Server-Sent Events are amazing!"}

id: 2
data: Another update from the server.
```

---

### **When to Use SSE**
SSE is a good choice when:
1. **Real-Time Updates**:
   - Applications need live updates from the server, such as notifications or live scores.
2. **Low Client Interaction**:
   - The communication is mostly one-way (server to client).
3. **Fallback Simplicity**:
   - SSE works well with HTTP and doesn't require special configurations like WebSockets.

---

### **Advantages of SSE**
1. **Ease of Use**:
   - Works over standard HTTP; no need for additional protocols.
2. **Automatic Reconnection**:
   - Built-in client-side reconnection mechanism.
3. **Efficient**:
   - Suitable for lightweight, server-to-client communication.

---

### **Limitations of SSE**
1. **Unidirectional**:
   - Data flows only from the server to the client; for bi-directional communication, WebSockets may be better.
2. **Browser Support**:
   - SSE is widely supported but not available in all environments (e.g., IE).
3. **Scalability**:
   - Long-lived connections can be resource-intensive for the server, especially with many clients.
4. **HTTP/2 Compatibility**:
   - Although SSE works over HTTP/2, WebSockets might take better advantage of HTTP/2's multiplexing capabilities.

---

### **SSE vs WebSockets**

| Feature                  | SSE                                  | WebSockets                            |
|--------------------------|---------------------------------------|---------------------------------------|
| **Direction**            | Unidirectional (server to client).   | Bidirectional.                        |
| **Protocol**             | HTTP (text/event-stream).            | Custom protocol over TCP.             |
| **Reconnection**         | Automatic.                          | Needs manual implementation.          |
| **Use Case**             | Real-time server-to-client updates.  | Interactive apps (e.g., chat).        |

---

SSE is a lightweight and powerful tool for real-time data delivery when you need unidirectional updates without the complexity of WebSockets.


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
 - SSTable
 - memtable
 - log structure merge tree
 - clustered index
 - multi dimensional indexes, why they are good for geospatial data
 - R trees in POSTGres
 - difference between oltp and olap
 




## State system design acronyms.
 
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
