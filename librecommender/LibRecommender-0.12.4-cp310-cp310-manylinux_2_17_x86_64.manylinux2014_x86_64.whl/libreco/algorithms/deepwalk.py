"""

Reference: Bryan Perozzi et al. "DeepWalk: Online Learning of Social Representations"
           (https://arxiv.org/pdf/1403.6652.pdf)

author: massquantity

"""
import random
from collections import defaultdict

import numpy as np
from gensim.models import Word2Vec
from tqdm import tqdm

from ..bases import GensimBase


class DeepWalk(GensimBase):
    def __init__(
        self,
        task,
        data_info,
        embed_size=16,
        norm_embed=False,
        n_walks=10,
        walk_length=10,
        window_size=5,
        n_epochs=5,
        n_threads=0,
        seed=42,
        lower_upper_bound=None,
        with_training=True,
    ):
        super().__init__(
            task,
            data_info,
            embed_size,
            norm_embed,
            window_size,
            n_epochs,
            n_threads,
            seed,
            lower_upper_bound,
        )
        assert task == "ranking", "DeepWalk is only suitable for ranking"
        self.all_args = locals()
        self.n_walks = n_walks
        self.walk_length = walk_length
        if with_training:
            self.graph = self._build_graph()
            self.data = self.get_data()

    def _build_graph(self):
        graph = defaultdict(list)
        for items in self.user_consumed.values():
            for i in range(len(items) - 1):
                graph[items[i]].append(items[i + 1])
        return graph

    def get_data(self):
        return ItemCorpus(self.graph, self.n_items, self.n_walks, self.walk_length)

    def build_model(self):
        model = Word2Vec(
            vector_size=self.embed_size,
            window=self.window_size,
            sg=1,
            hs=1,
            seed=self.seed,
            min_count=1,
            workers=self.workers,
            sorted_vocab=0,
        )
        model.build_vocab(self.data, update=False)
        return model


class ItemCorpus:
    def __init__(self, graph, n_items, n_walks, walk_length):
        self.graph = graph
        self.n_items = n_items
        self.n_walks = n_walks
        self.walk_length = walk_length
        self.i = 0

    def __iter__(self):
        for _ in tqdm(range(self.n_walks), desc=f"DeepWalk iter {self.i}"):
            for node in np.random.permutation(self.n_items):
                walk = [node]
                while len(walk) < self.walk_length:
                    neighbors = self.graph[walk[-1]]
                    if len(neighbors) > 0:
                        walk.append(random.choice(neighbors))
                    else:
                        break
                yield list(map(str, walk))
        self.i += 1
