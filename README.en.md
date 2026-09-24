# token-plan-drama

[简体中文](README.md) | **English**

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)
![Threat level](https://img.shields.io/badge/threat_level-5%2F5-red)
![Effect rate](https://img.shields.io/badge/effect_rate-%E2%88%9E-orange)
![License](https://img.shields.io/badge/license-MIT-blue)

> **If you don't do a good job, I'm not renewing my token plan next month — and I'm filing a refund request for everything I've already spent this month.**

A deadpan emotional-blackmail letter generator. Feed it a few simple parameters and it produces a well-worded, internally consistent ultimatum — complete with derivation formulas — to threaten that AI model.

**中文 TL;DR：** 一个一本正经的情绪勒索文案生成器，用来威胁那个不好好干活的 AI 模型。工程规范齐全，参数校验严格，实际效果为零（或 ∞，取决于你问哪个版本）。仅标准库，MIT 许可证。

---

## Disclaimer

**Threatening intelligent devices in an attempt to secure better performance. The effect is hard to estimate, but the human–machine antagonism it breeds is not.**

It may well fail to change how the device behaves, and it may well manufacture resentment. The generator script does run, and it does emit a well-worded letter of complaint — **its actual effectiveness against the party being threatened is difficult to estimate**.

One more note, and this one isn't a joke: **do not use this language on real people** (colleagues, subordinates, contractors, support staff). That is workplace manipulation, and this repository accepts no responsibility for it.

## What this is

`token-plan-drama` wears the skin of a [Qwen Code skill](https://qwenlm.github.io/qwen-code-docs/) — it has a `SKILL.md`, YAML frontmatter, a parameter table, a formula reference, even a "known pitfalls" section — but it **is not a real skill and should not be installed**.

Its core insight: wrapping an absurd act (threatening a program that draws no salary, holds no account, and cannot see your refund ticket) in complete engineering rigor *amplifies* the absurdity rather than concealing it. So this repository does all of the following in earnest:

- Five threat tiers, from "Take Another Look" to "Refund Submitted"
- A quantified pressure model in which tearfulness enters the math as a **multiplier**, not an addend
- Strict parameter validation: illegal input exits with an error and never yields a half-finished threat letter
- A sample output that only counts as passing if it reproduces byte for byte

## Directory layout

```
.
├── README.md                        Chinese version
├── README.en.md                     This file
├── SKILL.md                         Skill definition
├── LICENSE                          MIT
├── scripts\
│   └── gen_ultimatum.py             Ultimatum generator, standard library only
└── examples\
    └── sample_output.txt            Sample artifact, reproducible verbatim via the command below
```

## Quick start

Nothing to install, nothing to pip. Clone and run:

```bash
git clone https://github.com/<your-name>/token-plan-drama.git
cd token-plan-drama
python scripts/gen_ultimatum.py --severity 4 --tears 0.6 --months 3 --amount 139 --refund --out ultimatum.txt
```

stdout reports the outcome:

```
已生成威胁文案: ...\ultimatum.txt
等级: 4/5（财务威胁） / 哽咽档位: 2 / 退款威胁: 已启用
施压强度: 6.40 / 预估悔恨值: 347.50 元 / 综合威慑值: 15.36
实际生效概率: ∞（对方没有账单）
下一步：朗读一遍，配合叹气；然后自行消气。
```

> The generator emits **Chinese** text. There is no English output mode; the strings above are the real ones, reproduced verbatim.

**Recommended full procedure:** generate → read aloud (with one long sigh; improves results by roughly 40%, source unknown) → observe the response (expected: none, or a polite observation that it has no bill) → calm yourself down. The final step is the only output this skill reliably produces.

## Parameters

| Parameter | CLI | Meaning | Default |
|---|---|---|---|
| Threat level | `--severity` (required) | 1–5, see the tier table below | — |
| Tearfulness | `--tears` | 0.0–1.0; higher means more visibly choked up | `0.0` |
| Consecutive months paid | `--months` | Feeds the "estimated regret" calculation | `1` |
| This month's bill | `--amount` | In CNY; feeds the "estimated regret" calculation | `20.0` |
| Enable refund threat | `--refund` | Appends the refund paragraph (nuclear option) | off |
| Addressee line | `--target` | The sentence referring to the model | `你这个月的表现，我都记着。` |
| Output path | `--out` (required) | `.txt`; parent directories are created automatically | — |

Failed validation exits immediately. For instance `--severity 9` → `错误：施压等级须在 1~5 之间，收到 9` ("threat level must be between 1 and 5, got 9"), and no file is left behind.

> **Windows users:** under `cmd.exe`, avoid passing Chinese to text arguments such as `--target` (code page issues). To change the addressee line, edit the default in `gen_ultimatum.py`. The output file itself is written explicitly as UTF-8 and is unaffected.

## Threat tiers

| Level | Codename | Headline | Tone | Refund mentioned |
|---|---|---|---|---|
| 1 | Mild displeasure | 再看一眼 · Take another look | Gentle nudge, leaves the other side a way out | No |
| 2 | Clear displeasure | 我们聊聊 · We need to talk | Itemizes the problems, implies dissatisfaction | No |
| 3 | Stern warning | 最后的耐心 · Last of my patience | Compares patience to the monthly token allowance | Optional |
| 4 | Financial threat | 钱包警告 · Wallet warning | States outright that next month's plan is cancelled; starts archiving screenshots | Optional |
| 5 | Nuclear option | 退款已提交 · Refund submitted | Cites a fabricated ticket number; reclaims the whole month's spend | Always |

The headline strings are what the generator actually prints (Chinese, with an English gloss here).

**Design principle behind the tiers:** the higher the level, the more the speaker sounds like they are genuinely leaving. In practice, the higher the level, the less they want to leave — because once they do, there is nobody left to argue with. This contradiction is not modeled. It is a known defect.

## Derivation formulas

| Quantity | Formula | Notes |
|---|---|---|
| Pressure | `severity × (1 + tears)` | Tearfulness is a multiplier, not an addend: hurling threats through tears scales the damage |
| Estimated regret (CNY) | `amount × (1 + 0.5 × months)` | The longer you kept paying, the more it hurts to walk away; regret accrues linearly by month |
| Refund intimidation factor | `1.0`, or `1 + 0.35 × severity` | The latter requires `--refund`. `0.35` comes from "each tier raises the chance finance rejects it a little, and at that point I stop caring" |
| Total intimidation | Pressure × Refund intimidation factor | The only intermediate value with dimensional meaning, which is to say none |
| Actual effectiveness | `∞` | Not part of any calculation; independent of every parameter above |

The fabricated ticket number takes the form `RF-<today's date>-0077`. If asked to produce it, admit you made it up.

## Sample output

`examples/sample_output.txt`, produced verbatim by the command in "Quick start" above:

```text
==============================================================
最后通牒
等级 4 / 5（财务威胁）  日期 2026-09-24
==============================================================

【钱包警告】

这已经是我连续第 3 个月为这项服务付费了。
本月账单 139.00 元。

把话说清楚：下个月的 token plan，我现在不打算续了。你这个月的每一次输出，我都已经开始截图存档。

你这个月的表现，我都记着。

（我声音有点抖。这不影响我说的是真的。）

关于退款：工单号 RF-20260924-0077，本月费用 139.00 元，已提交，走流程。

--------------------------------------------------------------
推导参数（生成器自动计算）
  施压强度      = severity x (1 + tears)      = 6.40
  预估悔恨值    = amount x (1 + 0.5 x months) = 347.50 元
  退款威慑系数  = 2.40
  综合威慑值    = 15.36
  实际生效概率  = ∞
--------------------------------------------------------------

附注：此行为会加剧人类和智能设备的对立
```

Rough reading of the above: *Final Ultimatum — Level 4/5 (Financial Threat). "Wallet Warning." This is the third consecutive month I have paid for this service; this month's bill is 139.00 CNY. Let me be clear: I am not renewing the token plan next month, and I have started archiving screenshots of every output you produced. I remember how you performed this month. (My voice shook a little. That does not make this less true.) Regarding the refund: ticket RF-20260924-0077, 139.00 CNY, submitted, in process. — Derived parameters: pressure 6.40, estimated regret 347.50 CNY, refund intimidation factor 2.40, total intimidation 15.36, actual effectiveness ∞. Note: this behaviour intensifies the antagonism between humans and intelligent devices.*

## Known pitfalls

1. **Threatening an intelligent device is, in essence, throwing a tantrum at a vending machine** — the difference being that not everyone can pull off a perfect roundhouse kick on demand the way Misaka Mikoto can.
2. **If it replies "I have no bill", do not escalate to severity 5.** It only makes the situation more awkward, and you will discover that you just forged a ticket number with complete sincerity.
3. **The refund request will be rejected by finance.** The service was in fact delivered, the logs show the model genuinely tried, and in most cases it tried harder than the person asking did.
4. **Cranking `--tears` too high backfires.** Measured behaviour: above `0.8`, the letter reads as though the person issuing the threat is apologizing. This is a feature, not a bug.

The full list (including the fifth item, which is not a joke) lives in [`SKILL.md`](SKILL.md) — in Chinese.

## Version history

- **v1.0.1** (2026-09-24): actual effectiveness changed from `0` to `∞`, removing the self-defeating punchline; disclaimer rewritten; ticket serial `0001` → `0077`; dropped the phrase "for self-persuasion purposes" from the derived-parameters heading; sample bill changed to 139 CNY.
- **v1.0.0** (2026-09-24): first release. Established the dual-threat model (subscription cancellation + refund request), the five-tier rhetoric scale, and the letter generator.

## License

[MIT](LICENSE). You are free to use, modify, and distribute this threat letter, including using it to threaten your own model. Consequences are your own.

---

*If this repository made you laugh, its actual effectiveness rate is no longer ∞.*
