# mariadb-shell-plugin-demo
This demo plugin shows how to extend the MariaDB Shell with extension objects.

It will register a new MariaDB Shell global object called "hello" with two functions, hello_world() and show_schemas(), and a version() function for the plugin manager. The global object has the name the plugin has in the [plugin repository manifest](https://github.com/mzinner/mariadb-shell-plugins), which is how the plugin manager tells that the plugin is installed.

After installing the demo into the plugins directory of the MariaDB Shell, the plugin can be accessed like this.

```
MariaDB Py> \? hello
NAME
      hello - A demo plugin that showcases the shell's plugin feature.

DESCRIPTION
      This global object is the Hello World example plugin of the MariaDB
      Shell. Please consult the MariaDB Shell manual to get more information
      about how to create your own plugins.

FUNCTIONS
      hello_world()
            Prints 'Hello world!'

      help([member])
            Provides help about this object and it's members

      show_schemas([session])
            Lists all database schemas.

      version()
            Returns the version of the plugin.

MariaDB Py> hello.hello_world()
Hello world!
```

The functions are commands of the command line as well.

```
$ mariadb-shell -- hello hello-world
Hello world!
$ mariadb-shell --uri user@localhost -- hello show-schemas
```

## Installation
The easiest way to install this demo is the plugin manager of the MariaDB Shell, using the [mariadb-shell-plugins](https://github.com/mzinner/mariadb-shell-plugins) repository.

```
MariaDB Py> plugins.repositories.add("github/mzinner")
MariaDB Py> plugins.install("hello")
```

To install it by hand, type the following commands after you have installed the MariaDB Shell and the git command line tools.

This will clone the repository and copy the files to the right path in order to be automatically loaded on MariaDB Shell startup.

### macOS / Linux
```
$ mkdir -p ~/.mariadb-shell/plugins
$ git clone https://github.com/mzinner/mariadb-shell-plugin-demo.git ~/.mariadb-shell/plugins/hello
```

### Windows
```
> mkdir %AppData%\MariaDB\mariadb-shell\plugins
> git clone https://github.com/mzinner/mariadb-shell-plugin-demo.git %AppData%\MariaDB\mariadb-shell\plugins\hello
```

## Extending the MariaDB Shell

Please take a look at the init.py file to learn how to extend the MariaDB Shell with plugins. It uses the `@plugin` and `@plugin_function` decorators of `mysqlsh.plugin_manager`, which register the global object and its functions, derive their help from the docstrings, and make the functions available in Python mode and on the command line.
