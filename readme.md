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
  Ex: [hanoi_tower.py] [power_calculator.py] [multiplication_calculator.py] [factorial_calculator.py] [sequence_max_min.py]

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
  Ex: [hanoi_tower_iteractive_with_stack.py] [math_expression_balance.py] [stack_with_deque.py] [stack_with_list.py]

* **Queue**: collection where objects can be inserted/removed as FIFO (First In, First Out).
  > Operations: enqueue (insert element), dequeue (remove element), first (first element in the queue), is_empty, len
  > All operations are O(1)
  > Applications: real life queues, task queues in servers, auxiliar structure for tree traversal, tokenization of arithmetic expressions.
  > Double linked list is good to implement queue (deque in python).
  Ex: [arithmetic_expression_evaluation.py] [queue_with_deque.py]


**SORTING**: process of ordering elements from an object collection
  > Transitive property: a < b and b < c -> a < c
  > Different between sort and sorted (for python):
    * sort: method -> original_list.sort() - change the original list object by sorting its elements (return None) - consume less memory
      # object.sort(key=function_that_return_sorting_criteria()) -> function can return a tuple to give more options of comparison in case of tie
      # object.sort(reverse=True) -> sort in reverse way
    * sorted: function -> new_list = sorted(original_list) - create a new list by copying and sorting elements from original list - consume more memory
  > Important magic methods: __gt__, __lt__, __equal__ (@total_ordering)
  > Algorithms Alaysis:
    * Simple algorithm: O(nˆ2) - bubble, selection, insertion
    * Complex algorithms: O(n.log[n]) - quick (mean case), merge, heap
    # Python uses a hybrid algorithm: Tim Sort (derived from merge and insertion sort algorithms)

**Selection Sort**: 
> Process:
1. Search for minimal value iterating over elements of a list
2. Remove the minimal value and put it as the last element in the ordered list
3. Repeat steps 1 and 2 until the list is completely ordered
> Analysis:
* Number of iterations: n+(n-1)+(n-2)+...+1 -> O(nˆ2)
* Any difference if list is random or ordered

**Bubble Sort**: 
> Process:
1. Iterate n-1 times through the list
2. Change the element by its sucessor if the element is bigger than the sucessor
> Analysis:
* Number of iterations: n*(n-1) -> O(nˆ2)

**Insertion Sort**: 
> Process:
1. Choose one element
2. Add it to the end of the sorted list
3. Move it to the correct position
4. Repeat steps 1, 2 and 3 until the list is completely ordered
> Analysis:
* Number of iterations: n*(n-1) -> O(nˆ2)

**Merge Sort**:
> Paradigm:
* Divide and conquer (obvious solution for len(seq)<=1)
> Process:
DIVIDE
1. Divide list in the middle
2. For each half, check if its length is >= 1
  a. If len(sub_list) > 1, repeat step 1 for it
  b. If len(sub_list) == 1, this is and sorted list
CONQUER
3. When step b is executed, order the last two unitary lists and group it into one sorted list
4. Repeat step 3 until all sub lists are grouped into one sorted list
> Analysis:
* Number of iterations: divide -> O(n) | conquer -> O(log(n)) | merge sorting -> O(n.log(n))

**Quick Sort**:
> Paradigm:
* Divide and conquer (obvious solution for len(seq)<=1)
> Process:
DIVIDE
1. Choose one pivot
2. Create two lists, one with elements lower than the pivot and other with the greater elements
CONQUER
1. Order the sub_lists using quick sort until the original list is ordered (concatenation)
> Analysis:
* Number of iterations: 
  a. Mean case (pivot in the middle) -> O(n.log(n))
  b. Worst case (pivot = last element and list is sorted) -> O(n^2)                   
* To avoid problems, choose pivot randomly or as median

**Radix Sort**: to be searched...


**TREE**: