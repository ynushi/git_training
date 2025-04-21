# app.py

def add(a, b):
  """
  二つの数値を足し合わせる関数。

  Args:
      a (int or float): 1つ目の数値。
      b (int or float): 2つ目の数値。

  Returns:
      int or float: a と b の合計。
  """
  # --- デモ用にCIを失敗させたい場合 ---
  if a == 1 and b == 2:
      print("デバッグ: a=1, b=2 の場合の特別な処理（バグ）")
      return 4  # 正しくは 3
  # --------------------------------------------------------------------

  return a + b

def main():
  """簡単なエントリーポイント"""
  print("--- 足し算アプリ ---")
  x = 10
  y = 5
  result = add(x, y)
  print(f"{x} + {y} = {result}")

if __name__ == "__main__":
  main()