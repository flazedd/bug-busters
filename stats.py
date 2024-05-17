import json
from utility import utils
from config import constant
from datetime import datetime
from config.constant import ORACLES

# def get_stats(folder, file_name, test_name):
#     utils.set_pitest_in_gradle(folder, file_name, test_name)
#     result = utils.exec_pitest()
#     return utils.get_statistics(result)


# def percentage_improvement(a, b):
#     improvement = ((b - a) / a) * 100
#     return improvement


# args = utils.get_args()
# print(args)
obj = {}

for oracle in ORACLES:
    print(f'[+] Current oracle: {oracle}')
    key = oracle.__str__()
    obj[key] = oracle.get_dict()
    # for arg in oracle.get_args():
    #     print(arg)
    #     folder = arg[0]
    #     file_name = arg[1]
    #     oracle.get_dict()

utils.save_results(obj, constant.JSON_NAME)

# {'Line coverage %': find_numbers_before_percent(part1),
#                   'Mutations killed %': find_numbers_before_percent(part2),
#                   # 'Mutations': find_numbers_before_percent(part3)
#                   }

# Example arg instance: ('templateit_5', 'OpMatcher', 1)
# for arg in args:
#     folder = arg[0]
#     file_name = arg[1]
#     stats_baseline = get_stats(folder, file_name, file_name + 'Test')
#     stats_improved = get_stats(folder, file_name, file_name + 'Test_Improved')
#
#     improvement_lc = percentage_improvement(stats_baseline['Line coverage %'], stats_improved['Line coverage %'])
#     improvement_lcp = stats_improved['Line coverage %'] - stats_baseline['Line coverage %']
#     improvement_mk = percentage_improvement(stats_baseline['Mutations killed %'], stats_improved['Mutations killed %'])
#     improvement_mkp = stats_improved['Mutations killed %'] - stats_baseline['Mutations killed %']
#
#     local = {}
#     local.setdefault('Improvement', {})
#     local.setdefault('Baseline_test', {})
#     local.setdefault('Improved_test', {})
#     local['Improvement']['Line coverage'] = {'%p': improvement_lcp, '%': improvement_lc}
#     local['Improvement']['Mutations killed'] = {'%p': improvement_mkp, '%': improvement_mk}
#     local['Baseline_test']['Line coverage'] = {'%p': stats_baseline['Line coverage %']}
#     local['Baseline_test']['Mutations killed'] = {'%p': stats_baseline['Mutations killed %']}
#     local['Improved_test']['Line coverage'] = {'%p': stats_improved['Line coverage %']}
#     local['Improved_test']['Mutations killed'] = {'%p': stats_improved['Mutations killed %']}
#     obj.setdefault(folder, {})
#     obj[folder][file_name] = local
#
# save_results(obj, constant.JSON_NAME)
