# -*- coding: utf-8 -*-

#                      愿大千世界，人人年薪百万
#
#                            _ooOoo_
#                           o8888888o
#                           88" . "88
#                           (| -_- |)
#                            O\ = /O
#                        ____/`---'\____
#                      .   ' \\| |// `.
#                       / \\||| : |||// \
#                     / _||||| -:- |||||- \
#                       | | \\\ - /// | |
#                     | \_| ''\---/'' | |
#                      \ .-\__ `-` ___/-. /
#                   ___`. .' /--.--\ `. . __
#                ."" '< `.___\_<|>_/___.' >'"".
#               | | : `- \`.;`\ _ /`;.`/ - ` : | |
#                 \ \ `-. \_ __\ /__ _/ .-` / /
#         ======`-.____`-.___\_____/___.-`____.-'======
#                            `=---='
#
#         .............................................

from typing import List


# 公积金社保缴纳基数上限
UP_BAND = 31014


def get_tax_info(taxable_amount):
    if taxable_amount <= 36000:
        tax_rate = 0
        quick_deduct = 0
    elif 3_6000 < taxable_amount <= 14_4000:
        tax_rate = 0.1
        quick_deduct = 2520
    elif 14_4000 < taxable_amount <= 30_0000:
        tax_rate = 0.2
        quick_deduct = 16920
    elif 30_0000 < taxable_amount <= 42_0000:
        tax_rate = 0.25
        quick_deduct = 31920
    elif 42_0000 < taxable_amount <= 66_0000:
        tax_rate = 0.3
        quick_deduct = 52920
    elif 66_0000 < taxable_amount <= 96_0000:
        tax_rate = 0.35
        quick_deduct = 85920
    else:
        tax_rate = 0.45
        quick_deduct = 181920

    return tax_rate, quick_deduct


class Salary:
    """
    在同一公司连续工作
    """
    def __init__(self, *, month, pre, after, tax):
        self.month = month
        self.pre = pre
        self.after = round(after, 2)
        self.tax = round(tax, 2)

    def __str__(self):
        return f'<Salary>: {self.month}月，税前：{self.pre}，税后：{self.after}，纳税：{self.tax}'

    def __repr__(self):
        return self.__str__()


class Tax:
    """
    在同一公司连续工作
    """
    def __init__(
            self,
            *,
            salary: int,
            months: int = 12,
            bonus: float = 0,
            pension: float = 0.08,
            medical: float = 0.02,
            unemployment: float = 0.005,
            housing: float = 0.07,
            special: int = 12000,
            exemption: int = 5000
    ):
        self.salary = salary              # 税前工资
        self.bonus = bonus                # 税前奖金
        self.months = months              # 计薪月数
        self.pension = pension            # 养老金比例
        self.medical = medical            # 医疗保险比例
        self.unemployment = unemployment  # 失业保险比例
        self.housing = housing            # 住房公积金比例
        self.special = special            # 专项附加扣除
        self.exemption = exemption        # 免税额度，个税起征点

        self.pre_annual_salary = salary * months + bonus  # 税前年薪
        self.salary_lst = []  # 每月工资信息
        self.payed_tax = 0    # 已交个税

    def monthly(self):

        base = self.salary if self.salary <= UP_BAND else UP_BAND
        # 社保、公积金等专项扣除
        nation_deduct = base * (self.pension + self.medical + self.unemployment + self.housing)
        # 合计专项扣除
        total_deduct = self.exemption + nation_deduct
        print(total_deduct)
        # 专项扣除后的年收入
        deduct_annual = 0
        for i in range(1, 13):
            salary = self.salary if i < 12 else self.salary * (self.months - 11)

            deduct_annual += (salary - total_deduct)
            if deduct_annual <= 0:
                deduct_annual = 0
            if deduct_annual <= 3_6000:
                # 当月所需纳税额
                pay_tax = deduct_annual * 0.03
                hand_income = salary - nation_deduct - pay_tax
                salary = Salary(month=i, pre=self.salary, after=hand_income, tax=pay_tax)
                self.salary_lst.append(salary)
                self.payed_tax += pay_tax
            else:
                tax_rate, quick_deduct = get_tax_info(deduct_annual)

                # 当月所需纳税额
                pay_tax = deduct_annual * tax_rate - quick_deduct - self.payed_tax
                # 当月到手
                hand_income = salary - nation_deduct - pay_tax

                s = Salary(month=i, pre=salary, after=hand_income, tax=pay_tax)
                self.salary_lst.append(s)
                self.payed_tax += pay_tax

        hand_annual = 0
        pay_tax = 0
        for salary in self.salary_lst:
            hand_annual += salary.after
            pay_tax += salary.tax
            print(salary)

        print(f'[每月预扣] 税前：{self.pre_annual_salary}，税后：{round(hand_annual, 2)}，纳税：{pay_tax}')

    def yearly(self):
        base = self.salary if self.salary <= UP_BAND else UP_BAND
        # 社保、公积金等专项扣除
        nation_deduct = base * (self.pension + self.medical + self.unemployment + self.housing) * 12
        # 免税总额
        total_exemption = self.exemption * 12
        # 专项附加扣除
        special_exemption = self.special
        # 应税金额
        taxable_amount = self.pre_annual_salary - total_exemption - special_exemption - nation_deduct

        tax_rate, quick_deduct = get_tax_info(taxable_amount)
        pay_tax = taxable_amount * tax_rate - quick_deduct
        hand_annual = self.pre_annual_salary - pay_tax - nation_deduct
        print(f'[年度结算] 税前：{self.pre_annual_salary}，税后：{round(hand_annual, 2)}，纳税：{pay_tax}')


