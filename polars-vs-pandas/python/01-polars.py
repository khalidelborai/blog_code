import polars as pl
import pyperf
runner = pyperf.Runner()

# Load the dataset
def load_dataset(filename):
    df = pl.read_csv(filename)
    return df

runner.bench_func('load_dataset', load_dataset, 'data/dataset.csv')
