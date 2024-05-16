The site design will address the following:
• What belongs inside each layer?
• What is passed between layers?
• Can we change/add/delete code later without breaking anything?
• If something breaks, how do I find and fix it?
• What about security?
• Can the site scale and perform well?
• Can we keep all this as clear and simple as possible?
• Why do I ask so many questions? Why, oh why?

When designing a website, you could start from one of the following:
• The Web layer and work down
• The Data layer and work up
• The Service layer and work out in both directions

RESTful designs have these core components:
    Resources
        The data elements your application manages
    IDs
        Unique resource identifiers
    URLs
        Structured resource and ID strings
    Verbs or actions
        Terms that accompany URLs for different purposes:
        GET
            Retrieve a resource.
        POST
            Create a new resource.
        PUT
            Completely replace a resource.
        PATCH
            Partially replace a resource.
        DELETE
            Resource goes kaboom.

    verb /resource/
        Apply verb to all resources of type resource.
    verb /resource/id
        Apply verb to the resource with ID id.

    web requests often carry more information, indicating to do the following:
        • Sort results
        • Paginate results
        • Perform another function

- Project Structure
src
    Contains all the website code
    web
        The FastAPI web layer
    service
        The business logic layer
    data
        The storage interface layer
    model
        Pydantic model definitions
    fake
        Early hardwired (stub) data
Each of these directories will soon gain three files:
__init__.py
    Needed to treat this directory as a package
creature.py
    Creature code for this layer
explorer.py
    Explorer code for this layer

FastAPI’s dependency injection is particularly useful here. Data may come from dif‐
ferent parts of the HTTP message, and you’ve already seen how you can specify one
or more of these dependencies to say where the data is located:
    Header
        In the HTTP headers
    Path
        In the URL
    Query
        After the ? in the URL
    Body
        In the HTTP body
Other, more indirect, sources include the following:
• Environment variables
• Configuration settings

Multiple Routers - APIRouter
    src/web/explorer.py

=== Now Start the Project ===
1. Define Data Models model/explorer.py, creature.py --- MOdel Explorer, Creature
2. Create Database - Fake Data fake/explorer.py(Explorer) - functions(CRUD,URL VERBs(get, post, patch, put, delete)), creature.py - fake data(Creature)
3. Sub Route - web/explorer, creature
4. Pagination and Sorting
    ex:
        Sort
            GET /explorer?sort=country: Get all explorers, sorted by country code.
        Paginate
            GET /explorer?offset=10&size=10: Return (in this case, unsorted) explorers in
            places 10 through 19 of the whole list.
        Both
            GET /explorer?sort=country&offset=10&size=10
    Although you could specify these as individual query parameters, FastAPI’s dependency injection can help:
    • Define the sort and paginate parameters as a Pydantic model.
    • Provide the parameters model to the get_all() path function with the Depends
    feature in the path function arguments.

=== Web layer(interface) -> SERVICE layer -> Data Layer
Whenever a function in the Web layer needs data that is managed by the Data layer,
that function should ask the Service layer to be an intermediary. This requires more
code and may seem unnecessary, but it’s a good idea
it talks to the Data layer, but in a hushed voice so the Web layer doesn’t know exactly what it’s
saying. But it also defines any specific business logic, such as interactions between
resources. Mainly, the Web and Data layers should not care what’s going on in there.
(The Service layer is a Secret Service.)

The SERVICE layer is the heart of the website, its reason for being. It takes requests
from multiple sources, accesses the data that is the DNA of the site, and returns
responses.
Common service patterns include a combination of the following:
• Create / retrieve / change (partially or completely) / delete
• One thing / multiple things
At the RESTful router layer, the nouns are resources.

=== Other Service-Level Stuff ===
here are some technical site-helper ideas
    • Logging - FastAPI logs each API call to an endpoint—including the timestamp, method, and
URL—but not any data delivered via the body or headers.
    • Metrics - Popular metrics tools nowadays include Prometheus for gathering metrics and
Grafana for displaying metrics.
    • Monitoring
    • Tracing - A new open source project has taken earlier tracing products like Jaeger and branded
them as OpenTelemetry. It has a Python API and at least one integration with
FastAPI.

=== Real DATA layer ===
- SQLite - DB-API
Missing & Data Existance -- errors.py

=== Authentication and Authorization ===  --- Security Section
Authentication - Who are you?
    Username/email and password
        Using classic HTTP Basic and Digest Authentication
    API key
        An opaque long string with an accompanying secret
    OAuth2
        A set of standards for authentication and authorization
    JavaScript Web Tokens (JWT)
        An encoding format containing cryptographically signed user information
    
    --- implementation
    - simple one - auth.py
    - oauth2     - web/user.py, User Model, User Data Layer, User Service Layer, User Web Layer ---> main.py(Top Layer)

    - pip install
        JWT handling
            pip install python-jose[cryptography]
        Secure password handling
            pip install passlib
        Form handling
            pip install python-multipart

Authorization  - What do you want?
    User-Admintable, UserPermission table(access control-Read Only, Read, Write), UserRole

MiddleWare
    FastAPI enables insertion of code at the Web layer that does the following:
        • Intercepts the request
        • Does something with the request
        • Passes the request to a path function
        • Intercepts the response returned by the patch function
        • Does something with the response
        • Returns the response to the caller
    In some cases, you could use either middleware or dependency injection with Depends().
    Middleware is handier for more global security issues like CORS,

