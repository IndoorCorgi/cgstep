#!/usr/bin/env python3
"""
tmc5240.pyソースを解析してcli.pyパラメーターソース, パラメーター一覧を出力
"""

import pathlib
import re


def main():
  src_path = pathlib.Path(__file__).parents[1] / 'cgstep/tmc5240.py'
  with open(src_path, 'r') as src_file:
    lines = src_file.readlines()

  code_path = pathlib.Path(__file__).parent / 'autogen_param_code.py'
  parameters = []
  conv_param = False

  with open(code_path, 'w') as code_file:
    code_file.write(param_header())
    block_level = 0
    parameter = ''
    comments = ''
    first = True
    for i in range(len(lines)):
      if block_level == 0:  # パラメーター処理ブロック外
        if re.search(r'\# Global Configuration Registers', lines[i]):
          code_file.write(lines[i - 1])
          code_file.write(lines[i])
          block_level = 1

      elif block_level == 1:  # パラメーター処理ブロック内
        if re.search(r'\@property', lines[i]):
          if parameter != '':
            print(parameter)
            code_file.write(param_code(parameter, read_only, first, conv_param))
            code_file.write(comments)
            first = False
          parameter = ''
          comments = ''
          read_only = True
          block_level = 2
        elif re.search(parameter + '.setter', lines[i]) and parameter != '':
          read_only = False
        elif re.search(r'\# Converted parameters', lines[i]):  # これ以降換算パラメーター
          # 最後のパラメーターを書き込んでクリア
          code_file.write(param_code(parameter, read_only, first, conv_param))
          parameter = ''
          comments = ''
          read_only = True

          # コメントを書き込んでconv_paramをセットする
          code_file.write('\n')
          code_file.write(lines[i - 1])
          code_file.write(lines[i])
          conv_param = True
        elif re.search(r'\# RPZ-Stepper Functions', lines[i]):  # コメント行処理より先に行う
          print(parameter)
          code_file.write(param_code(parameter, read_only, first, conv_param))
          break
        elif re.search(r'^\s*\#', lines[i]):
          comments += lines[i]

      elif block_level == 2:  # @propertyの次の行
        if re.search(r'def ', lines[i]):
          parameter = lines[i].rstrip()
          parameter = re.sub(r'.*def +', '', parameter)
          parameter = re.sub(r'\(.*$', '', parameter)
          parameters.append(parameter)
          block_level = 1
        else:
          raise ValueError('Unexpected code after @property line')
    footer = '  else:\n'
    footer += '    return False\n'
    footer += '  return True\n'
    code_file.write(footer)
    code_file.write(supported_param(parameters))


def param_header():
  """
  パラメーター処理関数の先頭部分のコードを返す
  """
  code = 'def param(motor, args):\n'
  code += '  """'
  code += """
  パラメーター設定を行うコマンドなら処理
  Args:
    motor: TMC5240クラス
    args: argparseでパースされた引数
  
  Returns: 処理したらTrue, 無関係なコマンドならFalse
"""
  code += '  """\n'
  return code


def param_code(parameter, read_only, first=False, conv_param=False):
  """
  パラメーターparameter処理コードを返す
  
  Args:
    parameter: パラメーター名
    read_only: 読み出し専用かどうか
    first: if文の一番最初のパラメーターかどうか
    conv_param: 小数を扱うパラメーターかどうか
  """
  if first:
    code = "  if args.command=='" + parameter + "':\n"
  else:
    code = "  elif args.command=='" + parameter + "':\n"
  if conv_param:
    code += '    motor.steps_per_rev = args.steps_per_rev\n'
  code += '    if args.write is None:\n'
  if conv_param:
    code += '      print(motor.' + parameter + ')\n'
  else:
    code += '      print_val(motor.' + parameter + ', args)\n'
  code += '    else:\n'
  if read_only:
    code += "      raise ValueError('{} is not writable parameter'.format(args.command))\n\n"
  else:
    if conv_param:
      code += '      motor.' + parameter + ' = float(args.write)\n\n'
    else:
      code += '      motor.' + parameter + ' = int(args.write, 0)\n\n'
  return code


def supported_param(parameters):
  """
  見つかったパラメーター一覧をコードに挿入するコメント形式で返す
  """
  code = '\n"""'
  for i in range(len(parameters)):
    if i == len(parameters) - 1:
      code += parameters[i]
    else:
      code += parameters[i] + ', '
    if (i + 1) % 6 == 0:
      code += '\n'
  code += '"""\n'
  return code


if __name__ == '__main__':
  main()
