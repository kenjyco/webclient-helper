## Install

```
$ pip3 install webclient-helper
```

#### Or, install with beautifulsoup4 and lxml

Install system requirements for `lxml`

```
$ sudo apt-get install -y libxml2 libxslt1.1 libxml2-dev libxslt1-dev

or

% brew install libxml2
```

Install with pip

```
$ pip3 install webclient-helper[bs4]
````

## Usage

> `import webclient_helper as wh`

Create an instance of WebClient and use the HTTP methods (OPTIONS, HEAD, GET,
POST, PUT, PATCH, DELETE) to interact with an API.

```
WebClient(username=None, password=None, token=None, token_type=None, base_url='',
          user_agent=None, content_type='application/json', extra_headers={})

    Interact with an API on the web

    If you need to obtain a token from a login endpoint, define a "login"
    method when you subclass WebClient and set self._token and self._token_type

    Example:

        def login(self):
            headers = {'Content-Type': 'application/json'}
            data = {'email': self._username, 'password': self._password}
            response = self.session.post(
                self._base_url + '/api/login',
                headers=headers,
                json=data
            )
            self._token = response.json().get('access_token')
            self._token_type = 'Bearer'


    __init__(self, username=None, password=None, token=None, token_type=None,
             base_url='', user_agent=None, content_type='application/json',
             extra_headers={})
        - username: if specified, set auth on session (requires password)
        - password: if specified, set auth on session (requires username)
        - token: if specified, use this token in the "Authorization" header
          (requires token_type)
        - token_type: if specified, use as part of the value in the
          "Authorization" header
        - base_url: base url for service/API that a subclass would interact with
        - user_agent: if specified, set "User-Agent" header
        - content_type: content type for requests
        - extra_headers: a dict of extra headers to set on the session

        If no login method is defined, any supplied username/password will be
        passed to new_requests_session (for basic auth)

    OPTIONS(self, url, headers=None, debug=False, retry=False, **kwargs)
        Send a OPTIONS request and return response object

        - url: url/endpoint
        - headers: dict of headers to update on the session before making request
        - debug: if True, enter debugger before returning
        - retry: if True and initial response is "401 Unauthorized", call
          self.set_session() and try again

        Other kwargs are passed to webclient_helper.session_method

    HEAD(self, url, headers=None, debug=False, retry=False, **kwargs)
        Send a HEAD request and return response object

        - url: url/endpoint
        - headers: dict of headers to update on the session before making request
        - debug: if True, enter debugger before returning
        - retry: if True and initial response is "401 Unauthorized", call
          self.set_session() and try again

        Other kwargs are passed to webclient_helper.session_method

    GET(self, url, headers=None, params=None, debug=False, retry=False, **kwargs)
        Send a GET request and return response object

        - url: url/endpoint
        - headers: dict of headers to update on the session before making request
        - params: a dict with query string vars and values
        - debug: if True, enter debugger before returning
        - retry: if True and initial response is "401 Unauthorized", call
          self.set_session() and try again

        Other kwargs are passed to webclient_helper.session_method

    POST(self, url, headers=None, data=None, json=None, debug=False, retry=False, **kwargs)
        Send a POST request and return response object

        - url: url/endpoint
        - headers: dict of headers to update on the session before making request
        - data: a dict to send in the body (non-JSON)
        - json: a dict to send in the body
        - debug: if True, enter debugger before returning
        - retry: if True and initial response is "401 Unauthorized", call
          self.set_session() and try again

        Other kwargs are passed to webclient_helper.session_method

    PUT(self, url, headers=None, data=None, debug=False, retry=False, **kwargs)
        Send a PUT request and return response object

        - url: url/endpoint
        - headers: dict of headers to update on the session before making request
        - data: a dict to send in the body (non-JSON)
        - debug: if True, enter debugger before returning
        - retry: if True and initial response is "401 Unauthorized", call
          self.set_session() and try again

        Other kwargs are passed to webclient_helper.session_method

    PATCH(self, url, headers=None, data=None, debug=False, retry=False, **kwargs)
        Send a PATCH request and return response object

        - url: url/endpoint
        - headers: dict of headers to update on the session before making request
        - data: a dict to send in the body (non-JSON)
        - debug: if True, enter debugger before returning
        - retry: if True and initial response is "401 Unauthorized", call
          self.set_session() and try again

        Other kwargs are passed to webclient_helper.session_method

    DELETE(self, url, headers=None, debug=False, retry=False, **kwargs)
        Send a DELETE request and return response object

        - url: url/endpoint
        - headers: dict of headers to update on the session before making request
        - debug: if True, enter debugger before returning
        - retry: if True and initial response is "401 Unauthorized", call
          self.set_session() and try again

        Other kwargs are passed to webclient_helper.session_method

    history_explorer(self, return_selections=False)
        Select responses from history to explore in ipython (if ipython installed)

        - return_selections: if True, return the selections from history
```

## Example (GitHub)

> See <https://docs.github.com/en/rest/reference> for endpoints to hit.
>
> Note: To (fully) use the GitHub API, first generate a "personal access token"
> at <https://github.com/settings/tokens/new> and save it to your `~/.bashrc` or
> `~/.zshrc` file.

```
export GITHUB_ACCESS_TOKEN="ghp_vx..."
```

Then use it in your Python code (after `source ~/.bashrc` or `source ~/.zshrc`
for the first time)

```
import webclient_helper as wh
from os import getenv


access_token = getenv('GITHUB_ACCESS_TOKEN')
gh_client = wh.WebClient(token=access_token, token_type='token')
resp = gh_client.GET('https://api.github.com/user/repos')
data = resp.json()
```

## Example (subclass with custom login)

```
import webclient_helper as wh


class SomeClient(wh.WebClient):
    def login(self):
        headers = {'Content-Type': 'application/json'}
        data = {'email': self._username, 'password': self._password}
        response = self.session.post(
            self._base_url + '/api/login',
            headers=headers,
            json=data
        )
        self._token = response.json().get('access_token')
        self._token_type = 'Bearer'

    def get_something(self, params=None, debug=False):
        return self.GET(
            '/api/something',
            params=params,
            debug=debug
        )


some_client = SomeClient(
    username='myuser',
    password='mypass',
    base_url='https://somewhere.com',
)

something1 = some_client.get_something(params={'x': 1, 'y': 5})
something2 = some_client.get_something(params={'x': 2, 'y': 10})
```
