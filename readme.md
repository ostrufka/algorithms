# ---------------------------- #
# Algorithms & Data Structutes #
# ---------------------------- #

> Run doctests: pytest <file_path/file.py> --doctest-modules -v

**Big-O Notation**:
> Good:
    O(1)
    O(log(n))
    O(n)
> Bad:
    O(n.log(n))
    O(nˆ2)
    O(nˆc)
> Terrible:
    O(cˆn)
    O(n!)
    O(nˆn)

* **Algorithm Complexity for Usual Python Operations with Iterables (List)**
  * *Unmutable Operations*:
    **********************
  > Len(data)             -> O(1)
  > data[j]               -> O(1)
  > data.count(value)     -> O(n)
  > data.index(value)     -> O(k+1) [up to find it]
  > value in data         -> O(k+1) [up to find it]
  > data1 == data2        -> O(k+1) [up to find it] *same for: !=, <, <=, >, >=
  > data[j:k]             -> O(k-j+1)
  > data1 + data2         -> O(n1 + n2)
  > c * data              -> O(cn)

  * *Mutable Operations*:
    **********************
  > data[j] = val         -> O(1)
  > data.append(value)    -> O(1)* [amortized]
  > data.insert(k, value) -> O(n-k+1)* [amortized]
  > data.pop()            -> O(1)* [amortized]
  > data.pop(k)           -> O(n-k)* [amortized]
  > del data(k)           -> O(n-k)* [amortized]
  > data.remove(value)    -> O(n)* [amortized]
  > data1.extend(data2)   -> O(n2)*
  > data1 += data2        -> O(n2)*
  > data.reverse()        -> O(n)
  > data.sort()           -> O(n.log(n))

* **Recursion**: function that calls itself (define smaller instances of the problem).
  > Uses a pile of execution to store execution states info for each call.
  > Tail Recursion Optimization
  > Recursion can replace loops
  Ex: [hanoi_tower.py] [power_calculator.py] [multiplication_calculator.py] [factorial_calculator.py]

* **Vector/Array**: contiguous space in mamory. 
  > Element access in O(1).
  > Need to specify size in definition.

* **Linked List**:
  > Simple Linked List
  > Double Linked List
  > Circular Linked List
  Ex: [simple_linked_list.py] [double_linked_list.py]

* **Stack**: collection where objects can be inserted/removed as FILO (First In, Last Out).
  > Memory stack follows the stack (pile) abstraction.
  > Operations: push (insert element), pop (remove element), top (element in the top), is_empty
  > All operations are O(1)
  > Applications: browser history, CTRL + Z, programs execution pile, transform recursive problems to iteractive, aux. structure for tree navegation.

* **Queue**: collection where objects can be inserted/removed as FIFO (First In, First Out).
  > Operations: enqueue (insert element), dequeue (remove element), first (first element in the queue), is_empty, len
  > All operations are O(1)
  > Applications: real life queues, task queues in servers, auxiliar structure for tree traversal, tokenization of arithmetic expressions.
  > Double linked list is good to implement queue (deque in python).
