"""
1. 아래 방식으로 JSONL 데이터(프롬프트-응답 쌍)를 준비하세요.
2. GPU 환경에서 Hugging Face Transformers+PEFT로 파인튜닝하세요.

from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, BitsAndBytesConfig
from peft import LoraConfig
from trl import SFTTrainer

dataset = load_dataset("json", data_files={"train": "your_train.jsonl", "validation": "your_val.jsonl"})

model_name = "mistralai/Mistral-7B-Instruct-v0.2"
bnb_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype="bfloat16")
model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

lora_config = LoraConfig(
    r=64,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

training_args = TrainingArguments(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    warmup_steps=2,
    max_steps=30,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=1,
    output_dir="./mistral-finetuned"
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    args=training_args,
    peft_config=lora_config,
    tokenizer=tokenizer,
    dataset_text_field="prompt"
)

trainer.train()
"""
