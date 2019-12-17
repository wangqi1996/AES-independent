# encoding=utf-8

def get_parser():
    args_parser = ArgumentParser()

    args_parser.add_argument('--config_file', '-c',
                             default='/home/user_data55/wangdq/code/AES-bert/src/config/config.yml', type=str)
    args_parser.add_argument('--train', action="store_true", default=False)
    args_parser.add_argument('--eval', action="store_true", default=False)
    args_parser.add_argument('--load', action="store_true", default=False)  # 从checkpoint中恢复
    args_parser.add_argument('--set_id', type=int, default=1)  # 1-8
    args_parser.add_argument('--batch_size', type=int, default=32)
    args_parser.add_argument('--model_name', default='xlnet', type=str)

    return args_parser


CONFIG_FILE_MAPPING = {
    'config.yml':'/home/user_data55/wangdq/code/AES-bert/src/config/config.yml',
    'lstm_config.yml': '/home/user_data55/wangdq/code/AES-bert/src/config/lstm_config.yml',
    'bert_config.yml': '/home/user_data55/wangdq/code/AES-bert/src/config/bert_config.yml'

}
def parse_args(parser):
    args = parser.parse_args()
    if args.config_file == 'config.yml':
        args.config_file = '/home/user_data55/wangdq/code/AES-bert/src/config/config.yml'
    elif args.config_file == 'lstm_config.yml':
        args.config_file = '/home/user_data55/wangdq/code/AES-bert/src/config/lstm_config.yml'
    elif args.config_file == 'bert_config.yml':
        args.config_file = '/home/user_data55/wangdq/code/AES-bert/src/config/bert_config.yml'
    if args.config_file:
        data = yaml.load(open(args.config_file))
        arg_dict = args.__dict__
        for key, value in data.items():
            if isinstance(value, list):
                arg_dict[key] = []
                for v in value:
                    arg_dict[key].append(v)
            else:
                arg_dict[key] = value
    return args
