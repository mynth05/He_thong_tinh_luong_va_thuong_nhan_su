"""
/*********************************
 * Mã sinh viên: [202418992]
 * Họ tên:       [Pham Thị Minh Thuý]
 *********************************/
"""

from typing import List, Optional
from employee import Employee


class Payroll:
    """Lớp quản lý và tổng hợp bảng lương theo kỳ."""

    def __init__(self, period: str):
        if not period or not period.strip():
            raise ValueError("Lỗi: Kỳ tính lương không được để trống!")
        self._period: str = period.strip()
        self._employees: List[Employee] = []

    @property
    def period(self) -> str:
        return self._period

    @property
    def employees(self) -> List[Employee]:
        return self._employees

    def find_employee(self, employee_id: str) -> Optional[Employee]:
        """Tìm kiếm nhân sự theo mã (không phân biệt hoa thường)."""
        if not employee_id:
            return None
        target_id = employee_id.strip().lower()
        for emp in self._employees:
            if emp.employee_id.lower() == target_id:
                return emp
        return None

    def add_employee(self, employee: Employee) -> bool:
        """Thêm nhân viên mới; ràng buộc không thêm nhân sự trùng mã."""
        if employee is None:
            return False
        if self.find_employee(employee.employee_id) is not None:
            print(f"Cảnh báo: Nhân viên mã {employee.employee_id} đã tồn tại trong kỳ {self._period}!")
            return False
        self._employees.append(employee)
        return True

    def calculate_total_payroll(self) -> float:
        """Tổng chi trả bảng lương thông qua lời gọi đa hình emp.calculate_gross_pay()."""
        return sum(emp.calculate_gross_pay() for emp in self._employees)

    def calculate_payroll_by_department(self, department: str) -> float:
        """Tính tổng chi trả cho một phòng ban cụ thể."""
        if not department:
            return 0.0
        target_dept = department.strip().lower()
        return sum(
            emp.calculate_gross_pay()
            for emp in self._employees
            if emp.department.lower() == target_dept
        )

    def find_highest_paid_employee(self) -> Optional[Employee]:
        """Tìm nhân sự có thu nhập cao nhất trong kỳ; xử lý an toàn nếu danh sách rỗng."""
        if not self._employees:
            return None
        return max(self._employees, key=lambda emp: emp.calculate_gross_pay())

    def display_payroll(self) -> None:
        """Hiển thị toàn bộ bảng lương bằng lời gọi đa hình."""
        print(f"\n{'='*38} BẢNG LƯƠNG KỲ {self._period} {'='*38}")
        if not self._employees:
            print("Danh sách nhân sự kỳ này hiện đang trống.")
            return

        for emp in self._employees:
            emp.display_payroll_info()

        print("-" * 105)
        print(f"TỔNG CHI TRẢ TOÀN BẢNG LƯƠNG: {self.calculate_total_payroll():>15,.0f} VNĐ")
        print(f"{'='*105}\n")