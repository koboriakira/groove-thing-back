from groovy_thing_back.domain.group import Group


def test_firestore_data():
    # setup
    group = Group(id="music", name="音楽")

    # execute
    actual = group.to_firestore_data()

    # verify
    expect = {
        "name": "音楽",
        "enable_count": False
    }
    assert actual[0] == "music"
    assert actual[1] == expect
