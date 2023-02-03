# main developer: Yixi Ding <dingyixi@hotmail.com>
import csv
import os
from pathlib import Path
from typing import Optional

import datasets
from datasets import Dataset, DatasetDict
from pytorch_lightning import LightningDataModule
from torch.utils.data import DataLoader, random_split

from SciAssist.utils.data_reader import csv_reader
from SciAssist.utils.data_utils import DataUtilsForSeq2Seq


class SciSummDataModule(LightningDataModule):
    def __init__(
        self,
        data_repo: str,
        train_batch_size: int = 8,
        num_workers: int = 0,
        pin_memory: bool = False,
        data_cache_dir: str = ".cache",
        seed: int = 777,
        data_utils = DataUtilsForSeq2Seq
    ):
        super().__init__()
        self.save_hyperparameters(logger=False)
        self.data_cache_dir = Path(self.hparams.data_cache_dir)
        self.data_utils = self.hparams.data_utils
        self.data_collator = self.data_utils.collator()

        self.data_train: Optional[Dataset] = None
        self.data_val: Optional[Dataset] = None
        self.data_test: Optional[Dataset] = None

    def prepare_data(self) -> DatasetDict:

        # Prepare keywords
        id2kw = {}
        with open("/home/dingyx/project/SciAssist/data/Task2/From-ScisummNet-2019/scisumm_keywords10_yake_bigram_target.csv", 'r', newline='', encoding='ISO-8859-1') as f:
            rows = csv.reader(f)
            # Get Column names
            keys = next(rows)
            # Add values by column
            for row in rows:
                id2kw[row[0]] = row[1]


        file_list = []
        root_dir = "/home/dingyx/project/SciAssist/data/Task2/From-ScisummNet-2019/"
        for dirpath, dirnames, files in os.walk(root_dir):
            file_list = dirnames
            break

        texts = []
        summaries = []
        keywords = []
        for file in file_list:
            with open(os.path.join(root_dir, file, "summary", file + ".scisummnet_human.txt"), "r") as f:
                summary = f.readlines()
                summary = " ".join(summary[1:])
                summaries.append(summary)
            with open(os.path.join(root_dir, file, file + ".txt"), "r") as f:
                text = f.readlines()
                text = " ".join(text)
                texts.append(text)
            keywords.append(id2kw[file].split("#")[:2])
        raw_datasets = {
            "text": texts,
            "summary": summaries,
            "keywords": keywords
        }
        raw_datasets = Dataset.from_dict(raw_datasets)
        return raw_datasets

    def setup(self, stage: Optional[str] = None):
        if not self.data_train and not self.data_val and not self.data_test:
            raw_datasets = self.prepare_data()
            processed_datasets = DatasetDict()
            processed_datasets["whole"] = raw_datasets
            tokenized_datasets = processed_datasets.map(
                lambda x: self.data_utils.tokenize_and_align_labels(x, inputs_column="text", labels_column="summary"),
                batched=True,
                remove_columns=processed_datasets["whole"].column_names,
                load_from_cache_file=True
            )
            # self.data_val = tokenized_datasets["validation"]
            # If labels are not provided, delete the column "labels"
            # self.data_test = tokenized_datasets["test"].remove_columns("labels")
            length = len(tokenized_datasets["whole"])
            train_size = int(0.9 * length)
            validate_size = length - train_size
            self.data_train, self.data_val = random_split(tokenized_datasets["whole"], [train_size, validate_size])


    def train_dataloader(self):
        return DataLoader(
            dataset=self.data_train,
            batch_size=self.hparams.train_batch_size,
            num_workers=self.hparams.num_workers,
            pin_memory=self.hparams.pin_memory,
            collate_fn=self.data_collator,
            shuffle=True,
        )

    def val_dataloader(self):
        return DataLoader(
            dataset=self.data_val,
            batch_size=self.hparams.train_batch_size,
            num_workers=self.hparams.num_workers,
            pin_memory=self.hparams.pin_memory,
            collate_fn=self.data_collator,
            shuffle=False,
        )

    # def test_dataloader(self):
    #     return DataLoader(
    #         dataset=self.data_test,
    #         batch_size=self.hparams.train_batch_size,
    #         num_workers=self.hparams.num_workers,
    #         pin_memory=self.hparams.pin_memory,
    #         collate_fn=self.data_collator,
    #         shuffle=False,
    #     )
    #
