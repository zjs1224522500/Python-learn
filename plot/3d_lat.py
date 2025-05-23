import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

# 固定参数
p = 0.5
alpha = 0.1
storage_term = (1 + alpha) / (
    1 + 2 * alpha
)  # 存储成本项（常数）

# 生成 K_s 和 K_l 的网格数据
K_s = np.linspace(
    0.5, 2.0, 100
)  # EC小IO延迟比（0.1~2倍）
K_l = np.linspace(
    0.5, 3.0, 100
)  # EC大IO延迟比（0.1~3倍）
K_s_grid, K_l_grid = np.meshgrid(K_s, K_l)

# 计算 R 值矩阵（向量化计算）
numerator = K_s_grid + (1 - p) * K_l_grid
denominator = 1 + (1 - p) * K_l_grid
R = (numerator / denominator) * storage_term

# 创建 3D 画布
fig = plt.figure(figsize=(10, 7.5))
ax = fig.add_subplot(111, projection="3d")

# 绘制 3D 曲面（颜色映射为 viridis，透明度 0.8）
surf = ax.plot_surface(
    K_s_grid,
    K_l_grid,
    R,
    cmap="viridis",
    alpha=0.8,
)

# 标记 R=1 的等高线（红色虚线，线宽 2）
contour = ax.contour(
    K_s_grid,
    K_l_grid,
    R,
    levels=[1],
    colors="black",
    linestyles="-",
    linewidths=2,
)

# ----------------- 添加辅助线（修正后）-----------------
# 辅助线1：固定 K_s=1.3，绘制 K_l 对应的 R 曲线
K_s_fixed = 1.3
idx_K_s = np.argmin(
    np.abs(K_s - K_s_fixed)
)  # 找到最接近 K_s=1.3 的索引
ax.plot(
    K_s_grid[:, idx_K_s],
    K_l_grid[:, idx_K_s],
    R[:, idx_K_s],
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"$K_s$={K_s_fixed}",
)

# 辅助线2：固定 K_l=1.5，绘制 K_s 对应的 R 曲线
K_l_fixed = 1.5
idx_K_l = np.argmin(
    np.abs(K_l - K_l_fixed)
)  # 找到最接近 K_l=1.5 的索引
ax.plot(
    K_s_grid[idx_K_l, :],
    K_l_grid[idx_K_l, :],
    R[idx_K_l, :],
    color="green",
    linestyle="-.",
    linewidth=2,
    label=f"$K_l$={K_l_fixed}",
)

# ----------------- 直接标记交点 -----------------
# 计算交点坐标
K_s_point = 1.3
K_l_point = 1.5
R_point = (
    (K_s_point + 0.5 * K_l_point)
    / (1 + 0.5 * K_l_point)
    * storage_term
)

# 绘制红色标记点
ax.scatter(
    K_s_point,
    K_l_point,
    R_point,
    color="black",
    s=100,
    label=f"($K_s$=1.3, $K_l$=1.5)",
)

# 添加坐标文本标注
ax.text(
    K_s_point + 0.03,  # X方向偏移（避免文字重叠）
    K_l_point + 0.05,  # Y方向偏移
    R_point + 0.1,  # Z方向偏移（抬高文字）t,
    f"R={R_point:.2f}",
    color="white",
    fontsize=10,
    bbox=dict(  # 背景框参数
        facecolor="black",
        alpha=0.7,
        edgecolor="none",
        boxstyle="round",
    ),
    zorder=10,  # 确保文字在顶层
)


# 设置坐标轴标签和标题
ax.set_xlabel(f"$K_s$", fontsize=12, labelpad=10)
ax.set_ylabel(f"$K_l$", fontsize=12, labelpad=10)
# ax.set_zlabel(
#     "Score Value", fontsize=12, labelpad=10
# )
ax.set_title(
    f"Model",
    fontsize=14,
    pad=20,
)

# 添加颜色条
cbar = fig.colorbar(
    surf, ax=ax, shrink=0.6, aspect=10
)
cbar.set_label("Score Value", fontsize=12)

legend_elements = [
    # R=1 等高线（如果存在）
    Line2D(
        [0],
        [0],
        color="black",
        linestyle="-",
        linewidth=3,
        label="R=1",
    ),
    Line2D(
        [0],
        [0],
        color="blue",
        linestyle="-.",
        linewidth=3,
        label=f"$K_s$={K_s_fixed}",
    ),
    Line2D(
        [0],
        [0],
        color="green",
        linestyle="--",
        linewidth=3,
        label=f"$K_l$={K_l_fixed}",
    ),
    # 交点标记
    Line2D(
        [0],
        [0],
        marker="o",
        color="black",
        linestyle="None",
        markersize=10,
        markerfacecolor="black",
        markeredgecolor="white",
        label=f"($K_s$=1.3, $K_l$=1.5)",
    ),
]

# 手动添加图例（精确定位）
ax.legend(
    handles=legend_elements,
    loc="upper right",  # 基准定位点
    bbox_to_anchor=(0.94, 0.9),
    fontsize=10,
    framealpha=0.7,
    edgecolor="black",
    facecolor="white",
    ncol=1,  # 单列显示
)

# 调整视角（俯仰角 30 度，方位角 45 度）
ax.view_init(elev=20, azim=110)
plt.tight_layout()
plt.show()
