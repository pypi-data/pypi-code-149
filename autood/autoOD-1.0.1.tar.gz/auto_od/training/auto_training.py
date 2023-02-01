import glob
import io
import os
import selectors
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from collections import namedtuple
from typing import Any

import pandas as pd
import tensorflow as tf

try:
    from object_detection.utils import colab_utils
except:
    pass
from object_detection.utils import dataset_util
from PIL import Image
from tensorboard import program

from auto_od.core.logger import logger
from auto_od.training.configuration.config import PipelineConfig
from auto_od.training.stop.stop_algo import StopAlgo
from auto_od.utils.info_messages import (df_created, file_created,
                                         file_deleted, file_exists,
                                         file_not_found)

sys.path.insert(0, 'models/research')


class ObjectDetection(PipelineConfig, StopAlgo):
    def __init__(self, config_path: str):
        PipelineConfig.__init__(self, config_path=config_path)
        self.all_data_dir: str = os.path.join(self.settings.dataset_dir, self.settings.all_data_folder)
        self.test_dir: str = os.path.join(self.settings.dataset_dir, self.settings.test_folder)
        self.train_dir: str = os.path.join(self.settings.dataset_dir, self.settings.train_folder)

        self.additional_dir: str = os.path.join(self.settings.path_to_work_dir, self.settings.additional_folder)
        self.models_dir: str = os.path.join(self.additional_dir, self.settings.models_folder)
        self.annotations_dir: str = os.path.join(self.additional_dir, self.settings.annotations_folder)

        self.label_map_dir: str = os.path.join(self.annotations_dir, 'label_map.pbtxt')
        self.data_csv_dir: str = os.path.join(self.annotations_dir, 'data.csv')
        self.test_record: str = os.path.join(self.annotations_dir, 'test_data.record')
        self.train_record: str = os.path.join(self.annotations_dir, 'train_data.record')

        self.models: pd.DataFrame = self.get_model()
        self.pipeline_folder = self.models.iloc[self.settings.model_id]['Link'].split('/')[-1].split('.')[
                                   0] + '/pipeline.config'
        self.pipeline_dir: str = os.path.join(self.models_dir, self.pipeline_folder)
        StopAlgo.__init__(self, config_path=config_path)

    def get_model(self) -> pd.DataFrame:
        """!
        Get pretrained models' info.
        @return DataFrame with models, their speeds and COCOMaP.
        """
        models = None
        models_dir = self.settings.pretrained_model_dir
        try:
            models = pd.read_csv(models_dir)
        except FileNotFoundError:
            logger.error(file_not_found.format(models_dir))
        return models

    def label_map(self, annotations: list[str]) -> None:
        """!
        Create labels' file with pbtxt format.
        @param list annotations: Labels' list.
        """
        try:
            os.remove(self.label_map_dir)
            logger.info(file_deleted.format(self.label_map_dir))
        except FileNotFoundError:
            logger.info(file_not_found.format(self.label_map_dir) + ' It will be created.')

        with open(self.label_map_dir, 'a') as f:
            for id_ in range(1, len(annotations) + 1):
                list_of_string = ['item\n', '{\n', '  id: {}'.format(int(id_)), '\n',
                                  "  name:'{0}'".format(str(annotations[id_ - 1])), '\n', '}\n']
                for string in list_of_string:
                    f.write(string)

    @staticmethod
    def xml_to_csv(path: str) -> pd.DataFrame:
        """!
        Formation of a DataFrame containing info about objects in images.
        @param str path: Directory path with xml files.
        @return DataFrame with objects' info.
        """
        xml_list = []
        for xml_file in glob.glob(path + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
        column_name = ['id', 'width', 'height', 'class_', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_df = pd.DataFrame(xml_list, columns=column_name)
        logger.info(df_created.format('xml_df'))
        return xml_df

    def create_annot_csv(self) -> pd.DataFrame:
        """!
        Get DataFrame containing info about objects on images and write it to csv file.
        @return DataFrame with objects' info
        """
        if os.path.exists(self.data_csv_dir):
            annot = pd.read_csv(self.data_csv_dir)
            logger.info(file_exists.format('data.csv'))
            return annot

        xml_df = self.xml_to_csv(self.all_data_dir)
        xml_df.to_csv(self.data_csv_dir)
        logger.info(file_created.format('data.csv'))
        return xml_df

    @staticmethod
    def create_tf_example(group, path: str, annotations: list[str]) -> Any:
        """!
        Prepare data to write TFRecord files.
        @param group: DataFrame (id, object) data.
        @param str path: Path to train/test data.
        @param list annotations: Objects.
        @return Data in the TF format.
        """

        def class_text_to_int(row_label, dictionary):
            return dictionary[row_label]

        d = {k: v for v, k in enumerate(annotations, start=1)}
        with tf.io.gfile.GFile(os.path.join(path, '{}'.format(group.id)), 'rb') as fid:
            encoded_image_data = fid.read()
        encoded_jpg_io = io.BytesIO(encoded_image_data)
        img = Image.open(encoded_jpg_io)
        filename = group.id.encode('utf8')
        height = img.size[1]
        width = img.size[0]
        image_format = b'jpeg'
        xmins = []
        xmaxs = []
        ymins = []
        ymaxs = []
        classes_text = []
        classes = []

        for index, row in group.object.iterrows():
            xmins.append(row['xmin'] / width)
            xmaxs.append(row['xmax'] / width)
            ymins.append(row['ymin'] / height)
            ymaxs.append(row['ymax'] / height)
            classes_text.append(row['class_'].encode('utf8'))
            classes.append(class_text_to_int(row['class_'], d))

        tf_example = tf.train.Example(features=tf.train.Features(feature={
            'image/height': dataset_util.int64_feature(height),
            'image/width': dataset_util.int64_feature(width),
            'image/filename': dataset_util.bytes_feature(filename),
            'image/source_id': dataset_util.bytes_feature(filename),
            'image/encoded': dataset_util.bytes_feature(encoded_image_data),
            'image/format': dataset_util.bytes_feature(image_format),
            'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
            'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
            'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
            'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
            'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
            'image/object/class/label': dataset_util.int64_list_feature(classes),
        }))
        return tf_example

    def write_to_record(self, annot: pd.DataFrame, annotations: list[str]) -> None:
        """!
        Convert annotations to the TFRecord format.
        @param annot: DataFrame with objects' data.
        @param list annotations: Objects' list.
        """

        def split(df: pd.DataFrame, group_name: str) -> list:
            data = namedtuple('data', ['id', 'object'])
            gb = df.groupby(group_name)
            return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

        train = os.listdir(self.train_dir)
        test = os.listdir(self.test_dir)
        df_train = annot.loc[~annot.id.isin(test)]
        df_test = annot.loc[~annot.id.isin(train)]
        writer = tf.io.TFRecordWriter(os.path.join(self.annotations_dir, 'train_data.record'))

        grouped_train = split(df_train, 'id')
        for group in grouped_train:
            tf_example = self.create_tf_example(group, self.train_dir, annotations)
            writer.write(tf_example.SerializeToString())
        writer.close()

        writer = tf.io.TFRecordWriter(os.path.join(self.annotations_dir, 'test_data.record'))
        grouped_test = split(df_test, 'id')
        for group in grouped_test:
            tf_example = self.create_tf_example(group, self.test_dir, annotations)
            writer.write(tf_example.SerializeToString())
        writer.close()

    def create_pipeline_config(self, annotations: list[str]) -> None:
        """!
        Generate custom pipeline.config; Add relevant parameters to the detection task.
        @param list annotations: Objects' list.
        """
        fine_tune_checkpoint = '/'.join(self.pipeline_dir.split('/')[:-1]) + '/checkpoint/ckpt-0'
        new_pipeline_dir = os.path.join(self.models_dir, 'pipeline.config')
        self.generate_config(pipeline_dir=self.pipeline_dir, new_pipeline_dir=new_pipeline_dir,
                             test_record=self.test_record, train_record=self.train_record,
                             fine_tune_checkpoint=fine_tune_checkpoint, label_map_dir=self.label_map_dir,
                             annotations=annotations)
        logger.info(file_created.format(new_pipeline_dir))

    def prepare(self) -> None:
        """!
        Generate all files to start training.
        @return
        """
        if tf.test.gpu_device_name():
            logger.info('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
        else:
            logger.info("Please install GPU version of TF")
        model = os.path.join(self.models_dir,
                             self.models.iloc[self.settings.model_id]['Link'].split('/')[-1]).split('.')[0]
        if not os.path.exists(model):
            os.system(f"wget -P {self.models_dir} {self.models.iloc[self.settings.model_id]['Link']}")
            tarfile = os.path.join(self.models_dir, self.models.iloc[self.settings.model_id]['Link'].split('/')[-1])
            os.system(f'tar -xzf {tarfile} -C {self.models_dir}')

        time.sleep(5)

        df = self.create_annot_csv()
        annotations = list(set(df['class_']))
        logger.info('Objects that will be detected: {}'.format(', '.join(annotations)))
        self.label_map(annotations)

        time.sleep(5)
        self.write_to_record(df, annotations)
        time.sleep(5)
        self.create_pipeline_config(annotations)
        time.sleep(15)

    def train(self) -> None:
        """!
        Start model training.
        @return
        """
        output_dir = os.path.join(self.models_dir, 'output')
        pipeline_dir = os.path.join(self.models_dir, 'pipeline.config')
        mm_tf2_path = os.path.join(self.settings.path_to_work_dir, "models/research/object_detection/model_main_tf2.py")
        command_train = [
            "python", mm_tf2_path, f"--pipeline_config_path={pipeline_dir}",
            f"--model_dir={output_dir}", "--alsologtostderr",
            "--checkpoint_every_n=200", "--max_to_keep=15"
        ]
        size_val_done = 0

        def execute(cmd: list[str], size: int) -> None:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            sel = selectors.DefaultSelector()
            sel.register(process.stdout, selectors.EVENT_READ)
            sel.register(process.stderr, selectors.EVENT_READ)
            if self.settings.early_stopping:
                self.run_eval()
            while True:
                for key, _ in sel.select():
                    data = key.fileobj.read1().decode()
                    if not data:
                        exit()
                    if key.fileobj is process.stdout:
                        print(data, end="")
                        flag = self.select_logs(log=data)
                        self.read_train_loss(flag=flag)
                    else:
                        print(data, end="", file=sys.stderr)
                        flag = self.select_logs(log=data)
                        self.read_train_loss(flag=flag)
                    if self.settings.early_stopping:
                        size = self.run_stop_algo(size=size)

        execute(cmd=command_train, size=size_val_done)
        if self.settings.early_stopping:
            _ = self.run_stop_algo(size=size_val_done)

    def run_eval(self) -> None:
        """!
        Run validation. Result log file: val_loss.log
        @return
        """
        output_dir = os.path.join(self.models_dir, 'output')
        pipeline_dir = os.path.join(self.models_dir, 'pipeline.config')
        mm_tf2_path = os.path.join(self.settings.path_to_work_dir, "models/research/object_detection/model_main_tf2.py")

        command = [
            "python", mm_tf2_path, f"--pipeline_config_path={pipeline_dir}",
            f"--model_dir={output_dir}", f"--checkpoint_dir={output_dir}"
        ]
        self.eval(command)

