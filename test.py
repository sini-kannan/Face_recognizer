import h5py

model_file_path = 'models/model.h5'
try:
    with h5py.File(model_file_path, 'r') as f:
        # Print keys to see the structure of the file
        print("Keys in model file:", list(f.keys()))
except IOError:
    print("Error: Unable to open model file.")