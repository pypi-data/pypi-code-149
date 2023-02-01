from __future__ import annotations

from warnings import warn

from dataclasses import dataclass, field
from random import random
from typing import cast, Dict, List, Optional, Tuple, Union

from . import efnlp_pb2 as pb


def split_input(encoded: List[int], num_segments: int, block_size: int) -> List[List[int]]:

    remainder = len(encoded) % num_segments
    normalized_size = int((len(encoded) - remainder) / num_segments)
    if normalized_size <= block_size:
        raise ValueError("too many segments for specified block size")

    segment_sizes = [normalized_size + (1 if i < remainder else 0) for i in range(num_segments)]

    s, e = 0, segment_sizes[0]
    segments = []
    for i in range(num_segments):
        segments.append(encoded[max(0, s - block_size) : e])
        s += segment_sizes[i]
        if i == num_segments - 1:
            e = len(encoded)
        else:
            e += segment_sizes[i + 1]

    return segments


def merge_split_input(segments: List[List[int]], block_size: int) -> List[int]:
    recomposed = segments[0]
    for i in range(1, len(segments)):
        recomposed += segments[i][block_size:]
    return recomposed


@dataclass
class Language:

    size: int
    stot: Dict[str, int]
    ttos: Dict[int, str]

    @staticmethod
    def from_proto_file(name: str) -> Language:
        with open(name, "rb") as f:
            return Language.from_proto_bytes(f.read())

    @staticmethod
    def from_proto_bytes(data: bytes) -> Language:
        P = pb.Language()
        P.ParseFromString(data)
        return Language.from_proto(P)

    @staticmethod
    def from_proto(L: pb.Language) -> Language:
        return Language(
            size=len(L.lang),
            stot={e.data: e.token for e in L.lang},
            ttos={e.token: e.data for e in L.lang},
        )

    def proto(self) -> pb.Language:
        L = pb.Language()
        for t, s in self.ttos.items():
            e = pb.Encoder(token=t, data=s)
            L.lang.append(e)
        return L

    def encode(self, s: str) -> List[int]:
        raise NotImplementedError("Base Language doesn't encode (yet)")

        # General: incrementally parse forward with the longest match
        # in a prefix tree?
        #
        # i = 0
        # while i is not None:
        #   t, i = self.encoder.encode(s, i) # token and next char (i + len(match) | None)
        #
        # what's an "encoder"? 
        # 
        # class Encoder:
        #   depth: int
        #   prefixes: Dict[str, Encoder]
        #   
        #   def encode(self, s: str, i: int) -> Tuple[int, Optional[int]]:
        #       if i >= len(s):
        #           raise ValueError("cannot encode past string length")
        #       if s[i] not in self.prefixes:
        #           return None
        #       self.prefixes.encode(s, i)
        #           
        # 

    def decode(self, tokens: Union[int, List[int]]) -> str:
        if isinstance(tokens, list):
            return "".join(self.ttos[t] for t in tokens)
        return self.decode([tokens])


@dataclass
class CharLanguage(Language):
    @staticmethod
    def from_corpus(C: str) -> CharLanguage:
        lang = sorted(list(set(c for c in C)))
        return CharLanguage(
            size=len(lang),
            stot={c: i for i, c in enumerate(lang)},
            ttos={i: c for i, c in enumerate(lang)},
        )

    @staticmethod
    def from_proto_file(name: str) -> CharLanguage:
        with open(name, "rb") as f:
            return CharLanguage.from_proto_bytes(f.read())

    @staticmethod
    def from_proto_bytes(data: bytes) -> CharLanguage:
        P = pb.Language()
        P.ParseFromString(data)
        return CharLanguage.from_proto(P)

    @staticmethod
    def from_proto(L: pb.Language) -> CharLanguage:
        return CharLanguage(
            size=len(L.lang),
            stot={e.data: e.token for e in L.lang},
            ttos={e.token: e.data for e in L.lang},
        )

    def encode(self, s: str) -> List[int]:
        return [self.stot[c] for c in s]


