import matplotlib.pyplot as plt

# Adjust these consts
NUM_CONFIGS        = 14
CONTENT_START_LINE = 4
TOTAL_LUTS_COL     = 9
LOGIC_LUTS_COL     = 11
FFS_COL            = 17

with open('results.txt', 'r') as file:
    content = file.readlines()

configurations = [line.strip() for line in content[-NUM_CONFIGS:]]

# Sanity check
if "Baseline Standalone Rocket SoC" not in configurations:
    print("[Debug] Number of Configurations:", NUM_CONFIGS)
    print("[Debug] First Configuration:", configurations[0])
    raise ValueError("The expected first configuration 'Baseline Standalone Rocket SoC' is missing. Check NUM_CONFIGS.")

data_lines = content[CONTENT_START_LINE-1:CONTENT_START_LINE+NUM_CONFIGS-1]
total_luts = []
logic_luts = []
ffs = []

for line in data_lines:
    parts = line.split()
    total_luts.append(int(parts[TOTAL_LUTS_COL].split('(')[0]))
    logic_luts.append(int(parts[LOGIC_LUTS_COL].split('(')[0]))
    ffs.append(int(parts[FFS_COL].split('(')[0]))

fig, ax = plt.subplots(figsize=(14, 8))
index = range(len(configurations))
bar_width = 0.25
opacity = 0.8

rects1 = ax.bar(index, total_luts, bar_width, alpha=opacity, color='b', label='Total LUTs')
rects2 = ax.bar([p + bar_width for p in index], logic_luts, bar_width, alpha=opacity, color='r', label='Logic LUTs')
rects3 = ax.bar([p + bar_width * 2 for p in index], ffs, bar_width, alpha=opacity, color='g', label='FFs')

ax.set_xlabel('Configuration')
ax.set_ylabel('Counts')
ax.set_title('Total LUTs, Logic LUTs, and FFs by Configuration')
ax.set_xticks([p + bar_width for p in index])
ax.set_xticklabels(configurations, rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.savefig('dse-utilization.png', format='png', dpi=300)
plt.show()
