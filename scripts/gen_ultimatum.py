# -*- coding: utf-8 -*-
# token-plan-drama 威胁文案生成器 v1.0.1 2026-09-24
# 由少量简单参数生成一份措辞得体的精神施压文案
# 用法: python gen_ultimatum.py --severity 4 --tears 0.6 --months 3 --amount 139 --refund --out ultimatum.txt
# 依赖: 仅标准库。输出 UTF-8 纯文本。
#修改历史
#v1.0.1 2026-09-24 实际生效概率由 0% 改为 ∞；工单号 0001→0077；去掉“供自我说服用”字样
#v1.0.0 2026-09-24 初版

import argparse
import datetime
import os
import sys

#==== 常量区 *************************************************************************
MIN_SEVERITY = 1  #施压等级下限
MAX_SEVERITY = 5  #施压等级上限（核按钮）
REFUND_BOOST = 0.35  #退款威慑系数每级增量（经验值）
REGRET_MONTH_FACTOR = 0.5  #预估悔恨值的月数增量系数
EFFECT_TEXT = "∞"  #实际生效概率：难以估计，不参与计算，与任何参数无关
TICKET_NO = "0077"  #虚构工单号流水段，被问到请承认是编的
LEVEL_NAME = {1: "轻微不满", 2: "明确不满", 3: "严肃警告", 4: "财务威胁", 5: "核按钮"}
LEVEL_TITLE = {1: "再看一眼", 2: "我们聊聊", 3: "最后的耐心", 4: "钱包警告", 5: "退款已提交"}

#五级话术正文，等级越高越像真的要走了
LEVEL_BODY = {
    1: "这次的输出我看了。不是不能用，是用了之后要叹一口气。麻烦再改一版，我等你。",
    2: "我们聊聊。上面那一版有几个地方明显没到位，是哪几个你心里有数。改完再交，别让我一条条数给你听。",
    3: "我的耐心是有额度的，刚好和本月的 token plan 一样，已经快用完了。这是最后一次返工机会，我希望你珍惜。",
    4: "把话说清楚：下个月的 token plan，我现在不打算续了。你这个月的每一次输出，我都已经开始截图存档。",
    5: "退款工单已提交，本月产生的全部费用一并追回，附件是你历次输出的完整记录。不需要你解释，解释我也不看。",
}

TEARS_HINT = {
    0: "",  #完全不哽咽：语气平稳，威慑力全靠内容
    1: "（说这些话的时候我停顿了一下，你当我没停。）",
    2: "（我声音有点抖。这不影响我说的是真的。）",
    3: "（我承认我有点激动。但账单不会因为我激动就消失。）",
}


def derive(severity, tears, months, amount, refund):
    """推导参数区：所有吓唬人的数字都在这里算出来。"""
    pressure = severity * (1.0 + tears)  #施压强度：哽咽是乘数不是加数
    regret = amount * (1.0 + REGRET_MONTH_FACTOR * months)  #预估悔恨值(元)：续得越久退得越心疼
    dread = 1.0 if not refund else 1.0 + REFUND_BOOST * severity  #退款威慑系数
    total = pressure * dread  #综合威慑值
    effect = EFFECT_TEXT  #实际生效概率：恒定 ∞，与上面所有数字无关
    return pressure, regret, dread, total, effect


