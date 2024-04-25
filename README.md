# openAI
## openAI API 사용하기 
### 라이브러리 
```bash
pip install --upgrade openai
```
### 코드에서는 key를 my_key에 적어서 사용했습니다. 
이 API_KEY는 
여기서 만들수 있습니다.

<img src="https
### 다른 방법은 다음과 같이 환경변수에 등록하면 나의 API_KEY를 노출 하지 않고 사용 가능함.
```bash
setx OPENAI_API_KEY "your-api-key-here"
```
### 그럴때는 다음과 같이 사용합니다. 

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
```