class MixSalary:
    """
    换工作导致工资变化时使用
    """

    def __init__(
            self,
            *,
            salary: int,
            month: int,
            pension: float = 0.08,
            medical: float = 0.02,
            unemployment: float = 0.005,
            housing: float = 0.07,
    ):
        self.salary = salary
        self.month = month
        self.pension = pension
        self.medical = medical
        self.unemployment = unemployment
        self.housing = housing

    @property
    def nation_rate(self):
        """ 社保、公积金等比例 """
        return self.pension + self.medical + self.unemployment + self.housing

    @property
    def nation_deduct(self):
        """ 社保、公积金等专项扣除 """
        base = self.salary if self.salary <= UP_BAND else UP_BAND
        return base * self.nation_rate


class MixTax:

    def __init__(
            self,
            *,
            salaries: List[MixSalary],
            bonus: float = 0,
            special: int = 12000,
            exemption: int = 5000
    ):
        self.salaries = salaries    # 税前工资
        self.bonus = bonus          # 税前奖金
        self.special = special      # 专项附加扣除
        self.exemption = exemption  # 免税额度，个税起征点

        self.pre_annual_salary = bonus  # 税前年薪，预加奖金
        self.salary_lst = []  # 每月工资信息
        self.payed_tax = 0    # 已交个税

    def monthly(self):
        pre_annual_salary = 0
        # 专项扣除后的年收入
        deduct_annual = 0
        for salary in self.salaries:
            income = salary.salary if salary.month < 12 else salary.salary + self.bonus
            pre_annual_salary += income
            # 合计专项扣除
            total_deduct = salary.nation_deduct + self.exemption
            # 更新应税收入
            deduct_annual += (income - total_deduct)
            if deduct_annual <= 0:
                deduct_annual = 0
            if deduct_annual <= 3_6000:
                # 当月所需纳税额
                pay_tax = deduct_annual * 0.03
                hand_income = income - salary.nation_deduct - pay_tax
                salary = Salary(month=salary.month, pre=income, after=hand_income, tax=pay_tax)
                self.salary_lst.append(salary)
                self.payed_tax += pay_tax
                print(salary)
            else:
                tax_rate, quick_deduct = get_tax_info(deduct_annual)
                # 当月所需纳税额
                pay_tax = deduct_annual * tax_rate - quick_deduct - self.payed_tax
                # 当月到手
                hand_income = income - salary.nation_deduct - pay_tax

                s = Salary(month=salary.month, pre=income, after=hand_income, tax=pay_tax)
                print(s)
                self.salary_lst.append(s)
                self.payed_tax += pay_tax

        hand_annual = 0
        pay_tax = 0
        for salary in self.salary_lst:
            hand_annual += salary.after
            pay_tax += salary.tax
            # print(salary)

        print(f'[每月预扣] 税前：{pre_annual_salary}，税后：{round(hand_annual, 2)}，纳税：{pay_tax}')

    def yearly(self):
        pre_annual_salary = self.pre_annual_salary
        # 免税总额
        total_exemption = self.exemption * 12
        # 专项附加扣除
        special_exemption = self.special
        # 全年社保、公积金等专项扣除
        nation_deduct = 0

        for salary in self.salaries:
            nation_deduct += salary.nation_deduct
            pre_annual_salary += salary.salary

        # 应税金额
        taxable_amount = pre_annual_salary - total_exemption - special_exemption - nation_deduct

        tax_rate, quick_deduct = get_tax_info(taxable_amount)
        pay_tax = taxable_amount * tax_rate - quick_deduct
        if pay_tax <= 0:
            pay_tax = 0
        hand_annual = pre_annual_salary - pay_tax - nation_deduct
        print(f'[年度结算] 税前：{pre_annual_salary}，税后：{round(hand_annual, 2)}，纳税：{pay_tax}')


def test_tax():
    tax = Tax(
        salary=100000,
        months=18,
        special=18000
    )
    tax.monthly()
    tax.yearly()


def test_mix_tax():
    salary1 = MixSalary(salary=100000, month=1)
    salary2 = MixSalary(salary=100000, month=2)
    salary3 = MixSalary(salary=100000, month=3)
    salary4 = MixSalary(salary=100000, month=4)
    salary5 = MixSalary(salary=100000, month=5)
    salary6 = MixSalary(salary=100000, month=6)
    salary7 = MixSalary(salary=100000, month=7)
    salary8 = MixSalary(salary=100000, month=8)
    salary9 = MixSalary(salary=100000, month=9)
    salary10 = MixSalary(salary=100000, month=10)
    salary11 = MixSalary(salary=100000, month=11)
    salary12 = MixSalary(salary=100000, month=12)

    salaries = [
        salary1, salary2, salary3, salary4, salary5,
        salary6, salary7, salary8, salary9, salary10,
        salary11, salary12
    ]
    mix_tax = MixTax(
        salaries=salaries,
        bonus=600000,
        special=18000
    )
    mix_tax.monthly()
    mix_tax.yearly()


if __name__ == '__main__':
    test_tax()
    test_mix_tax()
