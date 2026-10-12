# Delta Mush 变形器

使用 Delta Mush 变形器可过滤变形瑕疵和创建平滑效果。

Delta Mush 变形器充当低通过过滤器，可移除变形瑕疵和引导最终结果更接近原始静止几何体。它可在许多不同的工作流中很有用，如绘制自由蒙皮、粗糙模拟结果的平滑以及校正后快照。

Delta Mush 对几何体的静止状态应用 Laplacian 平滑算法，并以曲面空间坐标存储每个顶点的静止状态与平滑状态之间的差异（增量）。然后，对几何体的当前状态应用 Laplacian 平滑算法，并重新应用以曲面空间坐标存储的增量来移除变形链引入的变形瑕疵。

**注**

Delta Mush

变形器基于以下人员所做的工作：

Joe Mancewicz、Matt L. Derksen 和 Cyrus A. Wilson，*Delta mush: smoothing deformations while preserving detail*（Delta mush：平滑变形并保留细节），SIGGRAPH 2014, ACM, New York, NY, USA, Article 28, 1 pages。
