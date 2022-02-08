# pylint: skip-file
import sys
import matplotlib.pyplot as plt
import numpy as np

# Parameters
SIZE = 5
TEAMS = 2
LANG = "fr"

# Argv
if len(sys.argv) > 1:
    SIZE = int(sys.argv[1])
if len(sys.argv) > 2:
    TEAMS = int(sys.argv[2])
if len(sys.argv) > 3:
    LANG = sys.argv[3]

# Words
with open(LANG + ".txt", "br") as file:
    lines = np.random.choice(file.readlines(), SIZE * SIZE, replace=False)
    words = list(line.decode("latin-1").strip() for line in lines)

# Areas
seq = 1 + np.array(range(SIZE * SIZE)) % (TEAMS + 1)
seq[TEAMS] = 2  # Neutral -> first team
seq[-1] = 0  # Death square
np.random.shuffle(seq)
seq = np.reshape(seq, (SIZE, SIZE))

# Plots
plt.figure(figsize=(16, 16))
plt.imshow(seq * 0, cmap="bwr", vmin=-1, vmax=1)
for i in range(SIZE * SIZE):
    x, y = np.unravel_index(i, (SIZE, SIZE))
    txt = plt.text(x, y, words[i], horizontalalignment="center", fontsize=20, fontweight="bold")
    if seq[x, y] == 0: # Death square
        death_word = txt
plt.tight_layout()
plt.axis("off")
plt.savefig("public.png")

plt.imshow(np.transpose(seq), cmap="gist_ncar", interpolation="none")
plt.setp(death_word, color="w")
cmap = plt.get_cmap('gist_ncar')
plt.title("Vous commencez" if LANG == "fr" else "You start", color = cmap(int(2 / (TEAMS+1) * 256)))
plt.savefig("secret.png")
plt.close()
