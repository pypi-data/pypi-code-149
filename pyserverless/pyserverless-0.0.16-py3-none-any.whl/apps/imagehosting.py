#!/usr/bin/env python3
from codefast.asyncio import async_render

import base64 
import hashlib
from pyserverless.auth import auth 
import os 

try:
    os.system('pip3 install PyGithub')
    os.system('pip3 install python-multipart')
except:
    pass 

def _github_upload(content:bytes)->str:
    from github import Github, InputGitTreeElement
    _token = auth['117_git_token']
    repo = Github(_token, timeout=300).get_user().get_repo('imagehosting')
    data = base64.b64encode(content)
    file_name = hashlib.md5(content).hexdigest() + '.png'
    blob = repo.create_git_blob(data.decode("utf-8"), "base64")
    path = f'2023/{file_name}'
    element = InputGitTreeElement(path=path,
                                  mode='100644',
                                  type='blob',
                                  sha=blob.sha)
    element_list = list()
    element_list.append(element)

    master_ref = repo.get_git_ref('heads/master')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)
    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(f"Uploading {file_name }", tree, [parent])
    master_ref.edit(commit.sha)
    return f'https://cdn.jsdelivr.net/gh/117v2/imagehosting@master/2023/{file_name}'


async def github_upload(content:bytes)->str:
    return await async_render(_github_upload, content)