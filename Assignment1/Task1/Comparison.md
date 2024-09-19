# ServerLess Functions

|  | AWS | Azure  | GCP |
| --- | --- | --- | --- |
| Programming Language  |  Supports a wide range of languages including Node.js, Python, Java, C#, Go, Ruby, and **custom runtimes.** | Supports C#, JavaScript, F#, Java, PowerShell, Python, and TypeScript. |  Supports a wide range of languages including Node.js, Python, Java, C#, Go, Ruby, and custom runtimes. |
|  | 1 | 2 | 3 |
| Execution Time | 15 min | 10 MIN or **Unlimited**  | 9 Min |
| Memory Allocation | 128 MB to 10 GB | 128 MB to 14 GB | 128 MB to 8 GB |
| Integration with Other Services | 1 | 2 | 3 |
| Cold Start Performance |  |  |  |
| Deployment and Packaging | 10 GB | 15 GB | 4GB |

| Feature | AWS Lambda | Azure Functions | Google Cloud Functions |
| --- | --- | --- | --- |

| **Cold Start Latency** | Milliseconds to a few seconds, **Provisioned Concurrency** available to reduce cold starts | Noticeable in consumption plan; **Premium Plan** or **Dedicated Plan** reduces it | Generally faster, no **Provisioned Concurrency** feature |
| --- | --- | --- | --- |

| **Languages Supported** | Node.js, Python, Ruby, Java, Go, .NET, custom via containers | C#, JavaScript, F#, Python, Java, PowerShell, custom runtimes | Node.js, Python, Go, Java, C#, Ruby, PHP, custom via containers |
| --- | --- | --- | --- |

| **Pricing** | Free tier: 1M requests, 400,000 GB-seconds; pay for requests and duration | Free tier: 1M executions, 400,000 GB-seconds; pay for execution time | Free tier: 2M invocations, 400,000 GB-seconds, 200,000 CPU-seconds; pay for invocations, memory |
| --- | --- | --- | --- |

| **Execution Timeout** | 15 minutes | 5 minutes (consumption plan), unlimited (premium/dedicated) | 9 minutes |
| --- | --- | --- | --- |

| **Concurrency Limits** | 1,000 concurrent executions, soft limit (can increase) | No direct limit, but execution rates can be throttled | 1,000 concurrent requests per region (can increase) |
| --- | --- | --- | --- |

| **Triggers and Event Sources** | S3, API Gateway, DynamoDB, CloudWatch, EventBridge, and more | HTTP, Azure Storage, Event Grid, Service Bus, and more | HTTP, Cloud Pub/Sub, Cloud Storage, Firebase, and more |
| --- | --- | --- | --- |

| **Scaling** | Automatic scaling; **Provisioned Concurrency** for predictable scaling | Automatic scaling; more control with premium/dedicated plans | Automatic scaling, region-dependent; no **Provisioned Concurrency** |
| --- | --- | --- | --- |

| **Deployment and Management** | Versioning, aliases, integrates with AWS CodeDeploy for blue/green deployments | Supports deployment slots, integrates with Azure DevOps | Versioning, integrates with Google Cloud Build for CI/CD |
| --- | --- | --- | --- |

| **Custom Domains & API Management** | Supported via API Gateway (caching, throttling, security) | Custom domains and Azure API Management for advanced routing | Custom domains via Cloud Endpoints or API Gateway |
| --- | --- | --- | --- |

| **Monitoring and Logging** | Integrated with CloudWatch for logging, metrics, and monitoring | Logs/metrics via Azure Monitor, Application Insights | Integrated with Stackdriver for logging and metrics |
| --- | --- | --- | --- |

| **Networking** | Supports VPC integration for private subnet access | VNet integration for accessing resources in Azure Virtual Network | VPC connectors for secure access within Google Cloud VPC |
| --- | --- | --- | --- |

| **Security** | IAM roles, KMS encryption, VPC security features | Managed identities for Azure resources, network isolation, encryption at rest | IAM for access control, integrates with Google KMS, VPC security |
| --- | --- | --- | --- |

DynamoDB

### Comparison of AWS, Google, and Azure Serverless NoSQL Offerings

| Feature | **AWS DynamoDB** | **Google Cloud Firestore** | **Azure Cosmos DB** |
| --- | --- | --- | --- |
| **Scalability** | - Auto-scaling tables- Global tables for cross-region replication | - Automatic scaling- Multi-region replication | - Auto-scaling- Global distribution with geo-replication |
| **Performance** | - Single-digit millisecond read/write latencies | - Low-latency reads, especially when using regional replication | - Multi-master writes with low-latency reads globally |
| **Consistency Models** | - Strong consistency (for the same region) or eventual consistency | - Offers both strong and eventual consistency | - Tunable consistency models (5 levels from strong to eventual) |
| **Data Model Flexibility** | - Key-value and document store- Schema-less | - Document-oriented store- Schema-less, but supports structured documents | - Multi-model: Key-value, document, and graph databases- Schema-less |
| **Data Storage Limits** | - No specific limits on storage size | - No upper storage limits | - Scales to petabytes of storage |
| **Security** | - Encryption at rest and in transit- Fine-grained access control (IAM) | - Encryption at rest and in transit- Access control via IAM | - Encryption at rest and in transit- Role-based access control and VNet integration |
| **Cost** | - Pay-per-request (read/write units)- Reserved capacity pricing- Free tier available | - Pay-as-you-go pricing- Free usage tier- Operations-based pricing model | - Pay-as-you-go pricing- Free tier available- Various throughput and request unit pricing |
| **Integrations** | - Integrated with AWS Lambda, CloudWatch, etc.- Streams for real-time data processing | - Integrated with Firebase, Google Compute Engine, etc. | - Integrated with Azure Functions, Logic Apps, Power BI, etc.- Strong analytics and ML support |
| **Availability and Durability** | - 99.999% availability for multi-region- Automatic replication across regions | - 99.999% availability with multi-region setup- Automatic replication | - 99.999% multi-region availability- Multi-region replication |
| **Developer Experience** | - Comprehensive SDKs for various programming languages- Easy integration with AWS services | - Easy integration with Google Cloud and Firebase services- Real-time updates | - Multi-API support (SQL, MongoDB, Cassandra, Gremlin)- SDKs for multiple languages and real-time updates |