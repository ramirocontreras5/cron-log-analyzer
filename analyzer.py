with open("cron_log.txt") as cron_file:
    lines = cron_file.readlines()

commands_counter= 0

for line in lines:
    
    if "CMD" in line:
        parts = line.strip().rsplit("CMD (", 1)
        timestamp = parts[0].split(" ")
        time = timestamp[2]
        print(time, parts[1].strip(")"))
        commands_counter += 1

print(f"Total commands executed: {commands_counter}")