import typetalk

extra_plugin_dir = '.'


def test_command(testbot):
    testbot.push_message('!example')
    assert 'Example' in testbot.pop_message()
