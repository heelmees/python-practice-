def count_items_purchased(n):
    purchases = {}

    for i in range(n):
        record = input("Введите запись о покупке (ID покупателя Товар Количество): ").split()
        buyer_id, item, count = int(record[0]), record[1], int(record[2])

        if buyer_id not in purchases:
            purchases[buyer_id] = []

        purchases[buyer_id].append((item, count))

    for buyer_id, purchase_list in purchases.items():
        print(f"{buyer_id}:")
        for item, count in purchase_list:
            print(f"{item} {count}")

count_items_purchased(int(input("Введите количество записей о покупках: ")))