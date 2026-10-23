In this task, I learned about client-server communication, URLs, HTTP methods, status codes, headers, JSON, API keys and rate limits.

1. Client and Server

A device or application that sends a request, such as a browser or mobile application. A request is received by a server and processed by it and a response is sent back to the server. For instance, if I log in to a website, I send my logins to the website server which checks them and sends me a response.

2. URL Anatomy

URL is the network location of a resource on the World Wide Web. It is composed of various segments such as protocol, domain, port, path, query string and fragment. For example, in https://example.com/users?id=10, HTTPS is the protocol, example.com is the domain, /users is the path, and id=10 is a query parameter.

3. HTTP Methods

HTTP methods used to do various things on a server. GET - used for data retrieval, POST - used for data submission, PUT - used for data update/replacement, DELETE - used for data deletion.

4. HTTP Status Codes

Status codes allow us to know if the request was successful or not. 2xx codes are considered successful, e.g. 200 OK and 201 Created. 4xx indicates an error in the request made by the client, for example, 400 Bad Request, 401 Unauthorized and 404 Not Found. 5xx codes are server errors like 500 Internal Server Error, or 503 Service Unavailable.

5. Headers and JSON Bodies

Headers: These are additional pieces of information for a request or response. For instance, Content-Type will indicate to the server what type of data is being passed. JSON is a format used to exchange data between applications. It has key-value pairs and is used in API request and response.

6. API Keys

An API key is a key to identify an application or control its access to an API. Assists the server in verifying requests. API keys should not be shared or posted publicly, and must be securely stored. They can be stored in environment variables or a .env file.

7. Rate Limits

The rate limiting mechanism is used to limit the number of requests that can be made to an API within a given time period. The server might return a 429 Too Many Requests error message if the number of requests exceeds, as the server may only be able to handle a limited number of requests. Rate limits can be accommodated by waiting and making retries, implementing the Retry-After header, implementing exponential backoff and caching previously received data and eliminating unnecessary API calls.

Through this task, I understood how APIs allow applications to communicate with servers and how HTTP methods, status codes and rate limits help us work with APIs properly.