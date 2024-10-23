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


def continue_prompt(user_prompt: str) -> str:
    encode_inputs = tokenizer(user_prompt, return_tensors="pt").to(model.device)

    output_ids = model.generate(
        encode_inputs["input_ids"],
        attention_mask=encode_inputs["attention_mask"],
        max_new_tokens=10,
        repetition_penalty=2.0,
        pad_token_id=tokenizer.eos_token_id,
    )

    generated_prompt = tokenizer.batch_decode(output_ids[0], skip_special_tokens=True)

    return generated_prompt


if __name__ == "__main__":
    try:
        while True:
            user_prompt = input(">")
            generated_prompt = continue_prompt(user_prompt)
            print(generated_prompt)
            print("".join(generated_prompt))

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
