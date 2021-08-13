
def sum(a,b):
    print(f'__name__:{__name__}')
    return a + b


def main():
    print(f'Test Sum: {sum(10,20)}')

if __name__ == '__main__':
    print(f'__name__:{__name__}')
    main()