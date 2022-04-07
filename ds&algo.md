#Data Structures & Alogrithms

___
## * Big 'O' Notation - $O(n)$
 ###### Effeciency of code, runs faster

  - $n$ === **length of input to a function**
    _the quantity of an iteration_
efficiency = complexity


Space & Time:
- How long does the code take to run
- How much storage space do we need
  ____

```py
function(input)
  create output string    # <output>
  return output string    # <output>
```
____
### Time Efficiency
####`n == iteration`
iteration = each variable in an array

**Efficiency**== (`input + output`) * `runtime`

The more iterations, the more power used

--

```python
def function(param):
  return param   # <output>
```
// $O(1)$
  _ie. O(n+1) -> 1 line of output_
__

$eg.$
if there are two lines of code in a `for loop`, we do 2 * each variable in an array - that is, 2 * each iteration.
The `for loop` line itself acts as 1 line fo code, so it'll be 2 + 1.
**// 3 input lines of code for each iteration**
___

### Advanced

- Higher level programming langauges = less lines of code, but more power used for each line.
- Lower level programming languages = more lines of code, but less power used for each line

>_eg. changing one letter to another for every iteration will consume 26 computations(alphabetically) to change a letter_

Steps in a program = computation
The more computation, the more energy is used
___

### Approximation
_Some quantities of computation must be performed for EACH variable of an input_.
_We talk about_ efficiency _in the **worst case, average case** and **best case**_.
>_eg._ looking for a letter in the alphabet - `$ for loop`
**the worst case** = 26
**average case** = 13
**best case** = 1
These cases will represent the iteration number in the $Big"O"Notation$

When reffering to $O(n)$, you must specify which **case approximation** is queried.

___

### Space Efficiency

Uses the same **notation** in the $Big"O"$.

---

####Manatees Quiz
```py

"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    for manatee in manatees:
        print manatee['name']

def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee
```

_# of iterations per example?_
1. n = manatees
//  $O(n)$
2. `!`iterating :: code will complete in constant - _1 iteration_
// $O(1)$
3. 2 four loops, 1 normal, 1 nested. nested four loops = * runtimes
   for every dictionary -> for every property
// $O(nm)$
4. iterating over a loop twice
// $O(n^2)$

---

## Collections

- `!` inherent order
- any data types

##### List is an ordered Collection
**Arrays** are the most common implementation of a List[  ]
Each array has a location called an **Index** - the number associated with the location in an array.

--
Python Array - name: `List[  ]` - type: `Array[  ]`
// **Hybrid Array** -> _lots of built-in optimizations_
- Inserting into an **Array** is $O(n)$ - _need to make space for insertion_
- Inserting into a **List** is $O(1)$
- Python List == $O(n)$
  + Inserting into Python List is $O(n)$
  + Searching Python List is $O(1)$

>With a normal list, you might need to traverse through every element to find the length, but Python does some work behind the scenes to get you the list length in constant time ( $O(1)$ )

\\traverse - _travel across_\\

---

### Linked List

>A linked list is an extension of a list but **is not** an Array.

There are `!` indices in a linked list. Instead each element points to the next object with a `next: ` reference keyword. **Insertion** takes _constant_ time in a Linked List since we are just shifting around **pointers** & not iterating over every element in a list.

##### Doubly Linked List: _pointers connecting to the next & previous element of a List._

>Be careful not to lose references when adding/removing elements.

---

### Stacks

>Stacks are list-based data structures

They are structured with elements stacked on each other where you can add or remove to the pile. To access the element of the bottom of stack, all other elements must be removed first.

Insert element into stack = `push` $O(1)$
Remove element from stack = `pop` $O(1)$

_Stacks can be implemeneted with other data types ie. `stack functionality`_

The look and connections of an element cannot be specified, just the methods for adding and removing them. _eg. you can use a linked list to implemenet a stack._

`LIFO` - **L**ast **I**n **F**irst **O**ut
  The last element you put on the stack when you use `push` is the first one to be removed when you use `pop`.

__

`Stack Functionality` is built-in with **Python Lists[  ]**

\\\\~ rememeber: to turn a data type in a stick use _built-in functions_ (methods) such as `pop()` or `append()` ~\\\\

---

### Data Structure & Algorithms FreeCodeCamp

__

#### Time Complexity
_How long it takes an algorithm to run_

#### Space Complexity
_The amount of memory taken up on a computer by an algorithm_














