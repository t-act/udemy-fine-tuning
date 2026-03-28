from openai import OpenAI
import settings

client = OpenAI(api_key = settings.API_KEY)

print("OpenAIにjsonlファイルのアップロードを開始します")
upload_response = client.files.create(
    file = open("../data/poker_glossary_finetune.jsonl", "rb"),
    purpose = "fine-tune"
)

file_id = upload_response.id
files = client.files.list()

# fine tune
print(f"jsonlファイル: {file_id} を使用し、Fine-Tuningを開始します")
client.fine_tuning.jobs.create(
    training_file = file_id,
    model = "gpt-4.1-mini-2025-04-14"
)

# job = client.fine_tuning.jobs.retrieve("fftjob-xmfXTVQkDpgoTqnl5CyJLnyc")
# job = client.fine_tuning.jobs.cancel("fftjob-xmfXTVQkDpgoTqnl5CyJLnyc")
# print(job.status)
