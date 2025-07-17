import litellm

a = {'messages':[{"role": "user", "content": "Hello!"}]}

# 替换为你的 one-api 地址和 API Key
response = litellm.completion(
    model="gpt-3.5-turbo",  # 对应 one-api 中配置的模型名称
    **a,
    # messages=[{"role": "user", "content": "Hello!"}],
    api_base="https://api.linkerai.top/v1",  # one-api 服务地址
    api_key="sk-yAevPhUZNxnQzP2DA0340d365c1a4757B999031b3aE95b63",  # one-api 分配的 Key
)

print(response)