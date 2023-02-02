#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
from urllib import parse

import requests

form_header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}


class openApi:
    # curl - -location - -request
    # POST
    # 'https://knows-init.emotibot.com/annotationPermit/permit/login' \
    # - -header
    # 'Accept: application/json, text/plain, */*' \
    # - -header
    # 'Accept-Language: zh-CN,zh;q=0.9' \
    # - -header
    # 'Authorization: Bearer' \
    # - -header
    # 'Cache-Control: no-cache' \
    # - -header
    # 'Connection: keep-alive' \
    # - -header
    # 'Content-Type: application/x-www-form-urlencoded' \
    # - -header
    # 'If-Modified-Since: 0' \
    # - -header
    # 'Origin: https://knows-init.emotibot.com' \
    # - -header
    # 'Pragma: no-cache' \
    # - -header
    # 'Referer: https://knows-init.emotibot.com/gemini/login.html' \
    # - -header
    # 'Sec-Fetch-Dest: empty' \
    # - -header
    # 'Sec-Fetch-Mode: cors' \
    # - -header
    # 'Sec-Fetch-Site: same-origin' \
    # - -header
    # 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
    # - -header
    # 'X-Appid;' \
    # - -header
    # 'X-Enterpriseid;' \
    # - -header
    # 'X-Locale: zh-cn' \
    # - -header
    # 'X-Userid;' \
    # - -header
    # 'appid;' \
    # - -header
    # 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
    # - -header
    # 'sec-ch-ua-mobile: ?0' \
    # - -header
    # 'sec-ch-ua-platform: "macOS"' \
    # - -header
    # 'userId;' \
    # - -data - urlencode
    # 'account=mengzhenzhang' \
    # - -data - urlencode
    # 'passwd=7e2ba10110f719dd65a0403305770b08'
    @staticmethod
    def getAuth(host, userName, passWord):
        pwd = hashlib.md5(passWord.encode())
        req_data = {
            "account": userName,
            "passwd": pwd.hexdigest()
        }
        loginUrl = host + "/annotationPermit/permit/login"
        try:
            response = requests.post(url=loginUrl, data=req_data, headers=form_header)
            res = response.json()
            return userInfo(res['result'], host)
        except Exception as e:
            print(str(e))
            return None

    # curl - -location - -request
    # GET
    # 'https://knows-init.emotibot.com/kmBackend/space/page/7ad0051d31144cf0ba27cb28be5ac919/4/13f146ee4909488aaaa96f574fbd776c?page=1&pageSize=20' \
    # - -header
    # 'Accept: application/json, text/plain, */*' \
    # - -header
    # 'Accept-Language: zh-CN,zh;q=0.9' \
    # - -header
    # 'Cache-Control: no-cache' \
    # - -header
    # 'Connection: keep-alive' \
    # - -header
    # 'Cookie: experimentation_subject_id=ImI3M2Y5OTlhLTUzMDQtNDNjOS1iOWEyLWE2YmNlODA4YThlZSI%3D--325f559b4b66c5d24ee7172a20c1b9d4b6ffcbe2; Hm_lvt_e6bafdc067540de4a868e9148a1b0540=1666060914; ajs_user_id=%22487c7855771517e53c298074d18cab589ad03e08%22; ajs_anonymous_id=%223bdf5274-9216-41c2-b99f-d43d0f465daf%22; verify=852e6958bb812c5d09551541317b5ddc' \
    # - -header
    # 'Pragma: no-cache' \
    # - -header
    # 'Referer: https://knows-init.emotibot.com/gemini/' \
    # - -header
    # 'Sec-Fetch-Dest: empty' \
    # - -header
    # 'Sec-Fetch-Mode: cors' \
    # - -header
    # 'Sec-Fetch-Site: same-origin' \
    # - -header
    # 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
    # - -header
    # 'X-Enterpriseid: 7ad0051d31144cf0ba27cb28be5ac919' \
    # - -header
    # 'X-Local: zh-cn' \
    # - -header
    # 'X-Locale: zh-cn' \
    # - -header
    # 'X-Userid: 13f146ee4909488aaaa96f574fbd776c' \
    # - -header
    # 'enterpriseId: 7ad0051d31144cf0ba27cb28be5ac919' \
    # - -header
    # 'orgId: 4' \
    # - -header
    # 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
    # - -header
    # 'sec-ch-ua-mobile: ?0' \
    # - -header
    # 'sec-ch-ua-platform: "macOS"' \
    # - -header
    # 'userId: 13f146ee4909488aaaa96f574fbd776c'
    @staticmethod
    def getSpace(userInfo, page, pageSize):
        url = userInfo.host + "/kmBackend/space/page/" + userInfo.info.enterprise + "/" + userInfo.info.orgId + "/" + userInfo.info.id
        params = {
            "page": page,
            "pageSize": pageSize
        }
        print(userInfo.token)
        header = {
            "Authorization": "Bearer " + userInfo.token
        }
        print(url)
        response = doHttpGet(url, params, header)
        print(response.json())
        return response.json()

    # curl - -location - -request
    # GET
    # 'https://knows-init.emotibot.com/kmBackend/category/authFolder' \
    # - -header
    # 'Accept: application/json, text/plain, */*' \
    # - -header
    # 'Accept-Language: zh-CN,zh;q=0.9' \
    # - -header
    # 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE2NzUyMzg5NTYsImN1c3RvbSI6eyJjdXN0b20iOm51bGwsImRpc3BsYXlfbmFtZSI6Ium7hOiClum-mSIsImVtYWlsIjoieGlhb2xvbmdodWFuZ0BlbW90aWJvdC5jb20iLCJlbnRlcnByaXNlIjoiN2FkMDA1MWQzMTE0NGNmMGJhMjdjYjI4YmU1YWM5MTkiLCJpZCI6IjEzZjE0NmVlNDkwOTQ4OGFhYWE5NmY1NzRmYmQ3NzZjIiwib3JnSWQiOjQsInBob25lIjoiIiwicHJvZHVjdCI6W10sInJvbGVzIjp7ImFwcHMiOlt7ImFwcF90eXBlIjowLCJpZCI6IjJlMTZhNTI5M2MzYTRlM2FiYmNiZTBlM2E0YWM2YWQ1IiwibmFtZSI6IueruemXtOefpeivhuW6k8K35L2_55So5omL5YaMJueuoeeQhuinhOiMgyIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiOTAyNDE5OGUxZGFhNGYxNjkzYWNlMjFiNGE0YjdlYmQiLCJuYW1lIjoiSVQgU3VwcG9ydCIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiZTQ0YmFlNDk5YzNhNDAzMjk1NGMyZDc5MGUxNGJiN2QiLCJuYW1lIjoi56u56Ze06aG555uu5oqA5pyv56m66Ze0LUNTIiwicm9sZSI6ImVlZWJiZGNjMmM2OTQyYzE5Y2M0YzkzNTk1ZTNjZTA2In0seyJhcHBfdHlwZSI6MCwiaWQiOiI5MGQ3ZmQ1MDZjOTM0YjhhYTg0N2VkZWJhYWJhNjNkMSIsIm5hbWUiOiLnq7npl7RCRuWboumYnyIsInJvbGUiOiJlZWViYmRjYzJjNjk0MmMxOWNjNGM5MzU5NWUzY2UwNiJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiODIxZWVlYzdlNTMwNDFmNGE5ZDgzYTYwYTAxMGNhYzYiLCJuYW1lIjoi56u56Ze05Lqn5ZOB5ZWG55So5Y-R5biDIiwicm9sZSI6IjdjMWVlMTQ2OTNlNTQ4NjJhZDlhMTllNWIwNWEwOGFkIn0seyJhcHBfdHlwZSI6MCwiaWQiOiIzODg4YTMxZGUwMjQ0MWMyODhlNmZlM2FhMDMzZTMyOCIsIm5hbWUiOiLpobnnm67mjpLpm7flv5ciLCJyb2xlIjoiZWVlYmJkY2MyYzY5NDJjMTljYzRjOTM1OTVlM2NlMDYifSx7ImFwcF90eXBlIjowLCJpZCI6IjU4N2U5YWNlZmVlODRhN2JhNzQ2YjgyNDliODgxOGY5IiwibmFtZSI6IumhueebruS6pOS7mOiuree7g-iQpSIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiNmZkM2MzMTJmOWViNDQ4YmEzNWUxOWUxZWUxMzY0ZjciLCJuYW1lIjoi56u56Ze05LqR5Z-65bqn5Zui6ZifIiwicm9sZSI6ImMxYTNkZmYwNzdmMTQ4YjY4NjQzNTA0ZGQyNWM2NTU4In0seyJhcHBfdHlwZSI6MCwiaWQiOiJmZjAwYmExYzIwNDQ0NDNiYmY4YzQ3ZjQ2ZGFlMWIwMiIsIm5hbWUiOiLkvY7ku6PnoIHlt6XlhbciLCJyb2xlIjoiZWVlYmJkY2MyYzY5NDJjMTljYzRjOTM1OTVlM2NlMDYifSx7ImFwcF90eXBlIjowLCJpZCI6IjE2YzExYWIyOGY1MTRlNzE5MmI2MzY3ZDdjZjY0ZWU2IiwibmFtZSI6IuW8gOWPkeiAheS4reW_gyIsInJvbGUiOiI3YzFlZTE0NjkzZTU0ODYyYWQ5YTE5ZTViMDVhMDhhZCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiOTQ0ZGY4MGQzMWQxNDc3MmEzMjdlYjVlMWMxZWI1NTYiLCJuYW1lIjoi5paw5YW15a2m5bqf6JClIiwicm9sZSI6IjdjMWVlMTQ2OTNlNTQ4NjJhZDlhMTllNWIwNWEwOGFkIn0seyJhcHBfdHlwZSI6MCwiaWQiOiIzMDhkMzkzNTI0MzY0YTFlODQxOTY3MjJkNTcxNzY3MSIsIm5hbWUiOiJYLUF2YXRhciIsInJvbGUiOiI3YzFlZTE0NjkzZTU0ODYyYWQ5YTE5ZTViMDVhMDhhZCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiMzA0NmVmNTUyYzgyNDAzYTk4YTk1YTU2ODdmY2FmMWUiLCJuYW1lIjoi56u56Ze06L-Q6JCl5Zui6ZifIiwicm9sZSI6ImMxYTNkZmYwNzdmMTQ4YjY4NjQzNTA0ZGQyNWM2NTU4In0seyJhcHBfdHlwZSI6MCwiaWQiOiI3OGZlMjkzMzIyMGQ0MTI3YjkyNjc1MWFjZGIzOGFjMyIsIm5hbWUiOiJQwrfljaDlj5HpvpkiLCJyb2xlIjoiN2MxZWUxNDY5M2U1NDg2MmFkOWExOWU1YjA1YTA4YWQifSx7ImFwcF90eXBlIjowLCJpZCI6IjAwZWY0YjYxYThlYjRmNjhhZWI1MjUwNDAzMGM4YzgwIiwibmFtZSI6IueruemXtOaZuuiDveefpeivhuW6k-WboumYnyIsInJvbGUiOiJlZWViYmRjYzJjNjk0MmMxOWNjNGM5MzU5NWUzY2UwNiJ9XSwiZ3JvdXBzIjpbXX0sInN0YXR1cyI6MSwidHlwZSI6MiwidXNlcl9uYW1lIjoieGlhb2xvbmdodWFuZyJ9LCJpc3MiOiJzaW1wbGUtYXV0aCIsImV4cCI6MTY3NTMyNTM1Nn0.Br6cmZjZ5xSTF6rjvdu6EbZ3jNZR5W8dgRlHyxlyyxM' \
    # - -header
    # 'Cache-Control: no-cache' \
    # - -header
    # 'Connection: keep-alive' \
    # - -header
    # 'Cookie: experimentation_subject_id=ImI3M2Y5OTlhLTUzMDQtNDNjOS1iOWEyLWE2YmNlODA4YThlZSI%3D--325f559b4b66c5d24ee7172a20c1b9d4b6ffcbe2; Hm_lvt_e6bafdc067540de4a868e9148a1b0540=1666060914; ajs_user_id=%22487c7855771517e53c298074d18cab589ad03e08%22; ajs_anonymous_id=%223bdf5274-9216-41c2-b99f-d43d0f465daf%22; verify=852e6958bb812c5d09551541317b5ddc' \
    # - -header
    # 'Pragma: no-cache' \
    # - -header
    # 'Referer: https://knows-init.emotibot.com/km/' \
    # - -header
    # 'Sec-Fetch-Dest: empty' \
    # - -header
    # 'Sec-Fetch-Mode: cors' \
    # - -header
    # 'Sec-Fetch-Site: same-origin' \
    # - -header
    # 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
    # - -header
    # 'X-Enterpriseid: 7ad0051d31144cf0ba27cb28be5ac919' \
    # - -header
    # 'X-Local: zh-cn' \
    # - -header
    # 'X-Locale: zh-cn' \
    # - -header
    # 'X-Userid: 13f146ee4909488aaaa96f574fbd776c' \
    # - -header
    # 'enterpriseId: 7ad0051d31144cf0ba27cb28be5ac919' \
    # - -header
    # 'orgId: 4' \
    # - -header
    # 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
    # - -header
    # 'sec-ch-ua-mobile: ?0' \
    # - -header
    # 'sec-ch-ua-platform: "macOS"' \
    # - -header
    # 'spaceId: 239' \
    # - -header
    # 'userId: 13f146ee4909488aaaa96f574fbd776c'
    @staticmethod
    def getSpaceFolder(userInfo, spaceId):
        url = userInfo.host + "/kmBackend/category/authFolder"
        header = {
            "Authorization": "Bearer " + userInfo.token,
            "enterpriseId": userInfo.info.enterprise,
            "orgId": userInfo.info.orgId,
            "spaceId": str(spaceId),
            "userId": userInfo.info.id
        }
        response = doHttpGet(url, None, header)
        print(response.json())
        return response.json()

    #     curl - -location - -request
    #     POST
    #     'https://knows-init.emotibot.com/kmBackend/knowledge/save' \
    #     - -header
    #     'Accept: application/json, text/plain, */*' \
    #     - -header
    #     'Accept-Language: zh-CN,zh;q=0.9' \
    #     - -header
    #     'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE2NzUyMzg5NTYsImN1c3RvbSI6eyJjdXN0b20iOm51bGwsImRpc3BsYXlfbmFtZSI6Ium7hOiClum-mSIsImVtYWlsIjoieGlhb2xvbmdodWFuZ0BlbW90aWJvdC5jb20iLCJlbnRlcnByaXNlIjoiN2FkMDA1MWQzMTE0NGNmMGJhMjdjYjI4YmU1YWM5MTkiLCJpZCI6IjEzZjE0NmVlNDkwOTQ4OGFhYWE5NmY1NzRmYmQ3NzZjIiwib3JnSWQiOjQsInBob25lIjoiIiwicHJvZHVjdCI6W10sInJvbGVzIjp7ImFwcHMiOlt7ImFwcF90eXBlIjowLCJpZCI6IjJlMTZhNTI5M2MzYTRlM2FiYmNiZTBlM2E0YWM2YWQ1IiwibmFtZSI6IueruemXtOefpeivhuW6k8K35L2_55So5omL5YaMJueuoeeQhuinhOiMgyIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiOTAyNDE5OGUxZGFhNGYxNjkzYWNlMjFiNGE0YjdlYmQiLCJuYW1lIjoiSVQgU3VwcG9ydCIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiZTQ0YmFlNDk5YzNhNDAzMjk1NGMyZDc5MGUxNGJiN2QiLCJuYW1lIjoi56u56Ze06aG555uu5oqA5pyv56m66Ze0LUNTIiwicm9sZSI6ImVlZWJiZGNjMmM2OTQyYzE5Y2M0YzkzNTk1ZTNjZTA2In0seyJhcHBfdHlwZSI6MCwiaWQiOiI5MGQ3ZmQ1MDZjOTM0YjhhYTg0N2VkZWJhYWJhNjNkMSIsIm5hbWUiOiLnq7npl7RCRuWboumYnyIsInJvbGUiOiJlZWViYmRjYzJjNjk0MmMxOWNjNGM5MzU5NWUzY2UwNiJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiODIxZWVlYzdlNTMwNDFmNGE5ZDgzYTYwYTAxMGNhYzYiLCJuYW1lIjoi56u56Ze05Lqn5ZOB5ZWG55So5Y-R5biDIiwicm9sZSI6IjdjMWVlMTQ2OTNlNTQ4NjJhZDlhMTllNWIwNWEwOGFkIn0seyJhcHBfdHlwZSI6MCwiaWQiOiIzODg4YTMxZGUwMjQ0MWMyODhlNmZlM2FhMDMzZTMyOCIsIm5hbWUiOiLpobnnm67mjpLpm7flv5ciLCJyb2xlIjoiZWVlYmJkY2MyYzY5NDJjMTljYzRjOTM1OTVlM2NlMDYifSx7ImFwcF90eXBlIjowLCJpZCI6IjU4N2U5YWNlZmVlODRhN2JhNzQ2YjgyNDliODgxOGY5IiwibmFtZSI6IumhueebruS6pOS7mOiuree7g-iQpSIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiNmZkM2MzMTJmOWViNDQ4YmEzNWUxOWUxZWUxMzY0ZjciLCJuYW1lIjoi56u56Ze05LqR5Z-65bqn5Zui6ZifIiwicm9sZSI6ImMxYTNkZmYwNzdmMTQ4YjY4NjQzNTA0ZGQyNWM2NTU4In0seyJhcHBfdHlwZSI6MCwiaWQiOiJmZjAwYmExYzIwNDQ0NDNiYmY4YzQ3ZjQ2ZGFlMWIwMiIsIm5hbWUiOiLkvY7ku6PnoIHlt6XlhbciLCJyb2xlIjoiZWVlYmJkY2MyYzY5NDJjMTljYzRjOTM1OTVlM2NlMDYifSx7ImFwcF90eXBlIjowLCJpZCI6IjE2YzExYWIyOGY1MTRlNzE5MmI2MzY3ZDdjZjY0ZWU2IiwibmFtZSI6IuW8gOWPkeiAheS4reW_gyIsInJvbGUiOiI3YzFlZTE0NjkzZTU0ODYyYWQ5YTE5ZTViMDVhMDhhZCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiOTQ0ZGY4MGQzMWQxNDc3MmEzMjdlYjVlMWMxZWI1NTYiLCJuYW1lIjoi5paw5YW15a2m5bqf6JClIiwicm9sZSI6IjdjMWVlMTQ2OTNlNTQ4NjJhZDlhMTllNWIwNWEwOGFkIn0seyJhcHBfdHlwZSI6MCwiaWQiOiIzMDhkMzkzNTI0MzY0YTFlODQxOTY3MjJkNTcxNzY3MSIsIm5hbWUiOiJYLUF2YXRhciIsInJvbGUiOiI3YzFlZTE0NjkzZTU0ODYyYWQ5YTE5ZTViMDVhMDhhZCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiMzA0NmVmNTUyYzgyNDAzYTk4YTk1YTU2ODdmY2FmMWUiLCJuYW1lIjoi56u56Ze06L-Q6JCl5Zui6ZifIiwicm9sZSI6ImMxYTNkZmYwNzdmMTQ4YjY4NjQzNTA0ZGQyNWM2NTU4In0seyJhcHBfdHlwZSI6MCwiaWQiOiI3OGZlMjkzMzIyMGQ0MTI3YjkyNjc1MWFjZGIzOGFjMyIsIm5hbWUiOiJQwrfljaDlj5HpvpkiLCJyb2xlIjoiN2MxZWUxNDY5M2U1NDg2MmFkOWExOWU1YjA1YTA4YWQifSx7ImFwcF90eXBlIjowLCJpZCI6IjAwZWY0YjYxYThlYjRmNjhhZWI1MjUwNDAzMGM4YzgwIiwibmFtZSI6IueruemXtOaZuuiDveefpeivhuW6k-WboumYnyIsInJvbGUiOiJlZWViYmRjYzJjNjk0MmMxOWNjNGM5MzU5NWUzY2UwNiJ9XSwiZ3JvdXBzIjpbXX0sInN0YXR1cyI6MSwidHlwZSI6MiwidXNlcl9uYW1lIjoieGlhb2xvbmdodWFuZyJ9LCJpc3MiOiJzaW1wbGUtYXV0aCIsImV4cCI6MTY3NTMyNTM1Nn0.Br6cmZjZ5xSTF6rjvdu6EbZ3jNZR5W8dgRlHyxlyyxM' \
    #     - -header
    #     'Cache-Control: no-cache' \
    #     - -header
    #     'Connection: keep-alive' \
    #     - -header
    #     'Content-Type: application/json;charset=UTF-8' \
    #     - -header
    #     'Cookie: experimentation_subject_id=ImI3M2Y5OTlhLTUzMDQtNDNjOS1iOWEyLWE2YmNlODA4YThlZSI%3D--325f559b4b66c5d24ee7172a20c1b9d4b6ffcbe2; Hm_lvt_e6bafdc067540de4a868e9148a1b0540=1666060914; ajs_user_id=%22487c7855771517e53c298074d18cab589ad03e08%22; ajs_anonymous_id=%223bdf5274-9216-41c2-b99f-d43d0f465daf%22; verify=852e6958bb812c5d09551541317b5ddc' \
    #     - -header
    #     'If-Modified-Since: 0' \
    #     - -header
    #     'Origin: https://knows-init.emotibot.com' \
    #     - -header
    #     'Pragma: no-cache' \
    #     - -header
    #     'Referer: https://knows-init.emotibot.com/km/' \
    #     - -header
    #     'Sec-Fetch-Dest: empty' \
    #     - -header
    #     'Sec-Fetch-Mode: cors' \
    #     - -header
    #     'Sec-Fetch-Site: same-origin' \
    #     - -header
    #     'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
    #     - -header
    #     'X-Locale: zh-cn' \
    #     - -header
    #     'enterpriseId: 7ad0051d31144cf0ba27cb28be5ac919' \
    #     - -header
    #     'orgId: 4' \
    #     - -header
    #     'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
    #     - -header
    #     'sec-ch-ua-mobile: ?0' \
    #     - -header
    #     'sec-ch-ua-platform: "macOS"' \
    #     - -header
    #     'spaceId: 17' \
    #     - -header
    #     'userId: 13f146ee4909488aaaa96f574fbd776c' \
    #     - -header
    #     'userName: xiaolonghuang' \
    #     - -data - raw
    #     '{
    #     "title": "CS",
    #     "rtfContent": "<p>cs</p>",
    #     "tagList": [],
    #     "stqList": [],
    #     "linkStqList": [],
    #     "attachmentList": [],
    #     "textSummarization": "",
    #     "keywordList": [],
    #     "kgAppId": "",
    #     "userGroupList": [],
    #     "userList": [],
    #     "folderId": 0,
    #     "folderIdList": [
    #         0
    #     ],
    #     "providedUser": "",
    #     "owner": "xiaolonghuang",
    #     "language": "zh-cn",
    #     "customStatus": "",
    #     "knowledgeConcentrated": "",
    #     "adaptProduct": "",
    #     "responsibilityDepartment": "",
    #     "applyArea": "",
    #     "channelIdList": [
    #         -1
    #     ],
    #     "bindKnowsList": [],
    #     "relations": [],
    #     "wordsStrList": [
    #         null,
    #         "{}"
    #     ],
    #     "submit": true,
    #     "startTime": "",
    #     "endTime": "",
    #     "workflowRecordId": 44065
    #
    # }'
    @staticmethod
    def saveKnowledge(userInfo, spaceId, knowledge):
        url = userInfo.host + "/kmBackend/knowledge/save"
        header = {
            "Authorization": "Bearer " + userInfo.token,
            "enterpriseId": userInfo.info.enterprise,
            "orgId": userInfo.info.orgId,
            "spaceId": str(spaceId),
            "userId": userInfo.info.id,
            "userName": userInfo.info.user_name
        }
        param = knowledge
        response = doHttpPost(url, param, header)
        print(response)
        return response

    #     curl - -location - -request
    #     POST
    #     'https://knows-init.emotibot.com/kmBackend/search/main' \
    #     - -header
    #     'Accept: application/json, text/plain, */*' \
    #     - -header
    #     'Accept-Language: zh-CN,zh;q=0.9' \
    #     - -header
    #     'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE2NzUyMzg5NTYsImN1c3RvbSI6eyJjdXN0b20iOm51bGwsImRpc3BsYXlfbmFtZSI6Ium7hOiClum-mSIsImVtYWlsIjoieGlhb2xvbmdodWFuZ0BlbW90aWJvdC5jb20iLCJlbnRlcnByaXNlIjoiN2FkMDA1MWQzMTE0NGNmMGJhMjdjYjI4YmU1YWM5MTkiLCJpZCI6IjEzZjE0NmVlNDkwOTQ4OGFhYWE5NmY1NzRmYmQ3NzZjIiwib3JnSWQiOjQsInBob25lIjoiIiwicHJvZHVjdCI6W10sInJvbGVzIjp7ImFwcHMiOlt7ImFwcF90eXBlIjowLCJpZCI6IjJlMTZhNTI5M2MzYTRlM2FiYmNiZTBlM2E0YWM2YWQ1IiwibmFtZSI6IueruemXtOefpeivhuW6k8K35L2_55So5omL5YaMJueuoeeQhuinhOiMgyIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiOTAyNDE5OGUxZGFhNGYxNjkzYWNlMjFiNGE0YjdlYmQiLCJuYW1lIjoiSVQgU3VwcG9ydCIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiZTQ0YmFlNDk5YzNhNDAzMjk1NGMyZDc5MGUxNGJiN2QiLCJuYW1lIjoi56u56Ze06aG555uu5oqA5pyv56m66Ze0LUNTIiwicm9sZSI6ImVlZWJiZGNjMmM2OTQyYzE5Y2M0YzkzNTk1ZTNjZTA2In0seyJhcHBfdHlwZSI6MCwiaWQiOiI5MGQ3ZmQ1MDZjOTM0YjhhYTg0N2VkZWJhYWJhNjNkMSIsIm5hbWUiOiLnq7npl7RCRuWboumYnyIsInJvbGUiOiJlZWViYmRjYzJjNjk0MmMxOWNjNGM5MzU5NWUzY2UwNiJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiODIxZWVlYzdlNTMwNDFmNGE5ZDgzYTYwYTAxMGNhYzYiLCJuYW1lIjoi56u56Ze05Lqn5ZOB5ZWG55So5Y-R5biDIiwicm9sZSI6IjdjMWVlMTQ2OTNlNTQ4NjJhZDlhMTllNWIwNWEwOGFkIn0seyJhcHBfdHlwZSI6MCwiaWQiOiIzODg4YTMxZGUwMjQ0MWMyODhlNmZlM2FhMDMzZTMyOCIsIm5hbWUiOiLpobnnm67mjpLpm7flv5ciLCJyb2xlIjoiZWVlYmJkY2MyYzY5NDJjMTljYzRjOTM1OTVlM2NlMDYifSx7ImFwcF90eXBlIjowLCJpZCI6IjU4N2U5YWNlZmVlODRhN2JhNzQ2YjgyNDliODgxOGY5IiwibmFtZSI6IumhueebruS6pOS7mOiuree7g-iQpSIsInJvbGUiOiJjMWEzZGZmMDc3ZjE0OGI2ODY0MzUwNGRkMjVjNjU1OCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiNmZkM2MzMTJmOWViNDQ4YmEzNWUxOWUxZWUxMzY0ZjciLCJuYW1lIjoi56u56Ze05LqR5Z-65bqn5Zui6ZifIiwicm9sZSI6ImMxYTNkZmYwNzdmMTQ4YjY4NjQzNTA0ZGQyNWM2NTU4In0seyJhcHBfdHlwZSI6MCwiaWQiOiJmZjAwYmExYzIwNDQ0NDNiYmY4YzQ3ZjQ2ZGFlMWIwMiIsIm5hbWUiOiLkvY7ku6PnoIHlt6XlhbciLCJyb2xlIjoiZWVlYmJkY2MyYzY5NDJjMTljYzRjOTM1OTVlM2NlMDYifSx7ImFwcF90eXBlIjowLCJpZCI6IjE2YzExYWIyOGY1MTRlNzE5MmI2MzY3ZDdjZjY0ZWU2IiwibmFtZSI6IuW8gOWPkeiAheS4reW_gyIsInJvbGUiOiI3YzFlZTE0NjkzZTU0ODYyYWQ5YTE5ZTViMDVhMDhhZCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiOTQ0ZGY4MGQzMWQxNDc3MmEzMjdlYjVlMWMxZWI1NTYiLCJuYW1lIjoi5paw5YW15a2m5bqf6JClIiwicm9sZSI6IjdjMWVlMTQ2OTNlNTQ4NjJhZDlhMTllNWIwNWEwOGFkIn0seyJhcHBfdHlwZSI6MCwiaWQiOiIzMDhkMzkzNTI0MzY0YTFlODQxOTY3MjJkNTcxNzY3MSIsIm5hbWUiOiJYLUF2YXRhciIsInJvbGUiOiI3YzFlZTE0NjkzZTU0ODYyYWQ5YTE5ZTViMDVhMDhhZCJ9LHsiYXBwX3R5cGUiOjAsImlkIjoiMzA0NmVmNTUyYzgyNDAzYTk4YTk1YTU2ODdmY2FmMWUiLCJuYW1lIjoi56u56Ze06L-Q6JCl5Zui6ZifIiwicm9sZSI6ImMxYTNkZmYwNzdmMTQ4YjY4NjQzNTA0ZGQyNWM2NTU4In0seyJhcHBfdHlwZSI6MCwiaWQiOiI3OGZlMjkzMzIyMGQ0MTI3YjkyNjc1MWFjZGIzOGFjMyIsIm5hbWUiOiJQwrfljaDlj5HpvpkiLCJyb2xlIjoiN2MxZWUxNDY5M2U1NDg2MmFkOWExOWU1YjA1YTA4YWQifSx7ImFwcF90eXBlIjowLCJpZCI6IjAwZWY0YjYxYThlYjRmNjhhZWI1MjUwNDAzMGM4YzgwIiwibmFtZSI6IueruemXtOaZuuiDveefpeivhuW6k-WboumYnyIsInJvbGUiOiJlZWViYmRjYzJjNjk0MmMxOWNjNGM5MzU5NWUzY2UwNiJ9XSwiZ3JvdXBzIjpbXX0sInN0YXR1cyI6MSwidHlwZSI6MiwidXNlcl9uYW1lIjoieGlhb2xvbmdodWFuZyJ9LCJpc3MiOiJzaW1wbGUtYXV0aCIsImV4cCI6MTY3NTMyNTM1Nn0.Br6cmZjZ5xSTF6rjvdu6EbZ3jNZR5W8dgRlHyxlyyxM' \
    #     - -header
    #     'Cache-Control: no-cache' \
    #     - -header
    #     'Connection: keep-alive' \
    #     - -header
    #     'Content-Type: application/json;charset=UTF-8' \
    #     - -header
    #     'Cookie: experimentation_subject_id=ImI3M2Y5OTlhLTUzMDQtNDNjOS1iOWEyLWE2YmNlODA4YThlZSI%3D--325f559b4b66c5d24ee7172a20c1b9d4b6ffcbe2; Hm_lvt_e6bafdc067540de4a868e9148a1b0540=1666060914; ajs_user_id=%22487c7855771517e53c298074d18cab589ad03e08%22; ajs_anonymous_id=%223bdf5274-9216-41c2-b99f-d43d0f465daf%22; verify=852e6958bb812c5d09551541317b5ddc' \
    #     - -header
    #     'If-Modified-Since: 0' \
    #     - -header
    #     'Origin: https://knows-init.emotibot.com' \
    #     - -header
    #     'Pragma: no-cache' \
    #     - -header
    #     'Referer: https://knows-init.emotibot.com/kmp/' \
    #     - -header
    #     'Sec-Fetch-Dest: empty' \
    #     - -header
    #     'Sec-Fetch-Mode: cors' \
    #     - -header
    #     'Sec-Fetch-Site: same-origin' \
    #     - -header
    #     'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
    #     - -header
    #     'X-Appid;' \
    #     - -header
    #     'X-Locale: zh-cn' \
    #     - -header
    #     'channelId: -1' \
    #     - -header
    #     'enterpriseId: 7ad0051d31144cf0ba27cb28be5ac919' \
    #     - -header
    #     'orgId: 4' \
    #     - -header
    #     'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
    #     - -header
    #     'sec-ch-ua-mobile: ?0' \
    #     - -header
    #     'sec-ch-ua-platform: "macOS"' \
    #     - -header
    #     'spaceId;' \
    #     - -header
    #     'userId: 13f146ee4909488aaaa96f574fbd776c' \
    #     - -data - raw
    #     '{
    #     "superSearch": false,
    #     "keyword": "文章标题",
    #     "customId": "",
    #     "type": 0,
    #     "orderByKey": "",
    #     "orderByDirection": "DESC",
    #     "startTime": "",
    #     "endTime": "",
    #     "updateStartTime": "",
    #     "updateEndTime": "",
    #     "folderIdList": [],
    #     "tagIdList": [],
    #     "authorIdList": [],
    #     "enterpriseId": "7ad0051d31144cf0ba27cb28be5ac919",
    #     "page": 1,
    #     "limit": 15,
    #     "expandKnowsType": "",
    #     "keywordPosition": [],
    #     "docType": [],
    #     "orgId": "4"
    #
    # }'
    @staticmethod
    def search(userInfo, spaceId, keyword, page, pageSize):
        url = userInfo.host + "/kmBackend/search/main"
        header = {
            "Authorization": "Bearer " + userInfo.token,
            "enterpriseId": userInfo.info.enterprise,
            "orgId": userInfo.info.orgId,
            "spaceId": str(spaceId),
            "userId": userInfo.info.id,
            "userName": userInfo.info.user_name
        }
        param = {
            "superSearch": False,
            "keyword": keyword,
            "customId": "",
            "type": 0,
            "orderByKey": "",
            "orderByDirection": "DESC",
            "startTime": "",
            "endTime": "",
            "updateStartTime": "",
            "updateEndTime": "",
            "folderIdList": [],
            "tagIdList": [],
            "authorIdList": [],
            "enterpriseId": userInfo.info.enterprise,
            "page": page,
            "limit": pageSize,
            "expandKnowsType": "",
            "keywordPosition": [],
            "docType": [],
            "orgId": str(userInfo.info.orgId)
        }
        response = doHttpPost(url, param, header)
        print(response)
        return response


# 发送http get请求
def doHttpGet(url, params, header):
    if params is not None:
        params = parse.urlencode(params, 'utf-8')
    print(header)
    resp_data = requests.get(url=url, params=params, headers=header)
    return resp_data


# 发送http post请求
def doHttpPost(url, params, headers):
    response = requests.post(url=url, json=params, headers=headers)
    return response.json()


class userInfo:
    def __init__(self, result, host):
        self.token = result['token']
        self.host = host
        self.info = info(result['info'])


class info:
    def __init__(self, info):
        self.id = info['id']
        self.user_name = info['user_name']
        self.display_name = info['display_name']
        self.email = info['email']
        self.phone = info['phone']
        self.type = info['type']
        self.roles = info['roles']
        self.enterprise = info['enterprise']
        self.status = info['status']
        self.orgId = str(info['orgId'])

#
# if __name__ =='__main__':
