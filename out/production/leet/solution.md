https://leetcode.com/problems/palindromic-substrings/

647\. Palindromic Substrings

Medium

Given a string `s`, return _the number of **palindromic substrings** in it_.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

```

**Example 2:**

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

```

**Constraints:**

-   `1 <= s.length <= 1000`
-   `s` consists of lowercase English letters.


This is a problem in which we'll explore structure. 
there are multiple ways to use structure to solve problems. 

A very common one, however, is using composition: 
> Break down a large structure into smaller blocks.


<style>

.alert-success {
    color: #155724;
    background-color: #d4edda;
    border-color: #c3e6cb;
}

.alert {
    position: relative;
    padding: .75rem 1.25rem;
    margin-bottom: 1rem;
    border: 1px solid transparent;
    border-radius: .25rem;
}

</style>

<div class="alert alert-success">

Breaking big problems into smaller ones, then solving them separately is the essence of dynamic programming.
</div>


Note, however, that we can do the exact opposite, that is:   
> Assemble a large structure starting from its components. 

<br></br>

<div class="alert alert-success">
In general, recognize a terminal case , and build from there. 
</div>


This is what we're going to explore in this problem. 
<br></br>

#

## 
A palindrome is always composed of other palidromes:
<br></br>

<table>
<thead>
  <tr>
    <th>r</th>
    <th>o</th>
    <th>t</th>
    <th>a</th>
    <th>v</th>
    <th>a</th>
    <th>t</th>
    <th>o</th>
    <th>r</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>v</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>a</td>
    <td>v</td>
    <td>a</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>t</td>
    <td>a</td>
    <td>v</td>
    <td>a</td>
    <td>t</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>o</td>
    <td>t</td>
    <td>a</td>
    <td>v</td>
    <td>a</td>
    <td>t</td>
    <td>o</td>
    <td></td>
  </tr>
  <tr>
    <td>r</td>
    <td>o</td>
    <td>t</td>
    <td>a</td>
    <td>v</td>
    <td>a</td>
    <td>t</td>
    <td>o</td>
    <td>r</td>
  </tr>
</tbody>
</table>

Each row demarks a palyndrome here.
Notice that saying "A palyndrome is always made of other palyndromes" also implies the reverse:

> "We can add letters around a palyndrome and get another palyndrome"

That means that the only way to get an palyndrome is to add letters around a single char ( terminal case )

<br></br>

##

#

We can visualize this as a matrix of "Reachability".

Consider each row as a 'starting index' and each
column as a 'ending index'. 
Each entry will hold a boolean value , denoting if the substring formed by indexing the source word with the corresponding indexes is a palyndrome or not.


The main diagonal of this matrix will refer to each
individual letter and hold the value true, since a single letter is a palyndrome. 

# 
<div>

<style type="text/css">
    /* Main Diag */
    .reachability tbody tr:nth-child(1) td:nth-child(2),
    .reachability tbody tr:nth-child(2) td:nth-child(3),
    .reachability tbody tr:nth-child(3) td:nth-child(4),
    .reachability tbody tr:nth-child(4) td:nth-child(5),
    .reachability tbody tr:nth-child(5) td:nth-child(6),
    .reachability tbody tr:nth-child(6) td:nth-child(7),
    .reachability tbody tr:nth-child(7) td:nth-child(8),
    .reachability tbody tr:nth-child(8) td:nth-child(9),
    .reachability tbody tr:nth-child(9) td:nth-child(10) {
        background-color: rgb(150, 50, 50);
    }

    /* Off Diag */

    .reachability tbody tr:nth-child(4) td:nth-child(7) {
        background-color: rgb(125, 50, 75);
    }


    .reachability tbody tr:nth-child(3) td:nth-child(8) {
        background-color: rgba(100, 50, 100);
    }

    .reachability tbody tr:nth-child(2) td:nth-child(9) {
        background-color: rgba(75, 50, 125);
    }


    .reachability tbody tr:nth-child(1) td:nth-child(10) {

        background-color: rgb(50, 50, 150);
    }

    /*  Borders */
    .reachability,
    .reachability thead tr th,
    .reachability tbody tr td {

        
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;

    }

    .reachability {
        width: 100%;
        height: 100%;
    }

    td {
        height: 7vw;
        /* width: 8vw; */


    }
</style>

<table class="reachability">
    <thead>
        <tr>
            <th></th>
            <th>r</th>
            <th>o</th>
            <th>t</th>
            <th>a</th>
            <th>v</th>
            <th>a</th>
            <th>t</th>
            <th>o</th>
            <th>r</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>r</td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>5</td>
        </tr>
        <tr>
            <td>o</td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>4</td>
            <td></td>
        </tr>
        <tr>
            <td>t</td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td>3</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>a</td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td>2</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>v</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>a</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>t</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>o</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
        </tr>
        <tr>
            <td>r</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
        </tr>
    </tbody>
</table>
</div>


#