class Sampler:

    # total: int
    # counts: Dict[int, int]

    def __init__(self, total: Optional[int] = 0, counts: Optional[Dict[int, int]] = None) -> None:
        self.total: int = total or 0
        self.counts: Dict[int, int] = {} if counts is None else {t: c for t, c in counts.items()}

    @staticmethod
    def from_proto_file(name: str) -> Sampler:
        with open(name, "rb") as f:
            return Sampler.from_proto_bytes(f.read())

    @staticmethod
    def from_proto_bytes(data: bytes) -> Sampler:
        assert isinstance(data, bytes)
        P = pb.Sampler()
        P.ParseFromString(data)
        return Sampler.from_proto(P)

    @staticmethod
    def from_proto(S: pb.Sampler) -> Sampler:
        assert isinstance(S, pb.Sampler), (type(S), S)
        s = Sampler(total=S.total)
        s.counts = {stc.token: stc.count for stc in S.counts}
        return s

    @staticmethod
    def copy(S: Sampler) -> Sampler:
        return Sampler(total=S.total, counts=S.counts)

    def proto(self) -> pb.Sampler:
        S = pb.Sampler(total=self.total)
        for t, c in self.counts.items():
            stc = pb.SamplerTokenCount(token=t, count=c)
            S.counts.append(stc)
        return S

    def __bytes__(self) -> bytes:
        return self.proto().SerializeToString()

    def __contains__(self, token: int) -> bool:
        return token in self.counts

    def __add__(self, t: int) -> Sampler:
        return self.add(t)

    def __iadd__(self, t: int) -> Sampler:
        return self.add(t)

    def __getitem__(self, t: int) -> int:
        return self.counts[t]

    def get(self, t: int, default: int = 0) -> int:
        return self.counts.get(t, default)

    def items(self):  # -> List[Tuple[int, int]]:
        return self.counts.items()

    def __iter__(self):
        return self.counts.__iter__()

    def __next__(self):
        return self.counts.__next__()

    def add(self, t: int) -> Sampler:
        self.total += 1
        if t in self.counts:
            self.counts[t] += 1
        else:
            self.counts[t] = 1
        return self

    def memory(self) -> int:
        return 4 + 2 * len(self.counts)

    def merge(self, other: Sampler) -> Sampler:
        self.total += other.total
        for t in self.counts:
            self.counts[t] += other.get(t)
        for t in other:
            if t not in self.counts:
                self.counts[t] = other[t]
        return self

    def sample(self) -> int:
        r = self.total * random()
        for t, c in self.counts.items():
            if r < c:
                return t
            r -= c
        raise Exception("We should not be here, sampler malformed")

    def probability(self, token: int) -> float:
        return self.counts.get(token, 0) / self.total


