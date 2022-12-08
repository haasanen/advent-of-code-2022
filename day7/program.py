class FileSystem:
    def __init__(self):
        self.root = {
            "..": None # Indicates parent directory.
        }
        self.current_directory = None
        self.listing = False

    def process_command(self, parts):
        command = parts[0]
        if command == "cd":
            argument = parts[1]
            if argument == "/":
                self.current_directory = self.root
                return
            else:
                self.current_directory = self.current_directory[argument]
                return
        if command == 'ls':
            self.listing = True
            return

    def process_listing(self, parts):
        filename = parts[1]
        if filename in self.current_directory:
            print(f"WARNING: Duplicate name ${filename}")
        if parts[0] == "dir":
            self.current_directory[filename] = {
                "..": self.current_directory
            }
        else:
            size = int(parts[0])
            self.current_directory[filename] = size

    def process_line(self, line: str):
        parts = line.split(" ")
        if parts[0] == "$":
            self.listing = False
            self.process_command(parts[1:])
            return
        if self.listing:
            self.process_listing(parts)
            return

    def get_root(self):
        return self.root

    def _get_folder_sizes(folder: dict) -> tuple[int, list[int]]:
        total_size = 0
        folder_sizes = list()
        for name, contents in folder.items():
            if name == "..":
                continue
            if type(contents) is dict:
                total, sizes = FileSystem._get_folder_sizes(contents)
                total_size += total
                folder_sizes.append(total)
                folder_sizes.extend(sizes)
            else:
                total_size += contents
        return total_size, folder_sizes
    
    def get_folder_sizes(self):
        return FileSystem._get_folder_sizes(self.root)

files = FileSystem()
with open("day7/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if len(line) > 0:
            files.process_line(line)

total_size, sizes = files.get_folder_sizes()
print("Answer 1:", sum(filter(lambda x: x <= 100000, sizes)))

disk_size = 70000000
needed_space = 30000000
free_space = disk_size - total_size
space_to_free = needed_space - free_space
if space_to_free < 1:
    print("No need to free space")
    exit()

sizes.sort()
print("Answer 2:", next((size for size in sizes if size >= space_to_free)))