CORS - Cross Origin Resource sharing

=== Test ===
automated testing - pytest/Unit Tests
• TypeError may be the closest, because None is a different type than Creature.
• ValueError is more suited for the wrong value for a given type, but I guess you could say that passing a missing string id to get_one(id) qualifies.
• You could define your own MissingError if you really want to.

• Some manual tests as you’re first writing the code
• Unit tests after you’ve fixed Python syntax errors
• Full tests after you have a full data flow across all layers

pip install pytest OR pip install pytest-mock   ### to get the automatic mocker fixture

set environment variable CRYPTID_UNIT_TEST for the pytest - fixture

- Automated Integration Tests
Integration tests show how well different code interacts between layers. But if you
look for examples of this, you get many different answers. Should you test partial call
trails like Web → Service, Web → Data, and so on?

To fully test every connection in an A → B → C pipeline, you’d need to test the following: (MOCK test)
• A → B
• B → C
• A → C

- Automated Full Tests
You can fully test each endpoint in the overall API in two ways:
    Over HTTP/HTTPS
        Write individual Python test clients that access the server. Many examples in this
        book have done this, with standalone clients like HTTPie, or in scripts using
        Requests.
    Using TestClient
        Use this built-in FastAPI/Starlette object to access the server directly, without an
        overt TCP connection.

Two packages are needed:
    Hypothesis
        pip install hypothesis
    Schemathesis
        pip install schemathesis

Run Schemathesis tests
     chemathesis http://localhost:8000/openapi.json

- Security Testing
Use Schemathesis, and Ref its Documentation - https://schemathesis.readthedocs.io/en/stable/auth.html

- Load Testing
Load tests show how your application handles heavy traffic:
    • API calls
    • Database reads or writes
    • Memory use
    • Disk use
    • Network latency and bandwidth

tools: pip install locust

=== Deployment ===
You’ll also need something above these servers to do the following:
• Keep them running (a supervisor)
• Gather and feed external requests (a reverse proxy)
• Return responses
• Provide HTTPS termination (SSL decryption)

- Multiple workers : pip install "uvicorn[standard]" gunicorn
    gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
        or
    uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
- HTTPS
    How to add HTTPS support to FastAPI by using "Traefik"
        https://github.com/tiangolo/blog-posts/blob/master/deploying-fastapi-apps-with-https-powered-by-traefik/README.md
- Docker
    If you want to host your FastAPI application on a cloud service, you’ll usually need to create a Docker image of it first
        https://fastapi.tiangolo.com/deployment/docker/

        https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-13-docker-deploy/
- Cloud Services
    https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-6b-linode-deploy-gunicorn-uvicorn-nginx/
    https://towardsdatascience.com/how-to-deploy-your-fastapi-app-on-heroku-for-free-8d4271a4ab9
- Kubernetes
    Kubernetes grew from internal Google code for managing internal systems that were
    becoming ever more godawfully complex. System administrators (as they were called
    then) used to manually configure tools like load balancers, reverse proxies, humidors1
    and so on. Kubernetes aimed to take much of this knowledge and automate it: don’t
    tell me how to handle this; tell me what you want. This included tasks like keeping a
    service running, or firing up more servers if traffic spikes.

    https://sumanta9090.medium.com/deploying-a-fastapi-application-on-kubernetes-a-step-by-step-guide-for-production-d74faac4ca36

=== Performance ===
Performance has two aspects:
• The time to handle a single request
• The number of requests that can be handled at once

- Async (async def / def)
- Caches
    https://docs.python.org/3/library/functools.html
    cache() and lru_cache()
- Databases, Files and Memory
    - In SQL, any column in a WHERE clause should be indexed.
    - SQL query optimizer : https://www.sqlite.org/optoverview.html
- Queues
    If you’re performing any task that takes longer than a fraction of a second (like send‐
    ing a confirmation email or downsizing an image), it may be worth handing it off to a
    job queue like Celery. --- https://docs.celeryq.dev/en/stable/
- Python Itself : Faster Python
    Alternatives include the following:
        • Use PyPy instead of the standard CPython. https://www.pypy.org/
        • Write a Python extension in C, C++, or Rust. https://docs.python.org/3/extending/extending.html
        • Convert the slow Python code to Cython (used by Pydantic and Uvicorn themselves). https://cython.org/
- Troubleshooting
    Look bottom-up from the time and place where you encounter a problem. This includes time and space performance issues, but also logic and async traps
- Kinds of Problems
    404 An authentication or authorization error.
    422 Usually a Pydantic complaint about use of a model.
    500 The failure of a service behind your FastAPI one.
- Logging
- Metrics(metrics, monitoring, observability, and telemetry)
    • Prometheus to gather metrics      https://prometheus.io/
    • Grafana to display them           https://grafana.com/
    • OpenTelemetry to measure timing   https://opentelemetry.io/

    https://github.com/trallnag/prometheus-fastapi-instrumentator
    https://dev.to/ken_mwaura1/getting-started-monitoring-a-fastapi-app-with-grafana-and-prometheus-a-step-by-step-guide-3fbn
    https://grafana.com/grafana/dashboards/16110-fastapi-observability/
    https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/fastapi/fastapi.html
    https://signoz.io/blog/opentelemetry-fastapi/
    https://opentelemetry.io/docs/languages/python/

- Database Test Loading
    test_load.py

=== Gallery ===
- FastAPI with AI - LLM