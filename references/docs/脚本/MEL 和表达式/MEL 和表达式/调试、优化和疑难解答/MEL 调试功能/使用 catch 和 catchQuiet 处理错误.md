# 使用 catch 和 catchQuiet 处理错误

[catch](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/catch.html) 语句将对一个表达式求值，并在表达式出现错误，但不会停止脚本时返回 true（如 catch 之外的错误）。

这允许您测试 if 语句中的指定或命令的执行，并在 catch 返回 true 时运行错误处理代码。

```text
int $divisor = 0;
if ( catch ($factor = 42/$divisor) ) {
 print "Attempt to divide by zero caught\n";
}
```

当 MEL 在 catch 语句内遇到除以零错误时，它会自动打印错误消息，但不会停止执行。catch 语句将返回真 true，因此 if 语句将执行块。

若要捕捉错误而无需 MEL 自动打印错误，请使用 [catchQuiet](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-Tech-Docs/Commands/catchQuiet.html) 语句，而不是 catch 语句。
