"""
/*********************************
 * Mã sinh viên: [202418992]
 * Họ tên:       [Pham Thị Minh Thuý]
 *********************************/
"""

from employee import Employee


class SalariedEmployee(Employee):
    """Nhân viên hưởng lương cố định theo tháng và phụ cấp trách nhiệm."""

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        department: str,
        monthly_salary: float,
        responsibility_allowance: float = 0.0,
    ):
        # Tái sử dụng constructor lớp cha
        super().__init__(employee_id, full_name, department)

        if monthly_salary < 0:
            raise ValueError("Lỗi: Lương cố định tháng không được âm!")
        if responsibility_allowance < 0:
            raise ValueError("Lỗi: Phụ cấp trách nhiệm không được âm!")

        self._monthly_salary: float = float(monthly_salary)
        self._responsibility_allowance: float = float(responsibility_allowance)

    @property
    def monthly_salary(self) -> float:
        return self._monthly_salary

    @property
    def responsibility_allowance(self) -> float:
        return self._responsibility_allowance

    def calculate_gross_pay(self) -> float:
        """grossPay = monthlySalary + responsibilityAllowance + monthlyBonus"""
        return self._monthly_salary + self._responsibility_allowance + self._monthly_bonus

    def get_employee_type(self) -> str:
        return "Salaried"

    def display_payroll_info(self) -> None:
        print(
            f"| {self._employee_id:<6} | {self._full_name:<18} | {self._department:<12} | "
            f"{self.get_employee_type():<10} | Lương: {self._monthly_salary:>11,.0f} đ | "
            f"Phụ cấp: {self._responsibility_allowance:>9,.0f} đ | "
            f"Thưởng: {self._monthly_bonus:>9,.0f} đ | Thu nhập: {self.calculate_gross_pay():>12,.0f} đ |"
        )