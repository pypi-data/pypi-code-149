import os

# 默认文件路径，不建议修改！！！
PATH_BASIC = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

PATH_PACKAGE = os.path.join(PATH_BASIC, "package")
PATH_PLUGIN = os.path.join(PATH_BASIC, "plugins")

PATH_ROBOT = os.path.join(PATH_BASIC, "robot")
PATH_MUSIC = os.path.join(PATH_BASIC, PATH_ROBOT, "music")
PATH_TEMP = os.path.join(PATH_BASIC, PATH_ROBOT, "temp")


# 用户路径，在代码根目录，可由用户修改
PATH_CONFIG_YAML = "config.yaml"
PATH_CUSTOM_PLUGIN = "plugins"
PATH_CUSTOM_MUSIC = "music"

# 指定临时文件名称
PATH_TEMP_MP3 = os.path.join(PATH_TEMP, "temp.mp3")
PATH_TEMP_WAV = os.path.join(PATH_TEMP, "temp.wav")



if __name__ == "__main__":
    for k, v in dict(locals()).items():
        if "PATH" in k:
            print(f"{k}:".rjust(20), v)
