"""
/*********************************
 * Mã sinh viên: [202418992]
 * Họ tên:       [Pham Thị Minh Thuý]
 *********************************/
"""

from employee import Employee


class HourlyEmployee(Employee):
    """Nhân viên hưởng lương theo giờ thực tế với hệ số ngoài 160h."""

    REGULAR_HOURS_LIMIT: float = 160.0
    OVERTIME_RATE_MULTIPLIER: float = 1.5

    def __init__(
        self,
        employee_id: str,
        full_name: str,
        department: str,
        hourly_rate: float,
        worked_hours: float = 0.0,
    ):
        super().__init__(employee_id, full_name, department)

        if hourly_rate <= 0:
            raise ValueError("Lỗi: Đơn giá giờ phải lớn hơn 0!")
        self._validate_hours(worked_hours)

        self._hourly_rate: float = float(hourly_rate)
        self._worked_hours: float = float(worked_hours)

    def _validate_hours(self, hours: float) -> None:
        if not (0.0 <= hours <= 250.0):
            raise ValueError("Lỗi: Số giờ làm hợp lệ trong tháng phải từ 0 đến 250 giờ!")

    @property
    def hourly_rate(self) -> float:
        return self._hourly_rate

    @property
    def worked_hours(self) -> float:
        return self._worked_hours

    def set_worked_hours(self, worked_hours: float) -> None:
        self._validate_hours(worked_hours)
        self._worked_hours = float(worked_hours)

    def calculate_gross_pay(self) -> float:
        """
        Tính thu nhập từ trạng thái hiện có mà không lưu riêng tiền làm thêm.
        Nếu workedHours <= 160: basePay = workedHours * hourlyRate
        Nếu workedHours > 160:  basePay = 160 * rate + (workedHours - 160) * rate * 1.5
        grossPay = basePay + monthlyBonus
        """
        if self._worked_hours <= self.REGULAR_HOURS_LIMIT:
            base_pay = self._worked_hours * self._hourly_rate
        else:
            regular_pay = self.REGULAR_HOURS_LIMIT * self._hourly_rate
            overtime_hours = self._worked_hours - self.REGULAR_HOURS_LIMIT
            overtime_pay = overtime_hours * self._hourly_rate * self.OVERTIME_RATE_MULTIPLIER
            base_pay = regular_pay + overtime_pay

        return base_pay + self._monthly_bonus

    def get_employee_type(self) -> str:
        return "Hourly"

    def display_payroll_info(self) -> None:
        regular_hours = min(self._worked_hours, self.REGULAR_HOURS_LIMIT)
        overtime_hours = max(0.0, self._worked_hours - self.REGULAR_HOURS_LIMIT)
        print(
            f"| {self._employee_id:<6} | {self._full_name:<18} | {self._department:<12} | "
            f"{self.get_employee_type():<10} | Giờ: {regular_hours:>4.0f} (TC:{overtime_hours:>3.0f}) | "
            f"Đơn giá: {self._hourly_rate:>9,.0f} đ | "
            f"Thưởng: {self._monthly_bonus:>9,.0f} đ | Thu nhập: {self.calculate_gross_pay():>12,.0f} đ |"
        )