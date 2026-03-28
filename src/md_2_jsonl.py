import os
from openai import OpenAI
import settings

JSONL_PATH = '../data/poker_glossary_finetune.jsonl'

if not os.path.exists(JSONL_PATH):
    print("markdownファイルからjsonlファイルの作成を開始します")
    client = OpenAI(api_key = settings.API_KEY)

    with open('../data/poker_glossary.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    prompt = f"""
{md_text}からファインチューニング用のQA用のjsonl形式で投入できるように30個作成してください openAIのモデルでファインチューニングできるように
```
{{
"messages":[{{"role": "user",...}}, {{"role": "assistant", ...}}]
}}
```
の形式で出力
must: jsonl以外の他のテキストは一切含めないこと。
"""

    res = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    reply = res.choices[0].message.content

    with open(JSONL_PATH, 'w', encoding='utf-8') as f:
        f.write(reply)
    print("jsonlファイルの作成が完了しました")

