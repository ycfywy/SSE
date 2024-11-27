from transformers import AutoTokenizer, AutoModelForCausalLM

# 定义保存路径
cache_dir = "D:/llama/llama3.2-3b"



tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B",cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-3B",cache_dir=cache_dir)