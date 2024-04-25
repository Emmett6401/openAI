# openAI
## openAI API 사용하기 
### 코드에서는 key를 my_key에 적어서 사용하고 
### 다른 방법은 다음과 같이 환경변수에 등록하면 나의 API_KEY를 노출 하지 않고 사용 가능함.
<img src = "https://github.com/Emmett6401/openAI/blob/main/111.png">
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