@dataclass
class SuffixTree:

    token: int  # token index
    depth: int = field(init=False)  # occurrences
    sampler: Sampler = field(init=False)
    children: Dict[int, SuffixTree] = field(init=False)  # "children" is a bad name

    def __post_init__(self) -> None:
        self.depth = 0
        self.sampler = Sampler()
        self.children = {}

    @staticmethod
    def from_proto_file(name: str) -> SuffixTree:
        with open(name, "rb") as f:
            return SuffixTree.from_proto_bytes(f.read())

    @staticmethod
    def from_proto_bytes(data: bytes) -> SuffixTree:
        P = pb.SuffixTree()
        P.ParseFromString(data)
        return SuffixTree.from_proto(P)

    @staticmethod
    def from_proto(T: pb.SuffixTree) -> SuffixTree:
        t = SuffixTree(token=T.token)
        t.sampler = Sampler.from_proto(T.sampler)
        for c in T.prefixes:
            t.children[c.token] = SuffixTree.from_proto(c)
        return t

    @staticmethod
    def copy(T: SuffixTree) -> SuffixTree:
        S = SuffixTree(token=T.token)
        S.depth = T.depth
        S.sampler = Sampler.copy(T.sampler)
        S.children = {t: SuffixTree.copy(T.children[t]) for t in T}
        return S

    def proto(self) -> pb.SuffixTree:
        T = pb.SuffixTree(token=self.token)
        T.sampler.CopyFrom(self.sampler.proto())
        for _, c in self.children.items():
            T.prefixes.append(c.proto())
        return T

    def __bytes__(self) -> bytes:
        return self.proto().SerializeToString()

    def __add__(self, child: SuffixTree) -> SuffixTree:
        return self.add(child)

    def __contains__(self, token: int) -> bool:
        return token in self.children

    def __getitem__(self, token: int) -> SuffixTree:
        return self.children[token]

    def __setitem__(self, token: int, child: SuffixTree) -> SuffixTree:
        self.children[token] = child
        return self

    def __iter__(self):
        return self.children.__iter__()

    def __next__(self):
        return self.children.__next__()

    def __call__(self, prefix: List[int]) -> float:
        """Convenience for sampling."""
        return self.sample(prefix)

    def get(self, token: int) -> Optional[SuffixTree]:
        """Return the child with given token, or None."""
        return self.children.get(token)

    def add(self, child: SuffixTree) -> SuffixTree:
        """Add a "child" token in the children map (though "children"
        is a bit misleading in context). Chainable."""
        self.children[child.token] = child
        return self

    def parse(self, prefix: List[int], successor: int) -> SuffixTree:
        """Parse a prefix into this SuffixTree, including the successor
        token. Chainable."""
        self.sampler += successor
        if len(prefix) > 0:
            C = self.get(prefix[-1])
            if C is None:
                C = SuffixTree(prefix[-1])
                self[prefix[-1]] = C
            C.parse(prefix[:-1], successor)
            self.depth = max(self.depth, C.depth + 1)

        return self

    @staticmethod
    def merge_proto_bytes(a: bytes, b: bytes) -> SuffixTree:
        return SuffixTree.merge_trees(
            SuffixTree.from_proto_bytes(a), SuffixTree.from_proto_bytes(b)
        )

    @staticmethod
    def merge_proto(a: pb.SuffixTree, b: pb.SuffixTree) -> SuffixTree:
        return SuffixTree.merge_trees(SuffixTree.from_proto(a), SuffixTree.from_proto(b))

    @staticmethod
    def merge_trees(a: SuffixTree, b: SuffixTree) -> SuffixTree:
        return a.merge(b)

    def merge(self, other: SuffixTree) -> SuffixTree:
        """Merge another SuffixTree into this one"""
        assert self.token == other.token
        self.depth += max(self.depth, other.depth)
        self.sampler.merge(other.sampler)
        for t in self:
            if t in other:
                self.children[t].merge(other.children[t])
        for t in other:
            if t not in self:
                self.children[t] = SuffixTree.copy(other.children[t])
                # TODO: is a copy required? why not just reference?
        return self

    def memory(self) -> int:
        """Return an estimate of the memory requirements for this tree"""
        return self.sampler.memory() + sum([4 + c.memory() for t, c in self.children.items()])

    def prefixes(self) -> List[List[int]]:
        """List all prefixes held in this SuffixTree. These are
        basically the set of paths to leaf nodes from this node."""
        if len(self.children) == 0:
            return [[self.token]]
        return [(p + [self.token]) for _, c in self.children.items() for p in c.prefixes()]

    def patterns(self) -> List[Tuple[List[int], int]]:
        """List all "patterns" held in this SuffixTree. These are
        basically the set of paths to leaf nodes from this node,
        along with any successor tokens."""
        if len(self.children) == 0:
            return [([self.token], t) for t in self.sampler.counts]
        return [
            (p[0] + [self.token], p[1]) for _, c in self.children.items() for p in c.patterns()
        ]

    def search(self, prefix: List[int]) -> List[int]:
        """Search for a given prefix in this tree. Returns
        the longest match."""
        if (len(prefix) > 0) and (prefix[-1] in self):
            if len(prefix) == 1:
                return [prefix[-1], self.token]
            return self[prefix[-1]].search(prefix[:-1]) + [self.token]
        return [self.token]

    def match(self, prefix: List[int]) -> bool:
        """Return true if the presented prefix is in the suffix tree"""
        if len(prefix) == 0:
            raise ValueError("can't match the empty token string")
        if prefix[-1] in self:
            if len(prefix) == 1:
                return True
            return self[prefix[-1]].match(prefix[:-1])
        return False

    def sample(self, prefix: List[int]) -> int:
        """Sample a token that likely follows a prefix. Requires
        a normalized tree for now. Recurses to search for the
        longest matching suffix for the prefix."""
        if len(prefix) == 0 or prefix[-1] not in self:
            return self.sampler.sample()
        return self[prefix[-1]].sample(prefix[:-1])

    def probability(self, prefix: List[int], successor: int) -> float:
        """Return pattern probability. Basically suffix search
        but returning the probability of the longest match."""

        if len(prefix) == 0:
            return self.sampler.counts.get(successor, 0) / self.sampler.total

        # search children
        C = self.children.get(prefix[-1])
        if C is None:
            return self.sampler.counts.get(successor, 0) / self.sampler.total

        # recurse into matched child with the prefix's prefix
        return C.probability(prefix[:-1], successor)

        # TODO: verify


