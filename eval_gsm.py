# open the json file and read the data
import json
import re
import argparse
from datasets import load_dataset
parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, default="experiment/gsm.jsonl")
args = parser.parse_args()


def extract_code(text):
    match = re.search(r"```(.*?)```", text, re.DOTALL)

    code_block = re.search(r'def solution\(\):.*?</s>', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    elif code_block:
        code_block = code_block.group(0)[:-4]
        return code_block
    return None


correct = 0
invalid_code = 0
error_executed_code = 0
data = load_dataset("json", data_files=args.file)
for item in data["train"]:
    answer = item["answer"]
    code = item["output_pred"]
    code = extract_code(code)
    if code is None:
        print("outpput:\n", item["output_pred"])
        invalid_code += 1
        continue
    predict_answer = None
    try:
        exec(code)
        exec("predict_answer = solution()")
    except Exception as e:
        print("code:\n", code)
        error_executed_code += 1
    if predict_answer == answer:
        correct += 1

all_count = len(data["train"])
print("Total count:", all_count)
print("Invalid code:", invalid_code)
print("Accuracy:", correct / all_count)
print("Error executed code:", error_executed_code)