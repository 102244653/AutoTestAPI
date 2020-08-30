import argparse

from src.execute import *
from src.hleper.send_email import send_email
from src.result_module.creat_excel_report import creat_excel_report
from src.result_module.creat_html_report import creat_html_report

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='接口自动化测试')
    parser.add_argument("--evn", type=str, default="sit")
    parser.add_argument("--html", type=bool, default=True)
    parser.add_argument("--excel", type=bool, default=True)
    parser.add_argument("--email", type=bool, default=True)
    args = parser.parse_args()
    case_suit = read_suit_case()
    for suit in case_suit:
        table_name, case_list = read_case_by_table(args.evn, suit)
        execute_case(table_name, case_list)
    if args.html:
        creat_html_report()
    if args.excel:
        creat_excel_report()
    if args.email:
        send_email()