class SuffixTreeSet:

    # size: int  # "vocab" size
    # depth: int = field(init=False)
    # trees: Dict[int, SuffixTree] = field(init=False)
    # sampler: Sampler = field(init=False) # for counting raw token occurrences

    def __init__(self, size: int = 0) -> None:
        self.size: int = size
        self.depth: int = 0
        self.trees: Dict[int, SuffixTree] = {t: SuffixTree(t) for t in range(self.size)}
        self.sampler: Sampler = Sampler()

    @staticmethod
    def from_proto_file(name: str) -> SuffixTreeSet:
        with open(name, "rb") as f:
            return SuffixTreeSet.from_proto_bytes(f.read())

    @staticmethod
    def from_proto_bytes(data: bytes) -> SuffixTreeSet:
        P = pb.SuffixTreeSet()
        P.ParseFromString(data)
        return SuffixTreeSet.from_proto(P)

    @staticmethod
    def from_proto(S: pb.SuffixTreeSet) -> SuffixTreeSet:
        s = SuffixTreeSet(size=len(S.prefixes))
        for c in S.prefixes:
            s.trees[c.token] = SuffixTree.from_proto(c)
        return s

    def proto(self) -> pb.SuffixTreeSet:
        S = pb.SuffixTreeSet()
        for _, c in self.trees.items():
            S.prefixes.append(c.proto())
        return S

    def __bytes__(self) -> bytes:
        return self.proto().SerializeToString()

    def __contains__(self, token: int) -> bool:
        return token in self.trees

    def __getitem__(self, token: int) -> SuffixTree:
        return self.trees[token]

    def __iter__(self):
        return self.trees.__iter__()

    def __next__(self):
        return self.trees.__next__()

    def items(self):
        return self.trees.items()

    def parse(self, prefix: List[int], successor: int) -> SuffixTreeSet:
        if len(prefix) == 0:
            raise ValueError("Cannot parse empty prefix")
        self.sampler += successor
        if prefix[-1] not in self.trees:
            self.trees[prefix[-1]] = SuffixTree(prefix[-1])
        self.trees[prefix[-1]].parse(prefix[:-1], successor)
        self.depth = max(self.depth, self.trees[prefix[-1]].depth + 1)
        return self

    def parse_all(
        self, tokens: List[int], block_size: int, ignore_start: bool = False
    ) -> SuffixTreeSet:
        if not ignore_start:
            for i in range(1, block_size):  # leading sub-block_size prefixes
                self.parse(tokens[0:i], tokens[i])
        for i in range(block_size, len(tokens) - 1):
            self.parse(tokens[i - block_size : i], tokens[i])
        return self

    def merge(self, other: SuffixTreeSet) -> SuffixTreeSet:
        assert self.size == other.size
        self.depth = max(self.depth, other.depth)
        for i in range(self.size):
            self.trees[i].merge(other.trees[i])
        return self

    def memory(self) -> int:
        return self.sampler.memory() + sum([T.memory() for _, T in self.trees.items()])

    def prefixes(self, token: Optional[int] = None) -> List[List[int]]:
        if token is None:
            r = []
            for t in range(self.size):
                r += self.prefixes(t)
            return r
        return self.trees[token].prefixes()

    def patterns(self, token: Optional[int] = None) -> List[Tuple[List[int], int]]:
        if token is None:
            r = []
            for t in range(self.size):
                r += self.patterns(t)
            return r
        return self.trees[token].patterns()

    def search(self, prefix: List[int]) -> List[int]:
        if len(prefix) == 0:
            raise ValueError("can't search the empty token string")
        if prefix[-1] in self:
            return self.trees[prefix[-1]].search(prefix[:-1])
        return []

    def match(self, prefix: List[int]) -> bool:
        if len(prefix) == 0:
            raise ValueError("can't match the empty token string")
        if prefix[-1] in self:
            return self.trees[prefix[-1]].match(prefix[:-1])
        return False

    def sample(self, prefix: List[int] = []) -> int:
        if (len(prefix) == 0) or (prefix[-1] not in self.trees):
            return self.sampler.sample()  # sample from raw token occurrence frequencies
        return self.trees[prefix[-1]].sample(prefix[:-1])

    def probability(self, prefix: List[int], successor: int) -> float:
        if (len(prefix) == 0) or (prefix[-1] not in self.trees):
            return self.sampler.probability(
                successor
            )  # raw occurrence probability of the successor
        return self.trees[prefix[-1]].probability(prefix[:-1], successor)

    def generate(self, size: int, window: int, prompt: List[int]) -> List[int]:
        code = prompt
        for i in range(size):
            prefix = code if len(code) < window else code[-window:]
            code.append(self.sample(prefix))
        return code


