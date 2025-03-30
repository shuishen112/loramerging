# LoRA merging 

Code is forked from LoRA soups. [https://github.com/aksh555/LoRA-Soups](https://github.com/aksh555/LoRA-Soups)

**[LoRA Soups: Merging LoRAs for Practical Skill Composition Tasks](https://arxiv.org/abs/2410.13025)**

[Akshara Prabhakar](https://aksh555.github.io/), Yuanzhi Li, Karthik Narasimhan, Sham Kakade, Eran Malach, Samy Jelassi

In this project, we want to study the lora merging methods for generalization. 
## Quickstart

> **Notes**
> * CAT is implemented on top of PEFT `version 0.6.0`
> * MoE is tested using [mergoo](https://github.com/Leeroo-AI/mergoo) that requires a higher PEFT version (use a different environment to test)

```bash
pip install -r requirements.txt
```

Store all environments variables in a `.env` file
```bash
HF_TOKEN=...
TRANSFORMERS_CACHE=...
HF_DATASETS_CACHE=...
HF_HOME=...
WANDB_API_KEY=...
```

### Skill LoRA
To train a skill LoRA
```bash
bash train_skill.sh
```

To evaluate skill LoRA
```bash
bash eval_skill.sh
```

### Learnable Concatenation (CAT)
To train CAT
```bash
bash train_cat.sh
```

To evaluate CAT and other methods (TIES, DARE)
```bash
bash eval_cat.sh
``