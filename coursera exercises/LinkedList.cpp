//============================================================================
// Name        : LinkedList.cpp
// Author      : Yannik
// Version     :
// Copyright   :
// Description : Linked List in C++
//============================================================================

#include <cstdlib>
#include <iostream>

using namespace std;

template <typename T>
class Node
{
public:
	T data;
	// introduce a 'next' node for doubly linked list
	Node<T>* next;
	Node<T>* prev;
	Node<T>() { prev = NULL; next = NULL; data = 0; }
	Node<T>(T t) { prev = NULL; next = NULL; data = t; }
};

// Convert Singly Linked List to Doubly Linked List
template <typename T>
class DList
{
public:
	Node<T>* head;
	Node<T>* tail;
	// introduce 'head' node for double link
	DList() { head = NULL; tail = NULL; }  // default constructor
	// appends to tail of list
	void Append(T data)
	{
		Node<T>* pdata = new Node<T>(data);
		if (tail == NULL)
		{
			tail = pdata;
			head = pdata;
		}
		else
		{
			pdata->prev = tail;
			tail->next = pdata;
			tail = pdata;
		}
	}
	// prepends to head of list
	void Prepend(T data)
	{
		//
		Node<T>* pdata = new Node<T>(data);
		if (head == NULL)
		{
			head = pdata;
			tail = pdata;
		}
		else
		{
			pdata->next = head;
			head->prev = pdata;
			head = pdata;
		}
	}
	// inserts data after found data
	void InsertAfter(T find, T data)
	{
		//
		Node<T>* pdata = new Node<T>(data);
		Node<T>* temp = head;
		// traverse to find the location to insert data
		while( temp->next != NULL) {
			if (temp->data == find) {
				pdata->next = temp->next;
				temp->next = pdata;
				pdata->prev = temp;
				pdata->next->prev = pdata;
				return;
			}
			temp = temp->next;
		}
		if (temp->data == find) {
			temp->next = pdata;
			pdata->prev = temp;
			tail = pdata;
			return;
		}
		// If we cannot find the data
		cout << "Data not found" << endl;
	}
	// inserts data before found data
	void InsertBefore(T find, T data)
	{
		//
		Node<T>* pdata = new Node<T>(data);
		Node<T>* prev_node;
		Node<T>* temp = head;
		// traverse to find the location to insert data
		if (temp != NULL && temp->data == find){
			pdata->next = temp;
			temp->prev = pdata;
			head=pdata;
		}

		while( temp != NULL) {
			if (temp->data == find) {
				prev_node = temp->prev;
				pdata->next = temp;
				prev_node->next = pdata;
				pdata->prev = prev_node;
				temp->prev = pdata;
				return;
			}
			temp = temp->next;
		}
		// If we cannot find the data
		cout << "Data not found" << endl;
	}
	// finds data node and returns it
	Node<T>* Search(T data)
	{
		//
		Node<T>* temp = head;
		// traverse to find the location to insert data
		while( temp != NULL) {
			if (temp->data == data) {
				cout << "Found the node with data: " << temp->data << "\n";
				return temp;
			}
			temp = temp->next;
		}
		// If we cannot find the data
		cout << "Data not found" << endl;
		return NULL;
	}
	// deletes a node from the list
	void Delete(T data)
	{
		//
		Node<T>* temp = head;
		Node<T>* prev_node;
		if (temp != NULL && temp->data == data){
			head = temp->next;
			free(temp);
			return;
		}
		// traverse to find the location to insert data
		while( temp != NULL) {
			if (temp->data == data) {
				prev_node = temp->prev;
				prev_node->next = temp->next;
				if (temp != tail){
					(temp->next)->prev = prev_node;
				}
				else {
					tail = prev_node;
				}
				free(temp);
				return;
			}
			temp = temp->next;
		}
		// If we cannot find the data
		cout << "Data not found" << endl;

	}
	// remove tail
	void DeleteTail(){
		if (tail != NULL) {
			Node<T>* temp = tail;
			Node<T>* prev_node;
			prev_node = temp->prev;
			prev_node->next = temp->next;
			tail = prev_node;
			free(temp);
		}
	}
	// remove head
	void DeleteHead(){
		if (head != NULL) {
			Node<T>* temp = head;
			head = temp->next;
			free(temp);
		}
	}
	// retrieve head
	T RetrieveHead(){
		if (head != NULL) {
			return head->data;
		}
		// return 0 if empty
		return 0;
	}
	// retrieve tail
	T RetrieveTail(){
		if (tail != NULL){
			return tail->data;
		}
		// return 0 if empty
		return 0;
	}
	// returns number of nodes in list
	int Count()
	{
		//
		int index = 0;
		Node<T>* temp = head;
		// traverse to find the location to insert data
		while( temp != NULL) {
			temp = temp->next;
			index++;
		}
		return index;
	}
	// returns true if list is empty
	bool IsEmpty()
	{
		//
		if (head==NULL) {
			return true;
		}
		return false;
	}
	// prints list from tail of list
	void Output()
	{
		Node<T>* rover = tail;
		while (rover != NULL)
		{
			cout << rover->data << '\t';
			rover = rover->prev;
		}
		cout << endl;
	}
	// prints list from head
	void OutputFromHead()
		{
			Node<T>* rover = head;
			while (rover != NULL)
			{
				cout << rover->data << '\t';
				rover = rover->next;
			}
			cout << endl;
		}