AccmType = Tuple[int, bytes]


class _SuffixTreeParser:  # (beam.DoFn):
    def __init__(
        self,
        language: CharLanguage,  # is beam so specific about this?
        block_size: int,
        documents: bool = False,
        doc_start_tok: int = 0,
        doc_end_tok: int = 1,
        text_encoded: bool = False,
        text_delimiter: str = ",",
        text_field: str = "segment",
    ):
        self.L = language
        self.B = block_size

        # TODO: annoying; setattr over generic kwargs? cleaner code
        # but much more opaque interface/API here
        self.documents = documents
        self.doc_start_tok = doc_start_tok
        self.doc_end_tok = doc_end_tok
        self.text_encoded = text_encoded
        self.text_delimiter = text_delimiter
        self.text_field = text_field

    def process(self, record):  # -> Generator[Tuple[int, bytes]]?

        # size: int; but what about dynamic parsing?
        T = SuffixTreeSet()

        # encode segment in language; TODO: generalize
        encoded: List[int] = []
        text = cast(str, record[self.text_field])
        if self.text_encoded:
            encoded = [int(i) for i in text.split(self.text_delimiter)]
        encoded = self.L.encode(text)

        # TODO: doc start + encoded + doc end...
        if self.documents:
            encoded = [self.doc_start_tok] + encoded + [self.doc_end_tok]

        # parse token string
        T.parse_all(encoded, self.B)

        # emit each tree
        for t, tree in T.trees.items():
            # TODO: tuple form sufficient for a "keyed" PCollection?
            yield (t, bytes(tree))  # bytes -> protobuf encoding


class _SuffixTreeMerge:  # (beam.CombineFn):
    # are we merging based on proto, or pyobjects?

    def create_accumulator(self) -> Optional[AccmType]:
        return None  # SuffixTree() but for what token?

    def add_input(self, accm: Optional[AccmType], inp: AccmType) -> AccmType:
        if accm is None:
            return inp
        tree = SuffixTree.merge_proto_bytes(accm[1], inp[1])
        return (tree.token, bytes(tree))

    # TODO: List/Iterable arg? or varargs?
    def merge_accumulators(self, accumulators: List[Optional[AccmType]]) -> Optional[AccmType]:
        tree = None
        for accm in accumulators:
            if accm:
                assert isinstance(accm, tuple), print(type(accm), accm)
                t, b = accm  # split into token/bytes
                if tree:
                    other = SuffixTree.from_proto_bytes(b)
                    tree.merge(other)  # won't merge if token mismatched
                else:
                    tree = SuffixTree.from_proto_bytes(b)
        if tree:
            return (tree.token, bytes(tree))
        return None

    def extract_output(self, accm: AccmType) -> AccmType:
        return accm


try:

    import apache_beam as beam

    class SuffixTreeParser(_SuffixTreeParser, beam.DoFn):  # MRO requires _SuffixTreeParser first
        pass

    class SuffixTreeMerge(
        _SuffixTreeMerge, beam.CombineFn
    ):  # MRO requires _SuffixTreeParser first
        pass

except ImportError as err:

    warn(
        f"Cannot import beam: SuffixTreeParser and SuffixTreeMerge will not be parallelized ({err})"
    )

    class Unimportable:
        def __init__(self, *args, **kwargs) -> None:
            raise NotImplementedError(
                f"Cannot initialize {self.__class__.__name__} without `beam` modules"
            )

    class SuffixTreeParser(_SuffixTreeParser):  # type:ignore
        pass

    class SuffixTreeMerge(_SuffixTreeMerge):  # type:ignore
        pass
