from setuptools import setup

__author__ = "jnwhiteh@gmail.com"

setup(
        name="Communicating Sequential Processes (CSP-M) Lexer",
        version="0.0.1",
        description=__doc__,
        author=__author__,
        packages=["csp_lexer"],
        entry_points='''[pygments.lexers]
csplexer = csp_lexer:CSPLexer
'''
)
