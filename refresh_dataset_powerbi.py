import adal
import requests
import json


authority url 'https://login.windows.net/common
resource _url - 'https://analysis.windows.net/powerbi/api
client_id - 'INSERT_YOUR CLIENT ID
username- YOUR POWERBI_ EMAIL
password- "YOUR POWERBI_PASSMORD
context - adal.AuthenticationContext (authority-authority url,
                                         validate authority-True,
                                         api_version-None)
token - context.acquire_token_with_usernane_password(resource-resource_url,
                                                           client_id-client id,
                                                          username-usernane,
                                                          password-password)
access_token - token.get('accessToken')
groups request url - 'https://apl.powerbl.com/v1.0/myorg/groups
header - ('Authorization': f'Bearer (access_token)")
groups_request json.loads (requests.get(url-groups_request url, headers-header).content)
groups - [d['id'] for d in groups_request['value']]
for group in groups:
    datasets_request_url - 'https://api.powerbi.con/v1.0/myorg/groups/'+ group /datasets
    datasets_request - json. loads (requests.get(url-datasets_request url, headers-header).content)
    datasets - [d[ 'id'] for d in datasets_request['value' ]]
    for dataset in datasets:
        refresh_url - 'https://api.powerbi.com/v1.0/myorg/groups/ group /datasets/ dataset + /refreshes
            requests.post (url-refresh_url, headers-header)

