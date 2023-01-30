from typing import List, Union, Dict, Tuple, Iterator, Set, Optional, cast
from os import linesep
from spacy.tokens import Token
from srsly import msgpack_decoders, msgpack_encoders  # type:ignore[import]


class ChainHolder:
    """The object returned by *token._.coref_chains*."""

    def __init__(self):
        self.chains = []

        # 'temp*' properties will be removed before processing ends
        self.temp_governing_sibling = None
        self.temp_has_or_coordination = False

    def __str__(self) -> str:
        return str(self.chains)

    def __repr__(self) -> str:
        return str(self)

    def print(self) -> None:
        print(linesep.join(chain.pretty_representation for chain in self.chains))

    def __iter__(self) -> Iterator["Chain"]:
        return iter(self.chains.copy())

    def __len__(self) -> int:
        return len(self.chains)

    def __getitem__(self, key: str) -> "Chain":
        return self.chains[key]

    @property
    def pretty_representation(self) -> str:
        return "; ".join(chain.pretty_representation for chain in self.chains)

    @staticmethod
    def resolve(token: Token) -> Optional[List[Token]]:
        """If *token* is an anaphor, returns a list of tokens to which *token* points;
        otherwise returns *None*.
        """

        def resolve_recursively(token: Token) -> Set[Token]:
            tokens_to_return = set()
            for chain in token._.coref_chains.chains:
                for mention in (
                    mention
                    for mention in chain.mentions
                    if len(mention.token_indexes) > 1
                    and token.i not in mention.token_indexes
                ):
                    # Mention contains multiple tokens, some of which may be anaphors and
                    # belong to further chains.
                    for contained_token in (
                        token.doc[index]
                        for index in mention.token_indexes
                        if index != token.i
                    ):
                        tokens_to_return.update(resolve_recursively(contained_token))
                    return tokens_to_return
            for chain in token._.coref_chains.chains:
                if (
                    len(
                        [
                            mention
                            for mention in chain.mentions
                            if len(mention.token_indexes) > 1
                            and token.i in mention.token_indexes
                        ]
                    )
                    > 0
                ):
                    # This token is pointing back to a multiple-token mention which should
                    # already have been dealt with further up the recursion stack
                    continue
                return {
                    token.doc[
                        chain.mentions[chain.most_specific_mention_index].root_index
                    ]
                }
            return {token}

        resolved_set = resolve_recursively(token)
        if len(resolved_set) == 1 and token in resolved_set:
            return None
        return sorted(list(resolved_set))  # type:ignore[type-var]

    @msgpack_encoders("coreferee_chain_holder")
    def serialize_obj(obj, chain=None):
        if isinstance(obj, ChainHolder):
            serialized_chain_holder = []
            for working_chain in obj.chains:
                serialized_chain_holder.append(
                    (
                        [
                            (mention.token_indexes, mention.pretty_representation)
                            for mention in working_chain.mentions
                        ],
                        working_chain.most_specific_mention_index,
                    )
                )
            return {"__coreferee_chain_holder__": serialized_chain_holder}
        return obj if chain is None else chain(obj)

    @msgpack_decoders("coreferee_chain_holder")
    def deserialize_obj(obj, chain=None):
        if "__coreferee_chain_holder__" in obj:
            chain_holder = ChainHolder()
            chain_holder.chains = []
            for index, (chain_representation, most_specific_mention_index) in enumerate(
                obj["__coreferee_chain_holder__"]
            ):
                mentions = []
                for (token_indexes, pretty_representation) in chain_representation:
                    mention = Mention()
                    mention.token_indexes = token_indexes
                    mention.pretty_representation = pretty_representation
                    mention.root_index = token_indexes[0]
                    mentions.append(mention)
                working_chain = Chain(mentions, most_specific_mention_index)
                working_chain.index = index
                chain_holder.chains.append(working_chain)
            return chain_holder
        return obj if chain is None else chain(obj)


