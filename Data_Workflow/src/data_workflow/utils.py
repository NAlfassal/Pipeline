import numpy as np
import pandas as pd

def bootstrap_diff_means(a, b, n_boot=2000, seed=0):
    a_clean = pd.to_numeric(a, errors="coerce").dropna().to_numpy()
    b_clean = pd.to_numeric(b, errors="coerce").dropna().to_numpy()
    
    rng = np.random.default_rng(seed)
    diffs = []
    
    for _ in range(n_boot):
        resample_a = rng.choice(a_clean, size=len(a_clean), replace=True)
        resample_b = rng.choice(b_clean, size=len(b_clean), replace=True)
        diffs.append(resample_a.mean() - resample_b.mean())
    
    diffs = np.array(diffs)
    observed = a_clean.mean() - b_clean.mean()
    
    return {
        "observed_diff": float(observed),
        "ci_low": float(np.quantile(diffs, 0.025)),
        "ci_high": float(np.quantile(diffs, 0.975))
    }