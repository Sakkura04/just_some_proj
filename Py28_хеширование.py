class HashTable:
    def __init__(self, size):
        self.size = size
        self.amount = 0
        self.hash_table = self.create_buckets()

# создаeм пустые скобки по заданому количеству
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # вставка значения
    def set_val(self, key, val):

        # Получаем значение, используя функцию хеш
        # и делим с осацей на размер таблиці
        hashed_key = hash(key) % self.size

        # bucket - ячейка соответствующая подобранному хеш-индексу
        bucket = self.hash_table[hashed_key]

        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_val = record # содержимое bucket

            # если содержимое bucket равно вставляемому содержимому меняем флаг
            if record_key == key:
                found_key = True
                break

        # если выше отмеченный флаг = 1, обновляем значение
        if found_key:
            bucket[index] = (key, val)
        # иначе добавляем новое значение в bucket
        else:
            self.amount += 1
            bucket.append((key, val))


    def searches(self, key):
        # Получаем индекс, по которому было спрятано значение
        hashed_key = hash(key) % self.size
        # bucket - ячейка соответствующая подобранному хеш-индексу
        bucket = self.hash_table[hashed_key]
        found_key = False
        #ищем значение в заданой ячейке
        for index, record in enumerate(bucket):
            record_key, record_val = record
            # если в bucket тот же ключ, что мы ищем, то меняем флаг
            if record_key == key:
                found_key = True
                break

        return [found_key, record_val]


    # возвращаем искомое значение
    def get_val(self, key):
        found_key = self.searches(key)[0]
        # если выше отмеченный флаг = 1, возвращаем найденное значение
        # иначе пишем, что ничего не нашли
        if found_key:
            return self.searches(key)[1]
        else:
            return "No record found"

    # удаление елемента
    def delete_val(self, key):
        # Получаем индекс, по которому было спрятано значение
        hashed_key = hash(key) % self.size
        # bucket - ячейка соответствующая подобранному хеш-индексу
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        # если флаг = 1, удаляем значение
        if found_key:
            self.amount -= 1
            bucket.pop(index)
        return

    # Принтим значение хеш-таблицы
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

    def __contains__(self, item):
        return self.search(item)[0]

    def __len__(self):
        return self.amount


if __name__ == "__main__":
    hash_table = HashTable(50)

    # insert some values
    hash_table.set_val('gfg@example.com', 'some value')
    print(hash_table)
    print()

    hash_table.set_val('portal@example.com', 'some other value')
    print(hash_table)
    print()

    # search/access a record with key
    print(hash_table.get_val('portal@example.com'))
    print()

    # delete or remove a value
    hash_table.delete_val('portal@example.com')
    print(hash_table)
