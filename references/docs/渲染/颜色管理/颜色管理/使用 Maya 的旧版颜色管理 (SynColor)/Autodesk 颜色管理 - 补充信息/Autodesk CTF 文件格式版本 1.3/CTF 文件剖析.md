# CTF 文件剖析

变换格式允许编写者定义任意颜色运算符（也称为处理节点）链。可用运算符类型集包括 1D LUT、3D LUT、矩阵以及下面定义的其他类型。此格式以 XML 编写，因此用户可读。

下面是一个示例：

```text
<?xml version="1.0" encoding="UTF-8"?>
<ProcessList id="7401489a-9e4d-441d-a8b7-795739801f4e" name="ACES to HD" version="1.2">
    <Info>
        <Copyright>Copyright 2013 Autodesk, Inc.  All rights reserved.</Copyright>
        <Release>2013.3.pr27</Release>
    </Info>
    <Description>ACES Reference Rendering Transform + HD video Output Device Transform</Description>
    <Description>aces_dev version 0.1.1</Description>
    <InputDescriptor>Academy Color Encoding Specification (ACES)</InputDescriptor>
    <OutputDescriptor>HD (Rec 709) video</OutputDescriptor>
    <LUT1D halfDomain="true" inBitDepth="32f" outBitDepth="32f" rawHalfs="true">
        <Array dim="65536 1">
    0
    1
    1

    <!-- 65533 lines omitted -->

        </Array>
    </LUT1D>
    <Matrix inBitDepth="32f" outBitDepth="32f">
        <Array dim="3 3 3">
 0.9259999990  0.0379999988  0.0359999985
 0.1299999952  0.8000000119  0.0700000003
-0.0350000001 -0.0350000001  1.0700000525
        </Array>
    </Matrix>
    <LUT1D halfDomain="true" inBitDepth="32f" outBitDepth="32f" rawHalfs="true">
        <Array dim="65536 1">
    0
    0
    0

    <!-- 65533 lines omitted -->

       </Array>
    </LUT1D>
    <LUT3D inBitDepth="32f" interpolation="tetrahedral" outBitDepth="32f">
        <Array dim="48 48 48 3">
 0.000669299  0.000704187  0.000766901
 0.001848371  0.001297010  0.010368987
 0.002599007  0.001144927  0.023227118

        </Array>
    </LUT3D>
    <Gamma inBitDepth="32f" outBitDepth="32f" style="moncurveFwd">
        <GammaParams gamma="2.600000000000000" offset="0.050000" />
    </Gamma>
    <Matrix inBitDepth="32f" outBitDepth="32f">
        <Array dim="3 3 3">
 3.2409698963 -1.5373831987 -0.4986107647
-0.9692436457  1.8759675026  0.0415550582
 0.0556300804 -0.2039769590  1.0569715500
        </Array>
    </Matrix>
    <Range inBitDepth="32f" outBitDepth="32f">
        <minInValue>  0.0000</minInValue>
        <maxInValue>  1.0000</maxInValue>
        <minOutValue>  0.0000</minOutValue>
        <maxOutValue>  1.0000</maxOutValue>
    </Range>
    <Gamma inBitDepth="32f" outBitDepth="12i" style="basicRev">
        <GammaParams gamma="2.400000000000000" />
    </Gamma>
</ProcessList>
```
