from types import LambdaType, GeneratorType

class iterlist(list):
  def map(self, fx: LambdaType) -> "iterlist":
    return iterlist(map(fx, self))
  
  def sum(self) -> int:
    return sum(self)
  
  def erase_None(self) -> 'iterlist':
    return iterlist([c for c in self if c is not None])

def read(path: str) -> iterlist[str]: return iterlist(open(path, "r").read().splitlines())
class tools:
  def foreach(l: list | GeneratorType, fx: LambdaType) -> list: return list(map(fx, l))
  def filter(l: str, fx: LambdaType) -> list: return list(filter(fx, l))

  def list_int(l: list | GeneratorType) -> list[int]: return tools.foreach(l, int)
  def list_float(l: list | GeneratorType) -> list[float]: return tools.foreach(l, float)
  def erase_none(l: list | GeneratorType) -> list: return [c for c in l if c is not None]

  def cut_off(s: str) -> str:
    i = 0
    while i < len(s):
      yield s[i:]
      i += 1
  
  def list_cut_off(s: str) -> iterlist[str]:
    return iterlist(tools.cut_off(s))