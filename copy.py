import os
import random

# Set the base directory
base_dir = "cross-view/datasets/argoverse/argoverse-tracking/train3"
sequence_id = "2bc6a872-9979-3493-82eb-fb55407473c9"
subdir = "road_gt_copy"

# Full path to the directory containing the PNGs
full_dir = os.path.join(base_dir, sequence_id, subdir)

# Output paths
train_file = "cross-view/splits/argo/train_files.txt"
val_file = "cross-view/splits/argo/val_files.txt"

# Get all .png files in the directory
png_files = [f for f in os.listdir(full_dir) if f.endswith(".png")]

# Generate full relative paths
relative_paths = [f"argoverse-tracking/train3/{sequence_id}/{subdir}/{f}" for f in png_files]

# Shuffle and split
random.shuffle(relative_paths)
split_index = int(0.8 * len(relative_paths))
train_paths = relative_paths[:split_index]
val_paths = relative_paths[split_index:]

# Write to train_files.txt
with open(train_file, 'w') as tf:
    for path in train_paths:
        tf.write(path + '\n')

# Write to val_files.txt
with open(val_file, 'w') as vf:
    for path in val_paths:
        vf.write(path + '\n')

print(f"Written {len(train_paths)} entries to train_files.txt and {len(val_paths)} to val_files.txt.")