	void PrintListRecursively(Node<T>* curr)
		{
			if (curr==NULL)
				{
					cout << "\t";
				    return;
				}
			cout << curr->data << "\t";
			PrintListRecursively(curr->next);
		}

	void PrintRecursively(){
		PrintListRecursively(head);
		cout << endl;
	}

};

template<typename T>
class Stack : private DList<T> {
public:
    Stack() : DList<T>::DList() {
    }

    ~Stack() {
    }

    void Push(T data) {
    	DList<T>::Prepend(data);
    }

    T Pop() {
    	T temp = DList<T>::RetrieveHead();
        DList<T>::DeleteHead();
        return temp;
    }

    T Peek() {
    	return DList<T>::RetrieveHead();
    }

    bool IsEmpty() {
        return DList<T>::IsEmpty();
    }

    int GetLength() {
        return DList<T>::Count();
    }

    void PrintStack(){
        	DList<T>::OutputFromHead();
    }

};

template<typename T>
class Queue : private DList<T> {
public:
	Queue() : DList<T>::DList() {
    }

    ~Queue() {
    }

    void Push(T data) {
    	DList<T>::Prepend(data);
    }

    T Pop() {
    	T temp = DList<T>::RetrieveTail();
        DList<T>::DeleteTail();
        return temp;
    }

    T Peek() {
    	return DList<T>::RetrieveTail();
    }

    bool IsEmpty() {
        return DList<T>::IsEmpty();
    }

    int GetLength() {
        return DList<T>::Count();
    }

    void PrintQueue(){
    	DList<T>::OutputFromHead();
    }

};

int main()
{
	int count = 10;
	DList<int> list;
	for (int x = 0; x < count; x++)
	{
		int rnumber = rand() % 100 + 1;
		list.Append(rnumber);
		cout << rnumber << "\t";
	}
	cout << endl;
	list.Output();

	cout << list.Count() << "\n";
	list.InsertAfter(59, 111);
	list.InsertBefore(79,10);
	list.OutputFromHead();
	list.Search(50);
	cout << list.IsEmpty() << "\n";
	list.Delete(10);
	list.Prepend(271);
	list.OutputFromHead();
	list.DeleteHead();
	list.OutputFromHead();
	list.PrintRecursively();

	int count_stack = 17;
	Stack<int> stack;
	for (int x = 0; x < count_stack; x++)
	{
		int rnumber = rand() % 100 + 1;
		stack.Push(rnumber);
		cout << rnumber << "\t";
	}
	cout << endl;
	cout << stack.Peek() << "\n";
	cout << stack.GetLength() << "\n";
	cout << stack.Pop() << "\n";
	cout << stack.GetLength()  << "\n";
	stack.PrintStack();

	int count_queue = 14;
	Queue<int> queue;
	for (int x = 0; x < count_queue; x++)
	{
		int rnumber = rand() % 100 + 1;
		queue.Push(rnumber);
		cout << rnumber << "\t";
	}
	cout << endl;
	cout << queue.Peek() << "\n";
	cout << queue.GetLength() << "\n";
	cout << queue.Pop() << "\n";
	cout << queue.GetLength()  << "\n";
	queue.PrintQueue();
	return 0;
}
