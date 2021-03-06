import sys
import unittest

import pytest
from bytecode import Bytecode, ConcreteBytecode, ControlFlowGraph

from tests import get_code


class CodeTests(unittest.TestCase):
    """Check that bytecode.from_code(code).to_code() returns code."""

    def check(self, source, function=False):
        ref_code = get_code(source, function=function)

        code = ConcreteBytecode.from_code(ref_code).to_code()
        self.assertEqual(code, ref_code)

        code = Bytecode.from_code(ref_code).to_code()
        self.assertEqual(code, ref_code)

        bytecode = Bytecode.from_code(ref_code)
        blocks = ControlFlowGraph.from_bytecode(bytecode)
        code = blocks.to_bytecode().to_code()
        self.assertEqual(code, ref_code)

    def test_loop(self):
        self.check(
            """
            for x in range(1, 10):
                x += 1
                if x == 3:
                    continue
                x -= 1
                if x > 7:
                    break
                x = 0
            print(x)
        """
        )

    def test_varargs(self):
        self.check(
            """
            def func(a, b, *varargs):
                pass
        """,
            function=True,
        )

    def test_kwargs(self):
        self.check(
            """
            def func(a, b, **kwargs):
                pass
        """,
            function=True,
        )


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
