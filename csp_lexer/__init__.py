from pygments.lexer import RegexLexer, bygroups, using, this
from pygments.token import *

class CSPLexer(RegexLexer):
    name = "CSP"
    aliases = ["csp"]
    filenames = ["*.csp"]

    tokens = {
            "root": [
                # comments
                (r'{-', Comment.Multiline, 'comment'),
                ('--.*$', Comment.Single),

                # whitespace
                (r'\n', Text),

                (r'\[(FD|T|F)=', Keyword),
                (r'\\|->|\[\]|\|~\||\|\|\||\[\||\|]|\[\[|\]\]|\|\|', Operator),
                (r'{\||\|}|{|}|\.\.|:|#|<-|<->|==|<|>|<=|>=|@|&|=|[+-/*%^]', Operator),
                (r'\b(assert|datatype|let|within|newtype|channel|external|transparent)\b', Keyword),
                (r'\b(if|then|else)\b', Keyword),
                (r'\b([0-9]+)\b', Number.Integer),
                (r'\b(true|false|True|False)\b', Keyword.Constant),
                (r'\b(length|length|null|head|tail|concat|elem|union|inter|diff|Union|Inter|member|card|empty|set|Set|Seq|seq|Int|Bool|Proc|Events|true|false|True|False|STOP|SKIP|CHAOS|prioritise|productions|extensions|diamond|normal|sbisim|tau_loop_factor|model_compress|explicate|wbisim|chase)\b', Name.Builtin),
                (r'\(|\)|,|\[|\]', Punctuation),
                (r'^(\s*)([a-zA-Z0-9_\']+)(\s*)(\(.*?\)|)(\s*=)', bygroups(Text, Name.Function, Text, using(this), Text)),
                (r'[A-Za-z_][A-Za-z0-9_\']*', Name),
                (r'[^\S\n]', Text),
                ],
            "comment": [
                # Multiline Comments
                (r'[^-{}]+', Comment.Multiline),
                (r'{-', Comment.Multiline, '#push'),
                (r'-}', Comment.Multiline, '#pop'),
                (r'[-{}]', Comment.Multiline),
                ],
            }

