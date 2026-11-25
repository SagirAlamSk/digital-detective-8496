# Mission 7 — How Computers Communicate

## 1. Task / Objective

The objective of this mission was to understand how computers communicate over networks, learn important networking concepts, and observe how network communication works using Terminal commands.

The mission focused on:

- Understanding LAN, MAN and WAN.
- Learning about DNS, routers, protocols and packet switching.
- Understanding the client-server model.
- Testing network connectivity using `ping`.
- Finding domain-related IP addresses using `nslookup` and `dig`.
- Explaining what happens when a user opens a website in a browser.

## 2. Work Completed

I completed the practical network connectivity and DNS lookup activities using macOS Terminal.

The following activities were performed:

1. Checked the Git repository status before starting the mission.
2. Reviewed the recent Git commit history.
3. Opened the `mission-07-networking` directory.
4. Created an `evidence` directory for mission-related evidence.
5. Used the `ping` command to test connectivity with `example.com`.
6. Used `nslookup` to retrieve the IP addresses associated with `example.com`.
7. Used `dig` to inspect DNS query information and understand the response.
8. Studied the basic networking concepts and how a browser communicates with a web server.

The connectivity test successfully received all four packets, with no packet loss.

The DNS lookup returned two IPv4 addresses for `example.com`, and the `dig` command successfully completed the DNS query.

## 3. Commands / Tools Used

| Command / Tool | Purpose | Observation |
|---|---|---|
| `cd` | Navigate between directories. | Used to enter the assignment repository and Mission 7 folder. |
| `mkdir -p` | Create a directory, including parent directories if required. | Created the `evidence` directory. |
| `git status` | Check the current repository state. | The repository was clean and up to date with `origin/main`. |
| `git log -3 --oneline` | Display recent commits in a compact format. | Confirmed the latest Git history before starting Mission 7. |
| `ping -c 4 example.com` | Test network connectivity by sending four packets. | All four packets were received successfully with 0% packet loss. |
| `nslookup example.com` | Retrieve DNS information for a domain. | Returned two IPv4 addresses for the domain. |
| `dig example.com` | Perform a detailed DNS query. | Returned a successful DNS response with status `NOERROR`. |

### Ping command observation

Command used:

`ping -c 4 example.com`

Results:

- Packets transmitted: 4
- Packets received: 4
- Packet loss: 0%
- Minimum response time: 7.412 ms
- Average response time: 17.595 ms
- Maximum response time: 32.139 ms

This showed that my computer could successfully communicate with the destination during the test.

### DNS lookup observation

Command used:

`nslookup example.com`

The lookup returned two IPv4 addresses:

- `104.20.23.154`
- `172.66.147.243`

The DNS query was handled using the configured DNS resolver.

### Detailed DNS observation

Command used:

`dig example.com`

Important results:

- Query status: `NOERROR`
- Query type: `A`
- Answer records: 2
- Query time: 45 ms
- DNS response: Successful

The `A` record provides an IPv4 address associated with a domain name.

The results demonstrate that DNS can return multiple addresses for a single domain.

## 4. My Understanding

### 4.1 Network Concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN (Local Area Network) | A network that connects devices within a limited geographical area. | Computers connected within a college computer laboratory. |
| MAN (Metropolitan Area Network) | A network that connects multiple smaller networks across a city or large metropolitan area. | A network connecting different branches of an organisation across a city. |
| WAN (Wide Area Network) | A network that connects devices and smaller networks across large geographical distances. | The Internet. |
| DNS (Domain Name System) | DNS translates human-readable domain names into IP addresses that computers use to locate servers. | Translating `example.com` into an IP address. |
| Router | A networking device that connects different networks and forwards data packets towards their destinations. | A home Wi-Fi router connecting devices to the Internet. |
| Protocol | A set of rules that devices follow to exchange information over a network. | HTTP, HTTPS and TCP/IP. |
| Packet Switching | A communication method in which data is divided into smaller packets that travel through a network and are reassembled at the destination. | Loading a webpage through the Internet. |
| Client-Server | A networking model where a client requests a resource or service and a server responds to that request. | A web browser requesting a webpage from a web server. |

### 4.2 Understanding Network Connectivity

The `ping` command helped me understand how a computer checks whether another device or server is reachable over a network.

It sends ICMP Echo Request packets to the destination and waits for ICMP Echo Reply packets.

In my test, all four packets were successfully received. This indicated that the destination was reachable during the test and that there was no packet loss in those four requests.

The response time also helped me understand network latency. The average response time was approximately 17.595 milliseconds.

However, a successful ping does not necessarily mean that every service on a website is working correctly. It only confirms that the destination responded to the ICMP connectivity test.

### 4.3 Understanding DNS

DNS works like a directory for the Internet.

People generally remember website names more easily than numerical IP addresses. DNS allows users to enter a domain name instead of manually remembering the server's IP address.

I used both `nslookup` and `dig` to investigate DNS.

`nslookup` provided a straightforward DNS lookup, while `dig` displayed more detailed information, including the query status, answer section, record type and query time.

Both commands successfully retrieved DNS information for `example.com`.

### 4.4 What Happens When a Website Opens?

When someone enters a website address into a browser, several networking operations happen behind the scenes.

1. **User enters a website address:** The user types a domain name into the browser, which acts as the client.

2. **DNS resolution:** The computer obtains the IP address associated with the domain name using DNS. It may first check cached DNS information before making a new query.

3. **Network communication:** The computer sends network traffic through its network connection and router towards the destination server.

4. **Connection establishment:** Depending on the protocol, the client establishes a connection with the server. For HTTPS, this also involves establishing a secure TLS connection.

5. **HTTP request:** The browser sends an HTTP request to the web server asking for the requested webpage or resource.

6. **Server response:** The server processes the request and sends an HTTP response containing the requested content or an appropriate error.

7. **Browser displays the website:** The browser processes the returned HTML, CSS, JavaScript and other resources to display the webpage to the user.

This process demonstrates how clients, servers, DNS, routers and communication protocols work together to make websites accessible.

## 5. Difficulties Faced

No major difficulties were encountered during the practical activities.

The network connectivity test and DNS lookup commands executed successfully.

One important observation was that DNS can return multiple IP addresses for the same domain. I initially expected a domain to have only one address, but the lookup results showed otherwise.

## 6. How I Resolved Them

I compared the results of `nslookup` and `dig` to understand why multiple addresses were returned.

I also examined the answer section of the `dig` output and identified the `A` records.

This helped me understand that a domain can resolve to multiple IP addresses, depending on how its DNS records are configured.

The successful `ping` test provided additional evidence that network communication with the example domain was working during the test.

## 7. Evidence / Files

The following files and evidence belong to this mission:

| File / Directory | Purpose |
|---|---|
| `README.md` | Complete Mission 7 documentation, including networking concepts, commands, observations and explanations. |
| `evidence/` | Directory reserved for privacy-safe screenshots or selected Terminal outputs. |

### Practical evidence recorded

- Successful four-packet connectivity test using `ping`.
- Successful domain lookup using `nslookup`.
- Detailed DNS query response using `dig`.
- Git repository status and recent commit history before starting the mission.

No personal IP addresses, private network information or sensitive computer details are intentionally included.

## 8. Commit Details

**Suggested commit message:**

`Explain networking concepts and website communication`

The mission documentation should be staged and committed separately, then pushed to the GitHub repository.

**Repository:** `digital-detective-8496`

**Branch:** `main`

**Commit status:** Pending the Mission 7 documentation commit and push.

