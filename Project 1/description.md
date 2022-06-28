<h1>Project 1: Doubly Linked Lists &amp; Recursion</h1>
<p><strong>Due: Thursday, September 24th @ 8:00pm</strong></p>
<p><em>This is not a team project, do not copy someone else&rsquo;s work.</em></p>
<p>&nbsp;</p>
<h2>Assignment Overview</h2>
<h3>Linked Lists</h3>
<p>A Linked List is a sequence data structure that provides association between objects through links.</p>
<h1><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/2ad5ee45-9700-4d16-9456-153c2b6fde0f/Untitled%20Diagram.svg" alt="Untitled Diagram.svg" width="677" height="155" /></h1>
<h3 style="text-align: right;"><sub>Singly linked list implementation</sub></h3>
<p>A well known current application of this is within the blockchain space. In a more general sense, you could think of a music playlist as a doubly linked list where each song is a node and there is a previous and next option as the links to navigate to each neighboring song in the playlist.</p>
<p>Linked Lists have underlying <strong>applications in abstract data structures</strong> such as trees and graphs (upcoming projects!). They are relatively simple to implement and provide <strong>easy insertions and deletions</strong> by managing pointers that does not require shifting elements like an array does. Because a linked list can increase and decrease on runtime, it only <strong>allocates memory when needed</strong> providing no memory wastage.&nbsp;</p>
<h4>Project</h4>
<p>You will be creating a <strong>cyclic doubly linked list</strong>. In this context, cyclic refers to the list forming a circular dependency or in other words forming a circle/cycle.</p>
<p>This will represent the underlying implementation of a <strong><a href="https://www.cplusplus.com/reference/list/list/">c++ List</a></strong>.&nbsp;I implore you to look at the core code that c++ uses for their list and use this to help you in your project. You can find an example of this here: <a href="https://www.rrsd.com/software_development/stl/stl/stl_list.h" target="_blank" rel="noopener noreferrer">STL_List</a>. Download this page, and open it up in an editor. This is not necessary, but can be helpful and pretty interesting.</p>
<p>This is what our data looks like. Here, we have a root <strong>node</strong> that provides access to the front and back of the list.&nbsp;</p>
<h1><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/4a389b3e-4a33-4188-9c64-c64e2b9e4300/Untitled%20Diagram%20%285%29.png" alt="Untitled Diagram (5).png" width="653" height="119" /></h1>
<h3 style="text-align: right;"><sub>Doubly linked list implementation</sub></h3>
<h3>Recursion</h3>
<p>Recursion is a technique that involves a function calling itself directly or indirectly.&nbsp; You will be implementing recursive functions within your List class when specified.</p>
<h2><img style="float: right;" src="https://s3.amazonaws.com/mimirplatform.production/files/dfe40e90-8f7b-4add-a99e-a45106b100e1/Screen%20Shot%202020-08-24%20at%207.30.05%20PM.png" alt="Screen Shot 2020-08-24 at 7.30.05 PM.png" width="256" height="136" /></h2>
<p>&nbsp;</p>
<p><sup><strong>Fun Fact: Type the word "recursion" into google. It is spelled correctly, but still says "Did you mean: <em>recursion</em>". When you click on it, the page will redirect to the same page. This resembles an infinite loop and exemplifies the meaning of recursion</strong>!</sup></p>
<h2>&nbsp;</h2>
<h2>Assignment Notes</h2>
<p>IMPORTANT: <strong>Only</strong> when inserting, pushing back or pushing front are you able to create a new Node object. You <strong>cannot</strong> create a new List object at all. You <strong>cannot</strong> use any container such as a Python list or string (with the exception of the __str__ method). <span style="text-decoration: underline;">Violation of this will result in the loss of all points for the related method.</span></p>
<ul>
<li>Docstrings have been provided for you in this project <span style="text-decoration: underline;">only</span>. Refer back to this project in order to reference how functions should be documented (<strong>description + parameter(s) + return</strong>).</li>
<li>Test cases will not test mismatching types. Example: <strong>List(container=[1, "a"])</strong>, and they should be able to handle any defined type as they are type-agnostic.</li>
<li>The methods below are given in a suggested logical order of implementation. Hint: perhaps you can utilize some methods presented earlier in the later...</li>
<li>Python allows comparison by reference using the keyword <span style="font-family: 'courier new', courier, monospace;">is<span style="font-family: geomanist, sans-serif;">. T</span></span>his will be very important in your project. Learn more about this <a href="https://www.geeksforgeeks.org/python-object-comparison-is-vs/">here</a>.</li>
<li>Note that for this project the test cases ONLY rely on the method/s they are testing (Yay!). In future projects, this may not be true.</li>
<li><strong>Types</strong>:
<ul>
<li><strong>T</strong>: Generic Type<br />
<ul>
<li>c++ List nodes' values are type-agnostic and also homogenous in type</li>
</ul>
</li>
<li><strong>Node</strong>: DoublyLinkedListNode&nbsp;</li>
<li>... types? What is <strong>Python Typing</strong>??
<ul>
<li>Mimics strongly &nbsp;typed languages such as &nbsp;C++ and Java, but does <em>not</em> enforce the types (new in Python 3.5)</li>
<li>Example:
<ul>
<li><strong><span style="font-family: monospace, monospace; font-size: 1em; background-color: transparent;">def foo(var: Generic[T]) -&gt; int:</span></strong></li>
<li><span style="font-family: geomanist, sans-serif; font-size: 1em; background-color: transparent;">This indicates we have a template parameter type of T with an int type as the return</span></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="list-style-type: none;">
<ul>
<li><span style="text-decoration: underline;">Benefits</span>: aids in debugging by indicating mismatching types for parameters and returns. It also provides cleaner code and documentation.</li>
<li>For those of you who use <a href="https://leetcode.com/problemset/all/">LeetCode's</a> Python3 IDE this should look familiar</li>
<li>Try this out on your own and reference the starter code for more clarity</li>
<li>Resources to learn more about Python Typing:</li>
</ul>
</li>
</ul>
</li>
</ul>
<ol>
<li style="list-style-type: none;">
<ol>
<li style="list-style-type: none;">
<ol>
<li style="list-style-type: none;">
<ol>
<li><a href="https://docs.python.org/3/library/typing.html#module-typing">Python Typing Docs</a></li>
<li><a href="https://realpython.com/python-type-checking/">Real Python - Good descriptive analysis</a></li>
<li><a href="https://mypy.readthedocs.io/en/stable/generics.html">Generics</a></li>
</ol>
</li>
</ol>
</li>
</ol>
</li>
</ol>
<ul>
<li><strong>Inner Functions</strong>:
<ul>
<li>We will be utilizing inner functions within some methods:</li>
<li>
<p><strong><span style="font-family: 'courier new', courier, monospace;">def foo(x):</span></strong></p>
<p><strong><span style="font-family: 'courier new', courier, monospace;">&nbsp; &nbsp; def inner_foo():</span></strong></p>
<p><strong><span style="font-family: 'courier new', courier, monospace;">&nbsp; &nbsp; &nbsp; &nbsp; print(x) </span></strong><span style="font-family: 'courier new', courier, monospace;"># I can access x!</span></p>
<p><strong><span style="font-family: 'courier new', courier, monospace;">&nbsp; &nbsp; inner_foo()</span></strong></p>
</li>
<li>Fibonacci Example (not very practical, but relatable):
<div class="line number1 index0 alt2">
<div class="line number1 index0 alt2"><span style="font-family: 'courier new', courier, monospace;"><strong><code class="python keyword">def</code> <code class="python plain">fib(n):</code></strong></span></div>
<div class="line number1 index0 alt2"><span style="font-family: 'courier new', courier, monospace;"><strong><code class="python plain"><code class="python spaces">&nbsp; &nbsp; def inner_fib(num):</code></code></strong></span></div>
<div class="line number3 index2 alt2"><span style="font-family: 'courier new', courier, monospace;"><strong><code class="python spaces">&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;</code><code class="python keyword">if</code> <code class="python plain">num &lt;=</code><code class="python value">&nbsp;1</code><code class="python plain">:</code></strong></span></div>
<div class="line number4 index3 alt1"><span style="font-family: 'courier new', courier, monospace;"><strong><code class="python spaces">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </code><code class="python keyword">return</code> num</strong></span></div>
<div class="line number5 index4 alt2"><span style="font-family: 'courier new', courier, monospace;"><strong><code class="python spaces"></code></strong><strong><code class="python value"></code></strong></span></div>
<div class="line number7 index6 alt2"><span style="font-family: 'courier new', courier, monospace;"><strong><code class="python spaces">&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;</code></strong></span><span style="font-family: 'courier new', courier, monospace;"><strong><code class="python keyword">return</code> <code class="python plain"><code class="python spaces">inner_fib</code></code><code class="python plain">(num </code><code class="python keyword">-</code> <code class="python value">1</code><code class="python plain">) </code><code class="python keyword">+</code> <code class="python plain"><code class="python spaces">inner_fib</code></code><code class="python plain">(num </code><code class="python keyword">-</code> <code class="python value">2</code><code class="python plain">)</code></strong></span></div>
<div class="line number9 index8 alt2"><span style="font-family: 'courier new', courier, monospace;"><strong>&nbsp; &nbsp; return inner_fib(n)</strong></span></div>
</div>
&nbsp;<sub>Additional reference: <a href="https://realpython.com/inner-functions-what-are-they-good-for/">Real Python - Inner Functions</a></sub></li>
</ul>
</li>
</ul>
<div class="line number9 index8 alt2">&nbsp;</div>
<h2>Assignment Specifications</h2>
<h3>class SinglyLinkedListNode:&nbsp;</h3>
<p><strong><em>DO NOT MODIFY this class</em></strong></p>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>val</strong>: value of self</li>
<li><strong>nxt</strong>: SinglyLinkedListNode - links next node</li>
</ul>
</li>
</ul>
<ul>
<li><strong style="background-color: transparent; font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';">__init__(self, val, nxt=None)</strong><br />
<ul>
<li><strong>val</strong>: <strong>T</strong>&nbsp;</li>
<li><strong>nxt</strong>: SinglyLinkedListNode</li>
<li>Assigns value of&nbsp;<strong>val&nbsp;</strong>and next node of&nbsp;<strong>nxt</strong></li>
</ul>
</li>
<li><strong>__str__(self)</strong>
<ul>
<li>Representation of <strong>val </strong>as a string</li>
<li><span style="text-decoration: underline;">Return</span>: str</li>
</ul>
</li>
<li><strong>__repr__(self)</strong>
<ul>
<li>Representation as a string utilizing <strong>__str__</strong></li>
<li><span style="text-decoration: underline;">Return</span>: str</li>
</ul>
</li>
<li><strong>__eq__(self, other)</strong>
<ul>
<li><strong>other</strong>: SinglyLinkedListNode</li>
<li>Compares this node for equality with another node by evaluating each <strong>val</strong></li>
<li><span style="text-decoration: underline;">Return</span>: bool</li>
</ul>
</li>
</ul>
<h3>class DoublyLinkedListNode(SinglyLinkedListNode):&nbsp;</h3>
<p><strong><em>DO NOT MODIFY this class</em></strong></p>
<ul>
<li><strong>Attribute</strong>
<ul>
<li><strong>prev</strong>: DoublyLinkedListNode - links previous node</li>
</ul>
</li>
</ul>
<ul>
<li><strong style="background-color: transparent; font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';">__init__(self, val, nxt=None, prev=None)</strong><br />
<ul>
<li><strong>val</strong>: <strong>T</strong>&nbsp;</li>
<li><strong>nxt</strong>: DoublyLinkedListNode</li>
<li><strong>prev</strong>: DoublyLinkedListNode</li>
<li>Assigns value of&nbsp;<strong>val,</strong>&nbsp;next node of&nbsp;<strong>nxt</strong>, and the previous node of&nbsp;<strong>prev</strong></li>
<li>Calls upon the constructor of its super class, SinglyLinkedListNode to assign <strong>val</strong> and <strong>nxt</strong></li>
</ul>
</li>
<li><strong>__eq__(self, other)</strong>
<ul>
<li><strong>other</strong>: DoublyLinkedListNode</li>
<li>Compares this node for equality with another node by evaluating each <strong>val</strong></li>
<li><span style="text-decoration: underline;">Return</span>: bool</li>
</ul>
</li>
</ul>
<p><sub>Note: Doubly Linked List Node derives from Singly Linked List Node&nbsp; to emphasize differences and overlaps between the two</sub></p>
<h3>class List:&nbsp;</h3>
<p>Represents an adaptation of a the c++ List implementation with the underlying data structure being a cyclic doubly linked list</p>
<p><strong><em>DO NOT MODIFY the following attribute/functions</em></strong></p>
<ul>
<li><strong>Attribute</strong>
<ul>
<li><strong>node</strong>: Node&nbsp;
<ul>
<li><span style="text-decoration: underline;">Root</span> node having a value of None</li>
<li>Serves as the <span style="text-decoration: underline;">head</span> and <span style="text-decoration: underline;">tail</span> as well as the access point for the lists' nodes</li>
<li><em>Note:</em> The <span style="text-decoration: underline;">root</span> is not identified by the value of None. Any node can technically have a value of None. The root is identified by reference using the keyword "is"&nbsp;<br />
<ul>
<li>example: <span style="font-family: 'courier new', courier, monospace;">node is self.node</span></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li><strong style="background-color: transparent; font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';">__init__(self, num=None, val=None, container=None)</strong>
<ul>
<li><strong>num</strong>: int</li>
<li><strong>val</strong>: <strong>T&nbsp;</strong></li>
<li><strong>container</strong>: Python list containing elements of <strong>T </strong>type</li>
<li>Creates root <strong>node</strong> and sets its prev and next member variable to itself</li>
<li>Assigns list with param values given (see <strong>assign</strong> method below for <strong>num</strong>, <strong>val</strong>, and <strong>container</strong> parameter meanings)</li>
<li><em>Time Complexity: O(n) --&gt; <span style="text-decoration: underline;">parameter n</span></em></li>
</ul>
</li>
<li><strong>__repr__(self)</strong>
<ul>
<li>Represents the list as a string utilizing <strong>__str__</strong></li>
<li><span style="text-decoration: underline;">Return</span>: str</li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
</li>
</ul>
<ul>
<li><strong>__eq__(self, other)</strong>
<ul>
<li><strong>other</strong>: List</li>
<li>Compares this List for equality with another List</li>
<li><span style="text-decoration: underline;">Return</span>: bool</li>
<li><em>Time Complexity: O(min(N, M)) --&gt; M is size of other&nbsp;&nbsp;</em></li>
</ul>
</li>
<li><strong>assign(self, num=None, val=None, container=None)</strong>
<ul>
<li><strong>num</strong>: int</li>
<li><strong>val</strong>: <strong>T</strong>&nbsp;</li>
<li><strong>container</strong>: Python list containing elements of <strong>T </strong>type</li>
<li>Populates self with nodes using the given parameters</li>
<li><strong>num</strong> represents the number of occurrences of <strong>val</strong> to assign to list. If <strong>val&nbsp;</strong>is not given, None is used.</li>
<li><strong>container&nbsp;</strong>is used to generate nodes based on its contents</li>
<li>Only valid combinations of use:<br />
<ul>
<li><strong>assign(num)</strong></li>
<li><strong>assign(num, val)</strong></li>
<li><strong>assign(container)</strong></li>
</ul>
</li>
<li>Note: This method is mainly used for testing or in other words to quickly generate nodes for a List. Take a look at the code given in the <strong>__init__</strong> as well as the visible testcases to understand more</li>
<li><em>Time Complexity: O(len(container)) || O(num)&nbsp;</em></li>
</ul>
</li>
<li><strong>clear(self)</strong>
<ul>
<li>Resets list by reassigning root <strong>node</strong>s' references to itself</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
</ul>
<p><strong><em>IMPLEMENT the following functions</em></strong></p>
<ul>
<li><strong>empty(self)</strong>
<ul>
<li><span style="text-decoration: underline;">Return</span>: bool - if List contains any additional nodes other than the root <strong>node</strong>, return False else True</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
<li><strong>front(self)</strong>
<ul>
<li><span style="text-decoration: underline;">Return</span>: Node - first node in the list&nbsp;or root <strong>node</strong> if empty</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
<li><strong>back(self)</strong>
<ul>
<li><span style="text-decoration: underline;">Return</span>: Node - last node in the list or root <strong>node</strong> if empty</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
<li><strong>swap(self, x)</strong>
<ul>
<li><strong>x</strong>: List</li>
<li>Swaps contents of lists</li>
<li>Hint: what holds references to all the nodes in a <strong>List</strong>?</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
<li><strong>__str__(self)</strong>
<ul>
<li><strong>MUST BE WRITTEN RECURSIVELY </strong>Must call inner function <strong>to_string(node)</strong> which is to be implemented recursively</li>
<li>Represents the list as a string&nbsp;
<ul>
<li><strong>1 &lt;-&gt; 2 &lt;-&gt; ...</strong>&nbsp; i.e., <strong>node.val &lt;-&gt; node.val &lt;-&gt; ...</strong>&nbsp;</li>
</ul>
</li>
<li><span style="text-decoration: underline;">Return</span>: str</li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
</li>
<li><strong>size(self)</strong>
<ul>
<li><strong>MUST BE WRITTEN RECURSIVELY </strong>Must call inner function <strong>size_list(node)</strong> which is to be implemented recursively</li>
<li><span style="text-decoration: underline;">Return</span>: int - size of list or number of nodes not including the root <strong>node</strong></li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
</li>
<li><strong>insert(self, position, val, num=1)</strong>
<ul>
<li><strong>position</strong>: Node</li>
<li><strong>val</strong>: <strong>T</strong></li>
<li><strong>num</strong>:&nbsp; int</li>
<li><strong>MUST BE WRITTEN RECURSIVELY</strong></li>
<li>Places node <span style="text-decoration: underline;">before</span> given <strong>position</strong> node with a val of&nbsp;<strong>val</strong></li>
<li>When <strong>num</strong> is given, insert <strong>num</strong> occurrences of node</li>
<li><span style="text-decoration: underline;">Return</span>: Node - node that points to the first of the newly inserted nodes</li>
<li><em>Time Complexity: O(num)&nbsp;</em></li>
</ul>
</li>
<li><strong>erase(self, first, last=None)</strong>
<ul>
<li><strong>first</strong>: Node</li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>last</strong>: Node</li>
<li>Erases node or nodes in list from first to, but not including last: [first, last). When last is not given, erase only first node</li>
<li><span style="text-decoration: underline;">Return</span>: Node - node that followed the last node erased</li>
<li>Example: <strong>0 &lt;-&gt; 1 &lt;-&gt; 2</strong><br />
<ul>
<li><strong>first</strong> = Node(1) --&gt; <strong>0 &lt;-&gt; 2 return node 2</strong></li>
<li><strong>first</strong> = Node(1) , <strong>last</strong> = Node(2) --&gt; <strong>0 &lt;-&gt; 2 return node 2</strong></li>
</ul>
</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
<li><strong>push_front(self, val)</strong>
<ul>
<li><strong>val</strong>:&nbsp;<strong>T</strong></li>
<li>Inserts new Node with value of <strong>val&nbsp;</strong>in the front of the list</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
</ul>
<ul>
<li><strong>push_back(self, val)</strong>
<ul>
<li><strong>val</strong>:&nbsp;<strong>T</strong></li>
<li>Inserts new Node with value of <strong>val&nbsp;</strong>in the back of the list</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
</ul>
<ul>
<li><strong>pop_front(self)</strong><br />
<ul>
<li>Erases Node<strong>&nbsp;</strong>in the front of the list</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
</ul>
<ul>
<li><strong>pop_back(self)</strong><br />
<ul>
<li>Erases Node in the&nbsp;back of the list</li>
<li><em>Time Complexity: O(1)</em></li>
</ul>
</li>
<li><strong>remove(self, val)</strong>
<ul>
<li><strong>val</strong>: <strong>T</strong>&nbsp;</li>
<li><strong>MUST BE WRITTEN RECURSIVELY </strong>Must call inner function <strong>remove_node(node)</strong> which is to be implemented recursively</li>
<li>Removes all nodes in the List containing a value of <strong>val</strong></li>
<li><strong>CANNOT call erase</strong></li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
</li>
</ul>
<ul>
<li><strong>remove_if(self, pred)</strong>
<ul>
<li><strong>pred</strong>: Predicate function
<ul>
<li>
<p class="p1"><span class="s1">Simply said, a predicate function is a function that returns a bool. In this instance, it is a unary predicate that takes in one parameter.</span></p>
</li>
<li><span class="s1">Feel free to create your own predicate functions in testing &amp; google them. Also, r</span><span class="s1">eference the visible test case.</span></li>
<li><span class="s1">Example: <span style="font-family: 'courier new', courier, monospace;">pred(node.val)&nbsp;</span></span></li>
<li><span class="s1">Click <a href="https://stackoverflow.com/questions/5921609/what-is-predicate-in-c">here</a></span><span class="s1"> to learn more.</span></li>
</ul>
</li>
<li><strong>MUST BE WRITTEN RECURSIVELY </strong>Must call inner function <strong>remove_if</strong><strong>(node)</strong> which is to be implemented recursively</li>
<li>Removes all Nodes when <strong>pred&nbsp;</strong>returns True</li>
<li><strong>CANNOT call erase</strong></li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
</li>
<li><strong>reverse(self)</strong><br />
<ul>
<li><strong>MUST BE WRITTEN RECURSIVELY </strong>Must call inner function <strong>reverse_list(node)</strong> which is to be implemented recursively</li>
<li>Reverses linked list <span style="text-decoration: underline;">in place, without using additional memory or in other words the addition of new List/Node objects.</span></li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
</li>
<li><strong>unique(self)</strong><br />
<ul>
<li><strong>MUST BE WRITTEN RECURSIVELY </strong>Must call inner function <strong>unique</strong><strong>_list(node)</strong> which is to be implemented recursively</li>
<li>Removes all but one element from every consecutive group of equal elements in the container</li>
<li>Examples:
<ul>
<li><strong>1 &lt;-&gt; 1 &lt;-&gt; 2 &lt;-&gt; 1 </strong>&nbsp; results in&nbsp; <strong>1 &lt;-&gt; 2 &lt;-&gt; 1</strong></li>
<li><strong>5 &lt;-&gt; 3 &lt;-&gt; 2 &lt;-&gt; 2</strong><strong> &lt;-&gt; 3 &lt;-&gt; 3 &lt;-&gt; 3 </strong>&nbsp;results in <strong>5 </strong><strong>&lt;-&gt; 3 &lt;-&gt; 2</strong><strong> &lt;-&gt; 3</strong></li>
</ul>
</li>
<li><strong>CANNOT call erase</strong></li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
</li>
</ul>
<h2>&nbsp;</h2>
<h2>Application</h2>
<p>You are a co-creator of a music player app, and there is a bug in your code that corrupted some users' playlists and left others untouched. As mentioned earlier, a music playlist can be a representation of a doubly linked list.&nbsp;</p>
<p><span style="text-decoration: underline;">There are three ways this bug affected your doubly linked lists*:</span></p>
<p>1. <span style="text-decoration: underline;">Proper</span> - no change</p>
<p>2. <span style="text-decoration: underline;">Broken</span> - unconnected Linked List that is linear</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/34a590f9-0e07-4f3a-839b-4dba18cd3aaf/Untitled%20Diagram%20%287%29.png" alt="Untitled Diagram (7).png" width="473" height="64" /></p>
<p>3. <span style="text-decoration: underline;">Improper</span> - creates an incorrect cycle&nbsp;</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/e476fca2-a201-4378-9458-df6ea8fa11fd/Untitled%20Diagram%20%286%29.png" alt="Untitled Diagram (6).png" width="425" height="87" /></p>
<p><sub>*Proper, broken and improper are names created just for this context and do not represent terms for linked lists in general</sub></p>
<p>&nbsp;</p>
<p><span style="text-decoration: underline;">Task</span>: Create a program using <strong>Floyd's Cycle Finding Algorithm</strong> that will correct the given playlists by fixing the linked lists that do not make a cycle (2), or identifying those linked lists that create incorrect circular dependencies (3) to let your co-creator fix those with his program.</p>
<h4><strong>Floyd's Cycle Finding Algorithm</strong></h4>
<p>Simple algorithm that uses two pointers, <span style="text-decoration: underline;">slow</span> and <span style="text-decoration: underline;">fast</span> in order to detect a cycle in a linked list. The slow moves at an increment of one node, while the fast moves at an increment of two. The nodes will either reach the end of the list or will run into each other confirming a cyclic linked list.</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/cfc7d8f9-c3ad-4ddd-ac3e-81e4e986170e/ezgif.com-crop.gif" alt="ezgif.com-crop.gif" width="466" height="177" /></p>
<p style="text-align: right;"><strong><sub>This is an example of Floyd's Algorithm on an improper linked list.</sub></strong></p>
<p><a href="https://en.wikipedia.org/wiki/Cycle_detection">Wiki Resource on Floyd's Algorithm</a></p>
<p><a href="https://www.youtube.com/watch?v=MFOAbpfrJ8g&amp;ab_channel=HackerRank">Video on Floyd's Algorithm</a></p>
<p>&nbsp;</p>
<p><strong>fix_playlist(lst)</strong></p>
<ul>
<li><strong>lst</strong>: List</li>
<li>Must call inner function <strong>fix_playlist_helper</strong><strong>(slow, fast)</strong>&nbsp;which&nbsp;<strong>MUST BE WRITTEN RECURSIVELY</strong></li>
<li>Checks if the given <strong>lst</strong> is <span style="text-decoration: underline;">proper</span>(1), <span style="text-decoration: underline;">broken</span>(2), or <span style="text-decoration: underline;">improper</span>(3)</li>
<li><span style="font-family: geomanist, sans-serif;">It is broken when there is no cycle</span></li>
<li>It is improper when <strong>lst</strong> forms a cycle with a node other than the root node</li>
<li><span style="font-family: geomanist, sans-serif;">If proper or broken, return True. If improper, return False</span></li>
<li><strong><span style="font-family: geomanist, sans-serif;">MUST</span></strong>
<ul>
<li><strong><span style="font-family: geomanist, sans-serif;">fix Lists that are <span style="text-decoration: underline;">broken</span> in place</span></strong></li>
<li><strong><span style="font-family: geomanist, sans-serif;">use Floyd's Cycle Finding Algorithm (above)</span></strong></li>
</ul>
</li>
<li><strong>CANNOT </strong>
<ul>
<li><strong>call any List methods </strong></li>
<li><strong>create any new Nodes or Lists</strong></li>
<li><strong>read prev values on nodes, you can only assign them</strong>
<ul>
<li><strong>example that is not allowed: <span style="font-family: 'courier new', courier, monospace;">if lst.node.prev is None</span></strong></li>
</ul>
</li>
</ul>
</li>
<li><em>Note1 </em>: Fixing an improper list was not included in order to reduce the problem's difficulty level. I would suggest looking it up if you are curious on the possible implementations for this.</li>
<li><em>Note2 </em>: Recognize the difference between <span style="text-decoration: underline;">broken</span> and <span style="text-decoration: underline;">improper</span>. Broken does <em>not&nbsp;</em>have a cycle while improper has an incorrect cycle.</li>
<li><em>Note3 </em>: This only accounts for forward pointers, you do not need to check for backwards pointers, but of course must have those properly assigned in the solution.</li>
<li><span style="text-decoration: underline;">Return</span>: bool</li>
<li><em>Time Complexity: O(N)</em></li>
</ul>
<p>&nbsp;</p>
<h2>Submission</h2>
<h4>Deliverables</h4>
<p>Be sure to upload the following deliverables in a .zip folder to Mimir by 8:00p Eastern Time on Thursday, 9/24/20.</p>
<pre><code>Project1.zip
    |<span class="hljs-type">&mdash; Project1</span>/
        |<span class="hljs-type">&mdash; README</span>.md        (<span class="hljs-keyword">for</span> project feedback)
        |<span class="hljs-type">&mdash; __init__</span>.py      (<span class="hljs-keyword">for</span> proper Mimir testcase loading)
        |<span class="hljs-type">&mdash; List</span>.py      (contains your solution source code)<br />        |<span class="hljs-type">&mdash; Node</span>.py      (supports List.py)<br /><br /></code></pre>
<h4>Grading</h4>
<ul>
<li>Tests (80)
<ul>
<li>Visible / Hidden Tests: __/80</li>
</ul>
</li>
<li>Manual (20)<br />
<ul>
<li>Time Complexity: __/18
<ul>
<li><strong>front, back, swap, empty, push_front, push_back, pop_front, pop_back</strong><strong>: </strong>0.5 each (4 total)</li>
<li><strong>size, string, insert, erase</strong><strong>: </strong>1 each (4 total)</li>
<li><strong>remove, remove_if, reverse, unique, fix_playlist : </strong>2 each (10 total)</li>
</ul>
</li>
<li>README.md is <em>completely</em> filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/2</li>
</ul>
</li>
</ul>
<p>&nbsp;</p>
<p>Project designed by Anna De Biasi</p>