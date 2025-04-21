import pytest
from app import add

@pytest.mark.parametrize("input_a, input_b, expected_output", [
    (7, 8, 15),      # ケース1
    (10, -3, 7),     # ケース2
    (-5, -5, -10),   # ケース3
    (0, 100, 100),   # ケース4
    (1, 2, 3),       # ケース5: デモ用の失敗ケース
])
def test_add_parametrized(input_a, input_b, expected_output):
  """パラメータ化されたadd関数のテスト"""
  assert add(input_a, input_b) == expected_output, f"{input_a} + {input_b} は {expected_output} のはず"