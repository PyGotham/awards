# Awards

An application to manage financial aid and scholarship applications and awards.

## Installation

[Poetry] is required to use this tool. It is available through most package
managers. For example, to install it with [pip], use

```
$ pip install poetry
```

After [Poetry] has been installed, the script's requirements can be installed by
running

```
$ poetry install
```

## Development

### Management commands

Several [Django] management commands are available through [tox] environments.
Invoking the commands this way will ensure that all of the project's
requirements are installed.

`createsuperuser`: Create a new user with access to the admin. While it will
prompt for a password, the value will be discarded; password-based logins are
not supported.

`dbshell`: Run `sqlite` for the configured database.

`makemigrations`: Generate new migrations for installed applications.

`migrate`: Apply all outstanding migrations by default. The name of an
application and either a forward or backward migration can be specified as well.

`runserver`: Run the development server with watchman_ watching for changes. If
the `PYTHONBREAKPOINT` environment variable is set, it will be passed through to
the environment. The following debuggers are supported:

- bpdb
- ipdb
- pdb
- pudb

`shell`: Run a [Django]-aware interactive interpreter. [bpython] or [ipython]
can be specified to select an interface other than the default Python REPL.

`startapp`: Create a new [Django] application with the specified name.

### Code style

This code base uses [pre-commit] to apply stylistic restraints. If you have it
installed globally, [pre-commit] will automatically run whenever you create a
new commit. It will also be available if you commit from inside a [Poetry]
shell.

```
$ poetry shell
$ git commit
```

Many of the linters and fixers used by [pre-commit] are also available from
inside a [Poetry] shell.

There are no style restrictions on the code beyond what [pre-commit] checks for.

### Testing

Testing is controlled via [tox]. If you wish to use it, it is installed as a
development dependency by [Poetry] and can be invoked with

```
$ poetry run tox
```

To have [tox] only perform static type checking of the code run

```
$ poetry run tox -e types
```

To run just the unit tests, use

```
$ poetry run tox -e unit
```

### CI

While the local use of both [pre-commit] and [tox] are encouraged, it is not
required. Both style checks and tests will be run as part of CI on [GitHub
Actions][actions].

If the [pre-commit] job would result in any changes, [pre-commit ci] will update
the pull request with the changes. It will also take care of keeping the
[pre-commit] hooks updated.

[actions]: https://docs.github.com/en/actions
[bpython]: https://bpython-interpreter.org
[django]: https://www.djangoproject.com
[ipython]: https://ipython.readthedocs.io
[pip]: https://pip.pypa.io
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
[pre-commit ci]: https://pre-commit.ci
[tox]: https://tox.readthedocs.io
