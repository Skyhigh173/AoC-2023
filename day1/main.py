import sys; sys.path.insert(0, '../'); from utils import *;

FILE: iterlist[str] = read("./input.txt")

class solution_1:
  def run() -> int:
    def process_line(x: str) -> int:
      r: list[str] = tools.filter(x, str.isdigit)
      return int(r[0] + r[-1])

    return FILE.map(process_line).sum()
  
class solution_2:
  def run() -> int:
    convert: dict[str, int] = {
      'one': '1', 'two': '2', 'three': '3',
      'four': '4', 'five': '5', 'six': '6',
      'seven': '7', 'eight': '8', 'nine': '9'
    }
    convert_values: tuple[str] = tuple(convert.values())
    convert_keys: list[str] = list(convert.keys())

    def process_string(x: str) -> str:
      # number?
      if x.startswith(convert_values): return x[0]

      # string number?
      word: list[str] = [c for c in convert_keys if x.startswith(c)]
      if word: return convert[word[0]]

    def process_line(x: str) -> int:
      r: iterlist[str] = tools.list_cut_off(x).map(process_string).erase_None()
      return int(r[0] + r[-1])

    return FILE.map(process_line).sum()


print(solution_1.run())
print(solution_2.run())