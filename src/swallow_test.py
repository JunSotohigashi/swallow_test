from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

CACHE_DIR = "/workspace/.cache/transformers"

model = AutoModelForCausalLM.from_pretrained("tokyotech-llm/Llama-3.1-Swallow-8B-v0.1", device_map="auto", torch_dtype="auto", cache_dir=CACHE_DIR)
tokenizer = AutoTokenizer.from_pretrained("tokyotech-llm/Llama-3.1-Swallow-8B-v0.1",  cache_dir=CACHE_DIR)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

messages = """以下に、あるタスクを説明する指示があります。リクエストを適切に完了するための回答を記述してください。

### 指示:
以下のトピックに関する詳細な情報を提供してください。

### 入力:
つばめに純粋理性批判は理解できますか？

### 応答:
"""

input_ids = tokenizer.encode(messages, add_special_tokens=True, return_tensors="pt").to(model.device)
output_ids = model.generate(input_ids,
                            max_new_tokens=1024,
                            streamer=streamer)
