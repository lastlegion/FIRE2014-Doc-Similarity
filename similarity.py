with open("queries/train/Q001") as f:
	content = f.read().splitlines()


#Simliarities
for line in content:
	term = line.split(",")[0];
	print term

print content