import os

import setuptools


with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()
setuptools.setup(
    name='nonebot_plugin_xiuxian_GCDI',
    version='1.0.3',
    author='QingmuCat',
    author_email='1242550160@qq.com',
    keywords=["pip", "nonebot2", "文游", "修仙"],
    url='https://github.com/QingMuCat/nonebot_plugin_xiuxian_GCDI',
    description='''修仙插件，QQ群与QQ频道均可使用，并且数据互通''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: Chinese (Simplified)"
    ],
    data_files=[
        ('nonebot_plugin_xiuxian_GCDI/xiuxian_info/font.ttf'),
        ('nonebot_plugin_xiuxian_GCDI/xiuxian_info/texture2d/back.png'),
        ('nonebot_plugin_xiuxian_GCDI/xiuxian_info/texture2d/line2.png'),
        ('nonebot_plugin_xiuxian_GCDI/xiuxian_info/texture2d/line3.png'),
        ('nonebot_plugin_xiuxian_GCDI/xiuxian_info/texture2d/line4.png'),
        ('nonebot_plugin_xiuxian_GCDI/xiuxian_info/texture2d/user_state.png'),
            ],
    include_package_data=True,
    platforms="any",
    install_requires=[
        'httpx', 'wcwidth', 'nonebot-adapter-onebot', 'nonebot_plugin_apscheduler', 'Pillow','nonebot_plugin_guild_patch','snoop'],
    )