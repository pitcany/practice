//============================================================================
// Name        : BinaryTree.cpp
// Author      : Yannik
// Version     :
// Copyright   : 
// Description : Binary Search Tree in C++
//============================================================================


#include <iostream>
#include <ctime>
#include <vector>
#include <cmath>
//#include "ConsoleColor.h"
using namespace std;

template <typename T>
struct TreeNode{
	T data;
	TreeNode<T> *left;
	TreeNode<T> *right;

	TreeNode<T>(T val){
		this->data = val;
		this->left = NULL;
		this->right = NULL;
	}

	TreeNode<T>(T val, TreeNode<T> left, TreeNode<T> right){
		this->data = val;
		this->left = left;
		this->right = right;
	}
};

template <typename T>
class BinarySearchTree
{
private:
	TreeNode<T> *root;

public:
	BinarySearchTree<T>(){
		root = NULL;
	}

	~BinarySearchTree<T>(){
		destroy_tree();
	}

	void destroy_tree(TreeNode<T>* leaf){
		if (leaf != NULL) {
			destroy_tree(leaf->left);
			destroy_tree(leaf->right);
			delete leaf;
		}
	}

	void destroy_tree(){
		destroy_tree(root);
	}

	//int reSize(int x){
	//	int value = pow(x, 2);
	//	return value;
	//}

	void insert(T value, TreeNode<T>* leaf){
		if (value < leaf->data){
			if (leaf->left != NULL){
				insert(value, leaf->left);
			} else {
				leaf->left = new TreeNode<T>(value);
				leaf->left->left = NULL;
				leaf->left->right = NULL;
			}
		} else if (value >= leaf->data) {
			if (leaf->right != NULL){
				insert(value, leaf->right);
			} else {
				leaf->right = new TreeNode<T>(value);
				leaf->right->right = NULL;
				leaf->right->left = NULL;
			}
		}
	}

	void insert(T value){
		if(root != NULL){
			insert(value, root);
		} else {
			root = new TreeNode<T>(value);
			root->left = NULL;
			root->right = NULL;
		}
	}

	TreeNode<T>* search(T value, TreeNode<T>* leaf){
		if (leaf != NULL){
			if(value == leaf->data){
				return leaf;
			}
			if(value < leaf->data){
				return search(value, leaf->left);
			} else {
				return search(value, leaf->right);
			}
		} else {
			return NULL;
		}
	}

	TreeNode<T>* search(T value){
		return search(value, root);
	}

	T parent(TreeNode<T>* leaf, T value, T parent){
		if (leaf == NULL)
			return;

		if (leaf->data == value){
			return parent;
		} else {
			parent(leaf->left, value, leaf->data);
			parent(leaf->right, value, leaf->data);
		}
	}

	T parent(T value){
		parent(root, value, -1);
	}

	void inOrder(TreeNode<T>* curr)
	{
		if (curr == NULL){
			return;
		}
		inOrder(curr->left);
		cout << curr->data << " ";
		inOrder(curr->right);
	}
	void preOrder(TreeNode<T>* curr)
	{
		if (curr == NULL){
			return;
		}
		cout << curr->data << " ";
		preOrder(curr->left);
		preOrder(curr->right);
	}
	void postOrder(TreeNode<T>* curr)
	{
		if (curr == NULL){
			return;
		}

		postOrder(curr->left);
		postOrder(curr->right);
		cout << curr->data << " ";
	}
//	void reverseOrder(TreeNode<T>* curr)
//	{
//		if (curr == NULL){
//			return;
//		}
//
//		reverseOrder(curr->right);
//		cout << curr->data << " ";
//		reverseOrder(curr->left);
//	}
};

int main()
{
	BinarySearchTree<int> ykp = BinarySearchTree<int>();
	vector<int> varray{ 42, 68, 35, 1, 70, 25, 79, 59, 63, 65 };
	for (int i = 0; i < varray.size(); i++)
		ykp.insert(varray[i]);
}
