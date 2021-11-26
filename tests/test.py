import pytest


def test_one_plus_two_wrong():
  a = 1
  b = 2
  c = 0
  assert a + b == c


def test_one_plus_two_true():
  a = 1
  b = 2
  c = 3
  assert a + b == c


def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError) as e:
    num = 1 / 0
  assert 'division by zero' in str(e.value)


@pytest.mark.math
@pytest.mark.smoketest
def test_one_plus_two_w_mark():
  a = 1
  b = 2
  c = 3
  assert a + b == c


products = [
  (2, 3, 6),    # положительные целые числа
  (1, 99, 99),  # умножение на 1
  (0, 99, 0),   # умножение на 0
  (3, -4, -12), # умножение положительного на отрицательное
  (-5, -5, 25), # умножение отрицательного на отрицательное
  (2.5, 6.7, 16.75)  # числа с плавающей запятой
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
  assert a * b == product


def data_for_test():
  test_data = [
    (3, 5, 8),
    (2, 5, 7)
  ]
  values_ids = ['3 + 5 = 8', 'ok']
  return (test_data, values_ids)


(values, values_ids) = data_for_test()


@pytest.mark.parametrize("a,b,expected", values, ids=values_ids)
def test_summ(a, b, expected):
  assert a + b == expected