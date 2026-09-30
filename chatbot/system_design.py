system_design = [
    (
        r"(?:what is|explain) system design[?.! ]*", 
            "System design chooses components, data flow, and trade-offs so a service meets its functional and operational needs."
    ),
    (
        r"(?:what is|explain) (?:a )?load balancer[?.! ]*", 
            "A load balancer distributes requests across healthy service instances."
    ),
    (
        r"(?:what is|explain) (?:a )?cache[?.! ]*", 
            "A cache stores frequently needed data closer to callers to reduce latency and backend work."
    ),
    (
        r"(?:what is|explain) cache invalidation[?.! ]*", 
            "Cache invalidation removes or refreshes stale entries when source data changes or a time limit expires."
    ),
    (
        r"(?:what is|explain) (?:a )?cdn[?.! ]*", 
            "A content delivery network serves cached content from locations closer to users."
    ),
    (
        r"(?:what is|explain) (?:a )?database index[?.! ]*", 
            "An index speeds up selected queries but costs storage and extra work on writes."
    ),
    (
        r"(?:what is|explain) (?:a )?replica(?:tion)?[?.! ]*", 
            "Replication copies data to another node for availability or read capacity, depending on the design."
    ),
    (
        r"(?:what is|explain) (?:a )?shard(?:ing)?[?.! ]*", 
            "Sharding partitions data across nodes to spread storage and request load."
    ),
    (
        r"(?:what is|explain) horizontal scaling[?.! ]*", 
            "Horizontal scaling adds more instances to share work."
    ),
    (
        r"(?:what is|explain) vertical scaling[?.! ]*", 
            "Vertical scaling gives an existing machine more CPU, memory, or storage."
    ),
    (
        r"(?:what is|explain) (?:a )?message queue[?.! ]*", 
            "A message queue buffers work so producers and consumers can run at different speeds."
    ),
    (
        r"(?:what is|explain) (?:a )?rate limit(?:er|ing)?[?.! ]*", 
            "Rate limiting caps requests over time to protect resources and enforce fair use."
    ),
    (
        r"(?:what is|explain) idempotency[?.! ]*", 
            "An idempotent operation has the same intended effect when repeated as when performed once."
    ),
    (
        r"(?:what is|explain) (?:a )?retry[?.! ]*", 
            "A retry repeats a failed request; use limits and backoff to avoid worsening outages."
    ),
    (
        r"(?:what is|explain) exponential backoff[?.! ]*", 
            "Exponential backoff increases the wait between retries, usually with jitter to spread out clients."
    ),
    (
        r"(?:what is|explain) (?:a )?circuit breaker[?.! ]*", 
            "A circuit breaker temporarily stops calls to a failing dependency and later probes for recovery."
    ),
    (
        r"(?:what is|explain) latency[?.! ]*", 
            "Latency is the time a request takes from start to response."
    ),
    (
        r"(?:what is|explain) throughput[?.! ]*", 
            "Throughput is the amount of work completed per unit of time."
    ),
    (
        r"(?:what is|explain) availability[?.! ]*", 
            "Availability is the proportion of time a service is usable according to its target definition."
    ),
    (
        r"(?:what is|explain) (?:an )?slo[?.! ]*", 
            "An SLO is a measurable target for service reliability, such as a request success rate."
    ),
    (
        r"(?:what is|explain) eventual consistency[?.! ]*", 
            "Eventual consistency means replicas may temporarily disagree but converge if updates stop."
    ),
    (
        r"(?:what is|explain) (?:the )?cap theorem[?.! ]*", 
            "CAP says that during a network partition, a distributed data system must trade off consistency and availability."
    ),
    (
        r"(?:what is|explain) (?:a )?single point of failure[?.! ]*", 
            "A single point of failure is a component whose outage can take down the whole service."
    ),
    (
        r"(?:what is|explain) observability[?.! ]*", 
            "Observability uses signals such as logs, metrics, and traces to understand system behavior."
    ),
]