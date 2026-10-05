"""
/*********************************
 * Mã sinh viên: [202418992]
 * Họ tên:       [Pham Thị Minh Thuý]
 *********************************/
"""

from salaried_employee import SalariedEmployee
from hourly_employee import HourlyEmployee
from sales_employee import SalesEmployee
from payroll import Payroll


def main():
    print("=== 1. CHẠY BỘ DỮ LIỆU KIỂM THỬ ĐỀ BÀI (MỤC C) ===")
    payroll = Payroll("2026-09")

    # 1. Nhân viên lương cố định: E001
    e1 = SalariedEmployee(
        employee_id="E001",
        full_name="Nguyễn Minh An",
        department="Đào tạo",
        monthly_salary=15_000_000,
        responsibility_allowance=2_000_000,
    )
    e1.add_bonus(1_000_000)  # Thưởng cố định không lý do
    payroll.add_employee(e1)

    # 2. Nhân viên theo giờ (không vượt ngưỡng 160h): E002
    e2 = HourlyEmployee(
        employee_id="E002",
        full_name="Trần Thu Bình",
        department="Hỗ trợ",
        hourly_rate=100_000,
        worked_hours=150,
    )
    e2.add_bonus(500_000, "Hoàn thành tốt ca trực hỗ trợ")  # Thưởng cố định kèm lý do
    payroll.add_employee(e2)

    # 3. Nhân viên theo giờ (có vượt ngưỡng 160h): E003
    e3 = HourlyEmployee(
        employee_id="E003",
        full_name="Lê Hoàng Chi",
        department="Hỗ trợ",
        hourly_rate=100_000,
        worked_hours=170,
    )
    # Không có thưởng
    payroll.add_employee(e3)

    # 4. Nhân viên kinh doanh: E004
    e4 = SalesEmployee(
        employee_id="E004",
        full_name="Phạm Quốc Dũng",
        department="Kinh doanh",
        base_salary=8_000_000,
        sales_revenue=200_000_000,
        commission_rate=0.05,
    )
    e4.add_bonus_rate(
        rate=0.02,
        reference_amount=50_000_000,
        reason="Thưởng 2% vượt hạn mức doanh số",
    )
    payroll.add_employee(e4)

    # Hiển thị bảng lương
    payroll.display_payroll()

    # Xác minh các chỉ số theo yêu cầu mục C
    total_payroll = payroll.calculate_total_payroll()
    support_dept_payroll = payroll.calculate_payroll_by_department("Hỗ trợ")
    highest_paid = payroll.find_highest_paid_employee()

    print(f"Tổng lương phòng Hỗ trợ : {support_dept_payroll:>15,.0f} đ (Kỳ vọng: 33.000.000 đ)")
    print(f"Tổng toàn bảng lương    : {total_payroll:>15,.0f} đ (Kỳ vọng: 70.000.000 đ)")
    if highest_paid:
        print(
            f"Nhân sự thu nhập cao nhất: {highest_paid.employee_id} - {highest_paid.full_name} "
            f"({highest_paid.calculate_gross_pay():,.0f} đ)"
        )

    # Chạy 10 test case biên và lỗi (Mục C.1)
    run_edge_and_exception_tests()


