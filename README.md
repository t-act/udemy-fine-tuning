# udemy-fine-tuning

ポーカー用語集を使ったOpenAI LLMファインチューニングのサンプルプロジェクト。

## 概要

1. ポーカー用語集（Markdown）からファインチューニング用QAデータ（JSONL）を生成
2. OpenAI APIにJSONLをアップロード
3. Fine-Tuningジョブを実行

## セットアップ

```bash
# 依存関係のインストール
uv sync

# APIキーの設定
cp .env.example .env  # .envを作成してAPIキーを記入
```

`.env` ファイル:

```
API_KEY=sk-...
```

## 使い方

```bash
cd src

# デフォルト実行（suffixなし）
python main.py

# 出力モデル名にsuffixを付与
python main.py --suffix poker-v1
```

`--suffix` を指定すると、ファインチューニング後のモデル名が `gpt-4.1-mini-2025-04-14:xxx-poker-v1` のようになります。

## ファイル構成

```
src/
  main.py        # エントリーポイント（引数: --suffix）
  fine_tuning.py # ファイルアップロード・Fine-Tuningジョブ実行
  md_2_jsonl.py  # MarkdownからJSONL生成
  scraping.py    # Webスクレイピングサンプル
  settings.py    # 環境変数読み込み
data/
  poker_glossary.md              # ポーカー用語集（元データ）
  poker_glossary_finetune.jsonl  # Fine-Tuning用QAデータ
  ymedu_tech_finetune.jsonl      # Fine-Tuning用QAデータ（技術系）
```

## 使用モデル

- データ生成: `gpt-4.1-mini`
- Fine-Tuning対象: `gpt-4.1-mini-2025-04-14`
