from urllib import request
from django.shortcuts import redirect
from django.http import HttpResponse
from oauthlib.oauth2 import WebApplicationClient
from . import consts

import requests
import json

client = WebApplicationClient(consts.GOOGLE_CLIENT_ID)


def ping(request):
    return HttpResponse("hello")

def get_google_provider_config():
    return requests.get(consts.GOOGLE_DISCOVERY_URL).json()

def signin(request):
    google_provider_cfg = get_google_provider_config()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri="http://127.0.0.1:8000/users/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

def signin_callback(request):
    code = request.GET.get("code")
    google_provider_cfg = get_google_provider_config()
    token_endpoint = google_provider_cfg["token_endpoint"]
    uri = request.build_absolute_uri()
    # uri = "https" + uri[4:]

    b = uri[:uri.index("?")]

    token_url, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=uri,
    redirect_url=uri[:uri.index("?")],
    code=code
)
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(consts.GOOGLE_CLIENT_ID, consts.GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return HttpResponse(f"User email not available or not verified by Google.", 400)
    return HttpResponse(f"user_id: {unique_id} user_email: {users_email} user_name: {users_name}")