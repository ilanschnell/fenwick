Fenwick Tree implementation in Python
=====================================

Problem:
--------

  * array of numbers
  * two operations:
     - element update
     - prefix sum calculation

|                       | element update | prefix sum   |
| :---                  |     :---:      |   :---:      |
| array of elements     |     O(1)       |   O(n)       |
| array of prefix sums  |     O(n)       |   O(1)       |
| Fenwick tree          |     O(log n)   |   O(log n)   |
