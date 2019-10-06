from nltk.tokenize import word_tokenize

import re
import stringcase

def identity(x):
    return x

_transform_op = re.compile('%([a-z]+)(\\d+)')
_hash_op = re.compile('%(#)(\\d+)')

_op_dict = {
  'id': identity,
  'pc': stringcase.pascalcase,
  'cc': stringcase.camelcase,
  'sc': stringcase.snakecase,
  'cn': stringcase.constcase,
  'uc': stringcase.uppercase,
  'lc': stringcase.lowercase
}

def transop(command, s):
  return _op_dict[command](s)

def replace(tokens, pattern, dict={}):
  r = pattern
  r = _transform_op.sub(lambda m: transop(m.group(1), tokens[int(m.group(2)) - 1]), r)
  r = _hash_op.sub(lambda m: dict[tokens[int(m.group(2)) - 1]], r)
  return r
 
def transform(blocks, pattern):
  stripped_blocks = list(filter(None, map(str.strip, blocks)))
  token_blocks = [word_tokenize(b) for b in stripped_blocks]

  transformed_blocks = []
  for tokens in token_blocks:
      transformed_blocks.append(replace(tokens, pattern))

  return transformed_blocks