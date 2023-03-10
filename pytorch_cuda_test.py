#!/sw/installed/Python/3.9.5-GCCcore-10.3.0/bin/python

import torch

print_list = []

print_list.append(str(torch.cuda.is_available()))
print_list.append(str(torch.cuda.device_count()))
print_list.append(str(torch.cuda.current_device()))
print_list.append(str(torch.cuda.get_device_name(0)))

#file_str = ('/workspace/pytorch_out.txt')
file_str = ('/home/zihlogin/llama_testen/pytorch_out.txt')

with open(file_str, 'w') as f:
    for print_line in print_list:
        f.write(f'{print_line}\n')

