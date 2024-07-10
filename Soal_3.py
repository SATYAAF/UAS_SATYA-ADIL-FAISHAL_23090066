# ini ENQUE buat pesen makanan pak miftah
class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke antrian.")
queue = RestaurantQueue()

queue.enqueue("lengko babeh")
queue.enqueue("soto babeh")
queue.enqueue("risol poltek")

print(queue.queue)

# ini deque buat hapus antrian dri dpan pak
class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

# Contoh penggunaan
queue = RestaurantQueue()

queue.enqueue("lengko babeh")
queue.enqueue("soto babeh")
queue.enqueue("risol poltek")
print(queue.queue) 
queue.dequeue()     
print(queue.queue) 

