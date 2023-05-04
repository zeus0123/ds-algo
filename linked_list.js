class Node {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.length = 0;
        this.tail = null;
    }

    push(val) {
        let newNode = new Node(val)
        if(!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            this.tail.next = newNode;
            this.tail = newNode; 
        }
        this.length++;
        return this;
    }

    pop() {
        if(!this.head) return undefined;
        let current = this.head;
        let newTail = current;
        // Traversing the List
        while(current.next) { 
            newTail = current;
            current = current.next;
        }
        console.log('new tail', newTail);
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if(this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return this;
    }
}

var list = new SinglyLinkedList();
list.push('Luggage Car');
list.push('I am');
list.push('Software Engineer');
list.pop();
console.log(list);