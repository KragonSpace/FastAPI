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