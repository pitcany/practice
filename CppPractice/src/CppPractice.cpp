//============================================================================
// Name        : CppPractice.cpp
// Author      : Yannik
// Version     :
// Copyright   : Your copyright notice
// Description : Practice for interviews
//============================================================================

#include <iostream>
using namespace std;

int main() {
	// Initialize the array length
	int arrLength = 5;

	// Initialize a pointer
	// to hold an array
	int * ptr = new int[arrLength] { 21, 47, 87, 35, 92 };

	// Display each element value
	// by incrementing the pointer (ptr++)
	cout << "Using pointer increment" << endl;
	cout << "Value\tAddress" << endl;
	while (*ptr)
	{
		cout << *ptr << "\t";
		cout << ptr << endl;
		ptr++;
	}

	// Move pointer back by 5
	ptr = ptr-5;

	// Display each element value
	// by accessing pointer index (ptr[])
	for (int i = 0; i < arrLength; ++i)
	{
		cout << ptr[i] << "\t";
		cout << &ptr[i] << endl;
	}

	return 0;
}
