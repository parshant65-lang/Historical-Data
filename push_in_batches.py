import os
import subprocess
import sys

REPO = "/home/parshant_01/Desktop/Historical-Data"

def run(cmd):
    print("RUN:", cmd if isinstance(cmd, str) else " ".join(cmd[:10]) + f" ... ({len(cmd)} args)")
    subprocess.check_call(cmd, cwd=REPO)

# Set configs
run(["git", "config", "http.version", "HTTP/1.1"])
run(["git", "config", "http.postBuffer", "524288000"])

out = subprocess.check_output(['git', 'status', '--porcelain'], cwd=REPO).decode().splitlines()
untracked = [line[3:].strip('/') for line in out if line.startswith('?? ')]
print(f"Total untracked to push: {len(untracked)}")

if not untracked:
    print("Nothing untracked!")
    sys.exit(0)

mid = len(untracked) // 2
batch1 = untracked[:mid]
batch2 = untracked[mid:]

print(f"Staging batch 1 ({len(batch1)} companies)...")
# Stage in chunks of 200 args to avoid arg max limits
for i in range(0, len(batch1), 200):
    run(["git", "add"] + batch1[i:i+200])

run(["git", "add", ".gitignore", "README.md"])
run(["git", "commit", "-m", f"Add {len(batch1)} companies to 1m date-wise archive (total: {1837 + len(batch1)} companies)"])

print("Pushing batch 1 to GitHub...")
run(["git", "push", "origin", "main"])
print("✅ Batch 1 pushed successfully!")

print(f"Staging batch 2 ({len(batch2)} companies)...")
for i in range(0, len(batch2), 200):
    run(["git", "add"] + batch2[i:i+200])

run(["git", "commit", "-m", f"Reach final milestone: 4,000 unique companies in 1m date-wise archive"])

print("Pushing batch 2 to GitHub...")
run(["git", "push", "origin", "main"])
print("✅ Batch 2 pushed successfully!")

