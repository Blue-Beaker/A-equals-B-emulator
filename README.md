# A=B emulator

An emulator for [A=B](https://store.steampowered.com/app/1720850/AB), written in python 3, mainly to test programs for the game more efficiently.  

Benefits:
- Runs faster than in-game
- You can use your favourite feature-rich text editor directly
- Test your program with a bunch of random strings at a time

Usage 1: `aequalsb.py [Program] [Input string]`  
Program is a raw text file with the A=B program. There is a "demo.aeqb" and "multiply.aeqb" for example.  
Input String can't contain spaces.

Usage 2: Make another python script to generate random inputs to test your program.  
- look at the example: [multitest.py](multitest.py) (Spoiler-warning: contains a solution to a puzzle in the game).  
    Success runs will show as green.  
    Failed runs shows as red and show all logs.  

If the logs are too long to display in terminal, you can redirect them to a text file, by appending ` > output.txt` to yout command line. It's a feature of your shell program, not of this script.


# A=B 模拟器

一个用python3写的 [A=B](https://store.steampowered.com/app/1720850/AB) 模拟器, 主要用于更有效率地调试游戏中的程序.  

优点:
- 比游戏中的解释器运行得更快
- 可以直接使用你自己的文本编辑器
- 一次用一堆随机输入测试你的程序

用法 1: `aequalsb.py [程序] [输入字符串]`  
程序是一个包含A=B程序的纯文本文件. 包含示例程序 "demo.aeqb" 和 "multiply.aeqb" .  
输入字符串不可包含空格.

用法 2: 编写另一个python脚本生成随机输入来测试你的程序.  
- 示例: [multitest.py](multitest.py) (剧透使用).  
    成功的运行显示为绿色.  
    失败的运行显示为红色,且输出所有日志.  

如果日志太长无法在终端完整显示, 可以将输出重定向到一个文本文件, 只需将 ` > output.txt` 加到命令末尾. 这是 shell 程序的功能, 不是本脚本的功能.