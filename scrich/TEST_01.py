import allure,pytest
class Test_001:
    @allure.step(title="测试步骤001")
    def test_01(self):
        allure.attach("描述","输入用户名")
        assert 1
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKED)

    @allure.step(title="测试步骤002")
    def test_02(self):
        allure.attach("描述", "输入密码")
        assert 0