class Chain:
    def __init__(self, mentions: List["Mention"], most_specific_mention_index: int):
        self.mentions = mentions
        self.most_specific_mention_index = most_specific_mention_index
        self.index: Optional[int] = None

    def __str__(self) -> str:
        return ": ".join(
            (str(self.index), ", ".join(str(mention) for mention in self.mentions))
        )

    def __repr__(self) -> str:
        return str(self)

    def __iter__(self) -> Iterator["Mention"]:
        return iter(self.mentions.copy())

    def __len__(self) -> int:
        return len(self.mentions)

    def __getitem__(self, i: int) -> "Mention":
        return self.mentions[i]

    @property
    def pretty_representation(self) -> str:
        return ": ".join(
            (
                str(self.index),
                ", ".join(mention.pretty_representation for mention in self.mentions),
            )
        )


class Mention:
    def __init__(self, root: Token = None, include_dependent_siblings: bool = False):
        if root is not None:  # root==None during deserialization, never otherwise
            doc = root.doc
            self.root_index = root.i
            self.token_indexes = [root.i]
            if include_dependent_siblings:
                self.token_indexes.extend(
                    [t.i for t in root._.coref_chains.temp_dependent_siblings]
                )
            if len(self.token_indexes) > 1:
                self.pretty_representation = "".join(
                    (
                        "[",
                        "; ".join(
                            "".join((doc[token_index].text, "(", str(token_index), ")"))
                            for token_index in self.token_indexes
                        ),
                        "]",
                    )
                )
            else:
                self.pretty_representation = "".join(
                    (doc[self.root_index].text, "(", str(self.root_index), ")")
                )

    def __eq__(self, other):
        return isinstance(other, Mention) and self.token_indexes == other.token_indexes

    def __hash__(self) -> int:
        return hash(tuple(self.token_indexes))

    def __str__(self) -> str:
        return str(self.token_indexes)

    def __repr__(self) -> str:
        return str(self.token_indexes)

    def __len__(self) -> int:
        return len(self.token_indexes)

    def __getitem__(self, key) -> int:
        return self.token_indexes[key]

    @staticmethod
    def number_of_training_mentions_marked_true(token: Token) -> int:
        if not hasattr(token._.coref_chains, "temp_potential_referreds"):
            return 0
        return len(
            [
                1
                for mention in token._.coref_chains.temp_potential_referreds
                if hasattr(mention, "true_in_training")
            ]
        )


class FeatureTable:
    """Captures the possible values of the various Spacy annotations that are observed
    to occur during a training corpus. These are then used as the basis for a oneshot
    representation of individual tokens.
    """

    def __init__(
        self,
        *,
        tags: List[str],
        morphs: List[str],
        ent_types: List[str],
        lefthand_deps_to_children: List[str],
        righthand_deps_to_children: List[str],
        lefthand_deps_to_parents: List[str],
        righthand_deps_to_parents: List[str],
        parent_tags: List[str],
        parent_morphs: List[str],
        parent_lefthand_deps_to_children: List[str],
        parent_righthand_deps_to_children: List[str]
    ):

        # In the notes that follow, 'referred token' means the token at the head of a
        # referred-to mention.

        # Tags a referring or referred token can have
        self.tags = tags

        # Morphological features a referring or referred token can have
        self.morphs = morphs

        # Entity types a referring or referred token can have
        self.ent_types = ent_types

        # Dependencies where a referring or referred token is the head and where the child
        # is to its left
        self.lefthand_deps_to_children = lefthand_deps_to_children

        # Dependencies where a referring or referred token is the head and where the child
        # is to its right
        self.righthand_deps_to_children = righthand_deps_to_children

        # Dependencies where a referring or referred token is the child and where it is to the
        # left of the parent
        self.lefthand_deps_to_parents = lefthand_deps_to_parents

        # Dependencies where a referring or referred token is the child and where it is to the
        # right of the parent
        self.righthand_deps_to_parents = righthand_deps_to_parents

        # Tags the parent of a referring or referred token can have
        self.parent_tags = parent_tags

        # Morphological features the parent of a referring or referred token can have
        self.parent_morphs = parent_morphs

        # Dependencies where the parent of a referring or referred token is the head and where the
        # child is to its left
        self.parent_lefthand_deps_to_children = parent_lefthand_deps_to_children

        # Dependencies where the parent of a referring or referred token is the head and where the
        # child is to its right
        self.parent_righthand_deps_to_children = parent_righthand_deps_to_children

    def __len__(self) -> int:
        return sum(len(getattr(self, property)) for property in self.__dict__)