Note that because every palyndrome MUST be made by
adding letters around a pre-existing palyndrome,
checking all possible palyndromes amounts to checking every neighbor ( top, right and diagonal ) index of known palyndromes, marking it accordingly, and repeating the process until every entry is filled.

 Here we use other numbers, alongside the gradient, to denote the direction of propagation of the "palyndroness" checking

What makes this process possibly complicated, however, is the manner in which we choose to check these neighbors. Note that some cells are neighboring many entries, and would be counted twice is a naive approach.


Here we paint in gray all the cells that are checked. With dotted white borders are the cells that would be checked twice: at the same time, they're above and to the right of a existing palyndrome.

<style type="text/css">
    /* Main Diag */
    .reachability2 tbody tr:nth-child(1) td:nth-child(2),
    .reachability2 tbody tr:nth-child(2) td:nth-child(3),
    .reachability2 tbody tr:nth-child(3) td:nth-child(4),
    .reachability2 tbody tr:nth-child(4) td:nth-child(5),
    .reachability2 tbody tr:nth-child(5) td:nth-child(6),
    .reachability2 tbody tr:nth-child(6) td:nth-child(7),
    .reachability2 tbody tr:nth-child(7) td:nth-child(8),
    .reachability2 tbody tr:nth-child(8) td:nth-child(9),
    .reachability2 tbody tr:nth-child(9) td:nth-child(10)
     {
        background-color: rgb(150, 50, 50);
    }


    .reachability2 tbody tr:nth-child(4) td:nth-child(7) {
        background-color: rgb(125, 50, 75);
    }


    .reachability2 tbody tr:nth-child(3) td:nth-child(8) {
        background-color: rgba(100, 50, 100);
    }

    .reachability2 tbody tr:nth-child(2) td:nth-child(9) {
        background-color: rgba(75, 50, 125);
    }


    .reachability2 tbody tr:nth-child(1) td:nth-child(10) {

        background-color: rgb(50, 50, 150);
    }

    .reachability2 tbody tr:nth-child(1) td:nth-child(3),
    .reachability2 tbody tr:nth-child(2) td:nth-child(4),
    .reachability2 tbody tr:nth-child(3) td:nth-child(5),
    .reachability2 tbody tr:nth-child(4) td:nth-child(6),
    .reachability2 tbody tr:nth-child(5) td:nth-child(7),
    .reachability2 tbody tr:nth-child(6) td:nth-child(8),
    .reachability2 tbody tr:nth-child(7) td:nth-child(9),
    .reachability2 tbody tr:nth-child(8) td:nth-child(10),
    .reachability2 tbody tr:nth-child(9) td:nth-child(11) {
        background-color: rgb(255, 255, 255, 0.2);
        border: 2px dotted rgba(255, 255, 255, 1);

    }

    .reachability2 tbody tr:nth-child(1) td:nth-child(4),
    .reachability2 tbody tr:nth-child(2) td:nth-child(5),
    .reachability2 tbody tr:nth-child(3) td:nth-child(6),
    .reachability2 tbody tr:nth-child(5) td:nth-child(8),
    .reachability2 tbody tr:nth-child(6) td:nth-child(9),
    .reachability2 tbody tr:nth-child(7) td:nth-child(10),
    .reachability2 tbody tr:nth-child(1) td:nth-child(9),
    .reachability2 tbody tr:nth-child(2) td:nth-child(8),
    .reachability2 tbody tr:nth-child(3) td:nth-child(7)
    {
        background-color: rgb(255, 255, 255, 0.2);
    }

    /* Off Diag */


    /*  Borders */
    .reachability2,
    td,
    th {

        
        text-align: center;

    }

    .reachability2 {
        width: 100%;
        height: 100%;
    }

    td {
        height: 8vw;


    }
</style>
<br></br>
<table class="reachability2">
    <thead>
        <tr>
            <th></th>
            <th>r</th>
            <th>o</th>
            <th>t</th>
            <th>a</th>
            <th>v</th>
            <th>a</th>
            <th>t</th>
            <th>o</th>
            <th>r</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>r</td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>5</td>
        </tr>
        <tr>
            <td>o</td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>4</td>
            <td></td>
        </tr>
        <tr>
            <td>t</td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td>3</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>a</td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td>2</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>v</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>a</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>t</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>o</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
        </tr>
        <tr>
            <td>r</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
        </tr>
    </tbody>
</table>
<br></br>

To avoid this double checking, instead of looking at the top, right and diag, we look only at the diag. This makes us miss the palydromes to the right, so we explicitly check for them.
Since the whole grid can be tiled by the combination of these two diagonals, we can be sure that we covered every possibility.


