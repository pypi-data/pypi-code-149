# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_naturel_gpt']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.2.1,<3.0.0',
 'nonebot2>=2.0.0rc3,<3.0.0',
 'openai>=0.26.4,<0.27.0',
 'transformers>=4.26.0,<5.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-naturel-gpt',
    'version': '1.1.1',
    'description': '一个基于NoneBot框架的Ai聊天插件，对接OpenAi文本生成接口',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="./image/README/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="./image/README/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n    ✨ 更人性化(拟人)的GPT聊天Ai插件! ✨<br/>\n    🧬 支持多个人格自定义 / 切换 | 尽情发挥你的想象力吧！ ⚙️<br/>\n    <a href="./LICENSE">\n        <img src="https://img.shields.io/badge/license-Apache 2.0-6cg.svg" alt="license">\n    </a>\n    <a href="https://pypi.python.org/pypi/nonebot-plugin-learning-chat">\n        <img src="https://img.shields.io/pypi/v/nonebot-plugin-learning-chat.svg" alt="pypi">\n    </a>\n    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n</div>\n\n## 💡功能列表\n\n* [X] 自动切换api_key: 支持同时使用多个openai_api_key，失效时自动切换\n* [X] 自定义人格预设: 可自定义的人格预设，打造属于你的个性化的TA\n* [X] 聊天基本上下文关联: 群聊场景短期记忆上下文关联，尽力避免聊天出戏\n* [X] 聊天记录总结记忆: 自动总结聊天记忆，具有一定程度的长期记忆能力\n* [X] 用户印象记忆: 每个人格对每个用户单独记忆印象，让TA能够记住你\n* [X] 人格切换: 可随时切换不同人格\n* [X] 数据持久化存储: 保存用户对话信息（使用pickle）\n* [X] 新增/编辑人格: 使用指令进行人格预设的编辑\n* [ ] 潜在人格唤醒机制: 一定条件下，潜在人格会被主动唤醒\n* [ ] 主动聊天参与逻辑: 尽力模仿人类的聊天参与逻辑，目标是让TA能够真正融入你的群组\n\n## 📕使用方式\n\n1. 安装本插件并启用，详见NoneBot关于插件安装的说明\n2. 加载插件并启动一次NoneBot服务\n3. 查看自动生成的 `config/naturel_gpt.config.yml` ，并填入你的OpenAi_Api_key\n4. 在机器人所在的群组或者私聊窗口@TA或者 `提到`TA当前的 `人格名` 即开始聊天\n5. 使用命令 `rg / 人格设定 / 人格 / identity` 即可查看bot信息和相关指令\n6. 启用后bot会开始监听所有消息并适时作出记录和回应，如果你不希望bot处理某条消息，请在消息前加上忽视符（默认为 `#` ，可在配置文件中修改）\n\n## 🛠️参数说明 — `config/naturel_gpt.config.yml`\n\n| 参数名                        | 类型  | 释义                                       |\n| ----------------------------- | ----- | ------------------------------------------ |\n| OPENAI_API_KEYS               | array | OpenAi的 `Api_Key，以字符串数组方式填入    |\n| CHAT_HISTORY_MAX_TOKENS       | int   | 聊天记录最大token数                        |\n| CHAT_MAX_SUMMARY_TOKENS       | int   | 聊天记录总结最大token数                    |\n| CHAT_MEMORY_MAX_LENGTH        | int   | 聊天记忆最大条数                           |\n| CHAT_MEMORY_SHORT_LENGTH      | int   | 短期聊天记忆参考条数                       |\n| CHAT_MODEL                    | str   | 聊天生成的语言模型                         |\n| CHAT_FREQUENCY_PENALTY        | float | 聊天频率重复惩罚                           |\n| CHAT_PRESENCE_PENALTY         | float | 聊天主题重复惩罚                           |\n| CHAT_TEMPERATURE              | float | 聊天生成温度: 越高越随机                   |\n| CHAT_TOP_P                    | float | 聊天信息采样率                             |\n| IGNORE_PREFIX                 | str   | 忽略前置修饰：添加此修饰的聊天信息将被忽略 |\n| REPLY_MAX_TOKENS              | int   | 生成回复的最大token数                      |\n| REQ_MAX_TOKENS                | int   | 发起请求的最大token数                      |\n| USER_MEMORY_SUMMARY_THRESHOLD | int   | 用户聊天印象总结触发阈值                   |\n| REPLY_ON_AT                   | bool  | 在被 `@TA` 时回复                        |\n| REPLY_ON_NAME_MENTION         | bool  | 在被 `提及` 时回复                       |\n| PRESETS                       | dict  | 人格预设集合                               |\n| NG_DATA_PATH                  | str   | 数据文件目录                               |\n| ADMIN_USERID                  | array | 管理员id，以字符串数组方式填入             |\n| \\_\\_DEBUG\\_\\_                 | bool  | 是否开启DEBUG输出                          |\n\n## 🎢更新日志\n\n### [2023/2/2] v1.1.0\n\n- 新增了预设编辑功能\n- 新增自定义管理员id功能，管理员可以删除预设 / 修改锁定的预设\n- 增加debug开关控制生成文本时的控制台输出（默认关闭）\n\n### [2023/2/2] v1.1.1\n\n- 修复查询人格错误的问题\n',
    'author': 'KroMiose',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
