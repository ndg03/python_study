# 所在包    python
# 项目名称  test
# 日期     2023/4/8/ 10:33
# 作者     你大锅
import openai_secret_manager
import openai

# 获取 API Key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# 设置 API Key
openai.api_key = open("api_key.txt", "r").read()

# 测试 API Key 是否可用
models = openai.Model.list()
print(models)