from transformers import AutoModelForCausalLM, AutoTokenizer

CACHE_DIR = "/workspace/.cache/transformers"

model = AutoModelForCausalLM.from_pretrained(
    "tokyotech-llm/Llama-3.1-Swallow-8B-v0.1",
    device_map="auto",
    torch_dtype="auto",
    cache_dir=CACHE_DIR,
)
tokenizer = AutoTokenizer.from_pretrained(
    "tokyotech-llm/Llama-3.1-Swallow-8B-v0.1", cache_dir=CACHE_DIR
)


system_prompt_head = """以下に、あるタスクを説明する指示があります。リクエストを適切に完了するための回答を記述してください。
### 指示:
以下のトピックに関する詳細な情報を提供してください。

### 入力:
"""

system_prompt_tail = """
### 応答:
"""


try:
    while True:
        user_prompt = input(">")
        encode_inputs = tokenizer(
            system_prompt_head + user_prompt + system_prompt_tail, return_tensors="pt"
        ).to(model.device)
        input_token_length = encode_inputs["input_ids"].shape[1]

        output_ids = model.generate(
            encode_inputs["input_ids"],
            attention_mask=encode_inputs["attention_mask"],
            max_new_tokens=10,
            repetition_penalty=2.0,
            pad_token_id=tokenizer.eos_token_id,
        )

        generated_prompt = tokenizer.decode(
            output_ids[0][input_token_length:], skip_special_tokens=True
        )

        print(generated_prompt)

except KeyboardInterrupt:
    print("KeyboardInterrupt")