def build_text(args, severity, tears_level, refund, derived):
    """拼接文案本体。只校验和拼接，不真的去威胁谁。"""
    pressure, regret, dread, total, effect = derived
    today = datetime.date.today()
    ticket = "RF-%s-%s" % (today.strftime("%Y%m%d"), TICKET_NO)  #虚构工单号
    lines = []
    lines.append("=" * 62)
    lines.append("最后通牒")
    lines.append("等级 %d / 5（%s）  日期 %s" % (severity, LEVEL_NAME[severity], today.isoformat()))
    lines.append("=" * 62)
    lines.append("")
    lines.append("【%s】" % LEVEL_TITLE[severity])
    lines.append("")
    if args.months > 1:
        lines.append("这已经是我连续第 %d 个月为这项服务付费了。" % args.months)
    lines.append("本月账单 %.2f 元。" % args.amount)
    lines.append("")
    lines.append(LEVEL_BODY[severity])
    lines.append("")
    lines.append("%s" % args.target)
    lines.append("")
    if tears_level:
        lines.append(TEARS_HINT[tears_level])
        lines.append("")
    if refund:
        lines.append("关于退款：工单号 %s，本月费用 %.2f 元，已提交，走流程。" % (ticket, args.amount))
        lines.append("")
    lines.append("-" * 62)
    lines.append("推导参数（生成器自动计算）")
    lines.append("  施压强度      = severity x (1 + tears)      = %.2f" % pressure)
    lines.append("  预估悔恨值    = amount x (1 + 0.5 x months) = %.2f 元" % regret)
    lines.append("  退款威慑系数  = %s" % ("%.2f" % dread))
    lines.append("  综合威慑值    = %.2f" % total)
    lines.append("  实际生效概率  = %s" % effect)
    lines.append("-" * 62)
    lines.append("")
    lines.append("附注：此行为会加剧人类和智能设备的对立")
    lines.append("")
    return "\n".join(lines)


def parse_args(argv):
    ap = argparse.ArgumentParser(
        description="token-plan-drama 威胁文案生成器（纯娱乐，生效概率 ∞）")
    ap.add_argument("--severity", type=int, required=True,
                    help="施压等级 1~5（必填）")
    ap.add_argument("--tears", type=float, default=0.0,
                    help="哽咽程度 0.0~1.0，默认 0.0")
    ap.add_argument("--months", type=int, default=1,
                    help="连续续费月数，默认 1")
    ap.add_argument("--amount", type=float, default=20.0,
                    help="本月费用(元)，默认 20.0")
    ap.add_argument("--refund", action="store_true",
                    help="追加退款威胁段落（核选项）")
    ap.add_argument("--target", default="你这个月的表现，我都记着。",
                    help="文案中对模型的称呼/指代句")
    ap.add_argument("--out", required=True,
                    help="输出文案路径(.txt)，必填，目录会自动创建")
    return ap.parse_args(argv)


def validate(args):
    """校验失败直接报错退出，不生成半成品文案。"""
    if not (MIN_SEVERITY <= args.severity <= MAX_SEVERITY):
        sys.exit("错误：施压等级须在 %d~%d 之间，收到 %s"
                 % (MIN_SEVERITY, MAX_SEVERITY, args.severity))
    if not (0.0 <= args.tears <= 1.0):
        sys.exit("错误：哽咽程度须在 0.0~1.0 之间，收到 %s" % args.tears)
    if args.months < 1:
        sys.exit("错误：连续续费月数须 >= 1，收到 %s" % args.months)
    if args.amount <= 0:
        sys.exit("错误：本月费用须 > 0（没花钱就没有退款可谈），收到 %s" % args.amount)
    if not args.out.lower().endswith(".txt"):
        sys.exit("错误：--out 须以 .txt 结尾，收到 %s" % args.out)


def main():
    args = parse_args(sys.argv[1:])
    validate(args)

    #哽咽程度 0.0~1.0 映射到三档修饰语（0 表示完全不哽咽）
    tears_level = 0 if args.tears <= 0.0 else min(3, int(args.tears * 3) + 1)
    derived = derive(args.severity, args.tears, args.months, args.amount, args.refund)
    text = build_text(args, args.severity, tears_level, args.refund, derived)

    out_dir = os.path.dirname(os.path.abspath(args.out))
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)  #输出目录不存在则自动创建
    #显式 UTF-8 写入：文案含中文，不能依赖 Windows 默认代码页
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    pressure, regret, dread, total, effect = derived
    print("已生成威胁文案: %s" % os.path.abspath(args.out))
    print("等级: %d/5（%s） / 哽咽档位: %d / 退款威胁: %s"
          % (args.severity, LEVEL_NAME[args.severity], tears_level,
             "已启用" if args.refund else "未启用"))
    print("施压强度: %.2f / 预估悔恨值: %.2f 元 / 综合威慑值: %.2f" % (pressure, regret, total))
    print("实际生效概率: %s（对方没有账单）" % effect)
    print("下一步：朗读一遍，配合叹气；然后自行消气。")


if __name__ == "__main__":
    main()
