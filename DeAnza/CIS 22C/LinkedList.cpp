/*
 * Linkedlist.h
 *
 *  Created on: Jul 12, 2022
 *      Author: yannik
 */

#ifndef LINKEDLIST_H_
#define LINKEDLIST_H_


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
	
	~DList() {
		//
		Node<T>* temp = head;
		// traverse to delete all nodes
		while (tail != NULL) {
			head = head->next;
			free(temp);
			temp = head;
		}
		tail = NULL;
	}
	// appends to tail of list
	void Append(T data) {
		Node<T>* pdata = new Node<T>(data);
		if (tail == NULL) {
			tail = pdata;
			head = pdata;
		}
		else {
			pdata->prev = tail;
			tail->next = pdata;
			tail = pdata;
		}
	}
	// prepends to head of list
	void Prepend(T data) {
		//
		Node<T>* pdata = new Node<T>(data);
		if (head == NULL) {
			head = pdata;
			tail = pdata;
		}
		else {
			pdata->next = head;
			head->prev = pdata;
			head = pdata;
		}
	}
	// inserts data after found data
	void InsertAfter(T find, T data) {
		//
		Node<T>* temp = head;
		// traverse to find the location to insert data
		while (temp != NULL) {
			if (temp->data == find) {
				Node<T>* pdata = new Node<T>(data);
				pdata->prev = temp;
				pdata->next = temp->next;
				temp->next = pdata;
				if (pdata->next != NULL)
					pdata->next->prev = pdata;
				else
					tail = pdata;
				return;
			}
			temp = temp->next;
		}
		// If we cannot find the data
		cout << "Data not found" << endl;
	}
	// inserts data before found data
	void InsertBefore(T find, T data) {
		//
		Node<T>* temp = head;
		// traverse to find the location to insert data
		while (temp != NULL) {
			if (temp->data == find) {
				Node<T>* pdata = new Node<T>(data);
				pdata->prev = temp->prev;
				pdata->next = temp;
				temp->prev = pdata;
				if (pdata->prev != NULL)
					pdata->prev->next = pdata;
				else
					head = pdata;
				return;
			}
			temp = temp->next;
		}
		// If we cannot find the data
		cout << "Data not found" << endl;
	}
	// finds data node and returns it
	Node<T>* Search(T data) {
		//
		Node<T>* temp = head;
		// traverse to find the location to insert data
		while (temp != NULL) {
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
	void Delete(T data) {
		//
		Node<T>* temp = head;
		Node<T>* prev_node;
		// traverse to find the location to insert data
		while (temp != NULL) {
			if (temp->data == data) {
				if (head == tail) {
					head = NULL;
					tail = NULL;
				}
				else {
					if (temp != head) 
						temp->prev->next = temp->next;
					else {
						head = head->next;
						head->prev = NULL;
					}
					if (temp != tail)
						temp->next->prev = temp->prev;
					else {
						tail = tail->prev;
						tail->next = NULL;
					}
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
	void DeleteTail() {
		if (tail != NULL) {
			Node<T>* temp = tail;
			if (tail == head) {
				head = NULL;
				tail = NULL;
			}
			else {
				tail = tail->prev;
				tail->next = NULL;
			}
			free(temp);
		}
	}
	// remove head
	void DeleteHead() {
		if (head != NULL) {
			Node<T>* temp = head;
			if (head == tail) {
				head = NULL;
				tail = NULL;
			}
			else {
				head = head->next;
				head->prev = NULL;
			}
			free(temp);
		}
	}
	// retrieve head
	T RetrieveHead() {
		if (head != NULL) {
			return head->data;
		}
		// return 0 if empty
		return 0;
	}
	// retrieve tail
	T RetrieveTail() {
		if (tail != NULL) {
			return tail->data;
		}
		// return 0 if empty
		return 0;
	}
	// returns number of nodes in list
	int Count() {
		//
		int index = 0;
		Node<T>* temp = head;
		// traverse to find the location to insert data
		while (temp != NULL) {
			temp = temp->next;
			index++;
		}
		return index;
	}
	// returns true if list is empty
	bool IsEmpty() {
		//
		if (head == NULL) {
			return true;
		}
		return false;
	}
	// prints list from tail of list
	void OutputFromTail() {
		Node<T>* rover = tail;
		while (rover != NULL) {
			cout << rover->data << "\t";
			rover = rover->prev;
		}
		cout << endl;
	}
	// prints list from head
	void OutputFromHead() {
		Node<T>* rover = head;
		while (rover != NULL) {
			cout << rover->data << "\t";
			rover = rover->next;
		}
		cout << endl;
	}

	void PrintListRecursively(Node<T>* curr) {
		if (curr == NULL) {
			cout << endl;
			return;
		}
		cout << curr->data << "\t";
		PrintListRecursively(curr->next);
	}

	void PrintRecursively() {
		PrintListRecursively(head);
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

	void PrintStack() {
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

	void PrintQueue() {
		DList<T>::OutputFromHead();
	}

};

//int main()
//{
//	int count = 10;
//	DList<int> list;
//	for (int x = 0; x < count; x++)
//	{
//		int rnumber = rand() % 100 + 1;
//		list.Append(rnumber);
//		cout << rnumber << "\t";
//	}
//	cout << endl;
//	list.Output();
//
//	cout << list.Count() << "\n";
//	list.InsertAfter(87, 111);
//	list.InsertBefore(78,10);
//	list.OutputFromHead();
//	list.Search(11);
//	cout << list.IsEmpty() << "\n";
//	list.Delete(78);
//	list.Prepend(271);
//	list.OutputFromHead();
//	list.DeleteHead();
//	list.OutputFromHead();
//	list.PrintRecursively();
//
//	int count_stack = 5;
//	Stack<int> stack;
//	for (int x = 0; x < count_stack; x++)
//	{
//		int rnumber = rand() % 100 + 1;
//		stack.Push(rnumber);
//		cout << rnumber << "\t";
//	}
//	cout << endl;
//	cout << stack.Peek() << "\n";
//	cout << stack.GetLength() << "\n";
//	cout << stack.Pop() << "\n";
//	cout << stack.GetLength()  << "\n";
//	stack.PrintStack();
//
//	int count_queue = 5;
//	Queue<int> queue;
//	for (int x = 0; x < count_queue; x++)
//	{
//		int rnumber = rand() % 100 + 1;
//		queue.Push(rnumber);
//		cout << rnumber << "\t";
//	}
//	cout << endl;
//	cout << queue.Peek() << "\n";
//	cout << queue.GetLength() << "\n";
//	cout << queue.Pop() << "\n";
//	cout << queue.GetLength()  << "\n";
//	queue.PrintQueue();
//	return 0;
//}


#endif /* LINKEDLIST_H_ */
