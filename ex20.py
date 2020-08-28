from sys import argv

scrpt, input_file = argv

def print_all(f):
    print(f.read)

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count, f.readline())

current_file = open(input_file)

print_all(current_file)

rewind(current_file)

corrent_line = 1
print_a_line(corrent_line,current_file)

corrent_line = corrent_line+1
print_a_line(corrent_line,current_file)

corrent_line = corrent_line+1

print_a_line(corrent_line,current_file)
