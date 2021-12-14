# Crypto.com QA challenge

## Description
The test automation is base on pytest with the customize runner

folder structure :

1. ```libs``` :  folder for test library, ex: web/app pageobject, api module
2. ```utils``` : folder for common tools
3. ```tests``` : folder for testcase 
4. ```runner.py``` : main python file to trigger run
5. ```testset.yaml``` : configuration for the tests to run
6. ```testenv.yaml``` : configuration for the testcase enviroment and variable




## Setup

requirment: python3

```
pip install -r requirements.txt
```

## Configuration

### testset.yaml
use to configure the tests to run
```yaml
configuration:
  report: report.html  #report file name
  testset: weatherapi  #testset name to run 


testsets:

  cryptoweb: # testset name
    - test_search_and_go_to_cro_page # testcase name
    - test_detail_page_change_1m_timeline
    - test_detail_page_change_5m_timeline
    - test_detail_page_change_30m_timeline


  weatherapi:

    - test_forecase_api_status
    - test_forecase_general_situation
    - test_forecase_day_three
```
### testenv.yaml
test enviroment and variable, can be read in ```self.config``` in testcase file ex:
```python
class Test(BaseWebTest):

    def test_open_app(self):

        browser = self.config.get("browser")

        open_app_with(browser)

```

## Excution

```
python runner.py
```


