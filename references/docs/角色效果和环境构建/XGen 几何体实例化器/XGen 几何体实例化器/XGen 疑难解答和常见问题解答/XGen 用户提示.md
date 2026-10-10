# XGen 用户提示

以下部分包含您可以在 XGen 工作流中使用的提示。

## UV 补偿

当您使用属性补偿时，模型中的面有时会不能正确对齐。例如，可以设置“倾斜 V = 1”(Tilt V = 1)（在表达式中使用时 OffU），所有基本体将不会指向同一方向。不能对齐的原因是 XGen 使用派生于 CV 缠绕顺序的模型的内在参数化。

您可以准备模型，使其内部的 UV 看起来像是从面到面任意排序的。大多数情况下，您也可以使用一些表达式来对此作出补偿。

要补偿不对齐的面，请执行下列操作：

1. 输入以下三个表达式作为全局表达式（请参见[表达式(Expressions)](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharEffEnvBuild/files/GUID-FE4C8CB8-E577-4BFC-A252-627CB32D3837.htm)）：

  ```text
float upOrDown: (abs(dot(norm($dPdv),[0,1,0]))>0.6 || abs(dot(norm($dPdu),[0,1,0]))>0.6)? 1 : 0
float flipY:      (abs(dot(norm($dPdu),[0,1,0]))>0.6)?90 : 0
float flipZ:      (abs(dot(norm($dPdu),[0,0,1]))>0.6)?90 : 0
```

2. 在“扭曲属性”(Twist Attribute)字段中输入以下内容：

  ```text
twist: upOrDown() ? flipY() :flipZ()
```

## 旋转朝向摄影机

要使基本体仅绕法线旋转，以朝向摄影机，请执行以下操作：

要旋转基本体以朝向摄影机：

1. 在“基本体”(Primitives)选项卡的“卡片”(Card)属性中输入：

  ```text
length: 0.3
width:  1.0
offV:   1.0
aboutN: $eye=norm($cam-$P);$ang=acosd(dot( $eye,[0,0,1])); $axis=cross([0,0,1],$eye); dot($axis,$N)>0 ?$ang : -$ang
```

2. 在“样条线”(Spline)属性中输入：

  ```text
length:   0.3
width:    1.0
bendV[0]: 1.0
aboutN:   $eye=norm($cam-$P);$ang=acosd(dot( $eye,[0,0,1])); $axis=cross([0,0,1],$eye); dot($axis,$N)>0 ?$ang : -$ang
```

## 修饰草地

在修饰长满草的大型区域时，请将“控制使用”(Control using)设置为“属性”(Attribute)，以控制基本体各个分段的噪波。可在无需创建导向的情况下创建属性驱动的描述：这样也可以设置默认的表达式，从而使其不需要导向。
