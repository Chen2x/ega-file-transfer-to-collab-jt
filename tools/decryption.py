#!/usr/bin/env python

import os
import sys
import json
import time
from random import randint
import subprocess
from utils import get_task_dict, save_output_json


task_dict = get_task_dict(sys.argv[1])
cwd = os.getcwd()

"""
    input:
      input_file:
        type: string
        is_file: true
      ega_file_id:  # passing through
        type: string
      file_name:  # passing through
        type: string
      file_md5sum:  # passing through
        type: string
      object_id:  # passing through
        type: string
"""
input_file = task_dict.get('input').get('input_file')
ega_file_id = task_dict.get('input').get('ega_file_id')
file_name = task_dict.get('input').get('file_name')
file_md5sum = task_dict.get('input').get('file_md5sum')
object_id = task_dict.get('input').get('object_id')


task_start = int(time.time())

try:
    r = subprocess.check_output(['touch', file_name])
    
except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
    sys.exit(1)  # task failed


# complete the task
task_stop = int(time.time())

"""
    output:
      file:
        type: string
        is_file: true
      ega_file_id:  # passing through
        type: string
      file_name:  # passing through
        type: string
      file_size:  
        type: string
      file_md5sum:  # passing through
        type: string
      object_id:  # passing through
        type: string
"""

output_json = {
    'file': os.path.join(cwd, file_name),
    'ega_file_id': ega_file_id,
    'file_name': file_name,
    'file_size': os.path.getsize(file_name),
    'file_md5sum': file_md5sum,
    'object_id': object_id,
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
