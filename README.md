# LC-Ancestor
a program solution to the lowest common ancestor(s) problem of node x and y for DAGs (directed Acyclic Graphs) 

the way im solving this is by 

1. finding all the ancestors of x and setting a flag for visited

2. finding all the ancestors of y and if(flag == true) increment a count on the parent nodes

3. therefore all the LCAs(if there are any) are all the nodes that have both the flag set to true and a count of 0

