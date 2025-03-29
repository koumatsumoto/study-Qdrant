# study-qdrant

このプロジェクトは [Vector Similarity Search 超入門](https://zenn.dev/tfutada/articles/acf8adbb2ba5be) の内容を学習するために作成したものです。

## セットアップ方法

このプロジェクトは Python 3.10 と Poetry を使用しています。

1. Poetry のインストール（まだの場合）
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. プロジェクトのセットアップ
```bash
# 依存関係のインストール
poetry install
```

## コードフォーマット

このプロジェクトは Black を使用してコードをフォーマットします。

```bash
# すべてのPythonファイルをフォーマット
poetry run black .
```

## 依存関係

主な依存関係：
- numpy: データ処理と数値計算
- pandas: データフレーム操作
- ginza: 日本語自然言語処理
- ja-ginza: 日本語モデル
- scikit-learn: 機械学習
- plotly: データ可視化

## Python バージョン要件

Python 3.10.x が必要です。
