# nHair 疑难解答

以下是对您在使用头发时可能会遇到的问题的解决方法。

## 使用“NURBS 曲线”(NURBS Curves)输出时头发模拟速度较慢

如果您在创建头发时将“输出”(Output)设定为“NURBS 曲线”(NURBS Curves)并创建了大量的头发，模拟进行初始化的速度可能较慢。解决方法是将“输出”(Output)设定为“Paint Effects 和 NURBS 曲线”(Paint Effects and NURBS Curves)并在运行模拟时隐藏曲线。

## “锁定长度”(Lock Length)启用时，“撤消”不起作用

在 NURBS 曲线中使用“锁定长度”(Lock Length)时，“撤消”不能正确工作。解决方法是稍微移动 CV，然后启用“锁定长度”(Lock Length)。

## 播放期间散乱而晃动的毛发

播放头发模拟时，如果头发散乱或无法松弛，则您可以执行下列任一操作：

- 首先，请在“属性编辑器”(Attribute Editor)中尝试调整 hairSystemShape 的“动力学特性”(Dynamic Properties)区域中的“阻尼”(Damp)。

- 针对 Nucleus 节点，增加“子步”(Substeps)值。

- 选择头发曲线，然后在其 follicleShape 节点中，将“模拟方法”(Simulation Method)更改为“被动”(Passive)。被动曲线对相邻的活动曲线的行为插值。
