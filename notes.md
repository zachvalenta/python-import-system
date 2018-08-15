# importing modules and project structure in Python

tldr: bootstrapped Python project stucture

a bit more: Python's import system is slightly mad and spread across a bevy of PEPs. Get ready to do some digging on Stack Overflow and reading articles with titles like ['Traps for the Unwary in Python's Import System'](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html). Here's what worked (and didn't) for me.

## what worked

* project structure
```sh
├── source
│   └── sut.py
└── tests
    ├── __init__.py
    └── test_sut.py
```

* command: `py3 -m unittest discover`
* run from: project root
* import statement in tests: `from source import sut`
* works in PyCharm:  ✅
* work from terminal: ✅

__reference__

* need to have `__init__.py` in `tests` for `unittest` CLI to pick it up via `py3 -m unittest discover`; if that doesn't matter to you, can remove it and run the tests by running `tests.test_sut`
* [answer that got me here](https://stackoverflow.com/a/24266885/6813490)

## what didn't work

📝 two different import statements = flakiness btw PyCharm and terminal

* project structure
```sh
.
├── __init__.py
├── source
│   ├── __init__.py
│   └── sut.py
└── tests
    └── test_sut.py
```

* command: `py3 -m unittest test_sut.py`
* run from: `test_structure/tests`
* import statement: `import sut`
* PyCharm:  ❌
* terminal: ❌ ("ModuleNotFoundError: No module named 'sut'")

---

* command: `py3 -m unittest test_sut.py`
* run from: `test_structure/tests`
* import statement: `from ..source import sut`
* PyCharm:  ✅
* terminal: ❌ ("ImportError: attempted relative import with no known parent package")
