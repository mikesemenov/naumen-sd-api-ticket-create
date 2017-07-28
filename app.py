import sys
from utils import create_parser, post_servicecall
from createcalls import run_call, run_av_check, run_new_task
import constants

# Выхов обработчика команд
parser = create_parser()
namespace = parser.parse_args(sys.argv[1:])
print(namespace)


# Обработка полученных команд
if namespace.command == 'phonecall':
    run_call(namespace)
elif namespace.command == 'avcheck':
    run_av_check(namespace)
elif namespace.command == 'newticket':
    run_new_task(namespace)


