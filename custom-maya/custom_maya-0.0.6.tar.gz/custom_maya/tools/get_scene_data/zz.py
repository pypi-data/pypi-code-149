import asyncio
import os
import time

from custom_maya import SceneDetails, async_scene


class CC(SceneDetails):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def func(self):
        import custom_maya
        import maya.cmds as cmds
        print(f'进入Maya文件并打印文件名-->{self.get_file_path()}')
        cmds.file(self.get_file_path(), open=True, f=True)
        cs = custom_maya.CustomScene(self.get_file_path())
        short_name, _ = os.path.splitext(os.path.basename(self.get_file_path()))
        #
        with open(f'D:\\Maya\\{short_name}.txt', 'w') as f:
            f.write(str(cs.get_custom_properties()) + str(cmds.ls(type='transform')))

            print('写入文件')


def get_file_path_list(root_dir):
    res = []
    suffix_list = ['.mb', '.ma']

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            short_file_name, suffix = os.path.splitext(os.path.basename(file))
            full_path = os.path.join(root, file)
            if suffix in suffix_list:
                res.append(full_path)
    return res


if __name__ == '__main__':
    t1 = time.time()
    cc = CC()

    # specify a list of Maya files to read
    file_paths = get_file_path_list(root_dir=r'D:\test_scenes')
    asyncio.run(async_scene(file_paths, cc))

    print(f'程序运行了{time.time() - t1}')