def run_edge_and_exception_tests():
    print("\n=== 2. THỰC THI 10 TÌNH HUỐNG KIỂM THỬ BIÊN VÀ NGOẠI LỆ (MỤC C.1) ===")
    passed = 0

    # Test 1: Tạo nhân viên với ID rỗng
    try:
        SalariedEmployee("", "Nguyen Van A", "IT", 10_000_000)
        print("Test 1 FAIL: Không bắt được mã ID rỗng")
    except ValueError as e:
        print(f"Test 1 PASS: Bắt thành công mã ID rỗng -> {e}")
        passed += 1

    # Test 2: Thêm trùng mã nhân sự vào Payroll
    p_test = Payroll("2026-10")
    emp_a = SalariedEmployee("E999", "An", "IT", 10_000_000)
    emp_b = SalariedEmployee("E999", "Bình", "HR", 12_000_000)
    p_test.add_employee(emp_a)
    if not p_test.add_employee(emp_b):
        print("Test 2 PASS: Ngăn chặn thành công thêm trùng lặp mã nhân sự E999")
        passed += 1
    else:
        print("Test 2 FAIL: Cho phép thêm trùng mã!")

    # Test 3: Thưởng số tiền âm
    try:
        emp_a.add_bonus(-100_000)
        print("Test 3 FAIL: Không bắt được thưởng âm")
    except ValueError as e:
        print(f"Test 3 PASS: Bắt thành công số tiền thưởng âm -> {e}")
        passed += 1

    # Test 4: Thưởng có lý do là chuỗi khoảng trắng
    try:
        emp_a.add_bonus(500_000, "   ")
        print("Test 4 FAIL: Không bắt được lý do thưởng rỗng")
    except ValueError as e:
        print(f"Test 4 PASS: Bắt thành công lý do thưởng rỗng -> {e}")
        passed += 1

    # Test 5: Tỷ lệ thưởng vượt quá 0.5 (50%)
    try:
        emp_a.add_bonus_rate(0.55, 10_000_000, "Thưởng 55%")
        print("Test 5 FAIL: Không bắt được tỷ lệ thưởng > 0.5")
    except ValueError as e:
        print(f"Test 5 PASS: Bắt thành công tỷ lệ thưởng vượt 50% -> {e}")
        passed += 1

    # Test 6: Số giờ làm vượt biên trên 250h
    try:
        HourlyEmployee("E100", "Worker Overload", "SX", 50_000, 251)
        print("Test 6 FAIL: Không bắt được số giờ làm > 250")
    except ValueError as e:
        print(f"Test 6 PASS: Bắt thành công số giờ làm quá tải (251h) -> {e}")
        passed += 1

    # Test 7: Số giờ làm ở đúng biên trên 250h hợp lệ
    border_emp = HourlyEmployee("E101", "Border Worker", "SX", 100_000, 250)
    # 160 * 100k + 90 * 100k * 1.5 = 16.000.000 + 13.500.000 = 29.500.000
    if border_emp.calculate_gross_pay() == 29_500_000:
        print("Test 7 PASS: Tính chuẩn xác biên trên 250h (Thu nhập: 29.500.000 đ)")
        passed += 1
    else:
        print("Test 7 FAIL: Sai số tính toán tại mốc 250h")

    # Test 8: Tỷ lệ hoa hồng vượt ngưỡng 0.3
    try:
        SalesEmployee("E102", "Super Sales", "Sale", 5_000_000, 0.35)
        print("Test 8 FAIL: Không bắt được tỷ lệ hoa hồng > 0.3")
    except ValueError as e:
        print(f"Test 8 PASS: Bắt thành công hoa hồng vượt 30% -> {e}")
        passed += 1

    # Test 9: Tìm nhân viên lương cao nhất khi Payroll rỗng
    empty_payroll = Payroll("2026-11")
    if empty_payroll.find_highest_paid_employee() is None and empty_payroll.calculate_total_payroll() == 0.0:
        print("Test 9 PASS: Bảng lương rỗng xử lý an toàn, trả về None và 0.0 đ")
        passed += 1
    else:
        print("Test 9 FAIL: Gặp lỗi khi xử lý bảng lương rỗng")

    # Test 10: Tính tổng phòng ban không tồn tại
    non_existent = p_test.calculate_payroll_by_department("Phòng Ảo")
    if non_existent == 0.0:
        print("Test 10 PASS: Phòng ban không tồn tại trả về đúng 0.0 đ")
        passed += 1
    else:
        print("Test 10 FAIL: Sai giá trị khi tính phòng không tồn tại")

    print(f"\n=> KẾT QUẢ KIỂM THỬ: {passed}/10 TEST CASES ĐẠT CHUẨN!")


if __name__ == "__main__":
    main()