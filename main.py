from avl import AVL


def main():
    if __name__ == '__main__':
        avl = AVL()
        avl.insert(6)
        avl.insert(10)
        avl.insert(20)
        avl.insert(5)
        avl.insert(13)
        avl.insert(14)
        avl.insert(3)
        avl.insert(2)
        avl.insert(7)
        avl.insert(8)
        avl.insert(4)
        avl.insert(15)
        avl.insert(55)
        avl.remove(5)
        avl.remove(10)
        avl.display()

        max_value = avl.get_max_value()
        if max_value:
            print(f'Max value: {max_value.data}')
        else:
            print('The tree is empty')

        min_value = avl.get_min_value()
        if min_value:
            print(f'Min value: {min_value.data}')
        else:
            print('The tree is empty')

        sum = avl.get_sum(avl.root)
        print(f'Sum of all values: {sum}')


if __name__ == "__main__":
    main()

