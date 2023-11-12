# Postmortem: Website SQL Database Outage

## Issue Summary:

**Duration:**
- Start Time: 10:00PM [10/10/2022] EAT
- End Time: 9:00AM [11/10/2022] EAT

**Impact:**
- The website experienced a complete outage for 11 hours.
- Users were unable to access the website during this time.
- Approximately 40% of users were affected.

## Timeline:

**Detection Time:**
- The issue was detected on 10:00PM [10/10/2022] EAT through automated monitoring alerts.

**Actions Taken:**
- Initial investigations focused on the web server, load balancer, and network connectivity.
- Assumed root cause: Potential server overload due to increased traffic.

**Misleading Paths:**
- Investigated potential DDoS attack due to a recent spike in traffic, which led to unnecessary time spent on network-level defenses.

**Escalation:**
- The incident was escalated to the Database Operations team after confirming that the issue was related to the SQL database.

**Resolution:**
- Identified a critical issue in the database server where the SQL service was unresponsive.
- The problem was resolved by restarting the SQL database service.

## Root Cause and Resolution:

**Root Cause:**
- The SQL database server experienced a deadlock situation, causing the service to become unresponsive.
- This deadlock was triggered by a poorly optimized database query in a critical application module.

**Resolution:**
- The immediate fix involved restarting the SQL service to clear the deadlock and restore normal operations.
- A long-term solution includes optimizing the problematic database query and implementing preventive measures to avoid similar deadlocks in the future.

## Corrective and Preventative Measures:

**Improvements/Fixes:**
- Implement thorough code reviews to identify and optimize resource-intensive database queries.
- Enhance monitoring capabilities to detect early signs of database performance issues.
- Conduct regular performance testing to identify potential bottlenecks before they impact production.

**Tasks to Address the Issue:**
- Conduct a comprehensive review of all critical application modules for potential performance improvements.
- Enhance monitoring by adding alerts for SQL database response time and deadlock occurrences.
- Schedule regular performance testing sessions to proactively identify and address potential issues before they impact users.

## Visual representation of the postmortem

| Start                    |
|--------------------------|
| Issue Detected           |
| (Monitoring Alert)       |
|--------------------------|
| Initial Investigation    |
| (Web Server, Load         |
| Balancer, Network)        |
|--------------------------|
| Assumed Root Cause:       |
| Server Overload           |
|--------------------------|
| Misleading Paths:         |
| - DDoS Investigation     |
|--------------------------|
| Escalation to Database    |
| Operations Team           |
|--------------------------|
| Database Investigation   |
| - Deadlock Identified     |
|--------------------------|
| Resolution               |
| - Restart SQL Service     |
|--------------------------|
| Root Cause Analysis      |
| - Poorly Optimized        |
|   Database Query          |
|--------------------------|
| Long-term Solution:       |
| - Optimize Database       |
|   Query                   |
|--------------------------|
| Corrective and            |
| Preventative Measures:    |
| - Code Reviews            |
| - Enhanced Monitoring     |
| - Performance Testing     |
|--------------------------|
| End                      |
|--------------------------|
