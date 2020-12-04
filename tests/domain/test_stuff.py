from groovy_thing_back.domain.stuff import Stuff, StuffBuilder
from groovy_thing_back.domain.use_cycle import UseCycle
from groovy_thing_back.domain.love_type import LoveType


def test_build_stuff_use():
    # execute
    builder = StuffBuilder()
    builder.doc_id('abc123')
    builder.name('test')
    builder.use_cycle(use_cycle=UseCycle.DAILY)
    actual = builder.build()

    # verify
    expect = {
        "doc_id": "abc123",
        "name": "test",
        "label": [],
        "use_cycle": UseCycle.DAILY,
        "love_type": LoveType.NOT_SELECTED
    }
    assert actual == Stuff(**expect)


def test_build_stuff_not_use():
    # execute
    builder = StuffBuilder()
    builder.doc_id('abc123')
    builder.name('test2')
    builder.use_cycle(
        use_cycle=UseCycle.NOT_USE,
        love_type=LoveType.MEMORY)
    actual = builder.build()

    # verify
    expect = {
        "doc_id": "abc123",
        "name": "test2",
        "label": [],
        "use_cycle": UseCycle.NOT_USE,
        "love_type": LoveType.MEMORY
    }
    assert actual == Stuff(**expect)


def test_convert_firestore_data_use_stuff():
    # setup
    DUMMY_DOC_ID = "dummy"
    data = {
        "doc_id": DUMMY_DOC_ID,
        "name": "test",
        "label": ["ラベル"],
        "use_cycle": UseCycle.DAILY,
        "love_type": LoveType.NOT_SELECTED
    }
    stuff = Stuff(**data)

    # execute
    actual = stuff.to_firestore_data()

    # verify
    expect = {
        "name": "test",
        "label": ["ラベル"],
        "use_cycle": UseCycle.DAILY.label(),
        "love_type": LoveType.NOT_SELECTED.label()
    }
    assert actual[0] == DUMMY_DOC_ID
    assert actual[1] == expect
