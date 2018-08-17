
# set the path-to-files
TRAIN_FILE = "./data/train.csv"
TEST_FILE = "./data/test.csv"

SUB_DIR = "./output"


NUM_SPLITS = 3
RANDOM_SEED = 2017

# types of columns of the dataset dataframe
CATEGORICAL_COLS = ['category_'+str(i).zfill(3) for i in range(23,321)]

NUMERIC_COLS =['value_'+str(i).zfill(3) for i in range(0,23)]

IGNORE_COLS = ["id", "target"]