<style type="text/css">
    /* Main Diag */
    .reachability4 tbody tr:nth-child(1) td:nth-child(2),
    .reachability4 tbody tr:nth-child(2) td:nth-child(3),
    .reachability4 tbody tr:nth-child(3) td:nth-child(4),
    .reachability4 tbody tr:nth-child(4) td:nth-child(5),
    .reachability4 tbody tr:nth-child(5) td:nth-child(6),
    .reachability4 tbody tr:nth-child(6) td:nth-child(7),
    .reachability4 tbody tr:nth-child(7) td:nth-child(8),
    .reachability4 tbody tr:nth-child(8) td:nth-child(9),
    .reachability4 tbody tr:nth-child(9) td:nth-child(10)
     {
        background-color: rgb(150, 50, 50);
    }

    /* Block paint */
    
    .reachability4 tbody tr:nth-child(1) td:nth-child(4),
    .reachability4 tbody tr:nth-child(2) td:nth-child(5),
    .reachability4 tbody tr:nth-child(3) td:nth-child(6),
    .reachability4 tbody tr:nth-child(4) td:nth-child(7),
    .reachability4 tbody tr:nth-child(5) td:nth-child(8),
    .reachability4 tbody tr:nth-child(6) td:nth-child(9),
    .reachability4 tbody tr:nth-child(7) td:nth-child(10) {
        
        background-color: rgb(255, 255, 255, 0.2);

    }
    
    .reachability4 tbody tr:nth-child(1) td:nth-child(6),
    .reachability4 tbody tr:nth-child(2) td:nth-child(7),
    .reachability4 tbody tr:nth-child(3) td:nth-child(8),
    .reachability4 tbody tr:nth-child(4) td:nth-child(9),
    .reachability4 tbody tr:nth-child(5) td:nth-child(10){
        
        background-color: rgb(255, 255, 255, 0.05);

    }
    
    .reachability4 tbody tr:nth-child(1) td:nth-child(8),
    .reachability4 tbody tr:nth-child(2) td:nth-child(9),
    .reachability4 tbody tr:nth-child(3) td:nth-child(10){
    
        background-color: rgb(255, 255, 255, 0.01);

    }

    .reachability4 tbody tr:nth-child(1) td:nth-child(3),
    .reachability4 tbody tr:nth-child(2) td:nth-child(4),
    .reachability4 tbody tr:nth-child(3) td:nth-child(5),
    .reachability4 tbody tr:nth-child(4) td:nth-child(6),
    .reachability4 tbody tr:nth-child(5) td:nth-child(7),
    .reachability4 tbody tr:nth-child(6) td:nth-child(8),
    .reachability4 tbody tr:nth-child(7) td:nth-child(9),
    .reachability4 tbody tr:nth-child(8) td:nth-child(10)
     {
        border: 2px dotted rgba(255, 255, 255, 1);
        

    }

    .reachability4 tbody tr:nth-child(1) td:nth-child(5),
    .reachability4 tbody tr:nth-child(2) td:nth-child(6),
    .reachability4 tbody tr:nth-child(3) td:nth-child(7),
    .reachability4 tbody tr:nth-child(4) td:nth-child(8),
    .reachability4 tbody tr:nth-child(5) td:nth-child(9),
    .reachability4 tbody tr:nth-child(6) td:nth-child(10)
     {
        border: 2px dotted rgba(255, 255, 255, 0.5);
        

    }
    .reachability4 tbody tr:nth-child(1) td:nth-child(7),
    .reachability4 tbody tr:nth-child(2) td:nth-child(8),
    .reachability4 tbody tr:nth-child(3) td:nth-child(9),
    .reachability4 tbody tr:nth-child(4) td:nth-child(10)
     {
        border: 2px dotted rgba(255, 255, 255, 0.3);
        

    }
    .reachability4 tbody tr:nth-child(1) td:nth-child(9),
    .reachability4 tbody tr:nth-child(2) td:nth-child(10)
     {
        border: 2px dotted rgba(255, 255, 255, 0.2);
        

    }

    

    /* Off Diag */


    /*  Borders */
    .reachability4,
    td,
    th {

        /* border-collapse: collapse; */
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;

    }

    .reachability4 {
        table-layout: fixed;
        width: 100%;
        height: 100%;
    }

    td {
        height: 8vw;


    }
</style>
<br></br>
<table class="reachability4">
    <thead>
        <tr>
            <th></th>
            <th>r</th>
            <th>o</th>
            <th>t</th>
            <th>a</th>
            <th>v</th>
            <th>a</th>
            <th>t</th>
            <th>o</th>
            <th>r</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>r</td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>5</td>
        </tr>
        <tr>
            <td>o</td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>4</td>
            <td></td>
        </tr>
        <tr>
            <td>t</td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td>3</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>a</td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td>2</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>v</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>a</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>t</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>o</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td></td>
        </tr>
        <tr>
            <td>r</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
        </tr>
    </tbody>
</table>


#

There are parallels that can be traced to laplacian methods, in which we translate the original problem into coordinates that inately satisfy the bounds when transformed back.

This can be seen as a coordinate transformation ( from row : column to evenness:radius , where evenness denotes if we're in a even or odd diagonal. )


    