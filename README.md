# CPU EMULATOR
This is emulator help me run code that will be running on my digital logic simulated a 4 bit cpu I built
![image](https://github.com/newor0599/worline-emu/assets/114163256/2624d419-00fc-4c40-91cf-8748621f124b)

(Digital logic simulator by [GGBRW](https://github.com/GGBRW/BOOLR))

## Operation code
| OP CODE | Args       | NAME | ICON DESC          | DESC
| ------- | ---------- | ---- | ------------------ | --------------------------|
| 0000    | Output loc | ADD  | 󰬈 +󰬉 ->           | Reg A + B to Ram          |
| 0001    | Output loc | SUB  | 󰬈 -󰬉 ->           | Reg A - B to Ram          |
| 0010    | NONE       | WRA  |  -> 󰬈             | Ram to Reg A              |
| 0011    | NONE       | WRB  |  -> 󰬉             | Ram to Reg B              |
| 0100    | Const      | WRR  |  ->              | Const to Ram              |
| 0101    | Const      | WRP  |  -> 󰕟             | Const to ram pointer      |
| 0110    | Ram loc    | WRO  |  ->              | Write output reg          |
| 0111    |            |      |                    |                           |
| 1000    |            |      |                    |                           |
| 1001    |            |      |                    |                           |
| 1010    |            |      |                    |                           |
| 1011    |            |      |                    |                           |
| 1100    |            |      |                    |                           |
| 1101    | Const      | JMP  |  -> 󰆙             | Jump to const             |
| 1110    | Const      | JON  | if negative  -> 󰆙 | Jump to const if negative |
| 1111    | NONE       | HLT  |                   | STOP ALL                  |

## TODO
- [ ] Emulator compiler
- [ ] Better output
- [ ] Clean up code
