"""Imports data fixtures."""

from typing import Tuple

from ..internals.builtins import Type18nDoc
from ..shared.shared_definitions import lang_base, lang_foreign_only
from ..schemas.src_tag import TagEventCategory, SourceTag
# from shared.dep_search.shared_types import Type18nDoc
# from shared.dep_search.shared_definitions import lang_base, lang_foreign_only
# from shared.dep_search.schemas.sources.tag import TagEventCategory, SourceTag


def example_event_category_music() -> TagEventCategory:
    """Example event category music."""

    slug = 'music'
    return TagEventCategory(
        id=1,
        name='Музыка',
        slug=slug,
        breadcrumbs=[{'slug': slug, 'title': 'Музычка для вас'}],
    )


def example_event_category_sport() -> TagEventCategory:
    """Example event category sport."""

    slug = 'sport'
    return TagEventCategory(
        id=2,
        name='Спорт',
        breadcrumbs=[{'slug': slug, 'title': 'Лучшие спортивные места'}],
    )


def example_event_category_shows() -> TagEventCategory:
    """Example event category shows."""
    slug = 'show'
    return TagEventCategory(
        id=1,
        name='Шоу',
        breadcrumbs=[{'slug': slug, 'title': 'Забористые шоу'}],
    )


def example_i18n_tag(
    pk: int,
    name: str,
    slug: str,
    event_category: TagEventCategory,
) -> Type18nDoc:
    """I18n tag."""

    i18n_doc = {
        lang_base: SourceTag(
            id=pk,
            name=name,
            slug=slug,
            event_category=event_category.dict(),
        )
    }

    for foreign in lang_foreign_only:
        i18n_doc.update({
            foreign: SourceTag(
                id=pk,
                name=f'{name} - {foreign}',
                slug=slug,
                event_category=event_category.dict(),
            )
        })

    return i18n_doc


def tag_sport() -> Tuple[int, Type18nDoc]:
    """Tag sport."""

    pk = 1
    return pk, example_i18n_tag(
        pk=pk,
        name='Спорт',
        slug='sport',
        event_category=example_event_category_sport(),
    )


def tag_theatre() -> Tuple[int, Type18nDoc]:
    """Tag theatre."""

    pk = 2
    return pk, example_i18n_tag(
        pk=pk,
        name='Театр',
        slug='theatre',
        event_category=example_event_category_shows(),
    )


def tag_concert() -> Tuple[int, Type18nDoc]:
    """Tag concert."""

    pk = 3
    return pk, example_i18n_tag(
        pk=pk,
        name='Концерты',
        slug='concert',
        event_category=example_event_category_music(),
    )


def tag_kids() -> Tuple[int, Type18nDoc]:
    """Tag kids."""

    pk = 4
    return pk, example_i18n_tag(
        pk=pk,
        name='Детям',
        slug='kids',
        event_category=example_event_category_shows(),
    )


def tag_classic() -> Tuple[int, Type18nDoc]:
    """Tag classic."""

    pk = 5
    return pk, example_i18n_tag(
        pk=pk,
        name='Классика',
        slug='classic',
        event_category=example_event_category_music(),
    )


def tag_vocal() -> Tuple[int, Type18nDoc]:
    """Tag vocal."""

    pk = 6
    return pk, example_i18n_tag(
        pk=pk,
        name='Вокал',
        slug='vocal',
        event_category=example_event_category_music(),
    )


def tag_ballet() -> Tuple[int, Type18nDoc]:
    """Tag ballet."""

    pk = 7
    return pk, example_i18n_tag(
        pk=pk,
        name='Балет',
        slug='ballet',
        event_category=example_event_category_shows(),
    )


def tag_opera() -> Tuple[int, Type18nDoc]:
    """Tag opera."""

    pk = 8
    return pk, example_i18n_tag(
        pk=pk,
        name='Опера',
        slug='opera',
        event_category=example_event_category_music(),
    )


def tag_cirque() -> Tuple[int, Type18nDoc]:
    """Tag cirque."""

    pk = 9
    return pk, example_i18n_tag(
        pk=pk,
        name='Цирк',
        slug='cirque',
        event_category=example_event_category_shows(),
    )


def tag_rock() -> Tuple[int, Type18nDoc]:
    """Tag rock."""

    pk = 10
    return pk, example_i18n_tag(
        pk=pk,
        name='Рок',
        slug='rock',
        event_category=example_event_category_music(),
    )


all_tags = [
    tag_sport(),
    tag_theatre(),
    tag_concert(),
    tag_kids(),
    tag_classic(),
    tag_vocal(),
    tag_ballet(),
    tag_opera(),
    tag_cirque(),
    tag_rock(),
]


def doc_tags():
    """Doc tags."""

    return {tag[0]: tag[1] for tag in all_tags}
