# llama-hpc

## Access
ssh zihlogin@taurus.hrsk.tu-dresden.de  

## Create virtualenv within workspace
module load Python  
ws_allocate -F scratch python_virtual_environment 1  
virtualenv --system-site-packages /scratch/ws/0/zihlogin-python_virtual_environment/env  
source /scratch/ws/0/zihlogin-python_virtual_environment/env/bin/activate  

Then, terminal line should start like this: (env) zihlogin@tauruslogin6:~>

## Clone llama github repo
in home directory, type:  
git clone https://github.com/facebookresearch/llama.git  

## Load module Pytorch and CUDA 11
module load PyTorch/1.10.0-foss-2021a-CUDA-11.3.1  

## Test Pytorch and CUDA
copy ~/gitlab_mn/llama-hpc/pytorch_cuda_test.py  
and ~/gitlab_mn/llama-hpc/test_job_file.sh  
to /home/zihlogin/llama_testen auf Taurus  
cd into /home/zihlogin/llama_testen and execute:  
sbatch test_job_file.sh  
There should be an output file /home/zihlogin/llama_testen/pytorch_out.txt  

## Install llama
inside repo main folder:  
pip install -r requirements.txt  
pip install -e .  

## Test llama
copy ~/gitlab_mn/llama-hpc/llama_job_file.sh to /home/zihlogin/llama_testen  
cd into /home/zihlogin/llama_testen, then run:  
sbatch llama_job_file.sh  

## Notes
Generally, check jobs using:  
squeue -u zihlogin  


