#!/usr/bin/env python3
import sys
import unittest

import pytest
from bytecode import (
    Bytecode,
    CompilerFlags,
    ConcreteBytecode,
    ConcreteInstr,
    ControlFlowGraph,
)
from bytecode.flags import infer_flags


class FlagsTests(unittest.TestCase):
    def test_type_validation_on_inference(self):
        with self.assertRaises(ValueError):
            infer_flags(1)

    def test_flag_inference(self):

        # Check no loss of non-infered flags
        code = ControlFlowGraph()
        code.flags |= (
            CompilerFlags.NEWLOCALS
            | CompilerFlags.VARARGS
            | CompilerFlags.VARKEYWORDS
            | CompilerFlags.NESTED
            | CompilerFlags.FUTURE_GENERATOR_STOP
        )
        code.update_flags()
        for f in (
            CompilerFlags.NEWLOCALS,
            CompilerFlags.VARARGS,
            CompilerFlags.VARKEYWORDS,
            CompilerFlags.NESTED,
            CompilerFlags.NOFREE,
            CompilerFlags.OPTIMIZED,
            CompilerFlags.FUTURE_GENERATOR_STOP,
        ):
            self.assertTrue(bool(code.flags & f))

        # Infer optimized and nofree
        code = Bytecode()
        flags = infer_flags(code)
        self.assertTrue(bool(flags & CompilerFlags.OPTIMIZED))
        self.assertTrue(bool(flags & CompilerFlags.NOFREE))
        code.append(ConcreteInstr("STORE_NAME", 1))
        flags = infer_flags(code)
        self.assertFalse(bool(flags & CompilerFlags.OPTIMIZED))
        self.assertTrue(bool(flags & CompilerFlags.NOFREE))
        code.append(ConcreteInstr("STORE_DEREF", 2))
        code.update_flags()
        self.assertFalse(bool(code.flags & CompilerFlags.OPTIMIZED))
        self.assertFalse(bool(code.flags & CompilerFlags.NOFREE))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
