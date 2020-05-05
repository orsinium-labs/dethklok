import ast
from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence

from ._unparse import Unparser


def make_metal(path: Path) -> None:
    """Autoformat the given file in place.
    """
    content = path.read_text(encoding='utf8')
    tree = compile(content, str(path), 'exec', ast.PyCF_ONLY_AST)
    with path.open(mode='w', encoding='utf8') as stream:
        Unparser(tree=tree, file=stream)


def sound_check(path: Path) -> bool:
    """Test if file formatting is stable.

    Returns True if second time formatting of file doesn't change anything.
    """
    make_metal(path=path)
    old_content = path.read_text(encoding='utf8')
    make_metal(path=path)
    new_content = path.read_text(encoding='utf8')
    return old_content == new_content


def main(argv: Sequence[str]) -> int:
    parser = ArgumentParser()
    parser.add_argument('command', choices=['format', 'test'])
    parser.add_argument('paths', nargs='+')
    args = parser.parse_args(args=argv)

    if args.command == 'format':
        for path in args.paths:
            make_metal(path=Path(path))
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
