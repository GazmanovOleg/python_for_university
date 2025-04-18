def get_summary_rss(file_path):
    total_rss = 0

    with open(file_path, 'r') as output_file:
        lines = output_file.readlines()[1:]
        for line in lines:
            columns = line.split()
            if len(columns) > 5:  
                total_rss += int(columns[5])

    return new_size(total_rss)

def new_size(size_in_bytes):
    for unit in ['Б', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

if __name__ == '__main__':
    file_path = 'output_file.txt'  
    summary_rss = get_summary_rss(file_path)
    print(f"Суммарный объем потребляемой памяти: {summary_rss}")
