# init.py
# -------
# Automatic loading of plugins at MariaDB Shell startup
# .....................................................
# The init.py file will be automatically loaded by the MariaDB Shell during
# startup when placed in a sub-directory of ~/.mariadb-shell/plugins/ on macOS
# and Linux or %AppData%\MariaDB\mariadb-shell\plugins\ on Windows.
# Example:
#   ~/.mariadb-shell/plugins/my_plugin/init.py
#
# When working on a collaborative project and a larger number of plugins will
# be hosted in the same repository, it is good practice to have a separate
# folder for each plugin and a separate init.py file in each folder. The
# MariaDB Shell will then automatically load all plugins at startup.
# Example:
#   ~/.mariadb-shell/plugins/my_plugins/schema/init.py
#   ~/.mariadb-shell/plugins/my_plugins/performance/init.py
#
# Registering new plugins
# .......................
# A plugin is registered with the two decorators of mysqlsh.plugin_manager:
#
# - @plugin on a class registers a global object of the class's name. The
#   docstring of the class is its help: the first paragraph the brief, the
#   rest the details. Inner classes become nested objects.
# - @plugin_function("object.functionName") on a function adds it to that
#   object. The docstring is the function's help, and is checked at load time:
#   every parameter needs an entry in its Args: section, with its type.
#
# The decorators derive everything else: the name is given in camelCase, as
# JavaScript and the command line see it, and the shell exposes it in
# snake_case in Python mode (hello.helloWorld -> hello.hello_world()). With
# cli=True, the function is also a command of the command line:
#   mariadb-shell -- hello hello-world
#
# The name of the global object is the name of the plugin: the plugin manager
# (plugins.list(), plugins.install(), plugins.update()) looks for a global
# object of the name given in the repository's manifest file to tell whether
# the plugin is installed, and calls its version() function to tell whether an
# update is available.

from mysqlsh.plugin_manager import plugin, plugin_function
from mysqlsh import globals, Error

# The version of the plugin, as the repository manifest lists it
VERSION = "0.0.2"


# The global object 'hello'
# -------------------------

@plugin
class hello:
    """A demo plugin that showcases the shell's plugin feature.

    This global object is the Hello World example plugin of the MariaDB
    Shell. Please consult the MariaDB Shell manual to get more information
    about how to create your own plugins.
    """


# The functions of 'hello'
# ------------------------

@plugin_function("hello.helloWorld", cli=True)
def hello_world():
    """Prints 'Hello world!'

    Returns:
        Nothing
    """
    print("Hello world!")


@plugin_function("hello.showSchemas", cli=True)
def show_schemas(session=None):
    """Lists all database schemas.

    Sample function that works either with a session passed as parameter or
    with the global session of the MariaDB Shell. A parameter with a default
    value is optional.

    Args:
        session (object): The session to be used on the operation. If omitted
            the MariaDB Shell's current session will be used.

    Returns:
        Nothing
    """
    if session is None:
        session = globals.shell.get_session()
        if session is None:
            # An Error reaches the user as a shell error, without a traceback
            raise Error("No session specified. Either pass a session object "
                        "to this function or connect the shell to a database.")
    globals.shell.dump_rows(session.run_sql("show schemas"))


@plugin_function("hello.version", cli=True)
def version():
    """Returns the version of the plugin.

    The plugin manager compares it with the version the repository manifest
    lists, to tell whether an update is available.

    Returns:
        The version as a string
    """
    return VERSION
