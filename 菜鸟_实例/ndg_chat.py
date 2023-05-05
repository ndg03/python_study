# 所在包    python
# 项目名称  ndg_chat
# 日期     2023/4/8/ 10:07
# 作者     你大锅
import openai

openai.api_key = "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"

completion = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Hello, world",
    max_tokens=5
)

print(completion.choices[0].text)