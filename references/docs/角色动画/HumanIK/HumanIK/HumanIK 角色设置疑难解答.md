# HumanIK 角色设置疑难解答

## 分解的蒙皮几何体或关节

### 问题

角色的某些关节或几何体的某些分段看起来与其父对象关节或其他几何体不成比例。如果已启用关节的“分段比例补偿”(Segment Scale Compensate)属性，则可能会出现这种情况。启用“分段比例补偿”(Segment Scale Compensate)时，缩放父对象关节也会缩放链中的下方关节，这是与 [HumanIK](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-EDBDA3DB-4715-40EF-9ADF-412F78BFF98E.htm) 解算器冲突的一个过程。

### 解决方案

如果遇到不成比例的几何体或关节，请确保已禁用“分段比例补偿”(Segment Scale Compensate)。在 HumanIK 骨架定义中映射关节时，会自动禁用“分段比例补偿”(Segment Scale Compensate)属性。（请参见[创建 HumanIK 骨架定义](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-AC690ECF-D5B7-4759-AD71-C1FEFD7CF7A8.htm)。）

有关该属性的详细信息，请参见[分段比例补偿](https://help.autodesk.com/cloudhelp/2022/CHS/Maya-CharacterAnimation/files/GUID-8CE29E9D-F1C5-42A3-A657-33E32887380A.htm#WS73099CC142F48755-7B21313411809411AE9-5F4A)。
