from queues.queue import Queue

def hot_potato(name_list, num):
    sample_queue = Queue()
    for name in name_list:
        sample_queue.enqueue(name)

    print(sample_queue.view())

    while sample_queue.size() > 1:
        for i in range(num):
            sample_queue.enqueue(sample_queue.dequeue())
        sample_queue.dequeue()

    print('current_queue', sample_queue.view())
    return sample_queue.dequeue()



output = hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],10)
print('output', output)