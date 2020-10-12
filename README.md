## Install

```
$ pip3 install webclient-helper
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
```

## Example (GitHub)

> Note: To use the GitHub API, first generate a "personal access token" at
> <https://github.com/settings/tokens/new>

```
from os import getenv

access_token = getenv('GITHUB_ACCESS_TOKEN')
gh_client = wh.WebClient(token=access_token, token_type='token')
data = gh_client.GET('https://api.github.com/user/repos')
```

## Example (subclass with custom login)

```
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
            self._base_url + '/api/something',
            params=params,
            debug=debug
        )


some_client = SentinelClient(
    username='myuser',
    password='mypass',
    base_url='https://somewhere.com',
)

something1 = some_client.get_something(params={'x': 1, 'y': 5})
something2 = some_client.get_something(params={'x': 2, 'y': 10})
```
