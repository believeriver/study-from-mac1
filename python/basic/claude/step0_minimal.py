"""
1次元Poisson方程式の最小実装
    -u''(x) = f(x),   u(0) = u(1) = 0

物理的なイメージ: 長さ1の棒。両端の温度を0に固定し、
内部に熱源 f(x) があるときの、定常状態での温度分布 u(x) を求める。
"""
import numpy as np
import matplotlib
# matplotlib.use("Agg")  # 画面なし環境で画像ファイルとして保存するため
import matplotlib.pyplot as plt


def build_matrix(n: int) -> np.ndarray:
    """
    n個の内部格子点に対する係数行列Aを作る。
    -u'' を中心差分で近似すると、各点で
        (-u[i-1] + 2*u[i] - u[i+1]) / h^2 = f(x_i)
    という関係になる。これを行列の形でまとめたもの。
    """
    h = 1.0 / (n + 1)  # 格子間隔(両端含めてn+2点、内部はn点)
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = 2.0
        if i > 0:
            A[i, i - 1] = -1.0
        if i < n - 1:
            A[i, i + 1] = -1.0
    A /= h**2
    return A


def build_rhs(n: int, f) -> np.ndarray:
    """右辺ベクトル b を作る。各内部格子点での f(x) の値。"""
    h = 1.0 / (n + 1)
    x = np.array([(i + 1) * h for i in range(n)])
    b = np.array([f(xi) for xi in x])
    return b, x


def solve_cg(A: np.ndarray, b: np.ndarray, tol: float = 1e-10, max_iter: int = 1000):
    """
    共役勾配法(CG)で A u = b を解く。
    A は対称正定値であることが前提。
    """
    n = len(b)
    u = np.zeros(n)
    r = b - A @ u          # 残差: 「今の解がどれだけ間違っているか」
    p = r.copy()           # 探索方向
    rs_old = r @ r

    residual_history = [np.sqrt(rs_old)]

    for _ in range(max_iter):
        Ap = A @ p
        alpha = rs_old / (p @ Ap)
        u = u + alpha * p
        r = r - alpha * Ap
        rs_new = r @ r
        residual_history.append(np.sqrt(rs_new))

        if np.sqrt(rs_new) < tol:
            break

        p = r + (rs_new / rs_old) * p
        rs_old = rs_new

    return u, residual_history


if __name__ == "__main__":
    n = 50  # 内部格子点の数

    # 熱源: f(x) = 1 (一定の熱源を仮定。シンプルな例)
    f = lambda x: 1.0

    A = build_matrix(n)
    b, x = build_rhs(n, f)

    u, residual_history = solve_cg(A, b)

    print(f"格子点数: {n}")
    print(f"CG反復回数: {len(residual_history) - 1}")
    print(f"最終残差: {residual_history[-1]:.2e}")
    print(f"u の最大値 (棒の中央付近の温度): {u.max():.6f}")
    print(f"u の最大値が出る位置 x = {x[np.argmax(u)]:.3f}")

    # 解析解 (f=1 の場合、厳密解は u(x) = x(1-x)/2 )
    u_exact = x * (1 - x) / 2
    error = np.max(np.abs(u - u_exact))
    print(f"解析解との最大誤差: {error:.2e}")

    # 可視化
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot(x, u, "o-", markersize=3, label="CG numerical solution")
    axes[0].plot(x, u_exact, "--", label="Analytical: u(x)=x(1-x)/2")
    axes[0].set_xlabel("x (position along rod)")
    axes[0].set_ylabel("u(x) (temperature)")
    axes[0].set_title("1D Poisson equation solution")
    axes[0].legend()
    axes[0].grid(alpha=0.3)

    axes[1].semilogy(residual_history, "o-", markersize=3)
    axes[1].set_xlabel("CG iteration")
    axes[1].set_ylabel("Residual (log scale)")
    axes[1].set_title("CG solver convergence history")
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.show()
    # plt.savefig("/home/claude/poisson_1d/result.png", dpi=120)
    print("\n結果を result.png に保存しました")
