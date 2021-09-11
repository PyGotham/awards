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

[pip]: https://pip.pypa.io
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
