"""
/*********************************
 * Mã sinh viên: 202418992
 * Họ tên:       Phạm Thị Minh Thuý
 *********************************/
"""

from abc import ABC, abstractmethod
from typing import Optional


class Employee(ABC):
    """Lớp trừu tượng cơ sở đại diện cho nhân sự trong doanh nghiệp."""

    def __init__(self, employee_id: str, full_name: str, department: str = "Unassigned"):
        # Constructor rút gọn & đầy đủ thông qua tham số mặc định (A.4)
        if not employee_id or not employee_id.strip():
            raise ValueError("Lỗi: Mã nhân sự không được để trống!")
        if not full_name or not full_name.strip():
            raise ValueError("Lỗi: Họ tên không được để trống!")
        if not department or not department.strip():
            raise ValueError("Lỗi: Phòng ban không được để trống!")

        self._employee_id: str = employee_id.strip()
        self._full_name: str = full_name.strip()
        self._department: str = department.strip()
        self._monthly_bonus: float = 0.0

    # Getters
    @property
    def employee_id(self) -> str:
        return self._employee_id

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def department(self) -> str:
        return self._department

    @property
    def monthly_bonus(self) -> float:
        return self._monthly_bonus

    # Nạp chồng phiên bản 1 & 2: Thêm khoản thưởng cố định (kèm lý do tùy chọn)
    def add_bonus(self, amount: float, reason: Optional[str] = None) -> None:
        """
        Thêm một khoản thưởng cố định vào tổng thưởng trong tháng.
        amount: Số tiền thưởng (> 0).
        reason: Lý do thưởng (nếu có thì không được rỗng).
        """
        if amount <= 0:
            raise ValueError("Lỗi: Số tiền thưởng phải lớn hơn 0!")
        if reason is not None and not reason.strip():
            raise ValueError("Lỗi: Lý do thưởng nếu có không được để trống!")

        self._monthly_bonus += float(amount)

    # Nạp chồng phiên bản 3: Thêm thưởng theo tỷ lệ trên số tiền tham chiếu kèm lý do
    def add_bonus_rate(self, rate: float, reference_amount: float, reason: str) -> None:
        """
        Tính thưởng theo tỷ lệ của một giá trị tham chiếu kèm lý do.
        rate: Tỷ lệ thưởng (0 < rate <= 0.5).
        reference_amount: Giá trị tham chiếu (> 0).
        reason: Lý do thưởng (bắt buộc, không rỗng).
        """
        if not (0.0 < rate <= 0.5):
            raise ValueError("Lỗi: Tỷ lệ thưởng phải nằm trong khoảng (0, 0.5] (tối đa 50%)!")
        if reference_amount <= 0:
            raise ValueError("Lỗi: Giá trị tham chiếu phải lớn hơn 0!")
        if not reason or not reason.strip():
            raise ValueError("Lỗi: Lý do thưởng không được để trống!")

        bonus_calculated = reference_amount * rate
        self._monthly_bonus += float(bonus_calculated)

    def reset_bonus(self) -> None:
        """Đặt lại thưởng về 0 khi bắt đầu kỳ tính lương mới."""
        self._monthly_bonus = 0.0

    @abstractmethod
    def calculate_gross_pay(self) -> float:
        """Phương thức trừu tượng tính thu nhập tháng, bắt buộc lớp con ghi đè."""
        pass

    @abstractmethod
    def get_employee_type(self) -> str:
        """Trả về chuỗi định danh loại nhân sự."""
        pass

    def display_payroll_info(self) -> None:
        """Hiển thị thông tin tổng hợp của nhân viên."""
        print(
            f"| {self._employee_id:<6} | {self._full_name:<18} | {self._department:<12} | "
            f"{self.get_employee_type():<10} | Thưởng: {self._monthly_bonus:>12,.0f} đ | "
            f"Tổng: {self.calculate_gross_pay():>12,.0f} đ |"
        )