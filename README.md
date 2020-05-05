# Dethklok

> We are here to make coffee metal. We will make everything metal. Blacker than the blackest black times infinity.
> - Nathan Explosion, Dethklok

The most uncompromising Python code formatter ever!

Dethklok uses a few code formatters under the hood:

+ [astunparse](https://github.com/simonpercivall/astunparse) -- extracted and improved [unparse.py](https://github.com/python/cpython/blob/3.7/Tools/parser/unparse.py) from the CPython source code. This script gets AST and formats it into the code, without knowing anything about how the code looked like before. From Python 3.9, it is a part of the standard library: [ast.unparse](https://docs.python.org/3.9/library/ast.html#ast.unparse).
+ [autopep8](https://github.com/hhatto/autopep8) -- a powerful and mature code formatter. We run it to make the produced code a bit less ugly.

## Installation

Supported Python versions are limited by what `astunparse` supports. For now, it's Python <=3.7.

```bash
python3 -m pip install --user dethklok
```

## Usage

```bash
python3 -m dethklok format **/*.py
```

## FAQ

**Q:** Is it [flake8](https://flake8.pycqa.org/en/latest/) compatible?

Almost. The tool outputs some statements in a single-line. The most noticeable example is docstrings. None of autoformatters I tried can make it multiline again.

**Q:** When should I use it?

The short answer is "NEVER". This is an experimental project that shows that producing the same AST without taking into account the initial formatting can't make the code readable. [I am a mediaocre developer](https://dev.to/sobolevn/i-am-a-mediocre-developer--30hn) but still formatting of my code has an intention and makes the code more readable: I group elements, I left comments, I align columns, I parenthesize parts of complex arithmetic operations. While some parts of the code can be easily autoformatted without breaking it, some parts shouldn't.

**Q:** Is it a joke about [black](https://github.com/psf/black) or what?

Well, a bit. Black targets to reformat everything, to have an opinion about part of every Python code. I admire that goal and really hope the project will grow and become mature some day. However, right now it's [unstable](https://github.com/psf/black#note-this-is-a-beta-product) and tries to fix things it can't fix (yet).

There are some formatters with similar philosophy in other languages (`go format`, `cargo format`, `elixir format`), and there are amazing. The difference is that these languages were designed with the formatter in mind, and every new feature is thoughtfully integrated with the formatter to make the result nice and idiomatic. Python is different.

**Q:** What should I use instead.

Luckily, there are plenty of cool formatters. They are doing only a small task but handle it really well. A few notable examples:

+ [autopep8](https://github.com/hhatto/autopep8) fixes only parts of the code that flake8 complaints about.
+ [isort](https://github.com/timothycrosley/isort) groups and sorts imports.
+ [add-trailing-comma](https://github.com/asottile/add-trailing-comma) adds trailing commas and formats long function call statements.
+ [unify](https://github.com/myint/unify) changes single quotes by double or vice versa, depends on what you prefer.

See the full list in [awesome-python-code-formatters](https://github.com/life4/awesome-python-code-formatters).
