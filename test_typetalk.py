pytest_plugins = ["errbot.backends.test"]

extra_plugin_dir = '.'

def test_command(testbot):
    testbot.push_message('!mycommand')
    assert 'This is my awesome command' in testbot.pop_message()
