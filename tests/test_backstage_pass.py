from statistics import quantiles
from turtle import back
from src.backstage_pass import BackstagePass

def test_backstage_pass_increase_value_more_than_10_days():
    backstage_pass = BackstagePass("backstage pass", sell_in=15, quality=10)

    backstage_pass.update_item()

    assert backstage_pass.quality == 11

def test_backstage_pass_increase_value_10_days():
    backstage_pass = BackstagePass("backstage pass", sell_in=10, quality=10)

    backstage_pass.update_item()

    assert backstage_pass.quality == 12

def test_backstage_pass_increase_value_5_days():
    backstage_pass = BackstagePass("backstage pass", sell_in=5, quality=10)

    backstage_pass.update_item()

    assert backstage_pass.quality == 13

def test_backstage_pass_passed_sell_by():
    backstage_pass = BackstagePass("backstage pass", sell_in=0, quality=10)

    backstage_pass.update_item()
    print(backstage_pass)
    print('hello')

    assert backstage_pass.quality == 0