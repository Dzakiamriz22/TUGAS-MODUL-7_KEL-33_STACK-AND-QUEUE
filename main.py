from ClassStack import Stack
from ClassQueue import Queue

# Menghitung jumlah karakter dalam kata tanpa spasi
def count_letters(word):
    return len(word.replace(" ", ""))

# Menambah data pada stack dan queue
def add_data(stack, queue):
    data = input("Masukkan Data (String) = ")
    length = count_letters(data)

    if length < 7:
        queue.enqueue(data)
    elif length > 7:
        stack.push(data)
    else:
        stack.push(data)
        queue.enqueue(data)

# Menampilkan data dalam Stack
def show_stack(stack):
    if stack.empty():
        print("Stack Kosong")
    else:
        print("Data dalam Stack : ")
        for item in stack.items[::-1]:
            print(item)

# Menampilkan data dalam Queue
def show_queue(queue):
    if queue.empty():
        print("Queue kosong")
    else:
        print("Data dalam Queue:")
        for item in queue.items:
            print(item)

# Menghapus data dari stack
def remove_stack(stack):
    count = int(input("Pop data sebanyak : "))

    print("Menghapus data dari Stack:")
    for _ in range(count):
        item = stack.pop()
        if item is not None:
            print("Data dihapus:", item)
        print("Stack yang tersisa :", end="")
        if stack.empty():
            print("Stack kosong")
        else:
            print(stack.items)

# Menghapus data dari queue
def remove_queue(queue):
    count = int(input("Dequeue data sebanyak : "))

    print("Menghapus data dari Queue:")
    for _ in range(count):
        item = queue.dequeue()
        if item is not None:
            print("Data dihapus:", item)
        
print("===============================")
print("=== PROGRAM STACK DAN QUEUE ===")
print("===============================")

def main():
    stack = Stack()
    queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Tambah data (String)")
        print("2. Tampil data Stack")
        print("3. Tampil data Queue")
        print("4. Hapus data Stack")
        print("5. Hapus data Queue")
        print("6. Exit")
        print("================================")

        menu = input("Pilih menu: ")

        if menu == "1":
            add_data(stack, queue)
        elif menu == "2":
            show_stack(stack)
        elif menu == "3":
            show_queue(queue)
        elif menu == "4":
            remove_stack(stack)
        elif menu == "5":
            remove_queue(queue)
        elif menu == "6":
            print("Terima kasih!")
            break
        else:
            print("Menu tidak valid.")

if __name__ == '__main__':
    main()