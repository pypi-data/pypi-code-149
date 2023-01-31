#!/usr/bin/env python
from flask import Flask, request, jsonify
from cux.oss import AliyunOSS
from typing import Callable, Dict, List, Optional, Set, Tuple, Union

import codefast as cf

from cux.sql import AppSlave
import json


def text_info(cid: int) -> dict:
    obj = AppSlave().transcription(cid)
    cf.info('text info return {}'.format(obj))
    if not obj:
        return {'Error': 'FOUND no information regarding cid: {}'.format(cid)}
    audio_path = obj.audio_file_path.split('com/')[1]
    text_path = obj.trans_file_path.split('com/')[1]

    alioss = AliyunOSS()
    obj.audio_url = alioss.sign(audio_path)
    obj.text_url = alioss.sign(text_path)
    obj.audio_info = json.loads(cf.shell(
        "ffprobe -v quiet -print_format json -show_format -show_streams '{}'".format(obj.audio_url.replace('\n', ''))))
    del obj.__dict__['single_file_path']
    del obj.__dict__['trans_file_path']
    del obj.__dict__['audio_file_path']
    return obj.__dict__


app = Flask(__name__)

TOKEN = '736d1e5be52f605ca1c726cabee0f3bc25e7f512'

@app.route('/text', methods=['POST', 'GET'])
def conversation_info():
    conversation_id = request.args.get(
        'conversation_id') or request.args.get('cid')
    token = request.args.get('token')
    if token != TOKEN:
        return jsonify({'Error': 'Invalid token'})
    cf.info('receive {}'.format(conversation_id))
    if conversation_id is None:
        return jsonify({'code': 400, 'msg': 'conversation_id is required'})

    return jsonify(text_info(conversation_id))


def ai_info(cid: int) -> Dict:
    try:
        return AppSlave().ai_process(cid, with_color=False)
    except Exception as e:
        cf.error(e)
        return {'Error': 'FOUND no information regarding cid: {}'.format(cid)}


@app.route('/ai', methods=['POST', 'GET'])
def _ai_info():
    token = request.args.get('token')
    if token != TOKEN:
        return jsonify({'Error': 'Invalid token'})

    conversation_id = request.args.get(
        'conversation_id') or request.args.get('cid')
    cf.info('receive {}'.format(conversation_id))
    if conversation_id is None:
        return jsonify({'code': 400, 'msg': 'conversation_id is required'})

    return jsonify(ai_info(conversation_id))


def serve():
    app.run(host='0.0.0.0', port=10001)


if __name__ == '__main__':
    serve()
