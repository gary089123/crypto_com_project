import pytest

@pytest.mark.usefixtures("set_env")
@pytest.mark.usefixtures("set_selenium_driver")
class BaseWebTest():
    pass



@pytest.mark.usefixtures("set_env")
class BaseAppTest():
    pass



@pytest.mark.usefixtures("set_env")
class BaseApiTest():
    pass

