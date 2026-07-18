import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

# CSV einlesen (Komma als Spaltentrenner)
ratings = pd.read_csv("ratings.csv", sep=",")

# Dezimalkomma → Dezimalpunkt (Python 3.13-kompatibel)
for col in ratings.columns:
    ratings[col] = ratings[col].astype(str).str.replace(",", ".", regex=False)

roles_per_formation = pd.read_csv("roles.csv")

players = ratings.iloc[:, 0].values
role_names = ratings.columns[1:]

# Ratings in echte Zahlen umwandeln
rating_matrix = ratings.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').fillna(0).values

results = []

for _, row in roles_per_formation.iterrows():
    tactic = row.iloc[0]
    tactic_roles = row.iloc[1:12].values  # 11 Rollen

    # Spaltenindizes für diese Rollen
    cols = [np.where(role_names == r)[0][0] for r in tactic_roles]
    cost = rating_matrix[:, cols]

    # Maximierung → Minimierung
    max_val = cost.max()
    cost_min = max_val - cost

    # Hungarian
    player_idx, role_idx = linear_sum_assignment(cost_min)

    # Zuordnung in Formation-Reihenfolge abbilden
    assignment_by_role = [None] * len(tactic_roles)
    for p_i, r_i in zip(player_idx, role_idx):
        assignment_by_role[r_i] = (p_i, r_i)

    total = cost[player_idx, role_idx].sum()
    avg = round(total / len(tactic_roles), 2)

    row_dict = {"Tactic": tactic, "AvgRating": avg}

    for pos, entry in enumerate(assignment_by_role, start=1):
        p_i, r_i = entry
        role = tactic_roles[r_i]
        player = players[p_i]
        rating = round(cost[p_i, r_i], 2)
        gap = round(rating - avg, 2)

        row_dict[f"Role{pos}"] = role
        row_dict[f"Player{pos}"] = player
        row_dict[f"Rating{pos}"] = rating
        row_dict[f"Gap{pos}"] = gap

    results.append(row_dict)

df = pd.DataFrame(results)

# Dezimalpunkt → Dezimalkomma (Python 3.13-kompatibel)
for col in df.columns:
    df[col] = df[col].apply(
        lambda x: str(x).replace('.', ',') if isinstance(x, float) else x
    )

df.to_csv("best_tactic_python.csv", index=False)
print("Fertig! Datei best_tactic_python.csv wurde erzeugt.")
