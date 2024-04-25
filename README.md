# openAI
## openAI API 사용하기 
### 라이브러리 
```bash
pip install --upgrade openai
```
### 코드에서는 key를 my_key에 적어서 사용했습니다. 
이 API_KEY는 
여기서 만들수 있습니다.
<img src="https://github.com/Emmett6401/openAI/blob/main/222.png">


### 다른 방법은 다음과 같이 환경변수에 등록하면 나의 API_KEY를 노출 하지 않고 사용 가능함.
```bash
setx OPENAI_API_KEY "your-api-key-here"
```
### 그럴때는 코드는 다음과 같이 사용합니다. 
```python
from openai import OpenAI
client = OpenAI() # 여기만 달라 집니다.

# 나머지는 같아요 

print(completion.choices[0].message)
```
