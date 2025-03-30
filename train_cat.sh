#!/bin/bash
export CUDA_VISIBLE_DEVICES=0
## CAT training
python cat_train.py \
    --model LLaMA-7B \
    --base_model yahma/llama-7b-hf \
    --adapter LoRA \
    --data_path data/skill_datasets/mix/metamath_code_alpaca_10k.json \
    --output_dir models/math_code_cat_debug \
    --batch_size 10 \
    --micro_batch_size 6 \
    --num_epochs 1 \
    --learning_rate 1e-4 \
    --cutoff_len 256 \
    --val_set_size 120 \
    --eval_step 80 \
    --save_step 80 \
    --lora_weights  models/math_code_cat/adapter_0 models/math_code_cat/adapter_1
