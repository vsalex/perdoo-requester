## The task

The task is to build a simple tool that lets you schedule REST requests for a given point in time in the future. Here are the requirements:

- A simple UI (Django admin or any other pre-built UI is enough) to:
    - Authenticate the user
    - Specify a new request, as well as when it should execute
    - View pending requests, as well as processed ones along with their status
- A scheduler that will perform the requests at the right time and store the results
- Host the system in the cloud on a platform of your choice so we can easily test it (we'll use [https://requestbin.com/](https://requestbin.com/) to ensure requests go through)
- Test suite to ensure reliability. If you don't have time, a short summary of what testing strategy you think fits best

Please use Django as the web framework, since that's what you'd be working with here at Perdoo. Other than that the architecture is entirely up to you!