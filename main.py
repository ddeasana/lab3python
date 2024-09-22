import random
def create_matrix(m, n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]


def write_matrix_to_file(filename, matrix):
    try:
        with open(filename, 'w') as f:
            for row in matrix:
                f.write(' '.join(map(str, row)) + '\n')
        print(f"Matrix written to {filename}.")
    except (IOError, OSError) as e:
        print(f"Error writing to file {filename}: {e}")


def read_matrix(filename):
    try:
        with open(filename, 'r') as f:
            matrix = [list(map(int, line.strip().split())) for line in f]
        print(f"Matrix read from {filename}.")
        return matrix
    except (IOError, OSError, ValueError) as e:
        print(f"Error reading from file {filename}: {e}")
        return []


def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


def write_transposed_matrix_to_file(filename, transposed_matrix):
    try:
        with open(filename, 'w') as f:
            for row in transposed_matrix:
                f.write(' '.join(map(str, row)) + '\n')
        print(f"Transposed matrix written to {filename}.")
    except (IOError, OSError) as e:
        print(f"Error writing to file {filename}: {e}")


def main():
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))

    if m < 5 or n < 5:
        print("The number of rows and columns must be at least 5.")
        return


    matrix = create_matrix(m, n)
    input_filename = 'matrix.txt'
    write_matrix_to_file(input_filename, matrix)
    matrix_from_file = read_matrix(input_filename)


    if matrix_from_file:
        transposed_matrix = transpose_matrix(matrix_from_file)
        output_filename = 'transposed_matrix.txt'
        write_transposed_matrix_to_file(output_filename, transposed_matrix)

main()
