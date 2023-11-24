import pandas as pd
import requests

# 读取原始Excel文件
input_file = 'input.xlsx'
df = pd.read_excel(input_file)

# 创建一个新的DataFrame用于存储结果
result_df = pd.DataFrame(columns=['github ID', 'Email Address'])

# GitHub个人访问令牌,在这里输入个人自己的令牌
personal_access_token = 'your_token'

# 设置GitHub API的URL模板
github_api_url_template = 'https://api.github.com/users/{username}'

# 设置HTTP请求头，包括认证信息
headers = {
    'Authorization': f'token {personal_access_token}'
}

# 遍历原始Excel中的每一行
for index, row in df.iterrows():
    github_username = row['github ID']

    # 发送GET请求到GitHub API
    response = requests.get(github_api_url_template.format(username=github_username), headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        if 'email' in user_data and user_data['email']:
            email_address = user_data['email']
        else:
            email_address = 'Email address not found'
    else:
        email_address = 'Error: Unable to fetch email'

    result_df = result_df.append({'GitHub Username': github_username, 'Email Address': email_address},
                                 ignore_index=True)

# 将结果保存到新的Excel文件
output_file = 'output.xlsx'
result_df.to_excel(output_file, index=False)

print(f'Results saved to {output_file}')
