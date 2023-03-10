#!/bin/bash

#SBATCH --nodes=1
#SBATCH --mincpus=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=2000
#SBATCH --gres=gpu:1
#SBATCH --time=00:05:00
#SBATCH --partition=alpha

srun torchrun --nproc_per_node 1 /home/zihlogin/llama/example.py --ckpt_dir $TARGET_FOLDER/model_size --tokenizer_path $TARGET_FOLDER/tokenizer.model

