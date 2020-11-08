from imports import *
from paths import *
from utils import *
from experiment import Experiment

logger = logging.getLogger()
logger.setLevel(logging.INFO)
NUM_WORKERS = 8 if torch.cuda.is_available() else 0


def main(h, run_num, seed, exp_params):
    logger.info("Running main func")
    logger.debug("Debug print")
    np.random.seed(seed)
    torch.manual_seed(seed)

    return {'metric1': np.random.rand(), 'metric2': np.random.rand()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-seed', type=int)
    parser.add_argument('-suffix')
    parser.add_argument('-debug', action='store_true')
    parser.add_argument('-num_runs', type=int)
    parser.add_argument('-same_seed', action='store_true')
    parser.add_argument('-hp', nargs='*')
    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)

    hparams = dict(
        bs=8
    )
    exp = Experiment(main_exp=main, hparams_exp=hparams, cli_args=args, exp_name='experiment')
    exp.run()
    exp.log_results()
    exp.summarize_results()
