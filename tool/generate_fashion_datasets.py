import os

# path for downloaded fashion images
from pathlib import Path
import shutil

root_dir = './data'
root_fashion_dir = os.path.join(root_dir, 'deepfashion')
assert len(root_fashion_dir) > 0, 'please give the path of raw deep fashion dataset!'

train_images = []
train_f = open(os.path.join(root_dir,'train.lst'), 'r')
for lines in train_f:
	lines = lines.strip()
	if lines.endswith('.jpg'):
		train_images.append(lines)

test_images = []
test_f = open(os.path.join(root_dir,'test.lst'), 'r')
for lines in test_f:
	lines = lines.strip()
	if lines.endswith('.jpg'):
		test_images.append(lines)

train_path = os.path.join(root_fashion_dir,'train')
if not os.path.exists(train_path):
	os.mkdir(train_path)

for item in train_images:
	from_ = os.path.join(root_fashion_dir, item)
	to_ = os.path.join(train_path, item)
	Path(to_).parent.mkdir(parents=True, exist_ok=True)
	shutil.copy(from_, to_)

test_path = os.path.join(root_fashion_dir,'test')
if not os.path.exists(test_path):
	os.mkdir(test_path)

for item in test_images:
	from_ = os.path.join(root_fashion_dir, item)
	to_ = os.path.join(test_path, item)
	Path(to_).parent.mkdir(parents=True, exist_ok=True)
	shutil.copy(from_, to_)

