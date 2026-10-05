"""
/*********************************
 * Mã sinh viên: [202418992]
 * Họ tên:       [Pham Thị Minh Thuý]
 *********************************/
"""

from employee import Employee


class SalesEmployee(Employee):
    """Nhân viên kinh doanh hưởng lương cơ bản và hoa hồng doanh số."""

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        department: str,
        base_salary: float,
        commission_rate: float,
        sales_revenue: float = 0.0,
    ):
        super().__init__(employee_id, full_name, department)

        if base_salary < 0:
            raise ValueError("Lỗi: Lương cơ bản không được âm!")
        if sales_revenue < 0:
            raise ValueError("Lỗi: Doanh số bán hàng không được âm!")
        if not (0.0 <= commission_rate <= 0.3):
            raise ValueError("Lỗi: Tỷ lệ hoa hồng phải nằm trong khoảng từ 0 đến 0.3 (30%)!")

        self._base_salary: float = float(base_salary)
        self._commission_rate: float = float(commission_rate)
        self._sales_revenue: float = float(sales_revenue)

    @property
    def base_salary(self) -> float:
        return self._base_salary

    @property
    def sales_revenue(self) -> float:
        return self._sales_revenue

    @property
    def commission_rate(self) -> float:
        return self._commission_rate

    def update_sales_revenue(self, additional_revenue: float) -> None:
        """Cập nhật doanh số có kiểm soát."""
        if additional_revenue < 0:
            raise ValueError("Lỗi: Doanh số cập nhật thêm không được âm!")
        self._sales_revenue += float(additional_revenue)

    def calculate_gross_pay(self) -> float:
        """grossPay = baseSalary + salesRevenue * commissionRate + monthlyBonus"""
        return self._base_salary + (self._sales_revenue * self._commission_rate) + self._monthly_bonus

    def get_employee_type(self) -> str:
        return "Sales"

    def display_payroll_info(self) -> None:
        print(
            f"| {self._employee_id:<6} | {self._full_name:<18} | {self._department:<12} | "
            f"{self.get_employee_type():<10} | Doanh số: {self._sales_revenue:>11,.0f} đ ({self._commission_rate*100:>2.0f}%) | "
            f"Thưởng: {self._monthly_bonus:>9,.0f} đ | Thu nhập: {self.calculate_gross_pay():>12,.0f} đ |"
        )