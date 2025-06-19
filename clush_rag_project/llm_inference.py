from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig

def load_mistral_model(model_id="mistralai/Mistral-7B-v0.1", quantize=False):
    if quantize:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype="bfloat16"
        )
        model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map="auto")
    else:
        model = AutoModelForCausalLM.from_pretrained(model_id)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    return model, tokenizer

def generate_response(prompt, model, tokenizer, max_new_tokens=512):
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.2
    )
    response = pipe(prompt)[0]['generated_text']
    return response