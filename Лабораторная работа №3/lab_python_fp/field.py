def field(items, *args):
    assert len(args) > 0, 'Передайте хотя бы один аргумент, не считая списка'
    if len(args) == 1:
        result = [items[i][args[0]] for i in range(len(items)) if (items[i][args[0]] != None)]
        if result:
            yield result;
    else:
        result = [{x: items[i][x] for x in args if (x in items[i].keys() and items[i][x] != None)} for i in
                  range(len(items))]
        if result:
            yield result;


goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
         {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
print(*list(field(goods, 'title')))
print(*list(field(goods, 'title', 'price', 'color')))
