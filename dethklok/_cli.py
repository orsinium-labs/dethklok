import ast
from argparse import ArgumentParser
from pathlib import Path
from io import StringIO
from typing import Sequence

import astunparse
import autopep8


ENCODING = 'utf8'


def make_metal(*, path: Path, content: str = None) -> str:
    """Autoformat the given file in place.
    """
    if content is None:
        content = path.read_text(encoding=ENCODING)
    tree = compile(content, str(path), 'exec', ast.PyCF_ONLY_AST)

    with StringIO() as buffer:
        astunparse.Unparser(tree=tree, file=buffer)
        buffer.seek(0)
        content = buffer.read()

    content = autopep8.fix_code(source=content)
    return content


def sound_check(path: Path) -> bool:
    """Test if file formatting is stable.

    Returns True if second time formatting of file doesn't change anything.
    """
    content1 = path.read_text(encoding=ENCODING)
    content2 = make_metal(path=path, content=content1)
    content3 = make_metal(path=path, content=content2)
    return content2 == content3


def main(argv: Sequence[str]) -> int:
    parser = ArgumentParser()
    parser.add_argument('command', choices=['format', 'test'])
    parser.add_argument('paths', nargs='+')
    args = parser.parse_args(args=argv)

    if args.command == 'format':
        for path in args.paths:
            path = Path(path)
            content = make_metal(path=path)
            path.write_text(content, encoding=ENCODING)
        return 0

    if args.command == 'test':
        not_ok = 0
        for path in args.paths:
            ok = sound_check(path=Path(path))
            if not ok:
                print('Formatting for file is unstable:', path)
                not_ok += 1
        return not_ok

    raise RuntimeError('unreachable')
