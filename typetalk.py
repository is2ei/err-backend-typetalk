from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Typetalk(BotPlugin):
    """
    Backend for Typetalk for Errbot
    """

    def activate(self):
        """
        Triggers on plugin activation

        """
        super(Typetalk, self).activate()

    def deactivate(self):
        """
        Triggers on plugin deactivation

        """
        super(Typetalk, self).deactivate()

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports

        """
        return {
            'EXAMPLE_KEY_1': "Example value",
            'EXAMPLE_KEY_2': ["Example", "Value"]
               }

    def check_configuration(self, configuration):
        """
        Triggers when the configuration is checked, shortly before activation

        Raise a errbot.ValidationException in case of an error

        """
        super(Typetalk, self).check_configuration(configuration)

    def callback_connect(self):
        """
        Triggers when bot is connected

        """
        pass

    def callback_message(self, message):
        """

        """
        pass

    def callback_botmessage(self, message):
        """

        """
        pass

    @webhook
    def example_webhook(self, incoming_request):
        """A webhook which simply returns 'Example'"""
        return "Example"

    # Passing split_args_with=None will cause arguments to be split on any kind
    # of whitespace, just like Python's split() does
    @botcmd(split_args_with=None)
    def example(self, message, args):
        """A command which simply returns 'Example'"""
        return "Example"

    @arg_botcmd('name', type=str)
    @arg_botcmd('--favorite-number', type=int, unpack_args=False)
    def hello(self, message, args):
        """
        A command which says hello to someone.

        If you include --favorite-number, it will also tell you their
        favorite number.
        """
        if args.favorite_number is None:
            return f'Hello {args.name}.'
        else:
            return f'Hello {args.name}, number is {args.favorite_number}.'
